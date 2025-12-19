# Rectangle Class (Basic OOP)
class RectangleBasic:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# Employee Class (Class Method)
class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    @classmethod
    def from_string(cls, employee_str):
        name, emp_id, salary = employee_str.split(",")
        return cls(name, emp_id, float(salary))

    def display_employee_info(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.employee_id}")
        print(f"Salary: {self.salary}")


# Polymorphism Example
class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):
    def move(self):
        print("Car is driving")

class Bike(Vehicle):
    def move(self):
        print("Bike is cycling")


# Operator Overloading
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y  # Dot product

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


# Abstraction & Inheritance
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area()")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


def print_shape_area(shape: Shape):
    print(f"Area = {shape.area()}")


# TESTING 
print("=== RectangleBasic Test ===")
r1 = RectangleBasic(5, 3)
print("Area:", r1.area())
print("Perimeter:", r1.perimeter())

print("\n=== Employee Test ===")
emp1 = Employee.from_string("John Doe,E123,50000")
emp1.display_employee_info()

print("\n=== Polymorphism Test ===")
vehicles = [Vehicle(), Car(), Bike()]
for v in vehicles:
    v.move()

print("\n=== Vector Test ===")
v1 = Vector(4, 3)
v2 = Vector(1, 1)
print("Subtraction:", v1 - v2)
print("Dot Product:", v1 * v2)

print("\n=== Shape Abstraction Test ===")
shapes = [
    Circle(3),
    Rectangle(4, 6)
]
for shape in shapes:
    print_shape_area(shape)
