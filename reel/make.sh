#!/bin/sh
# One command: voiceover (Gemini TTS) -> cues -> music + SFX -> frames -> final MP4.
# Needs GEMINI_API_KEY. Pass --dry to test the pipeline with silent placeholder voice lines.
set -e
cd "$(dirname "$0")"
pip install -q --break-system-packages numpy imageio-ffmpeg 2>/dev/null || true
FF=$(python3 -c "import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())")
[ -d node_modules/playwright ] || npm install --silent
python3 tts.py "$@"
python3 -c "import json;open('build/cues.js','w').write('window.CUES='+open('build/cues.json').read()+';')"
python3 music.py
python3 sfx.py
python3 -m http.server 8767 >/dev/null 2>&1 & SRV=$!
sleep 1
node render.mjs
kill $SRV
DUR=$(python3 -c "import json;print(json.load(open('build/cues.json'))['duration'])")
$FF -hide_banner -loglevel error -y -framerate 30 -i build/frames/f%05d.jpg -i build/vo.wav -i build/music.wav -i build/sfx.wav -filter_complex "\
[1:a]aresample=48000,aformat=channel_layouts=stereo,apad,atrim=0:$DUR,volume=1.3,asplit=2[vo][key];\
[2:a]aresample=48000,atrim=0:$DUR,volume=0.30[mus];\
[mus][key]sidechaincompress=threshold=0.04:ratio=6:attack=15:release=300[duck];\
[3:a]aresample=48000,aformat=channel_layouts=stereo,volume=0.5[fx];\
[vo][duck][fx]amix=inputs=3:normalize=0:duration=first,loudnorm=I=-14:TP=-1.5:LRA=11,aformat=channel_layouts=stereo[a]" \
-map 0:v -map "[a]" -c:v libx264 -preset slow -crf 18 -pix_fmt yuv420p -c:a aac -b:a 192k -ar 48000 -movflags +faststart -shortest build/ten-rupee-estates-reel.mp4
echo "done: reel/build/ten-rupee-estates-reel.mp4 (${DUR}s)"
