"""Render every artboard to downloadable files in assets/exports/.

    python assets/export.py              # all artboards
    python assets/export.py logo         # only the ones named

For each artboard it writes:
    <name>.png       exact size (1x)
    <name>@2x.png    double resolution
    <name>.jpg       exact size, JPEG (needs Pillow: pip install pillow)
    <name>.pdf       one page at the artboard size (A3 for the poster), text stays vector

Needs Google Chrome, Chromium or Microsoft Edge. Set CHROME=/path/to/browser to choose one.
Run it again after editing an artboard so the downloads on the canvas stay up to date.
"""
import json, os, shutil, subprocess, sys, tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
BOARDS_DIR = HERE / 'artboards'
OUT = HERE / 'exports'

CANDIDATES = [
    os.environ.get('CHROME'),
    r'C:\Program Files\Google\Chrome\Application\chrome.exe',
    r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
    r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe',
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    '/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge',
    shutil.which('google-chrome'), shutil.which('chromium'), shutil.which('chromium-browser'),
    shutil.which('chrome'), shutil.which('msedge'),
]


def find_browser():
    for c in CANDIDATES:
        if c and Path(c).exists():
            return c
    sys.exit('Could not find Chrome or Edge. Set CHROME=/path/to/browser and try again.')


def load_artboards():
    text = (BOARDS_DIR / 'artboards.js').read_text(encoding='utf-8')
    body = text.split('window.ARTBOARDS =', 1)[1].strip().rstrip(';')
    return json.loads(body)


def chrome(browser, profile, *args):
    cmd = [browser, '--headless=new', '--disable-gpu', '--hide-scrollbars',
           '--user-data-dir=' + profile, '--virtual-time-budget=5000', *args]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=120)


def export(browser, profile, b):
    name, w, h = b['file'], b['w'], b['h']
    url = (BOARDS_DIR / (name + '.html')).as_uri()
    png = OUT / (name + '.png')

    for scale, target in ((1, png), (2, OUT / (name + '@2x.png'))):
        chrome(browser, profile, '--window-size=%d,%d' % (w, h),
               '--force-device-scale-factor=%d' % scale, '--screenshot=' + str(target), url)

    chrome(browser, profile, '--no-pdf-header-footer', '--print-to-pdf=' + str(OUT / (name + '.pdf')), url)

    try:
        from PIL import Image
        Image.open(png).convert('RGB').save(OUT / (name + '.jpg'), quality=92, optimize=True, progressive=True)
    except ImportError:
        print('  (skipped JPG: install Pillow with "pip install pillow")')

    files = sorted(p.name for p in OUT.glob(name + '*') if p.suffix in ('.png', '.jpg', '.pdf'))
    print('%-22s %s' % (name, '  '.join(files)))


def main():
    browser = find_browser()
    boards = load_artboards()
    wanted = set(sys.argv[1:])
    unknown = wanted - {b['file'] for b in boards}
    if unknown:
        sys.exit('Unknown artboard(s): ' + ', '.join(sorted(unknown)))
    OUT.mkdir(exist_ok=True)
    profile = tempfile.mkdtemp(prefix='encompass-export-')
    try:
        for b in boards:
            if not wanted or b['file'] in wanted:
                export(browser, profile, b)
    finally:
        shutil.rmtree(profile, ignore_errors=True)


if __name__ == '__main__':
    main()
