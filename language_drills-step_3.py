# === Stage 3: Хранилище в памяти ===
# Project: LanguageDrills
import json
import os
from datetime import date


class WordStore:
    def __init__(self, filename="words.json"):
        self.filename = filename
        self.words = {}

    def load(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as f:
                self.words = json.load(f)

    def save(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.words, f, ensure_ascii=False, indent=2)

    def add(self, word, language, level, next_review=None):
        if next_review is None:
            next_review = date.today()
        word_id = f"{language}:{word}"
        self.words[word_id] = {
            "id": word_id,
            "word": word,
            "language": language,
            "level": level,
            "next_review": next_review.isoformat(),
        }
        self.save()
        return word_id

    def get(self, word_id):
        return self.words.get(word_id)

    def list(self, language=None):
        result = list(self.words.values())
        if language is not None:
            result = [w for w in result if w["language"] == language]
        return sorted(result, key=lambda w: (w["next_review"], w["word"]))


if __name__ == "__main__":
    store = WordStore()
    store.load()
    store.add("hello", "en", "beginner")
    store.add("привет", "ru", "beginner")
    store.add("goodbye", "en", "intermediate")
    for w in store.list("en"):
        print(w["word"], w["level"], w["next_review"])
    print(store.get("en:hello"))
