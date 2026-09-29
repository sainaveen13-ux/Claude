"""Use a recorded/generated voiceover file instead of tts.py.

Usage: python3 vo_import.py path/to/voiceover.wav [tempo]
Finds the pauses, assigns speech to the lines in lines.json (by word count, via dynamic programming),
and writes build/vo.wav + build/cues.json exactly like tts.py does.
"""
import json, os, subprocess, sys, wave, numpy as np, imageio_ffmpeg
HERE = os.path.dirname(os.path.abspath(__file__)); B = os.path.join(HERE, "build"); os.makedirs(B, exist_ok=True)
src, tempo = sys.argv[1], float(sys.argv[2]) if len(sys.argv) > 2 else 1.0
SR, LEAD, TAIL = 24000, 0.35, 2.0
raw = subprocess.run([imageio_ffmpeg.get_ffmpeg_exe(), "-v", "error", "-i", src, "-af", f"atempo={tempo}", "-ac", "1", "-ar", str(SR), "-f", "s16le", "-"], capture_output=True, check=True).stdout
x = np.frombuffer(raw, np.int16).astype(np.float32) / 32768
lines = json.load(open(os.path.join(HERE, "lines.json")))["lines"]
# speech segments from 10 ms energy frames
hop = SR // 100; e = np.sqrt(np.convolve(x ** 2, np.ones(hop) / hop, "same")[::hop] + 1e-12)
on = 20 * np.log10(e) > -40
segs, i = [], 0
while i < len(on):
    if on[i]:
        j = i
        while j < len(on) and (on[j] or (j + 25 < len(on) and on[j:j + 25].any())): j += 1   # bridge gaps < 0.25 s
        segs.append([i / 100, j / 100]); i = j
    else: i += 1
# group segments into lines: minimise squared error between group duration and expected share (by words)
W = np.array([len(l["text"].split()) + 1.5 for l in lines]); speech = sum(b - a for a, b in segs)
exp = W / W.sum() * speech; n, m = len(segs), len(lines)
INF = 1e18; dp = np.full((m + 1, n + 1), INF); bk = np.zeros((m + 1, n + 1), int); dp[0][0] = 0
for li in range(1, m + 1):
    for sj in range(li, n - (m - li) + 1):
        for sk in range(li - 1, sj):
            if dp[li - 1][sk] >= INF: continue
            d = segs[sj - 1][1] - segs[sk][0]; c = dp[li - 1][sk] + ((d - exp[li - 1]) / exp[li - 1]) ** 2
            if c < dp[li][sj]: dp[li][sj] = c; bk[li][sj] = sk
cuts, sj = [], n
for li in range(m, 0, -1): sk = bk[li][sj]; cuts.append((sk, sj)); sj = sk
cuts.reverse()
cues = [{"id": l["id"], "start": round(LEAD + segs[a][0], 3), "end": round(LEAD + segs[b - 1][1], 3)} for l, (a, b) in zip(lines, cuts)]
out = np.concatenate([np.zeros(int(LEAD * SR)), x])
with wave.open(os.path.join(B, "vo.wav"), "wb") as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((out * 32767).astype(np.int16).tobytes())
dur = round(LEAD + len(x) / SR + TAIL, 2)
json.dump({"cues": cues, "duration": dur}, open(os.path.join(B, "cues.json"), "w"), indent=1)
for c, l in zip(cues, lines): print(f'{c["start"]:6.2f}-{c["end"]:6.2f}  {l["text"]}')
print(f"segments {n}, video {dur}s")
