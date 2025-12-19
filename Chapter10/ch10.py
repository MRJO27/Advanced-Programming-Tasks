# 1. Context Manager - Timer
print("\n1. Context Manager - Timer")

import time

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        end = time.time()
        duration = end - self.start
        print(f"Execution took {duration:.2f} seconds")

print("Testing Timer:")
with Timer():
    for i in range(1000000):
        pass


# 2. Generator - even_numbers(n)
def even_numbers(n):
    for num in range(2, n + 1, 2):
        yield num

print("Even numbers up to 10:")
for num in even_numbers(10):
    print(num, end=" ")
print()


# 3. Coroutine - filter_positive()
def filter_positive():
    while True:
        num = yield
        if num > 0:
            print(f"Positive number: {num}")

print("Testing filter_positive coroutine:")
co = filter_positive()
next(co)
co.send(-3)
co.send(5)
co.send(0)


# 4. Factory Pattern - shape_factory()
class Circle:
    def draw(self):
        print("Drawing a Circle")

class Square:
    def draw(self):
        print("Drawing a Square")

def shape_factory(shape_type):
    if shape_type == "circle":
        return Circle()
    elif shape_type == "square":
        return Square()
    else:
        raise ValueError("Unknown shape type")

print("Testing shape factory:")
shape = shape_factory("circle")
shape.draw()

shape2 = shape_factory("square")
shape2.draw()

# 5. Observer Pattern
class Subject:
    def __init__(self):
        self.observers = []
    
    def attach(self, observer):
        self.observers.append(observer)
    
    def notify(self, message):
        for observer in self.observers:
            observer.update(message)

class Observer:
    def update(self, message):
        print(f"Received update: {message}")

print("Testing Observer pattern:")
subject = Subject()
obs1 = Observer()
obs2 = Observer()
subject.attach(obs1)
subject.attach(obs2)
subject.notify("Update available!")
