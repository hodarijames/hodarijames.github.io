#!/usr/bin/env python3
"""Pre-commit sanity check for the ISLANDS Lab site.

Run from the repo root:   python3 tools/check_site.py
Exits non-zero if anything looks wrong. Nothing here touches files.
"""
import re, sys, pathlib
from html.parser import HTMLParser

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGES = ['index.html','home.html','research.html','people.html',
         'publications.html','resources.html','library.html']
problems, notes = [], []

def flag(page, msg): problems.append(f"{page}: {msg}")
def note(page, msg): notes.append(f"{page}: {msg}")

class Links(HTMLParser):
    def __init__(self): super().__init__(); self.refs=[]
    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        for k in ('href','src'):
            if d.get(k): self.refs.append((tag, k, d[k]))

# ---- 1. internal links and images resolve -------------------------------
for page in PAGES:
    f = ROOT/page
    if not f.exists():
        flag(page, "page missing"); continue
    p = Links(); p.feed(f.read_text(encoding='utf-8', errors='replace'))
    for tag, attr, ref in p.refs:
        if re.match(r'^(https?:|mailto:|#|data:|//)', ref): continue
        target = (ROOT / ref.split('#')[0].split('?')[0])
        if not target.exists():
            flag(page, f"broken {tag} {attr} -> {ref}")

# ---- 2. placeholders ----------------------------------------------------
for page in PAGES:
    f = ROOT/page
    if not f.exists(): continue
    txt = f.read_text(encoding='utf-8', errors='replace')
    for token in ('TODO','FIXME','Lorem ipsum','XXXX','PLACEHOLDER'):
        if token.lower() in txt.lower(): flag(page, f"placeholder {token!r}")

# ---- 3. names spelled one way ------------------------------------------
# wrong form -> right form
NAMES = {
    r'\bSebastian Carrazco': 'Sebastián Carrazco',
    r'\bMakayla Jennings\b': 'Makaila Jennings',
    r'\bAbel Mendez\b': 'Abel Méndez',
    r'\bJacinda Byham\b': 'Jacinda Byam',
    r'\bKayla Roper\b': 'Kayla Gossett Roper',
}
for page in PAGES:
    f = ROOT/page
    if not f.exists(): continue
    txt = f.read_text(encoding='utf-8', errors='replace')
    txt_dec = txt.replace('&aacute;','á').replace('&eacute;','é')
    for bad, good in NAMES.items():
        if re.search(bad, txt_dec): flag(page, f"name: use '{good}'")

# ---- 4. survey numbers stay canonical ----------------------------------
# 615 observed / 580 analyzed / 33 pc / 7.4% (43) / 8.8% (51) / 529 mature
BANNED = {
    r'\b665 K Dwarfs\b': 'sample size is 615 observed, 580 analyzed',
    r'\b100 light-?years\b': '33 parsecs is the survey limit (about 108 light-years)',
}
for page in PAGES:
    f = ROOT/page
    if not f.exists(): continue
    txt = f.read_text(encoding='utf-8', errors='replace')
    for bad, why in BANNED.items():
        if re.search(bad, txt, re.I): flag(page, f"number: {why}")

# ---- 5. titles that are no longer current ------------------------------
STALE = [r'Co-?Director']
for page in PAGES:
    f = ROOT/page
    if not f.exists(): continue
    txt = f.read_text(encoding='utf-8', errors='replace')
    for bad in STALE:
        if re.search(bad, txt, re.I): flag(page, "stale title 'Co-Director' (stepped down July 2026)")

# ---- 6. share metadata present -----------------------------------------
NEEDS_META = ['index.html','home.html','research.html','people.html',
              'publications.html','resources.html']
for page in NEEDS_META:
    f = ROOT/page
    if not f.exists(): continue
    txt = f.read_text(encoding='utf-8', errors='replace')
    for needle, label in [('name="description"','meta description'),
                          ('og:image','og:image'),
                          ('rel="icon"','favicon')]:
        if needle not in txt: flag(page, f"missing {label}")

# ---- 7. gated material must not appear ---------------------------------
GATED = {
    r'COMPASS': 'COMPASS award is embargoed until the Notice of Award',
    r'80NSSC26K1248': 'grant number is embargoed until the Notice of Award',
    r'NRB\s*19770816B': 'Wow! repetition is embargoed until Méndez et al. is public',
    r'horn ambiguity': 'Wow! repetition is embargoed until Méndez et al. is public',
}
for page in PAGES:
    f = ROOT/page
    if not f.exists(): continue
    txt = f.read_text(encoding='utf-8', errors='replace')
    for bad, why in GATED.items():
        if re.search(bad, txt, re.I): flag(page, f"EMBARGOED: {why}")

# ---- report -------------------------------------------------------------
if notes:
    print("Notes:")
    for n in notes: print("  -", n)
if problems:
    print(f"\n{len(problems)} problem(s):")
    for p in problems: print("  x", p)
    sys.exit(1)
print(f"All checks passed across {len(PAGES)} pages.")
