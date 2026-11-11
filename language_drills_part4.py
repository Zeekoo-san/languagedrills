# === Stage 4: Редактирование записей ===
# Project: LanguageDrills
from datetime import date


ALLOWED_FIELDS = ("word", "language", "level")


class Word:
    def __init__(self, word, language, level, next_review):
        self.word = word
        self.language = language
        self.level = level
        self.next_review = next_review

    def __eq__(self, other):
        return (
            isinstance(other, Word)
            and self.word == other.word
            and self.language == other.language
            and self.level == other.level
            and self.next_review == other.next_review
        )


def patch_word(word, changes):
    allowed = set(ALLOWED_FIELDS)
    new = dict(word)
    for key, value in changes.items():
        if key not in allowed:
            raise ValueError(f"Поле '{key}' нельзя менять")
        new[key] = value
    return Word(new["word"], new["language"], new["level"], new["next_review"])


if __name__ == "__main__":
    original = Word("hello", "en", 3, date(2025, 1, 1))
    updated = patch_word(original, {"word": "hi", "level": 4})
    print(updated)
    try:
        patch_word(original, {"next_review": date(2030, 1, 1)})
    except ValueError as err:
        print(err)
