# CropBoost v2 — Multilingual Flask Model (Offline-first)

**What’s new**
- Language selector with i18n JSON (English, Hindi, Gujarati, Marathi, Bengali, Punjabi, Tamil, Telugu, Kannada, Malayalam, Urdu, Odia, Nepali, Assamese + extensible).
- Training Hub with trusted video/PDF/web resources.
- Bigger, more readable UI and Voice Read Aloud.
- Crop calendars + soil/water/IPM knowledge.
- PWA basics (manifest + service worker).

## Run
```bash
pip install -r requirements.txt
python app.py
# open http://localhost:8000
```

## Structure
- `app.py` — Flask backend + APIs, i18n endpoint.
- `templates/index.html` — Tailwind SPA UI + calculators, charts.
- `data/` — snapshots: `mandi_prices.csv`, `weather.json`, `schemes.json`, `trainings.json`, `kvk.json`, `crop_guides.json`, `crop_calendar.json`, `farming_knowledge.json`
- `static/i18n/*.json` — translations.

> To add more languages, create `static/i18n/<lang>.json` with the same keys.
