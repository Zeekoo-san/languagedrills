# === Stage 7: Связи между сущностями ===
# Project: LanguageDrills
from datetime import datetime


class Word:
    def __init__(self, word, language, level, next_review=None):
        self.word = word
        self.language = language
        self.level = level
        self.next_review = next_review


class Review:
    def __init__(self, word, scheduled_at, done_at=None, correct=None):
        self.word = word
        self.scheduled_at = scheduled_at
        self.done_at = done_at
        self.correct = correct


def get_reviews_for_word(word, reviews_by_word, now=None):
    now = now or datetime.now()
    if word is None or not reviews_by_word:
        return []
    scheduled = [
        review for review in reviews_by_word.get(word, [])
        if review.scheduled_at <= now
    ]
    for review in scheduled:
        if review.word is not word:
            raise ValueError(
                "Целостность нарушена: повтор ссылается на другое слово"
            )
    return scheduled


def check_word_reviews_integrity(word, reviews_by_word, now=None):
    reviews = get_reviews_for_word(word, reviews_by_word, now)
    if word is None:
        return False, reviews
    orphan_reviews = [
        review for review in reviews_by_word.get(word, [])
        if review.word is not word
    ]
    if orphan_reviews:
        return False, reviews
    return True, reviews


def build_reviews_by_word(reviews):
    index = {}
    for review in reviews:
        if review.word is None:
            continue
        index.setdefault(review.word, []).append(review)
    return index


def calculate_next_review(review):
    base = datetime(2000, 1, 1)
    if review.correct is None:
        return base + __import__("datetime").timedelta(days=1)
    if review.correct:
        return base + __import__("datetime").timedelta(days=7)
    return base + __import__("datetime").timedelta(days=30)
