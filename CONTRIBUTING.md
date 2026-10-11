# Mitmachen

## So läuft ein Beitrag

1. Oben rechts auf **Fork** klicken. Du bekommst eine eigene Kopie des Projekts.
2. In deiner Kopie ändern, was du verbessern möchtest. Kleine Änderungen gehen direkt im Browser (Stift-Symbol an einer Datei).
3. **Pull Request** öffnen und kurz beschreiben, was du geändert hast und warum.
4. Die automatische Mushaf-Prüfung läuft. Danach schaut sich ein Betreuer die Änderung an und übernimmt sie.

Fehler oder Ideen ohne eigene Änderung? Einfach ein **Issue** anlegen.

## Wo was steht

- **Texte, Wiederholungen, Übersetzungen:** `data/lesen.json` (Leseseite) und `data/player.json` (Player).
- **Aussehen und Bedienung:** `index.html` und `lesen.html`. Alles in einer Datei, ohne Build-Schritt.

Ein Eintrag in `data/player.json` besteht aus Abschnitten (`segs`):

| `k` | Bedeutung |
| --- | --- |
| `q` | Koran-Abschnitt. `f` = Datei `SSSAAA` bei everyayah.com, `a`/`b` = Start und Ende in ms, `w` = Wörter, `t` = Zeitmarken je Wort |
| `rec` | Eigene Aufnahme in `audio/hisn/`, `a`/`b` = Ausschnitt in ms |
| `self` | Keine Aufnahme: der Player hält an, man liest selbst und tippt auf „Weiter“ |

## Regeln für den Korantext

- Koranverse werden **nie von Hand abgetippt**. Sie stammen aus dem Uthmani-Text (Hafs) und werden automatisch geprüft (`tools/check_quran.py`).
- Bitte keine Rechtschreib-„Korrekturen“ am uthmanischen Schriftbild (z. B. `ٱلصَّلَوٰةَ`). Das ist so richtig.

## Besonders gesucht

- **Aufnahmen der Bittgebete**, die noch „selbst lesen“ sind, mit genau dem Wortlaut aus `data/lesen.json`. Bitte nur eigene Aufnahmen oder Aufnahmen mit klarer Erlaubnis.
- Übersetzungen in weitere Sprachen.

## Lizenz

Mit einem Beitrag erklärst du dich einverstanden, dass er unter den Lizenzen dieses Projekts steht (siehe `LICENSE` und `CREDITS.md`).
