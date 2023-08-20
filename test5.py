# Створити батьківський клас, тобто якась абстракція - Тварина, Машина, Персонаж гри, Ноутбук, загалом будь-що абстрактне.
# В цьому класі створити 2 методи, будь-яких.
# Також має бути __init__ з декільками атрибутами.
# А також створити два дочірніх класи, які будуть мати додаткові атрибути окрім батьківських
# Показати виклики цього всьго, що воно записалось, напрклад за допомогою print(...)

class Clothes:
    def __init__(self, type, color) -> None:
        self.type = type
        self.color = color

class Shoes(Clothes):
    def __init__(self, type, color, brand):
        self.brand = brand
        super().__init__(type, color)

think1 = Shoes("Sneakers", "White", "Nike")

class Hat(Clothes):
    def __init__(self, type, color, brand, inscription):
        self.brand = brand
        self.inscription = inscription
        super().__init__(type, color)

think2 = Hat("Cap", "Dark-green", " New York Yankees" , "Logo of brand")


print(f"Тип взуття - {think1.type}\nКолір взуття - {think1.color}\nБренд - {think1.brand}\n")

print(f"Тип - {think2.type}\nКолір - {think2.color}\nБренд - {think2.brand}\nНадпис - {think2.inscription}")
