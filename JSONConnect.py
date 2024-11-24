import json


"""Класс для работы с JSON-файлами, отвечает за загрузку и сохранение данных."""
class JSON:

    """данная функция загружает данные из JSON файла"""
    @staticmethod
    def load(file: str) -> list:
        try:
            with open(file, 'r', encoding='utf-8') as db:
                content = db.read()
                return json.loads(content) if content.strip() else []

        except FileNotFoundError:
            print(f'Файл {file} не найден. Возвращен пустой список.')
            return []
        except json.JSONDecodeError:
            print(f'Ошибка чтения JSON из файла {file}.')
            return []
        except Exception as e:
            print(f'Ошибка при загрузке {file}: {e}')
            return []

    """функция для добавления новых книг"""

    @staticmethod
    def save(file: str, books: list) -> None:
        try:
            with open(file, 'w', encoding='utf-8') as db:
                json.dump([book.__dict__ for book in books], db, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f'Ошибка при сохранении {file}: {e}')