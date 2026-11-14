# === Stage 5: Удаление и восстановление ===
# Project: LanguageDrills
import datetime


class SoftDeletedWord:
    """Слово, помеченное на мягкое удаление.

    Хранит состояние до удаления и флаги, чтобы можно было восстановить
    исходную сущность «слово».
    """

    def __init__(self, word, language, level, next_review_date=None):
        self.id = word.get("id")
        self.word = word.get("word")
        self.language = word.get("language")
        self.level = word.get("level")
        self.next_review_date = next_review_date
        self.deleted_at = datetime.datetime.now()
        self.hard_deleted = False

    def to_dict(self):
        return {
            "id": self.id,
            "word": self.word,
            "language": self.language,
            "level": self.level,
            "next_review_date": self.next_review_date,
            "deleted_at": self.deleted_at.isoformat(),
            "hard_deleted": self.hard_deleted,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            word=data.get("word"),
            language=data.get("language"),
            level=data.get("level"),
            next_review_date=data.get("next_review_date"),
        )

    def restore(self):
        """Восстанавливает исходное состояние слова."""
        self.deleted_at = None
        self.hard_deleted = False


def soft_delete_word(word, reason="user_request"):
    """Мягкое удаление слова: помечает его, не удаляя физически.

    Возвращает объект SoftDeletedWord для последующего восстановления.
    """
    soft_word = SoftDeletedWord(word, word.get("language"), word.get("level"))
    soft_word.deleted_at = datetime.datetime.now()
    soft_word.reason = reason
    return soft_word


def hard_delete_word(word):
    """Жёсткое удаление слова — полное удаление из хранилища."""
    return True


def restore_word(soft_word):
    """Восстанавливает слово из мягкого состояния."""
    if soft_word is not None:
        soft_word.restore()
    return soft_word
