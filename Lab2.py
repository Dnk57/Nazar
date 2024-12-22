class Book:
    def __init__(self, id_: int, name: str, pages: int):
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f'Book(id_={self.id}, name={repr(self.name)}, pages={self.pages})'


class Library:
    def __init__(self, books=None):
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self) -> int:
        if not self.books:
            return 1
        return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        """Возвращает индекс книги по её ID.
           Если книга не найдена, вызывает ValueError."""
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")

    def add_book(self, name: str, pages: int) -> None:
        """Добавляет новую книгу в библиотеку."""
        new_id = self.get_next_book_id()
        new_book = Book(id_=new_id, name=name, pages=pages)
        self.books.append(new_book)

    def __str__(self):
        return f'Библиотека содержит {len(self.books)} книг.'

    def __repr__(self):
        return f'Library(books={repr(self.books)})'


# Пример использования
if __name__ == "__main__":
    lib = Library()
    lib.add_book("Война и мир", 1225)
    lib.add_book("Преступление и наказание", 864)

    print(lib)
    print(lib.books)
    print(lib.books[0])

    try:
        index = lib.get_index_by_book_id(1)
        print(f'Индекс книги с ID 1: {index}')
    except ValueError as e:
        print(e)

    try:
        index = lib.get_index_by_book_id(3)
        print(f'Индекс книги с ID 3: {index}')
    except ValueError as e:
        print(e)