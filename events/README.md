# Events

Each event has its own folder, named `YYYY-MM-DD-short-name`. A folder holds:

- `README.md`: the event's documentation: details and titles in all three languages, links (registration, calendar, directions), its designs, the website text, and notes on how it went.
- `calendar.ics`: the file behind the website's "Add to Calendar" button.
- `photos/` (optional): web copies of event photos, shown on the website in a popup behind a **Show photos** button.
- Original photos, straight from the camera: kept in the folder on the drive, but never published (`.gitignore` excludes them).

The designs themselves stay in `assets/artboards/`, because the design canvas and the export script work from there. Each event's README links to its designs.

Everything in this folder is published on the website, so keep private details (participants, contacts, budgets) out of it.

## All events

| Date | Event | Language | Status |
|---|---|---|---|
| 2026-11-07 | [Berlin Voted — Now What? · برلين صوّتت، هلأ شو؟](2026-11-07-berlin-voted/README.md) | Arabic | Past |

## Adding an event

1. Copy [`_template/`](_template/) to `events/YYYY-MM-DD-short-name/` and fill in its `README.md`.
2. Make its `calendar.ics`. Copy the one from a previous event and change the `UID`, the dates (in UTC), `SUMMARY`, `DESCRIPTION` and `LOCATION`.
3. On the website, copy an `<article class="event-card">` in `index.html` into `#events-upcoming`. Set its `data-end` (with time zone) and its links, including `href="events/<folder>/calendar.ics"`. Add its text keys in all three languages in `translations.js`. Once the end time has passed, the event moves to **Past Events** by itself.
4. Add a row to the table above.
5. After the event, fill in **How it went** in its README and change its status to past.

## Adding photos to an event

1. Put the original photos in the event's folder. They stay private.
2. Make web copies in `photos/`, named `photo-1.jpg`, `photo-1-thumb.jpg`, `photo-2.jpg`… (1600 px and 640 px wide), with the camera metadata removed. GPS location in particular must go. Then add the copyright to their metadata: `Copyright (c) <year> EnCompass e.V. - encompass.ngo`, author `EnCompass e.V.`. Ask Claude, or use any image tool that strips metadata on export and lets you set copyright.
3. In `index.html`, add an `event-gallery` block to the event's card (copy the one from Berlin Voted). Point it at the new photos, and set the count in the button.
4. Add a short description for each photo in all three languages in `translations.js` (`events.eN.photo1`, …).
5. Make sure the people pictured are OK with being published.
