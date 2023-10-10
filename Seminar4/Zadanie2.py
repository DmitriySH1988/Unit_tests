# Задание 2. У вас есть класс BookService, который использует интерфейс BookRepository для получения
# информации о книгах из базы данных. Ваша задача написать unit-тесты для BookService, используя
# Mockito для создания мок-объекта BookRepository.

from unittest import TestCase
from unittest.mock import Mock

class Book:
    def __init__(self, id, title):
        self.id = id
        self.title = title

class BookRepository:
    def getAllBooks(self):
        pass

    def getBookById(self, id):
        pass

    def addBook(self, book):
        pass

    def updateBook(self, book):
        pass

    def deleteBook(self, id):
        pass

class BookService:
    def __init__(self, repository):
        self.repository = repository

    def getAllBooks(self):
        return self.repository.getAllBooks()

    def getBookById(self, id):
        return self.repository.getBookById(id)

    def addBook(self, book):
        self.repository.addBook(book)

    def updateBook(self, book):
        self.repository.updateBook(book)

    def deleteBook(self, id):
        self.repository.deleteBook(id)

class BookServiceTest(TestCase):
    def test_getAllBooks(self):
        # Создаем мок объект BookRepository
        repository_mock = Mock(spec=BookRepository)

        # Создаем объект BookService, передавая в него мок
        service = BookService(repository_mock)

        # Задаем ожидаемое поведение для метода getAllBooks()
        repository_mock.getAllBooks.return_value = [
            Book(1, "Book 1"),
            Book(2, "Book 2")
        ]

        # Вызываем метод, который тестируем
        books = service.getAllBooks()

        # Проверяем результат
        self.assertEqual(len(books), 2)
        self.assertEqual(books[0].title, "Book 1")
        self.assertEqual(books[1].title, "Book 2")

        # Проверяем, был ли метод вызван
        repository_mock.getAllBooks.assert_called_once()

    # Аналогично пишем тесты для остальных методов
