import doctest

class Fabric:
    def __int__(self, density: float , material : str):
        """
        Создание и подготовка к работе объекта "Ткань"
        :param density: плотность ткани
        :param material: Материал ткани
        """

        if not isinstance(density,(int, float)):
            raise TypeError ("Плотность ткани должна быть типа int или float")
        if density <= 0 :
            raise ValueError("Плотность ткани не может быть отрицательной")
        self.density = density

        if not isinstance(material,(str)):
            raise TypeError ("Материал ткани должен быть str")
        self.material = material

    def cheking_the_density (self)-> bool:
        """
        Функция которая проверяет плотная ли ткань
        :return: Плотность
        """

    def checking_the_material (self) -> bool:
        """
        Функция которая проверяет из какого материала выполнена ткань

        :return: Материал
        """
        ...

class bag:
    def __int__(self, size : float ,capacity : float):
        """
        Создание и подготовка к работе объекта "Сумка"
        :param size: Размер сумки
        :param capacity: Вместимость сумки
        """

        if not isinstance(size,(int,float)):
            raise TypeError("Размер сумки должна быть int или float")
        if size <= 0:
            raise ValueError("Размер сумки не должен быть отрицательным ")
        self.size = size

        if not isinstance(capacity,(int,float)):
            raise TypeError("Вместимость сумки должна быть int или float")
        if capacity < 0:
            raise ValueError("Вместимость сумки не может быть отрицательным числом")
        self.capacity = capacity
    def measure_size(self) -> bool:
        """
        Функция которая узнает точные размеры сумки

        :return: Является ли сумка большой
        """
        ...
    def checking_bag(self) -> bool:
        """
        Функция которая проверяет вместимость в сумке
        :return: Является ли сумка пустой
        """
        ...
class music:
    def __int__(self, duration: int , author : str):
        """
        Создание и подготовка к работе объекта "Музыка"
        :param duration: Продолжительность трека
        :param author: Исполнитель песни
        """
        if not isinstance(duration,(int)):
            raise TypeError("Продолжительность трека должно быть int")
        if duration < 0:
            raise ValueError("Продолжительность трека не может быть отрицательным числом")
        self.duration = duration
        if not isinstance(author,(str)):
            raise TypeError("Исполнитель песни должен быть str")
        self.author = author

    def listen_to_the_song (self)-> bool:
        """
        Функция которая прослушает песни и выявит её продолжительность

        :return: Продолжительность песни не большая
        """
        ...
    def read_the_information (self) -> bool:
        """
        Функция которая прочитает информацию о песне и узнает всю информацию
        :return: Исполнитель песни
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
    pass