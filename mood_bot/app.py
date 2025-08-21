from __future__ import annotations
import sys
from typing import Optional

from mood import determine_mood
from recommender import Recommender

COMFORT = {
    "sad": [
        "I'm really sorry you're feeling low. You're not alone; I'm here with you.",
        "Small steps count. Be gentle with yourself today.",
    ],
    "stressed": [
        "Breathe in for 4, hold 4, out for 6. Let's slow things down together.",
        "You're carrying a lot. It's okay to pause and rest.",
    ],
    "angry": [
        "It's valid to feel angry. Want to vent a bit more? I'm listening.",
        "Let's channel that energy. A walk or some music might help.",
    ],
    "lonely": [
        "I hear you. Loneliness is tough — but you are worthy of connection.",
        "Would you like a few uplifting songs or a cozy movie?",
    ],
    "happy": [
        "Love that energy! Let's keep the vibe going 🔥",
        "Awesome! How about something to celebrate the mood?",
    ],
    "neutral": [
        "Got it. Maybe we can nudge the mood upwards a bit?",
        "Chill vibes. Want something calm or energizing?",
    ],
}

def main(data_dir: Optional[str] = None) -> None:
    data_dir = data_dir or "data"
    rec = Recommender(songs_csv=f"{data_dir}/songs.csv", movies_csv=f"{data_dir}/movies.csv")

    print("🎧 Mood Recommender Bot")
    print("Tell me how you're feeling (type 'exit' to quit).")
    while True:
        try:
            text = input("\nYou: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBot: Take care ❤️")
            break
        if text.lower() in {"exit", "quit", "bye"}:
            print("Bot: Take care ❤️")
            break

        mood = determine_mood(text)
        comfort = COMFORT.get(mood, ["I'm here."])[0]
        print(f"Bot: I sense you're {mood}. {comfort}")

        # Ask preference
        pref = input("Do you want a song, a movie, or both? [song/movie/both]: ").strip().lower()
        if pref not in {"song", "movie", "both"}:
            pref = "both"

        if pref in {"song", "both"}:
            songs = rec.recommend_songs(mood, n=3)
            if songs:
                print("\n🎵 Songs you might like:")
                for title, artist in songs:
                    dash = f" — {artist}" if artist else ""
                    print(f"  • {title}{dash}")
        if pref in {"movie", "both"}:
            movies = rec.recommend_movies(mood, n=3)
            if movies:
                print("\n🎬 Movies you might like:")
                for title, year in movies:
                    yr = f" ({year})" if year else ""
                    print(f"  • {title}{yr}")

        print("\n(You can type more about how you feel, or 'exit' to quit.)")

if __name__ == "__main__":
    main()
