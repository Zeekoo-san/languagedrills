# === Stage 6: Связанная сущность ===
# Project: LanguageDrills
from datetime import date, timedelta


class Repeat:
    def __init__(self, word_id, interval_days):
        self.word_id = word_id
        self.interval_days = interval_days
        self.created = date.today()
        self.next_due = self.created + timedelta(days=interval_days)
        self.correct = 0
        self.incorrect = 0
        self.last_reviewed = None

    def __repr__(self):
        return (
            f"Repeat(word_id={self.word_id}, "
            f"interval_days={self.interval_days}, "
            f"next_due={self.next_due}, "
            f"correct={self.correct}, incorrect={self.incorrect})"
        )
