from __future__ import annotations
import random
from typing import List, Tuple

import pandas as pd

class Recommender:
    def __init__(self, songs_csv: str, movies_csv: str):
        self.songs = pd.read_csv(songs_csv)
        self.movies = pd.read_csv(movies_csv)

        # Normalize mood column
        for df in (self.songs, self.movies):
            df["mood"] = df["mood"].str.lower().str.strip()

    def _pick(self, df: pd.DataFrame, mood: str, n: int = 3) -> List[Tuple[str, str]]:
        if mood in set(df["mood"]):
            pool = df[df["mood"] == mood]
        elif "neutral" in set(df["mood"]):
            pool = df[df["mood"] == "neutral"]
        else:
            pool = df

        if pool.empty:
            return []

        sample = pool.sample(n=min(n, len(pool)), replace=False, random_state=random.randint(0, 2**32 - 1))
        results: List[Tuple[str, str]] = []
        if {"title", "artist"}.issubset(sample.columns):
            for _, r in sample.iterrows():
                results.append((str(r["title"]), str(r.get("artist", ""))))
        else:
            for _, r in sample.iterrows():
                results.append((str(r["title"]), str(r.get("year", ""))))
        return results

    def recommend_songs(self, mood: str, n: int = 3) -> List[Tuple[str, str]]:
        return self._pick(self.songs, mood, n)

    def recommend_movies(self, mood: str, n: int = 3) -> List[Tuple[str, str]]:
        return self._pick(self.movies, mood, n)
