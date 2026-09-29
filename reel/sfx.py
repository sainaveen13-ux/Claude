"""Sound effects, each tied to a voiceover cue so they stay in sync whatever the voice timing."""
import json, os, wave, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); B = os.path.join(HERE, "build")
cj = json.load(open(os.path.join(B, "cues.json"))); DUR = cj["duration"]; CUE = {c["id"]: c for c in cj["cues"]}
C = lambda i, f=0: CUE[i]["start"] + (CUE[i]["end"] - CUE[i]["start"]) * f
SR = 48000; out = np.zeros(int(SR * (DUR + 2))); rng = np.random.default_rng(7)
def lp(x, k):
    y = np.empty_like(x); a = 0.
    for i, v in enumerate(x): a += k * (v - a); y[i] = a
    return y
def put(t, x, g=1.): i = max(0, int(t * SR)); x = x[:len(out) - i]; out[i:i + len(x)] += x * g
def sine(f0, f1, d, r):
    n = int(d * SR); t = np.arange(n) / SR; f = np.linspace(f0, f1, n)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.minimum(1, t / .002) * np.exp(-t / r)
def whoosh(d=.45, up=True):
    n = int(d * SR); x = rng.standard_normal(n); t = np.linspace(0, 1, n); k = (.02 + .25 * t) if up else (.27 - .25 * t); y = np.empty(n); a = 0.
    for i in range(n): a += k[i] * (x[i] - a); y[i] = a
    return y * np.sin(np.pi * t) ** 1.5 * 2.2
def thud(): y = sine(95, 42, .6, .22); n = int(.04 * SR); y[:n] += lp(rng.standard_normal(n), .3) * np.exp(-np.arange(n) / SR / .01) * .8; return y
def pop(f=880): return sine(f * 1.4, f, .09, .03) * .7
def click(): n = int(.012 * SR); return rng.standard_normal(n) * np.exp(-np.arange(n) / SR / .002) * .5
def chime(b=1318.5, g=1.):
    n = int(1.6 * SR); t = np.arange(n) / SR
    return sum(np.sin(2 * np.pi * b * m * t) * a for m, a in [(1, 1), (1.5, .5), (2, .35), (3, .15)]) * np.minimum(1, t / .004) * np.exp(-t / .45) * .22 * g
def strike(): n = int(.2 * SR); x = rng.standard_normal(n); t = np.linspace(0, 1, n); return (x - lp(x, .35)) * np.sin(np.pi * t) ** .6 * .35
def ding(): return np.concatenate([chime(1568, 1.2)[:int(.12 * SR)], chime(2093, 1.2)])
def rain(d):
    n = int(d * SR); x = rng.standard_normal(n); y = lp(x, .5) - lp(x, .08); t = np.linspace(0, 1, n)
    dr = np.zeros(n); dr[rng.integers(0, n, int(d * 60))] = rng.uniform(.3, 1, int(d * 60)); dr = np.convolve(dr, np.exp(-np.arange(200) / 25), 'same')
    return (y * .25 + dr * .08) * np.minimum(1, t * 6) * np.minimum(1, (1 - t) * 5)
def bubbles(d):
    y = np.zeros(int(d * SR))
    for _ in range(int(d * 14)):
        s = sine(rng.uniform(500, 1400), rng.uniform(1500, 2600), .06, .02) * .5; i = rng.integers(0, len(y) - len(s)); y[i:i + len(s)] += s
    return y
def swell(d=.7): n = int(d * SR); t = np.linspace(0, 1, n); return lp(rng.standard_normal(n), .08) * t ** 3 * 1.6
def slide(): return sine(900, 420, .45, .5) * .25
def tick(): return sine(3200, 2800, .02, .006) * .35
def boing(): return sine(180, 620, .35, .25) * .45
put(.05, pop(1100), .8)
put(C("relax"), slide() * .7, .8)
put(C("intro"), chime(1046.5, .8))
put(C("intro", .32) - .12, whoosh(.3), .45); put(C("intro", .32), thud(), .5)
put(C("intro", .8) - .45, swell(.45), .5); put(C("intro", .8), thud(), .9); put(C("intro", .82), chime(2093, .7))
put(C("broker"), ding(), .9); put(C("broker", 1) + .1, whoosh(.4, False), .7)
for i in ("broker", "deposit", "landlord"): put(C(i) + .3, strike(), 1.); put(C(i) + .5, pop(1200), .8)
put(C("landlord", .45), boing(), .8)
put(C("wards") - .2, swell(.6), .35)
for tt in np.linspace(C("wards"), C("wards", 1), 24): put(tt, tick(), .6)
put(C("pick") - .2, whoosh(.9), .6); put(C("pick", .42), click(), 1.); put(C("pick", .45), pop(700), 1.); put(C("pick", .6), chime(1760, .8))
put(C("write") - .15, whoosh(.6), .6)
for i, f in (("write", .3), ("city", .2), ("city", .6), ("roast", .05), ("roast", .25), ("roast", .45)): put(C(i, f), pop(800 + 90 * len(i) + 300 * f), .9)
put(C("amen") - .1, whoosh(.5), .5)
put(C("pool") - .1, whoosh(.4), .4); put(C("pool", .4), rain(max(.8, C("lake") - C("pool", .4))), 1.)
put(C("lake") - .1, whoosh(.4), .4); put(C("lake", .45), bubbles(max(.8, C("metro") - C("lake", .45))), .9)
put(C("metro") - .1, whoosh(.4), .4)
for tt in np.linspace(C("metro", .55), C("metro", 1), 10): put(tt, tick(), .7)
put(C("metro", 1), slide(), .9)
put(C("lux") - .1, whoosh(.8), .55); put(C("you", .35), chime(1568, 1.)); put(C("you", .45), chime(2349, .7))
put(C("brand") - .7, swell(.7), .6); put(C("brand"), thud(), 1.); put(C("brand") + .03, chime(1046.5, .8))
put(C("hurry"), pop(1300), 1.)
for k in range(int(DUR - C("hurry", .75))): put(C("hurry", .75) + k, tick(), .9)
put(C("builder"), slide(), .9); put(C("bio"), pop(1000), .8)
out = out[:int(SR * DUR)]; out = out / np.max(np.abs(out)) * .8
with wave.open(os.path.join(B, "sfx.wav"), "wb") as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((out * 32767).astype(np.int16).tobytes())
print("sfx ok")
