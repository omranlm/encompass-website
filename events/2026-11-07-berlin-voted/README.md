# Berlin Voted — Now What? · برلين صوّتت، هلأ شو؟

**Status:** past event (7 November 2026)

## Details

| | |
|---|---|
| **Format** | Open discussion (حوار مفتوح) |
| **Language** | Arabic |
| **Date** | Saturday, 7 November 2026 |
| **Time** | 19:00 (Berlin time). The end time isn't on any material; 21:00 is assumed in the calendar file and the website |
| **Venue** | Casino for Social Medicine, Sonnenallee 100, 12045 Berlin |
| **Topic** | The results of the Berlin election and what happened afterwards |
| **Host** | EnCompass e.V. |

### Titles

| Where | Arabic | German | English |
|---|---|---|---|
| Posters, carousel, Google Form (colloquial) | برلين صوتت، هلأ شو؟ | — | — |
| Instagram post (official titles) | برلين صوتت: قراءة في نتائج الانتخابات | Berlin wählt: Die Wahl entschlüsselt — eine offene Diskussion | Berlin Votes: Decoding the Election — an open discussion |
| Website | برلين صوّتت، هلأ شو؟ | Berlin hat gewählt — und jetzt? | Berlin Voted — Now What? |

## Links

| | |
|---|---|
| **Registration** (Google Form) | https://forms.gle/igDyNW962T2jzQc28 |
| **Calendar** (Google Calendar, used by the poster QR codes) | https://calendar.app.google/beVnvqMKg3gZF25q9 |
| **Calendar file** (website "Add to Calendar" button) | [`calendar.ics`](calendar.ics) |
| **Directions** | [Google Maps](https://www.google.com/maps/search/?api=1&query=Sonnenallee+100,+12045+Berlin) |
| **Website** | https://encompass.ngo/#events |

## Designs

Edit the source in `assets/artboards/`, then run `python assets/export.py <name>` to refresh the downloads. All of them are also on the design canvas, [`assets/designs.html`](../../assets/designs.html).

| Design | Size | Source | Exports |
|---|---|---|---|
| Instagram post (AR / DE / EN, QR to directions) | 1080 × 1080 | [`instagram-post.html`](../../assets/artboards/instagram-post.html) | [PNG](../../assets/exports/instagram-post.png) · [JPG](../../assets/exports/instagram-post.jpg) · [PDF](../../assets/exports/instagram-post.pdf) |
| Carousel 1, event in Arabic (QR to calendar) | 1080 × 1080 | [`carousel-1-event-ar.html`](../../assets/artboards/carousel-1-event-ar.html) | [PNG](../../assets/exports/carousel-1-event-ar.png) · [JPG](../../assets/exports/carousel-1-event-ar.jpg) · [PDF](../../assets/exports/carousel-1-event-ar.pdf) |
| A3 print poster (QR to calendar and to registration) | 297 × 420 mm | [`print-poster-a3.html`](../../assets/artboards/print-poster-a3.html) | [PDF](../../assets/exports/print-poster-a3.pdf) · [PNG](../../assets/exports/print-poster-a3.png) |
| A3 print poster, fun version (QR to calendar and to registration) | 297 × 420 mm | [`print-poster-a3-fun.html`](../../assets/artboards/print-poster-a3-fun.html) | [PDF](../../assets/exports/print-poster-a3-fun.pdf) · [PNG](../../assets/exports/print-poster-a3-fun.png) |
| Google Form header (no QR) | 1600 × 400 | [`google-form-header.html`](../../assets/artboards/google-form-header.html) | [PNG](../../assets/exports/google-form-header.png) · [PNG @2x](../../assets/exports/google-form-header@2x.png) |

## Registration form text

The introduction written for the Google Form, in the posters' colloquial Arabic:

> **برلين صوّتت، هلأ شو؟ 🗳️**
>
> مرحبا! 👋
>
> الانتخابات خلصت، والنتائج صارت معروفة… بس شو يعني هالشي إلنا؟
> تعوا نقعد سوا ونحكي بصراحة عن نتائج الانتخابات بـبرلين، وشو صار بعدين، وكيف ممكن تأثر علينا وعلى حياتنا هون.
>
> حوار مفتوح بالعربي، بلا رسميات، وكل الآراء أهلا وسهلا فيها. 💬
>
> 📅 إيمتى؟ السبت 7 تشرين التاني (نوفمبر) 2026 · الساعة 7 المسا
> 📍 وين؟ Casino for Social Medicine — Sonnenallee 100, 12045 Berlin
>
> الأماكن محدودة، فسجّلوا من هون لنعرف قديش نحضّر 🙏
> ومنتشرّف إذا جبتوا معكن صحابكن!
>
> — فريق إنكومباس
> encompass.ngo

## On the website

- The event card is in `index.html` (`#events`), with `data-end="2026-11-07T21:00:00+01:00"`. It has moved to **Past Events** automatically since then.
- Its text keys in `translations.js` are `events.e1.tag`, `events.e1.title`, `events.e1.body`, `events.e1.pastBody` and `events.e1.when`.

## Photos

| File | Shows |
|---|---|
| [`photos/photo-1.jpg`](photos/photo-1.jpg) | Participants sitting in a circle during the discussion |
| [`photos/photo-2.jpg`](photos/photo-2.jpg) | The same circle a few seconds later |
| [`photos/photo-3.jpg`](photos/photo-3.jpg) | The discussion seen from the back of the room, under the Casino for Social Medicine sign |

- The files in `photos/` are web copies: 1600 px wide (plus a 640 px `-thumb` preview each), with **all camera metadata removed** (no GPS location, phone model or time).
- **Copyright:** © 2026 EnCompass e.V. All rights reserved. Each web copy carries this in its metadata (`Copyright (c) 2026 EnCompass e.V. - encompass.ngo`, author `EnCompass e.V.`), and the website's photo popup shows "Photo: © EnCompass e.V." under every photo. Reuse needs written permission from EnCompass e.V. (info@encompass.ngo).
- The full-size originals stay in this folder on the drive only. `.gitignore` keeps them out of git and off the website.
- On the website, the photos only load when a visitor clicks **Show photos**, and they open in a popup. Their descriptions (for screen readers and the popup caption) are the keys `events.e1.photo1`–`photo3` in `translations.js`.
- Participants' faces are recognizable. They were published at the organizers' decision. If anyone asks to be removed, delete the photo from `photos/` and its `<a>` line in `index.html`.

## How it went

*To fill in after the event. This file is published on the website, so leave out anything private, such as participants' names or contact details.*

- **Registrations:**
- **Attendance:**
- **Speakers / moderation:**
- **Main topics raised:**
- **Photos / media:** three photos of the discussion circle at the venue, taken 20:03–20:17. They're on the website behind the event's **Show photos** button (see *Photos* below).
- **What to keep or change next time:**
- **Follow-up:**
