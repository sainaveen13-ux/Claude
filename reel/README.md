# Ten Rupee Estates reel (50–55s)

Run `./make.sh` to get `build/ten-rupee-estates-reel.mp4`.

The build runs in this order:
1. `tts.py` has **Gemini TTS** read `lines.json` one line at a time, in an energetic, sarcastic Indian-English delivery. It writes `build/vo.wav` and the exact start and end time of each line.
2. `music.py` composes a 112 BPM music bed in code (plucks, bass, claps, tabla-style drum), matched to the voiceover length.
3. `sfx.py` synthesises the sound effects, each tied to a voiceover line.
4. `render.mjs` renders `reel.html` frame by frame at 30 fps and 1080×1920. Every animation is keyed to the voiceover cues, so changing the voice never breaks sync.
5. ffmpeg mixes the voice, music (ducked under the voice) and effects to −14 LUFS and encodes H.264.

Requirements: `GEMINI_API_KEY` set in the environment. Optional: `TTS_VOICE` (default `Puck`) and `TTS_MODEL` (default `gemini-2.5-flash-preview-tts`).
Test without a key: `./make.sh --dry` (silent placeholder voice).
Edit the script in `lines.json`. Keep the `id`s, because the animations refer to them.
