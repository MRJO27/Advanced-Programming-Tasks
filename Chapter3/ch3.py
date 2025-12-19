# 1) Remove Vowels (Pure Function)
print("\n1) Remove Vowels:")
def remove_vowels(text):
  vowels = "aeiouAEIOU"
  return ''.join(char for char in text if char not in vowels)

print(f"remove_vowels('Hello World') = '{remove_vowels('Hello World')}'")

# 2) Squares of Odd Numbers (map + filter)
print("\n2) Squares of Odd Numbers:")
numbers = [1, 2, 3, 4, 5, 6, 7]
odd_squares = list(map(lambda x: x**2, filter(lambda x: x % 2 != 0, numbers)))
print(f"Numbers: {numbers}")
print(f"Odd squares: {odd_squares}")

# 3) Fibonacci with Memoization
print("\n3) Fibonacci with Memoization:")
from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fibonacci(n):
  if n < 2:
    return n
  return fibonacci(n-1) + fibonacci(n-2)

start = time.time()
result = fibonacci(35)
end = time.time()
print(f"Fibonacci(35) = {result}")
print(f"Time taken: {end - start:.6f} seconds")

# 4) Closure - Make Adder
print("\n4) Closure - Make Adder:")
def make_adder(n):
  def adder(x):
    return n + x
  return adder

add_5 = make_adder(5)
print(f"make_adder(5)(10) = {add_5(10)}")

# 5) Higher-Order Function
print("\n5) Higher-Order Function:")
def apply_twice(func, value):
  return func(func(value))

print(f"apply_twice(lambda x: x + 1, 5) = {apply_twice(lambda x: x + 1, 5)}")
print(f"apply_twice(lambda x: x * 2, 3) = {apply_twice(lambda x: x * 2, 3)}")

# 6) Functional ETL Pipeline
print("\n6) Functional ETL Pipeline:")
from collections import Counter

def etl_pipeline(strings):
  stopwords = {"the", "a", "is", "and", "in", "on"}
  words = [word.lower() for text in strings for word in text.split()]
  filtered_words = filter(lambda w: w not in stopwords, words)
  return dict(Counter(filtered_words))

texts = ["The cat is on the roof", "A dog is in the yard"]
print(f"Texts: {texts}")
print(f"Word frequencies: {etl_pipeline(texts)}")

# 7) Custom Reduce Function
print("\n7) Custom Reduce Function:")
def my_reduce(func, iterable, initializer=None):
  it = iter(iterable)
  if initializer is None:
    value = next(it)
  else:
    value = initializer
  for element in it:
    value = func(value, element)
  return value

print(f"my_reduce(lambda x, y: x + y, [1, 2, 3, 4]) = {my_reduce(lambda x, y: x + y, [1, 2, 3, 4])}")

# 8) Log Call Decorator
print("\n8) Log Call Decorator:")
def log_call(func):
  def wrapper(*args, **kwargs):
    print(f"Calling {func.__name__}...")
    result = func(*args, **kwargs)
    print(f"{func.__name__} finished!")
    return result
  return wrapper

@log_call
def greet(name):
  print(f"Hello, {name}")

greet("Alice")
