#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成 torchaudio 桩包（DCU 环境用）。

PyPI 版 torchaudio 的 C 扩展链接 CUDA 运行库，与海光 DCU torch 不兼容。
ComfyUI 只用到 torchaudio 的：
  - functional.resample           → 用 torch F.interpolate 实现（够用）
  - functional.melspec / MelScale → 用 torch.stft + mel 滤波器组实现
  - transforms.MelSpectrogram / MelScale / Resample
本桩给出**可用实现**，不是空壳。
"""
import os, shutil, sys

B = sys.argv[1] if len(sys.argv) > 1 else "/root/private_data/h3"
TA = os.path.join(B, "py311_overlay", "torchaudio")
shutil.rmtree(TA, ignore_errors=True)

F = {}

F["__init__.py"] = '''"""torchaudio 桩（DCU 环境）—— 用纯 torch 实现 ComfyUI 实际用到的部分。"""
import math
import torch
import torch.nn.functional as F

__version__ = "2.9.0+stub"


def _sinc(x):
    return torch.where(x == 0, torch.ones_like(x), torch.sin(math.pi * x) / (math.pi * x))


def resample(waveform, orig_freq, new_freq, lowpass_filter_width=6, rolloff=0.99,
             resampling_method="sinc_interp_hann", beta=None, **kw):
    """重采样。用 F.interpolate 线性插值实现（数值够用，非 bit-exact）。"""
    oi, ni = int(orig_freq), int(new_freq)
    if oi == ni:
        return waveform
    x = waveform
    squeeze = None
    if x.dim() == 1:
        x = x[None, None, :]; squeeze = 0
    elif x.dim() == 2:
        x = x[None, :, :]; squeeze = 1
    n_out = int(round(x.shape[-1] * ni / oi))
    y = F.interpolate(x, size=n_out, mode="linear", align_corners=False)
    if squeeze == 0:
        return y[0, 0]
    if squeeze == 1:
        return y[0]
    return y


def _hz_to_mel(f):
    f = torch.as_tensor(f, dtype=torch.float64)
    return 2595.0 * torch.log10(1.0 + f / 700.0)


def _mel_to_hz(m):
    m = torch.as_tensor(m, dtype=torch.float64)
    return 700.0 * (10.0 ** (m / 2595.0) - 1.0)


def melscale_fbanks(n_freqs, f_min, f_max, n_mels, sample_rate, norm="slaney", mel_scale="htk"):
    all_freqs = torch.linspace(0, sample_rate // 2, n_freqs, dtype=torch.float64)
    m_min, m_max = _hz_to_mel(f_min), _hz_to_mel(f_max)
    m_pts = torch.linspace(m_min, m_max, n_mels + 2, dtype=torch.float64)
    f_pts = _mel_to_hz(m_pts)
    fb = torch.zeros(n_freqs, n_mels, dtype=torch.float64)
    f_diff = f_pts[1:] - f_pts[:-1]
    for m in range(n_mels):
        lo, c, hi = f_pts[m], f_pts[m + 1], f_pts[m + 2]
        up = (all_freqs - lo) / max(f_diff[m].item(), 1e-12)
        dn = (hi - all_freqs) / max(f_diff[m + 1].item(), 1e-12)
        fb[:, m] = torch.clamp(torch.minimum(up, dn), min=0.0)
        if norm == "slaney":
            fb[:, m] *= 2.0 / max((hi - lo).item(), 1e-12)
    return fb


def _stft_power(waveform, n_fft, hop_length, win_length, window, center=True,
                pad_mode="reflect", power=2.0, normalized=False, onesided=True):
    x = waveform
    if x.dim() == 1:
        x = x[None, :]
    if window is None:
        window = torch.hann_window(win_length, device=x.device, dtype=x.dtype)
    if x.dtype not in (torch.float32, torch.float64):
        x = x.float()
    spec = torch.stft(x, n_fft=n_fft, hop_length=hop_length, win_length=win_length,
                      window=window.to(x.dtype), center=center, pad_mode=pad_mode,
                      normalized=normalized, onesided=onesided, return_complex=True)
    p = spec.abs().pow(power)
    return p


def spectrogram(waveform, pad=0, window=None, n_fft=400, hop_length=None,
                win_length=None, power=2.0, normalized=False, center=True,
                pad_mode="reflect", onesided=True, **kw):
    hop_length = n_fft // 4 if hop_length is None else hop_length
    win_length = n_fft if win_length is None else win_length
    if pad > 0:
        waveform = F.pad(waveform, (pad, pad))
    return _stft_power(waveform, n_fft, hop_length, win_length, window,
                       center=center, pad_mode=pad_mode, power=power,
                       normalized=normalized, onesided=onesided)


def melspec(waveform, n_mels=128, n_fft=400, hop_length=None, win_length=None,
            f_min=0.0, f_max=None, pad=0, window=None, power=2.0, normalized=False,
            center=True, pad_mode="reflect", onesided=True, norm="slaney",
            mel_scale="htk", **kw):
    if f_max is None:
        f_max = 8000.0
    sr = 16000
    hop_length = n_fft // 4 if hop_length is None else hop_length
    win_length = n_fft if win_length is None else win_length
    spec = spectrogram(waveform, pad, window, n_fft, hop_length, win_length,
                       power, normalized, center, pad_mode, onesided)
    fb = melscale_fbanks(n_fft // 2 + 1, f_min, f_max, n_mels, sr, norm, mel_scale)
    return torch.matmul(spec.transpose(-1, -2).to(fb.dtype), fb).transpose(-1, -2).to(spec.dtype)


class _FB:
    def __init__(self, **kw):
        self.kw = kw

    def __call__(self, waveform):
        kw = dict(self.kw)
        if "sample_rate" in kw:
            kw.pop("sample_rate")
        return melspec(waveform, **kw)


from . import functional, transforms, io  # noqa: E402,F401
'''

F["functional.py"] = '''"""functional 子模块：转发到顶层实现。"""
from . import (resample, melspec, spectrogram, melscale_fbanks,  # noqa: F401
               _hz_to_mel, _mel_to_hz)

amplitude_to_DB = None


def _nyi(name):
    def f(*a, **k):
        raise NotImplementedError("torchaudio.functional.%s 桩" % name)
    return f


gain = _nyi("gain")
compute_deltas = _nyi("compute_deltas")
'''

F["transforms/__init__.py"] = '''"""transforms 子模块。"""
import torch
from .. import melspec, resample as _resample, melscale_fbanks


class MelSpectrogram:
    def __init__(self, sample_rate=16000, n_fft=400, win_length=None, hop_length=None,
                 f_min=0.0, f_max=None, pad=0, n_mels=128, window_fn=torch.hann_window,
                 power=2.0, normalized=False, wkwargs=None, center=True,
                 pad_mode="reflect", onesided=True, norm="slaney", mel_scale="htk"):
        self.sample_rate = sample_rate
        self.n_fft = n_fft
        self.win_length = win_length or n_fft
        self.hop_length = hop_length or n_fft // 4
        self.f_min = f_min
        self.f_max = f_max if f_max is not None else sample_rate / 2
        self.pad = pad
        self.n_mels = n_mels
        self.power = power
        self.normalized = normalized
        self.center = center
        self.pad_mode = pad_mode
        self.onesided = onesided
        self.norm = norm
        self.mel_scale = mel_scale
        self._fb = None

    def __call__(self, waveform):
        if self._fb is None or self._fb.device != waveform.device:
            self._fb = melscale_fbanks(self.n_fft // 2 + 1, self.f_min, self.f_max,
                                       self.n_mels, self.sample_rate, self.norm,
                                       self.mel_scale).to(waveform.device)
        from .. import spectrogram
        spec = spectrogram(waveform, self.pad, None, self.n_fft, self.hop_length,
                           self.win_length, self.power, self.normalized, self.center,
                           self.pad_mode, self.onesided)
        return torch.matmul(spec.transpose(-1, -2).to(self._fb.dtype), self._fb).transpose(-1, -2).to(spec.dtype)


class MelScale:
    def __init__(self, n_mels=128, sample_rate=16000, f_min=0.0, f_max=None,
                 n_stft=None, norm="slaney", mel_scale="htk"):
        self.n_mels = n_mels
        self.sample_rate = sample_rate
        self.f_min = f_min
        self.f_max = f_max if f_max is not None else sample_rate / 2
        self.n_stft = n_stft
        self.norm = norm
        self.mel_scale = mel_scale

    def __call__(self, spec):
        n = self.n_stft or spec.shape[-2]
        fb = melscale_fbanks(n, self.f_min, self.f_max, self.n_mels,
                             self.sample_rate, self.norm, self.mel_scale).to(spec.device)
        return torch.matmul(spec.transpose(-1, -2).to(fb.dtype), fb).transpose(-1, -2).to(spec.dtype)


class Resample:
    def __init__(self, orig_freq=16000, new_freq=16000, **kw):
        self.orig_freq, self.new_freq = orig_freq, new_freq

    def __call__(self, waveform):
        return _resample(waveform, self.orig_freq, self.new_freq)


class AmplitudeToDB:
    def __init__(self, **kw):
        pass

    def __call__(self, x):
        return 10.0 * torch.log10(torch.clamp(x, min=1e-10))


class Spectrogram:
    def __init__(self, n_fft=400, win_length=None, hop_length=None, pad=0,
                 window_fn=torch.hann_window, power=2.0, normalized=False,
                 center=True, pad_mode="reflect", onesided=True):
        self.kw = dict(n_fft=n_fft, win_length=win_length or n_fft,
                       hop_length=hop_length or n_fft // 4, pad=pad, power=power,
                       normalized=normalized, center=center, pad_mode=pad_mode,
                       onesided=onesided)

    def __call__(self, waveform):
        from .. import spectrogram
        return spectrogram(waveform, **self.kw)
'''

F["io/__init__.py"] = '''"""io 子模块桩。"""
def __getattr__(name):
    raise NotImplementedError("torchaudio.io.%s 桩（DCU 环境不可用）" % name)
'''

for rel, content in F.items():
    p = os.path.join(TA, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(content)

for root, dirs, _ in os.walk(TA):
    for d in list(dirs):
        if d == "__pycache__":
            shutil.rmtree(os.path.join(root, d), ignore_errors=True)

print("已生成 torchaudio 桩：%s" % TA)
for root, _, files in os.walk(TA):
    for fn in sorted(files):
        print("  " + os.path.relpath(os.path.join(root, fn), TA))
