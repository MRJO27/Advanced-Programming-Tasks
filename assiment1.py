# 1. Transform and Clean Data
products = [ " LAPTOP ", "phone ", " Tablet", "CAMERA  "]
cleaned = list(map(lambda x: x.strip().title(), products))
print(cleaned)

# 2. Convert Temperatures (Celsius → Fahrenheit)
celsius = [0, 10, 20, 30, 40]
fahrenheit = list(map(lambda c: (9/5)*c + 32, celsius))
print(fahrenheit)

# 3. Apply Multiple Transformations
nums = [1, 2, 3, 4, 5]
transformed = list(map(lambda x: x**2 + 10, nums))
print(transformed)

# 4. Extract First and Last Characters
words = ["python", "lambda", "programming", "map", "function"]
chars = list(map(lambda w: (w[0], w[-1]), words))
print(chars)

# 5. Nested Map Transformation
marks = [[45, 80, 70], [90, 60, 100], [88, 76, 92]]
updated_marks = list(map(lambda row: list(map(lambda x: round(x * 1.05), row)), marks))
print(updated_marks)

# 6. Normalize Numbers Between 0 and 1
nums = [5, 10, 15, 20, 25]
min_val, max_val = min(nums), max(nums)
normalized = list(map(lambda x: (x - min_val) / (max_val - min_val), nums))
print(normalized)

# 7. Extract Word Lengths from Sentences
sentences = ["Python is fun", "Lambda functions are powerful", "Map is useful"]
word_lengths = list(map(lambda s: list(map(len, s.split())), sentences))
print(word_lengths)

