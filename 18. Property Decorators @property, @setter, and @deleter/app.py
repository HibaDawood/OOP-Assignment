# 18. Property Decorators: @property, @setter, and @deleter
# Assignment:
# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.

class Product:

    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        print("Getting Price...")
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            print("Price cannot be negative!")

        else:
            print("Setting price...")
            self._price = value

    @price.deleter
    def price(self):
       print("Deleting price...")
       del self._price

p = Product(60000)
print(p.price)
p.price = 80000
print(p.price) 
p.price = -50 
del p.price          

