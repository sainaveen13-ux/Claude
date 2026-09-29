"""Generate the voiceover line by line with Gemini TTS and write cue times.

Needs GEMINI_API_KEY in the environment. Optional: TTS_MODEL, TTS_VOICE.
--dry makes silent placeholder lines (for testing the pipeline without a key).
Outputs: build/vo.wav, build/cues.json
"""
import base64, json, os, sys, time, urllib.request, wave, struct

HERE = os.path.dirname(os.path.abspath(__file__)); B = os.path.join(HERE, "build"); os.makedirs(B, exist_ok=True)
cfg = json.load(open(os.path.join(HERE, "lines.json")))
DRY = "--dry" in sys.argv
MODEL = os.environ.get("TTS_MODEL", "gemini-2.5-flash-preview-tts")
VOICE = os.environ.get("TTS_VOICE", "Puck")
SR, LEAD, GAP = 24000, 0.35, 0.22          # sample rate, silence before first line, gap between lines

def tts(text):
    key = os.environ["GEMINI_API_KEY"]
    body = {"contents": [{"parts": [{"text": f"{cfg['style']} {text}"}]}],
            "generationConfig": {"responseModalities": ["AUDIO"],
                                 "speechConfig": {"voiceConfig": {"prebuiltVoiceConfig": {"voiceName": VOICE}}}}}
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"
    for attempt in range(5):
        try:
            req = urllib.request.Request(url, json.dumps(body).encode(), {"Content-Type": "application/json", "x-goog-api-key": key})
            data = json.load(urllib.request.urlopen(req, timeout=120))
            part = data["candidates"][0]["content"]["parts"][0]["inlineData"]
            return base64.b64decode(part["data"])          # 16-bit mono PCM at 24 kHz
        except Exception as e:
            print("  retry", attempt + 1, e); time.sleep(2 ** attempt)
    sys.exit(f"TTS failed for: {text}")

def trim(pcm, thr=500):
    """Strip leading/trailing near-silence so gaps are consistent."""
    n = len(pcm) // 2; s = struct.unpack(f"<{n}h", pcm)
    i = next((k for k in range(n) if abs(s[k]) > thr), 0); j = next((k for k in range(n - 1, -1, -1) if abs(s[k]) > thr), n - 1)
    i = max(0, i - int(.03 * SR)); j = min(n, j + int(.08 * SR))
    return pcm[i * 2:j * 2]

out, cues, t = bytearray(b"\0\0" * int(LEAD * SR)), [], LEAD
for ln in cfg["lines"]:
    print("line:", ln["id"])
    pcm = bytes(int(len(ln["text"].split()) / 2.9 * SR) * 2) if DRY else trim(tts(ln["text"]))
    d = len(pcm) / 2 / SR
    cues.append({"id": ln["id"], "start": round(t, 3), "end": round(t + d, 3)})
    out += pcm + bytes(int(GAP * SR) * 2); t += d + GAP
with wave.open(os.path.join(B, "vo.wav"), "wb") as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(bytes(out))
json.dump({"cues": cues, "duration": round(t + 2.0, 2)}, open(os.path.join(B, "cues.json"), "w"), indent=1)
print(f"voiceover {t:.1f}s, video {t + 2:.1f}s")
