# === Stage 1: Каркас модуля ===
# Project: LanguageDrills
from datetime import date

class Word:
    def __init__(self, word, language, level, next_review):
        self.word = word
        self.language = language
        self.level = level
        self.next_review = next_review

    def __str__(self):
        return f"{self.language}: {self.word} (уровень {self.level}, повтор: {self.next_review})"

def make_demo_words():
    return [
        Word("Привет", "ru", 1, date(2025, 1, 1)),
        Word("Hello", "en", 1, date(2025, 1, 1)),
        Word("Bonjour", "fr", 2, date(2025, 1, 2)),
        Word("Hola", "es", 3, date(2025, 1, 3)),
        Word("Guten Tag", "de", 1, date(2025, 1, 4)),
    ]

def main():
    words = make_demo_words()
    print("LanguageDrills — тренажёр языка")
    print("Демо-список слов:")
    for w in words:
        print("  " + str(w))
    print(f"Всего демо-слов: {len(words)}")

if __name__ == "__main__":
    main()
