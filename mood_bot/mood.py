import pandas as pd
import random
import os
from datetime import datetime
from textblob import TextBlob


# Step 1: Mood detection
"""def detect_mood(user_input):
    blob = TextBlob(user_input)
    polarity = blob.sentiment.polarity  # -1 = very negative, +1 = very positive

    if polarity > 0.3:
        return "happy"
    elif polarity < -0.3:
        return "sad"
    else: 
        return "neutral"
        """
def determine_mood(text: str) -> str:
    text = text.lower()

    if any(word in text for word in ["sad", "depressed", "unhappy", "down"]):
        return "sad"
    elif any(word in text for word in ["angry", "mad", "furious", "annoyed"]):
        return "angry"
    elif any(word in text for word in ["stressed", "overwhelmed", "anxious", "tense"]):
        return "stressed"
    elif any(word in text for word in ["lonely", "alone", "isolated"]):
        return "lonely"
    elif any(word in text for word in ["happy", "joy", "excited", "glad", "cheerful"]):
        return "happy"
    else:
        return "neutral"



# Step 2: Load recommendations
def load_recommendations():
    df = pd.read_csv("recommendations.csv")  # must exist in same folder
    recs = {}

    for _, row in df.iterrows():
        mood = row["mood"]
        suggestion = row["recommendation"]

        if mood not in recs:
            recs[mood] = []

        recs[mood].append(suggestion)

    return recs


recommendations = load_recommendations()


# Step 3: Recommendation function
def recommend(mood):
    if mood not in recommendations:
        mood = "neutral"

    suggestion = random.choice(recommendations[mood])
    return suggestion


# Step 4: Save history
def save_history(user_input, mood, suggestion):
    history_file = "mood_history.csv"
    new_entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "user_input": user_input,
        "detected_mood": mood,
        "recommendation": suggestion
    }

    if os.path.exists(history_file):
        df = pd.read_csv(history_file)
        df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
    else:
        df = pd.DataFrame([new_entry])

    df.to_csv(history_file, index=False)


# Step 5: View history
def view_history():
    history_file = "mood_history.csv"
    if not os.path.exists(history_file):
        print("\n📜 No history yet.")
        return

    df = pd.read_csv(history_file)
    print("\n📜 Your History:")
    for i, row in df.iterrows():
        print(f"{i+1}. Mood: {row['detected_mood']} → Recommendation: {row['recommendation']}")


# Step 6: Chatbot
def chat():
    print("👋 Hi! I’m your Mood Recommender Bot.")
    print("Type 'exit', 'quit', or 'bye' anytime to stop.\n")
    print("💡 Type 'history' anytime to see your past moods.\n")

    while True:
        user_input = input("How are you feeling today? \n👉 ")

        if user_input.lower() in ["exit", "quit", "bye"]:
            print("👋 Goodbye! Hope I brightened your mood 💖")
            break

        if user_input.lower() == "history":
            view_history()
            continue

        mood = determine_mood(user_input)
        print(f"\nI think you're feeling: {mood} 💡")

        suggestion = recommend(mood)
        print(f"✨ Recommendation for you: {suggestion}\n")

        save_history(user_input, mood, suggestion)


if __name__ == "__main__":
    chat()
