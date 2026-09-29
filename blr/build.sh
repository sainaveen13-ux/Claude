#!/bin/sh
# Builds the two outputs from app.html:
#   dist/artifact.html  page fragment for the claude.ai artifact preview
#   index.html          full document for GitHub Pages
set -e
cd "$(dirname "$0")"
mkdir -p dist
python3 - <<'PY'
import json
app = open('app.html').read()
geo = open('geo.js').read()
plots = 'window.PLOTS=' + json.dumps(json.load(open('plots.json'))['plots'], separators=(',', ':')) + ';'
page = app.replace('/*GEO*/', geo).replace('/*PLOTS*/', plots)
open('dist/artifact.html', 'w').write(page)
open('index.html', 'w').write('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n</head>\n<body>\n' + page + '\n</body>\n</html>\n')
print('built', len(page), 'bytes')
PY
