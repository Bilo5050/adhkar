# Adhkar – Morgen- und Abendgedenken · أذكار الصباح والمساء

Eine schlanke Web-App für die Morgen- und Abendgedenken: abspielen, pausieren, **mitsprechen** oder **nachsprechen**, mit echter Rezitation. Dazu eine reine Leseseite auf Arabisch in großer Schrift.

**▶ App öffnen:** https://bilo5050.github.io/adhkar/

| Seite | Inhalt |
| --- | --- |
| [`index.html`](index.html) | Player: Morgen / Abend / Freitag, Mitsprechen mit Wortmarkierung, Nachsprechen mit Pausen, Wiederholungen (3×, 7×, 25×) laufen automatisch |
| [`lesen.html`](lesen.html) | Nur Arabisch, Schriftgröße einstellbar, Koranverse im Schriftbild des Mushaf |

Die App braucht keinen Server, kein Konto und keine Installation. Sie läuft im Browser auf jedem Handy.

## Mitmachen

Jede Hilfe ist willkommen: Aufnahmen für die Bittgebete, Übersetzungen, Fehlerkorrekturen, Design. Wie das geht, steht in [CONTRIBUTING.md](CONTRIBUTING.md).

**Der Korantext ist geschützt.** Bei jeder Änderung gleicht eine automatische Prüfung jeden Vers Zeichen für Zeichen mit dem Mushaf (Hafs, uthmanische Schrift) ab. Weicht ein Zeichen ab, wird die Änderung rot markiert und nicht übernommen.

## Aufbau

```
index.html          Player
lesen.html          Leseseite (nur Arabisch)
data/player.json    Abspielfolge: Texte, Wiederholungen, Audio-Abschnitte mit Wort-Zeitmarken
data/lesen.json     Texte der Leseseite mit deutscher Übersetzung und Lautschrift
audio/hisn/         Aufnahmen aus Hisn al-Muslim (Hamad ad-Duraihim)
tools/              Mushaf-Prüfung
```

Die Koran-Rezitation (Mishary Rashid Alafasy) wird direkt von [everyayah.com](https://everyayah.com) abgespielt und liegt nicht in diesem Repository. Quellen und Lizenzen stehen in [CREDITS.md](CREDITS.md).

---

## العربية

تطبيق ويب بسيط لأذكار الصباح والمساء: تشغيل وإيقاف، مع إمكانية **الترديد مع القارئ** أو **الترديد بعده**، بتلاوة حقيقية للشيخ مشاري العفاسي. وصفحة للقراءة فقط بخط كبير.
المشاركة مفتوحة للجميع، ونصّ القرآن محميّ بفحص آلي يطابق كل آية حرفًا بحرف مع المصحف (رواية حفص).

## English

A lightweight web app for the morning and evening adhkar: play, pause, **recite along** or **repeat after** a real recitation (Mishary Alafasy), plus an Arabic-only reading page in large type. Contributions are welcome. Every Quran verse is checked automatically, character by character, against the Mushaf (Hafs) on each change.
