class Animal:
    """
       Базовый класс, представляющий животное.
       - name (str): Имя животного.
       - age (int): Возраст животного.
       - species (str): Вид животного.
       """
    def __init__(self, name: str, age: int, species: str):
        self.name = name
        self.age = age
        self.species = species
    def __str__(self) -> str:
        return f"Животное: {self.name}, Возраст: {self.age}, Вид: {self.species}"

    def __repr__(self) -> str:
        return f"Animal(name={self.name}, age={self.age}, species={self.species})"

    def make(self) -> str:
        return f"{self.name} издает звук."

    def eat(self, food: str) -> str:
        return f"{self.name} ест {food}."


class Dog(Animal):
    """
    Дочерний класс, представляющий собаку.
    - name (str): Имя собаки.
    - age (int): Возраст собаки.
    - breed (str): Порода собаки.
    """

    def __init__(self, name: str, age: int, breed: str):
        super().__init__(name, age, species="Собака")
        self.breed = breed

    def __str__(self) -> str:
        return f"Собака: {self.name}, Возраст: {self.age}, Порода: {self.breed}"

    def __repr__(self) -> str:
        return f"Dog(name={self.name}, age={self.age}, breed={self.breed})"

    def make(self) -> str:
        return f"{self.name} лает: Гав-гав!"

    def fetch(self, item: str) -> str:
        return f"{self.name} приносит {item}."

