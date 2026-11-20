# === Stage 8: Генерация идентификаторов ===
# Project: LanguageDrills
import string
import uuid

PROJECT_PREFIX = "ld"


def generate_unique_id(prefix: str = PROJECT_PREFIX, length: int = 12) -> str:
    """Генерирует уникальный идентификатор с заданным префиксом проекта.

    Использует префикс и случайные символы из набора, проверяя коллизии
    с уже существующими идентификаторами, переданными в отдельном списке.
    """
    alphabet = string.ascii_lowercase + string.digits
    while True:
        random_part = "".join(alphabet[i % len(alphabet)] for i in range(length))
        candidate = f"{prefix}-{random_part}"
        if candidate not in existing_ids:
            return candidate


existing_ids: set[str] = set()


def register_id(id_value: str) -> None:
    """Регистрирует идентификатор для последующей проверки на коллизии."""
    existing_ids.add(id_value)


def is_duplicate(id_value: str) -> bool:
    """Проверяет, является ли переданный идентификатор дубликатом."""
    return id_value in existing_ids


def clear_existing_ids() -> None:
    """Очищает хранилище уже зарегистрированных идентификаторов."""
    existing_ids.clear()


def generate_batch_ids(count: int, prefix: str = PROJECT_PREFIX, length: int = 12) -> list[str]:
    """Генерирует список уникальных идентификаторов без коллизий между собой."""
    generated: list[str] = []
    while len(generated) < count:
        candidate = generate_unique_id(prefix, length)
        if not is_duplicate(candidate):
            generated.append(candidate)
    return generated
