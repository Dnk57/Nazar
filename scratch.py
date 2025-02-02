class Book:
    """Базовый класс книги."""

    def __init__(self, name: str, author: str):
        self._name = name  # Защищенные атрибуты
        self._author = author

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages  # Используем свойство для проверки

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, value: int):
        if not isinstance(value, int):
            raise ValueError("Количество страниц должно быть целым числом")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = value

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration  # Используем свойство для проверки

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, value: float):
        if not isinstance(value, (int, float)):
            raise ValueError("Продолжительность должна быть числом")
        if value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом")
        self._duration = float(value)

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"


# Проверка работы
if __name__ == "__main__":
    try:
        # Создание экземпляров
        book = Book("Война и мир", "Лев Толстой")
        print(book)  # Книга Война и мир. Автор Лев Толстой
        print(repr(book))  # Book(name='Война и мир', author='Лев Толстой')

        paper_book = PaperBook("1984", "Джордж Оруэлл", 328)
        print(paper_book)  # Книга 1984. Автор Джордж Оруэлл
        print(repr(paper_book))  # PaperBook(name='1984', author='Джордж Оруэлл', pages=328)

        audio_book = AudioBook("Мастер и Маргарита", "Михаил Булгаков", 15.5)
        print(audio_book)  # Книга Мастер и Маргарита. Автор Михаил Булгаков
        print(repr(audio_book))  # AudioBook(name='Мастер и Маргарита', author='Михаил Булгаков', duration=15.5)

        # Попытка изменить недоступные атрибуты
        book.name = "Новое название"  # AttributeError
    except Exception as e:
        print(f"Ошибка: {e}")

    # Проверка валидации
    try:
        invalid_paper_book = PaperBook("Тест", "Автор", -10)  # ValueError
    except ValueError as ve:
        print(f"Ошибка валидации: {ve}")

    try:
        invalid_audio_book = AudioBook("Тест", "Автор", -5.0)  # ValueError
    except ValueError as ve:
        print(f"Ошибка валидации: {ve}")