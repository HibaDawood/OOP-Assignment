<h1>OOP Practice Assignments in Python</h1>
This collection includes 21 hands-on exercises to master core Object-Oriented Programming (OOP) concepts using Python. Each exercise is standalone, with a dedicated file (e.g., exercise.py) containing functional code and explanatory comments.

<h1>🧠 Assignment Overview</h1>

1. **Using self**: Create `Student` class, use `self` to set `name` & `marks`, add `display()` to print details.  
2. **Using cls**: Create `Counter` class, track object count with class variable & method using `cls`.  
3. **Public Variables/Methods**: Create `Car` class with public `brand` & `start()`, access both externally.  
4. **Class Variables/Methods**: Create `Bank` class with `bank_name`, add `change_bank_name(cls, name)` to update it for all instances.  
5. **Static Methods**: Create `MathUtils` class with static method `add(a, b)` to return sum, no class/instance variables.  
6. **Constructors/Destructors**: Create `Logger` class, print messages on object creation & destruction.  
7. **Access Modifiers**: Create `Employee` class with public `name`, protected `_salary`, private `__ssn`, test access.  
8. **super()**: Create `Person` class to set name, inherit `Teacher`, add `subject`, use `super()` to call parent constructor.  
9. **Abstract Classes**: Use `abc` to create `Shape` with abstract `area()`, inherit `Rectangle` to implement `area()`.  
10. **Instance Methods**: Create `Dog` class with `name` & `breed`, add `bark()` to print message with name.  
11. **Class Methods**: Create `Book` class with `total_books`, add `increment_book_count()` to increase count.  
12. **Static Methods**: Create `TemperatureConverter` with static `celsius_to_fahrenheit(c)` to return Fahrenheit.  
13. **Composition**: Create `Engine` & `Car`, pass `Engine` to `Car` during init, access `Engine` method via `Car`.  
14. **Aggregation**: Create `Department` & `Employee`, use aggregation to store independent `Employee` in `Department`.  
15. **MRO & Diamond Inheritance**: Create `A`, `B`, `C`, `D` classes, override `show()` in `B` & `C`, `D` inherits both, test MRO.  
16. **Function Decorators**: Write `log_function_call` decorator to print message before `say_hello()` executes.  
17. **Class Decorators**: Create `add_greeting` decorator to add `greet()` method to `Person` class.  
18. **Property Decorators**: Create `Product` with private `_price`, use `@property`, `@setter`, `@deleter` to manage it.  
19. **callable() & __call__()**: Create `Multiplier`, set factor, use `__call__()` to multiply input, test with `callable()`.  
20. **Custom Exception**: Create `InvalidAgeError`, raise in `check_age(age)` if age < 18, handle with try-except.  
21. **Custom Iterable**: Create `Countdown`, take start number, use `__iter__()` & `__next__()` to count down to 0 in for-loop.

<h1>✅ How to Execute</h1>
Enter the assignment folder, e.g., cd 01_Using_Self
Run the script with:python app.py
<h1>📚 Prerequisites</h1>
Requires only a standard Python 3+ installation, no external libraries needed.
<h1>🎓 Learning Goals</h1>

These exercises aim to teach:

Object initialization and manipulation
Access and visibility rules
Inheritance and method behavior
Abstract design patterns
Decorator applications
Custom object capabilities
Dive into Python OOP and enjoy the journey! 🌟
