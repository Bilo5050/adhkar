#!/usr/bin/env python3
"""Mushaf-Prüfung: gleicht jeden Koranvers in data/player.json und data/lesen.json
Zeichen für Zeichen mit dem Uthmani-Text (Hafs) aus dem Paket quran-json ab.

Aufruf:  python3 tools/check_quran.py <pfad/zu/quran.json>
Quelle:  https://www.npmjs.com/package/quran-json (Text: The Noble Qur'an Encyclopedia, quranenc.com)
"""
import json, re, sys, unicodedata

N = lambda s: unicodedata.normalize("NFC", s)
quran = json.load(open(sys.argv[1], encoding="utf-8"))
player = json.load(open("data/player.json", encoding="utf-8"))
lesen = json.load(open("data/lesen.json", encoding="utf-8"))

def verse_words(s, v):
    return N(quran[s - 1]["verses"][v - 1]["text"].replace("۞", "")).split()

errors = []
runs = []          # contiguous recited word runs: (surah, ayah, first_word, last_word)

def item_lists():
    for sec in player:
        for it in sec["items"]:
            for key in ("segs", "segsE"):
                if it.get(key):
                    yield it["title"], it[key]
            if it.get("tail"):
                yield it["title"] + " (Wiederholung)", it["tail"]["segs"]

for title, segs in item_lists():
    cur = None
    for g in segs:
        if g.get("k") != "q":
            cur = None          # anything else in between (e.g. a reader's insertion) breaks the run
            continue
        s, v = int(g["f"][:3]), int(g["f"][3:])
        ref = verse_words(s, v)
        words = [N(w) for w in g["w"]]
        if len(g.get("t", [])) != len(words):
            errors.append(f"{title}: Zeitmarken passen nicht zur Wortzahl in {s}:{v}")
        # the phrase must be a contiguous, unchanged slice of the verse
        hit = next((i for i in range(len(ref) - len(words) + 1) if ref[i:i + len(words)] == words), None)
        if hit is None:
            errors.append(f"{title}: Abschnitt weicht vom Mushaf ab ({s}:{v}): {' '.join(words)}")
            cur = None
            continue
        end = hit + len(words) - 1
        if cur and cur[0] == s and cur[1] == v and cur[3] + 1 == hit:
            cur[3] = end
        else:
            cur = [s, v, hit, end]
            runs.append(cur)

# every recited passage must also stand unchanged on the reading page
# (brackets and verse-number markers between words are allowed there)
read_text = N(" ".join(it["ar_read"] for sec in lesen for it in sec["items"]))
read_text = re.sub(r"﴿[٠-٩]+﴾|[()]", " ", read_text)
read_text = re.sub(r"\s+", " ", read_text)
seen = set()
for s, v, a, b in runs:
    if (s, v, a, b) in seen:
        continue
    seen.add((s, v, a, b))
    phrase = " ".join(verse_words(s, v)[a:b + 1])
    if phrase not in read_text:
        errors.append(f"Leseseite: {s}:{v} fehlt oder weicht vom Mushaf ab")

used = {(s, v) for s, v, a, b in runs}

if errors:
    print("Mushaf-Prüfung FEHLGESCHLAGEN:")
    for e in errors:
        print("  -", e)
    sys.exit(1)
print(f"Mushaf-Prüfung bestanden: {len(used)} Verse, alle Zeichen identisch.")
