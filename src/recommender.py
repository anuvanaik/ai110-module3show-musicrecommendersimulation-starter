import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def _score(self, user: UserProfile, song: Song) -> Tuple[float, List[str]]:
        """Scores one song against a user profile using the genre/mood/energy recipe."""
        score = 0.0
        reasons = []

        if song.genre == user.favorite_genre:
            score += 5.0
            reasons.append(f"Genre match: {song.genre}")

        if song.mood == user.favorite_mood:
            score += 3.0
            reasons.append(f"Mood match: {song.mood}")

        energy_similarity = max(0.0, 1.00 - abs(song.energy - user.target_energy))
        score += energy_similarity * 2.0
        reasons.append(f"Energy similarity: {energy_similarity:.2f} (song={song.energy}, target={user.target_energy})")

        if user.likes_acoustic and song.acousticness > 0.5:
            score += 2.0
            reasons.append(f"Acoustic match: {song.acousticness}")

        return score, reasons

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Returns the top-k songs for a user, ranked highest score first."""
        scored = [(song, *self._score(user, song)) for song in self.songs]
        scored.sort(key=lambda item: item[1], reverse=True)
        return [song for song, _, _ in scored[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Returns a string explaining why a song was recommended to a user."""
        _, reasons = self._score(user, song)
        return "; ".join(reasons)

def load_songs(csv_path: str) -> List[Dict]:
    """Loads songs from a CSV file into a list of dicts (required by src/main.py)."""
    songs = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            songs.append({
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": float(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            })
    print(f"Loaded songs: {len(songs)}")
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Scores a single song against user preferences (required by recommend_songs() and src/main.py)."""
    score = 0.0
    reasons = []

    if song["genre"] == user_prefs["genre"]:
        score += 5.0
        reasons.append(f"Genre match: {song['genre']}")

    if song["mood"] == user_prefs["mood"]:
        score += 3.0
        reasons.append(f"Mood match: {song['mood']}")

    energy_similarity = max(0.0, 1.00 - abs(song["energy"] - user_prefs["energy"]))
    score += energy_similarity * 2.0
    reasons.append(f"Energy similarity: {energy_similarity:.2f} (song={song['energy']}, target={user_prefs['energy']})")

    if user_prefs.get("likes_acoustic", False) and song["acousticness"] > 0.5:
        score += 2.0
        reasons.append(f"Acoustic match: {song['acousticness']}")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Functional implementation of the recommendation logic (required by src/main.py)."""
    scored = [(song, *score_song(user_prefs, song)) for song in songs]
    scored.sort(key=lambda item: item[1], reverse=True)
    return [(song, score, "; ".join(reasons)) for song, score, reasons in scored[:k]]
