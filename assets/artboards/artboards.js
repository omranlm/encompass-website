// The list of artboards, shared by designs.html and export.py.
// Keep this as plain JSON after the "=" so export.py can read it.
// w/h: size in CSS pixels. row: canvas row. page: optional PDF page size (defaults to w × h px).
window.ARTBOARDS = [
  {"file": "visual-identity",     "title": "Visual Identity",              "w": 1600, "h": 1200, "row": 0},
  {"file": "logo",                "title": "Logo",                         "w": 1600, "h": 800,  "row": 0},
  {"file": "google-form-header",  "title": "Google Form header",           "w": 1600, "h": 400,  "row": 0, "note": "4 : 1"},
  {"file": "instagram-post",      "title": "Instagram post",               "w": 1080, "h": 1080, "row": 1},
  {"file": "carousel-1-event-ar", "title": "Carousel 1 · Event (Arabic)",  "w": 1080, "h": 1080, "row": 1},
  {"file": "carousel-2-about",    "title": "Carousel 2 · About EnCompass", "w": 1080, "h": 1080, "row": 1},
  {"file": "print-poster-a3",     "title": "Print poster · A3",            "w": 1123, "h": 1587, "row": 1, "page": "297mm 420mm", "note": "297 × 420 mm"},
  {"file": "print-poster-a3-fun", "title": "Print poster · A3 · Fun",      "w": 1123, "h": 1587, "row": 1, "page": "297mm 420mm", "note": "297 × 420 mm"}
];
