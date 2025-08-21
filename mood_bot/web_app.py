import streamlit as st
from mood import determine_mood
from recommender import Recommender

# Comfort messages
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

# App setup
st.set_page_config(page_title="Mood Recommender Bot", page_icon="🎧")
st.title("🎧 Mood Recommender Bot")
st.write("Tell me how you're feeling, and I'll suggest something for you 💡")

# Load recommender
rec = Recommender(songs_csv="data/songs.csv", movies_csv="data/movies.csv")

# User input
user_input = st.text_input("How are you feeling today?")

if user_input:
    mood = determine_mood(user_input)
    comfort_message = COMFORT.get(mood, ["I'm here for you."])[0]

    # Show detected mood & comfort
    st.subheader(f"🧠 I sense you're **{mood}**")
    st.write(f"💬 {comfort_message}")

    # Ask preference
    pref = st.radio("What would you like me to recommend?", ["Song", "Movie", "Both"])

    # Recommendations
    if pref in {"Song", "Both"}:
        songs = rec.recommend_songs(mood, n=3)
        if songs:
            st.write("🎵 **Songs you might like:**")
            for title, artist in songs:
                dash = f" — {artist}" if artist else ""
                st.write(f"- {title}{dash}")

    if pref in {"Movie", "Both"}:
        movies = rec.recommend_movies(mood, n=3)
        if movies:
            st.write("🎬 **Movies you might like:**")
            for title, year in movies:
                yr = f" ({year})" if year else ""
                st.write(f"- {title}{yr}")
