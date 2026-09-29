#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成 torchvision 桩包（DCU 环境用）。
PyPI 版 torchvision 的 _C.so 链接 CUDA 运行库，与海光 DCU torch 不兼容。
H3 视频管线只用 PIL + torch，不依赖 torchvision；本桩只满足 import。
"""
import os, shutil, sys

B = sys.argv[1] if len(sys.argv) > 1 else "/root/private_data/h3"
TV = os.path.join(B, "py311_overlay", "torchvision")
shutil.rmtree(TV, ignore_errors=True)

FILES = {}

FILES["__init__.py"] = '''"""torchvision 桩（DCU 环境）

PyPI 版 torchvision 的 _C.so 链接 CUDA 运行库（libcudart.so.12），
与海光 DCU torch 不兼容，无法安装。
H3 视频管线只用 PIL + torch，不依赖 torchvision。
本桩只满足 import；真正调用会抛 NotImplementedError。
"""
__version__ = "0.24.0+stub"

from . import transforms, ops, utils, io, models, datasets  # noqa: F401
'''

FILES["transforms/__init__.py"] = '''"""最小 transforms 桩：常用类用 PIL/torch 实现。"""
import torch
from PIL import Image


class _Base:
    def __call__(self, img):
        return self.forward(img)

    def forward(self, img):
        raise NotImplementedError(type(self).__name__)


class ToTensor(_Base):
    def forward(self, pic):
        import numpy as np
        if isinstance(pic, Image.Image):
            a = np.array(pic)
            if a.ndim == 2:
                a = a[:, :, None]
            t = torch.from_numpy(a.transpose((2, 0, 1))).contiguous()
            if t.dtype == torch.uint8:
                return t.float().div(255)
            return t
        return pic


class ToPILImage(_Base):
    def forward(self, t):
        import numpy as np
        a = t.mul(255).clamp(0, 255).byte().permute(1, 2, 0).cpu().numpy()
        return Image.fromarray(a)


class Resize(_Base):
    def __init__(self, size, interpolation=None, **kw):
        self.size = size

    def forward(self, img):
        if isinstance(img, Image.Image):
            s = self.size
            if isinstance(s, (list, tuple)):
                return img.resize((int(s[-1]), int(s[-2])), Image.BILINEAR)
            return img.resize((int(s), int(s)), Image.BILINEAR)
        return img


class CenterCrop(_Base):
    def __init__(self, size, **kw):
        self.size = size

    def forward(self, img):
        return img


class Normalize(_Base):
    def __init__(self, mean, std, **kw):
        self.mean, self.std = mean, std

    def forward(self, t):
        m = torch.as_tensor(self.mean, dtype=t.dtype, device=t.device).view(-1, 1, 1)
        s = torch.as_tensor(self.std, dtype=t.dtype, device=t.device).view(-1, 1, 1)
        return (t - m) / s


class Compose(_Base):
    def __init__(self, ts):
        self.ts = ts

    def forward(self, x):
        for t in self.ts:
            x = t(x)
        return x


from . import functional  # noqa: E402,F401
'''

FILES["transforms/functional.py"] = '''def _nyi(n):
    def f(*a, **k):
        raise NotImplementedError("torchvision.transforms.functional.%s 桩" % n)
    return f

resize = _nyi("resize")
to_tensor = _nyi("to_tensor")
normalize = _nyi("normalize")
center_crop = _nyi("center_crop")
'''

FILES["ops/__init__.py"] = '''def _nyi(n):
    def f(*a, **k):
        raise NotImplementedError("torchvision.ops.%s 桩" % n)
    return f

nms = _nyi("nms")
roi_align = _nyi("roi_align")
deform_conv2d = _nyi("deform_conv2d")
'''

_GETATTR = '''def __getattr__(name):
    raise NotImplementedError("torchvision.%s.%s 桩（DCU 环境不可用）" % (__name__.split(".")[-1], name))
'''

for m in ("utils", "io", "models", "datasets"):
    FILES[m + "/__init__.py"] = _GETATTR

for rel, content in FILES.items():
    p = os.path.join(TV, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(content)

# 清掉 __pycache__
for root, dirs, _ in os.walk(TV):
    for d in list(dirs):
        if d == "__pycache__":
            shutil.rmtree(os.path.join(root, d), ignore_errors=True)

print("已生成 torchvision 桩：%s" % TV)
for root, _, files in os.walk(TV):
    for fn in sorted(files):
        print("  " + os.path.relpath(os.path.join(root, fn), TV))
