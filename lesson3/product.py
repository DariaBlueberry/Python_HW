class Product:
    name = "Name"
    price = 'Price'

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def cost(self, amount):
        print(self.name, 'стоит', self.price, 'рублей')