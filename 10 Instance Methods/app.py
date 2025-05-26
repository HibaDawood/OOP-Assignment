# 10. Instance Methods
# Assignment:
# Create a class Dog with instance variables name and breed. Add an instance method bark() that prints a message including the dog's name.

class Dog:

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"Meet my dog {self.name},  simple, sweet, and full of love.")

my_dog = Dog( "Nova", "Husky")
my_dog.bark()
