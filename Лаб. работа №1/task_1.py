numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
a = numbers.index(None)
b = sum(x for x in numbers if x is not None)
c = b / len(numbers)
numbers[a] = c

# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers)
