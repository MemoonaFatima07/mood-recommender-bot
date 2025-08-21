# Mood Recommendation Bot (Python)

A tiny terminal bot that:
1) Detects your mood from text using NLP (NLTK VADER)
2) Recommends songs and/or movies that match or gently lift your mood
3) Offers a short, supportive message

## Quick Start

```bash
# 1) (Optional) Create a virtual environment
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# 2) Install dependencies
pip install -r requirements.txt

# 3) Run the bot
python app.py
```

Then type how you feel (e.g., "I'm feeling down and anxious") and follow the prompt
to get song/movie suggestions.

## How it works
- **Mood detection**: keyword overrides (angry/lonely/stressed) + VADER sentiment for happy/sad/neutral.
- **Recommendations**: simple content-based rules that select items tagged with your mood from `data/*.csv`.

## Next steps / Upgrades
- Add Spotify & TMDB APIs for richer, personalized picks
- Use a transformer emotion classifier (e.g., `transformers` with a small `distilbert` model)
- Keep history per user to learn preferences (collaborative filtering)
- Deploy as a Telegram bot (`python-telegram-bot`) or a web app (Streamlit/Flask)

---

Built for learning: simple, readable, and easy to extend.
