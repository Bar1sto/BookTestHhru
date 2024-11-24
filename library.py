import json
from JSONConnect import JSON

"""данный класс является моделью книги для управления бибилиотекой и имеет атрибуты"""
"""атрибуты:"""
"""book_id (int) - является уникальным идентификатором книги (ID)"""
"""title (str)- название книги"""
"""author (str) - автор книги"""
"""year (int) - год издания книги"""
"""status (str) - статус книги (в наличии или выдана)"""


class Book:
    def __init__(self, book_id: int, title: str, author: str, year: int, status: str = 'в наличии'):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def __str__(self):
        return f"ID: {self.book_id}, Название: {self.title}, Автор: {self.author}, Год: {self.year}, Статус: {self.status}"

    """функция для добавления новых книг"""
    @staticmethod
    def add_book() -> None:
        title = input("Введите название книги: ")
        author = input("Введите автора книги: ")
        try:
            year = int(input("Введите год издания книги: "))
        except ValueError:
            print("Год должен быть числом!")
            return

        books = [Book(**data) for data in JSON.load('db.json')]
        book_id = max((book.book_id for book in books), default=0) + 1
        new_book = Book(book_id, title, author, year)

        # добавляем объект книги
        books.append(new_book)
        JSON.save('db.json', books)
        print(f'Книга "{title}" добавлена с ID {book_id}.')

    """функция занимается удалением книг по ID"""
    @staticmethod
    def remove_book() -> None:
        try:
            book_id = int(input("Введите ID книги для удаления: "))
        except ValueError:
            print("ID должен быть числом!")
            return

        books = [Book(**data) for data in JSON.load('db.json')]
        updated_books = [book for book in books if book.book_id != book_id]

        if len(updated_books) == len(books):
            print(f"Книга с ID {book_id} не найдена.")
        else:
            JSON.save('db.json', updated_books)
            print(f"Книга с ID {book_id} успешно удалена.")

    """функция занимается удалением книг по ID"""
    @staticmethod
    def search_books() -> None:
        title = input("Введите название книги (или оставьте пустым): ").strip()
        author = input("Введите автора книги (или оставьте пустым): ").strip()
        year_input = input("Введите год издания книги (или оставьте пустым): ").strip()
        """проверка на правильность ввода года"""
        try:
            year = int(year_input) if year_input else None
        except ValueError:
            print("Год должен быть числом или пустым!")
            return

        """получение все книг из json'а и поиск нужной книги"""
        books = [Book(**data) for data in JSON.load('db.json')]
        found = False
        for book in books:
            if (title.lower() in book.title.lower() or not title) and \
                    (author.lower() in book.author.lower() or not author) and \
                    (year is None or book.year == year):
                print(f"ID: {book.book_id}, Название: {book.title}, Автор: {book.author}, "
                      f"Год: {book.year}, Статус: {book.status}")
                found = True

        if not found:
            print("Книга не найдена.")

    """данная функция выводит все книги"""
    @staticmethod
    def list_books() -> None:
        books = JSON.load('db.json')
        if not books:
            print("Библиотека пуста")
        else:
            for book in books:
                print(book)

    """данная функция измененяет статус книг по ID"""
    @staticmethod
    def change_status() -> None:
        try:
            book_id = int(input("Введите ID книги для изменения статуса: "))
            status = input("Введите новый статус книги: ")
        except ValueError:
            print("ID должен быть числом!")
            return
        """внесение нового статуса и его сохранение"""
        books = [Book(**data) for data in JSON.load('db.json')]
        for book in books:
            if book.book_id == book_id:
                book.status = status
                JSON.save('db.json', books)
                print(f"Статус книги с ID {book_id} успешно изменен на '{status}'.")
                return

        print(f"Книга с ID {book_id} не найдена.")

"""главная функция"""
def main():
    """цикл while нужен чтобы вывести консольный интерфейс и получить ввод от пользователя (обработка действий)"""
    while True:
        print("\nВыберите действие:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Найти книгу")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("6. Выйти")

        try:
            action = int(input("Введите номер действия: "))
        except ValueError:
            print("Введите число от 1 до 6.")
            continue

        match action:
            case 1:
                Book.add_book()
            case 2:
                Book.remove_book()
            case 3:
                Book.search_books()
            case 4:
                Book.list_books()
            case 5:
                Book.change_status()
            case 6:
                print("Выход из программы.")
                break
            case _:
                print("Неверный ввод, попробуйте снова.")


if __name__ == "__main__":
    main()
