class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    def name(self):
        return self.name

    def author(self):
        return self.author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook:
    def __init__(self, name: str, author: str, pages: int):
        self.name = name
        self.author = author
        self.pages = pages

    def pages(self):
        return self.pages
    def pages(self, value):
        if not isinstance(value, int):
            raise TypeError("Pages must be an integer")
        if value <= 0:
            raise ValueError("'Pages must be a positive integer ")
        self.pages = value

    def __repr__(self):
        return
        f"Книга (name='{self.name}', author='{self.author}' pages={self.pages})"

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"


class AudioBook:
    def __init__(self, name: str, author: str, duration: float):
        self.name = name
        self.author = author
        self.duration = duration

    def duration(self):
        return self.duration

    def duration(self, value):
        if not isinstance (value, float):
            raise TypeError("Duration must be a float")
        if value < 0:
            raise ValueError("Duration must be a non-negative float")
        self.duration = value

    def __repr__(self):
        return
        f"Книга(name='{self.name}' author = '{self.author}' duration = {self.duration})"


    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"
