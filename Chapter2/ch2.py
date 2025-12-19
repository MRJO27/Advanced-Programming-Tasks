# 1) Vector3D Class with Operator Overloading
print("\n1) Vector3D Class with Operator Overloading")
print("-" * 40)

class Vector3D:
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z
  
  def __add__(self, other):
    if isinstance(other, Vector3D):
      return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
    else:
      return NotImplemented
  
  def __sub__(self, other):
    if isinstance(other, Vector3D):
      return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
    else:
      return NotImplemented
  
  def __mul__(self, other):
    if isinstance(other, Vector3D):
      return Vector3D(self.x * other.x, self.y * other.y, self.z * other.z)
    else:
      return NotImplemented
  
  def __repr__(self):
    return f"Vector3D({self.x}, {self.y}, {self.z})"

# Testing the Vector3D class
v1 = Vector3D(1, 2, 3)
v2 = Vector3D(4, 5, 6)

print(f"v1 = {v1}")
print(f"v2 = {v2}")
print(f"v1 * v2 = {v1 * v2}")
print(f"v1 + v2 = {v1 + v2}")
print(f"v1 - v2 = {v1 - v2}")

# 2) Positive Number Descriptor
print("\n2) Positive Number Descriptor")
print("-" * 40)

class Positive:
  def __set_name__(self, owner, name):
    self.name = name
  
  def __get__(self, instance, owner):
    if instance is None:
      return self
    return instance.__dict__.get(self.name, 0)
  
  def __set__(self, instance, value):
    if not isinstance(value, (int, float)):
      print(f"{self.name} must be a number")
    elif value < 0:
      print(f"{self.name} must be a non-negative number")
    else:
      instance.__dict__[self.name] = value

class BankAccount:
  balance = Positive()
  
  def __init__(self, initial_balance=0):
    self.balance = initial_balance
  
  def deposit(self, amount):
    if amount <= 0:
      print("Deposit amount must be positive")
    else:
      self.balance += amount
  
  def withdraw(self, amount):
    if amount <= 0:
      print("Withdrawal amount must be positive")
    else:
      self.balance -= amount
  
  def __repr__(self):
    return f"BankAccount(balance={self.balance})"

# Testing BankAccount
account = BankAccount(100)
print(f"Initial account: {account}")
account.deposit(50)
print(f"After depositing 50: {account}")
account.withdraw(30)
print(f"After withdrawing 30: {account}")

# Try invalid operations
print("\nTesting invalid operations:")
account.deposit(-10)  # Should print error
account.withdraw(-5)  # Should print error

# 3) Point Class with __slots__
print("\n3) Point Class with __slots__")
print("-" * 40)

class Point:
  __slots__ = ('x', 'y')  # Only allow x and y as attributes
  
  def __init__(self, x, y):
    self.x = x
    self.y = y

# Create a Point instance normally
first_point = Point(1, 2)
print(f"First point: x={first_point.x}, y={first_point.y}")

# Try to add a new attribute (this will fail)
print("\nTrying to add new attribute 'z':")
try:
  first_point.z = 3
  print("Successfully added attribute 'z'")
except AttributeError as e:
  print(f"AttributeError: {e}")

# 4) Disassembling a Simple Function
print("\n4) Disassembling a Simple Function")
print("-" * 40)

import dis

def calculate_sum(a, b):
  return a + b

# Disassemble the function
print("Bytecode for calculate_sum(a, b):")
dis.dis(calculate_sum)

print("\n" + "=" * 50)
print("Bytecode Explanation:")
print("=" * 50)
print("""
LOAD_FAST:
- Loads a local variable onto the stack.
- Pushes the value of the variable from the function's local scope.

BINARY_ADD:
- Adds the top two items on the stack.
- Pops the two values, sums them, and pushes the result back.

RETURN_VALUE:
- Returns from the function.
- Pops the top value from the stack and returns it to the caller.

Python Virtual Machine (PVM) Stack Behavior:
- Stack-based (LIFO): Operations always use the top elements.
- Operand stack: Operands are popped from the stack, results are pushed back.
- No general-purpose registers: Unlike CPUs, PVM works entirely on the stack.
- Implicit operands: Instructions don't need explicit operands; they operate on stack top.
""")
