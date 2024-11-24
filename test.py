import unittest
from unittest.mock import patch, mock_open
from library import Book


class TestBook(unittest.TestCase):
    def test_init(self):
        book = Book(1, 'Test Book', 'Test Author', 2023)
        self.assertEqual(book.book_id, 1)
        self.assertEqual(book.title, 'Test Book')
        self.assertEqual(book.author, 'Test Author')
        self.assertEqual(book.year, 2023)
        self.assertEqual(book.status, 'в наличии')


if __name__ == '__main__':
    unittest.main()
