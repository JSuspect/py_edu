class Dog:
    # Атрибуты класса
    species = 'Canis familiaris'

    # Атрибуты экземпляра определяются в методе '__init__'
    # Такой метод называется dunder 
    # dunder — сокращение от double underscores, то есть двойное подчеркивание
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    # Спациальный dunder метод '__str__' позволяет выводить c помощью функции ptint() более осмысденную информацию
    def __str__(self):
        return f'{self.name} is {self.age} years old'

    # Метод экземпляра
    def description(self):
        return f'{self.name} is {self.age} years old'
    
    # Другой метод экземпляра
    def speak(self, sound):
        return f"{self.name} says {sound}"
    
    # Атрибуты экземпляра (dunder метод — сокращение от double underscores, то есть двойное подчеркивание).

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self) -> str:
        return f'The {self.color} car has {self.mileage:,}'
    
    def drive(self, miles):
        self.mileage = self.mileage + miles
