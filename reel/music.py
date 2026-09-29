"""Compose the background music bed in code: playful 112 BPM groove, fits the voiceover length."""
import json, os, wave, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); B = os.path.join(HERE, "build")
DUR = json.load(open(os.path.join(B, "cues.json")))["duration"]
SR, BPM = 48000, 112; beat = 60 / BPM; N = int(SR * (DUR + 1)); L = np.zeros(N); Rr = np.zeros(N)
rng = np.random.default_rng(3)
def add(t, x, g=1., pan=0.):
    i = int(t * SR); x = x[:max(0, N - i)]; L[i:i+len(x)] += x * g * (1 - max(0, pan)); Rr[i:i+len(x)] += x * g * (1 + min(0, pan))
def pluck(f, d=.45):                     # Karplus-Strong string
    n = int(d * SR); p = max(2, int(SR / f)); buf = rng.uniform(-1, 1, p); out = np.empty(n)
    for i in range(n): out[i] = buf[i % p]; buf[i % p] = .5 * (buf[i % p] + buf[(i + 1) % p]) * .996
    return out * .5
def bass(f, d):
    n = int(d * SR); t = np.arange(n) / SR; x = np.sin(2*np.pi*f*t) + .3*np.sin(4*np.pi*f*t)
    return x * np.minimum(1, t / .01) * np.exp(-t / (d * .8)) * .55
def kick():
    n = int(.35 * SR); t = np.arange(n) / SR; f = 50 + 90 * np.exp(-t / .03)
    return np.sin(2*np.pi*np.cumsum(f)/SR) * np.exp(-t / .12) * .9
def clap():
    n = int(.18 * SR); t = np.arange(n) / SR; x = rng.standard_normal(n); x = x - np.convolve(x, np.ones(6)/6, 'same')
    return x * (np.exp(-t / .045) + .6 * np.exp(-((t - .012) / .006) ** 2)) * .35
def tabla(f0, bend=1.6):                 # pitched membrane with a pitch bend, like a bayan/dayan stroke
    n = int(.3 * SR); t = np.arange(n) / SR; f = f0 * (1 + (bend - 1) * np.exp(-t / .04))
    return np.sin(2*np.pi*np.cumsum(f)/SR) * np.exp(-t / .09) * .45
def hat():
    n = int(.05 * SR); x = rng.standard_normal(n); x = x - np.convolve(x, np.ones(3)/3, 'same')
    return x * np.exp(-np.arange(n) / SR / .012) * .15
# C - G - Am - F, one chord per bar
CH = [(261.63, [261.63, 329.63, 392.0]), (196.0, [293.66, 392.0, 493.88]), (220.0, [261.63, 329.63, 440.0]), (174.61, [261.63, 349.23, 440.0])]
pl = {f: pluck(f * 2) for _, ch in CH for f in ch}
bar = 4 * beat; nb = int(DUR / bar) + 1
for b in range(nb):
    t0 = b * bar; root, ch = CH[b % 4]; intro = b < 1
    add(t0, bass(root / 2, beat * 1.6), .9); add(t0 + beat * 2.5, bass(root / 2, beat * .9), .7)
    for k, st in enumerate([0, .5, 1, 1.5, 2, 2.5, 3, 3.5]):
        f = ch[[0, 1, 2, 1, 2, 0, 1, 2][k]]; add(t0 + st * beat, pl[f], .35, pan=(-.4 if k % 2 else .4))
    if intro: continue
    for st in (0, 2): add(t0 + st * beat, kick(), .8)
    add(t0 + 2.5 * beat, kick(), .45)
    for st in (1, 3): add(t0 + st * beat, clap(), .9)
    for st in np.arange(0, 4, .5): add(t0 + st * beat, hat(), .8, pan=.3)
    for st, f, bd in ((.75, 180, 1.3), (1.5, 320, 1.1), (2.75, 180, 1.8), (3.5, 360, 1.1)): add(t0 + st * beat, tabla(f, bd), .55, pan=-.25)
# final hit on the last full beat
tend = DUR - 1.2; add(tend, kick(), 1.); add(tend, clap(), 1.)
for f in (261.63, 329.63, 392.0, 523.25): add(tend, pluck(f, 1.2), .5)
fade = np.ones(N); i0 = int((DUR - .9) * SR); fade[i0:] = np.linspace(1, 0, N - i0)
st = np.stack([L * fade, Rr * fade], 1); st = st / np.max(np.abs(st)) * .85
with wave.open(os.path.join(B, "music.wav"), "wb") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((st * 32767).astype(np.int16).tobytes())
print(f"music {DUR:.1f}s")
