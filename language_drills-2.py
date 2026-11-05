# === Stage 2: Проверка полей ===
# Project: LanguageDrills
import datetime


def normalize_language(raw):
    value = (raw or "").strip().lower()
    if value == "":
        return None
    aliases = {
        "русский": "ru",
        "английский": "en",
        "немецкий": "de",
        "французский": "fr",
        "испанский": "es",
        "итальянский": "it",
        "китайский": "zh",
        "японский": "ja",
        "корейский": "ko",
        "арабский": "ar",
    }
    return aliases.get(value)


def normalize_word(raw):
    value = (raw or "").strip()
    if value == "":
        return None
    return value


def normalize_level(raw):
    value = (raw or "").strip().lower()
    if value in ("beginner", "новичок", "1"):
        return 1
    if value in ("intermediate", "средний", "2"):
        return 2
    if value in ("advanced", "продвинутый", "3"):
        return 3
    return None


def normalize_next_date(raw):
    raw = (raw or "").strip()
    if raw == "":
        return None
    if raw.lower() in ("today", "сегодня"):
        return datetime.date.today()
    try:
        return datetime.datetime.strptime(raw, "%Y-%m-%d").date()
    except ValueError:
        return None


def validate_word(word, language, level, next_date):
    errors = []
    if word is None or word == "":
        errors.append("Необходимо ввести слово.")
    elif len(word) > 50:
        errors.append("Слово не может быть длиннее 50 символов.")

    if language is None:
        errors.append("Выберите язык.")
    elif len(language) > 10:
        errors.append("Неверный формат языка.")

    if level is None:
        errors.append("Укажите уровень сложности.")
    elif not isinstance(level, int):
        errors.append("Уровень должен быть целым числом.")

    if next_date is None:
        errors.append("Укажите дату следующего повторения.")
    elif next_date < datetime.date.today():
        errors.append("Дата не может быть в прошлом.")
    return errors
