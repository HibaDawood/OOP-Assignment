# 3. Public Variables and Methods
# Assignment:
# Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.

class Car:
    brand = "Temerario"

    def start(self):
        print("Vroom vroom! Car started with style!")

car = Car() 
print(car.brand) 
car.start()  