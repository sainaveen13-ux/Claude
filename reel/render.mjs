// Render every frame of reel.html. Usage: node render.mjs [--keyframes t1 t2 ...]
import { chromium } from 'playwright';
import fs from 'fs';
const FPS = 30, cues = JSON.parse(fs.readFileSync('build/cues.json')), DUR = cues.duration;
const args = process.argv.slice(2), kf = args[0] === '--keyframes' ? args.slice(1).map(Number) : null;
fs.mkdirSync(kf ? 'build/kf' : 'build/frames', { recursive: true });
const exe = fs.existsSync('/opt/pw-browsers/chromium') ? '/opt/pw-browsers/chromium' : undefined;
const b = await chromium.launch({ executablePath: exe });
const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
const errs = []; p.on('pageerror', e => errs.push(e.message));
await p.goto('http://localhost:8767/reel.html'); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(500);
const times = kf || Array.from({ length: Math.round(FPS * DUR) }, (_, i) => i / FPS);
for (let i = 0; i < times.length; i++) {
  await p.evaluate(t => render(t), times[i]);
  await p.screenshot({ path: kf ? `build/kf/k${String(i).padStart(2, '0')}.jpg` : `build/frames/f${String(i).padStart(5, '0')}.jpg`, type: 'jpeg', quality: kf ? 70 : 92 });
}
console.log(kf ? 'keyframes' : 'frames', times.length, errs.length ? 'ERRORS ' + errs.join(' | ') : 'no errors'); await b.close();
