# 13. Composition
# Assignment:
# Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.

class Engine:
    def start(self):
        print("Car is started...")

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start_engine(self):
        self.engine.start()

engine = Engine()
car = Car(engine)
car.start_engine()