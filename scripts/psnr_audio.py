import wave, struct, math, sys

def load(p):
    w = wave.open(p, 'rb')
    n = w.getnframes()
    ch = w.getnchannels()
    d = w.readframes(n)
    return struct.unpack('<%dh' % (n * ch), d), n, ch

a, n, c = load(sys.argv[1])
b, m, d = load(sys.argv[2])
k = min(n, m)
a1 = a[0::c][:k]
b1 = b[0::d][:k]
mse = sum((x - y) ** 2 for x, y in zip(a1, b1)) / k
mx = max(max(abs(x) for x in a1), 1)
psnr = 10 * math.log10(mx * mx / mse) if mse > 0 else float('inf')
ma = sum(a1) / k
mb = sum(b1) / k
cov = sum((x - ma) * (y - mb) for x, y in zip(a1, b1))
va = math.sqrt(sum((x - ma) ** 2 for x in a1) * sum((y - mb) ** 2 for y in b1))
corr = cov / va if va > 0 else 0
print('PSNR=%.2f dB  相关度=%.4f' % (psnr, corr))
