import re
from collections import Counter

# Email Validation
def validate_email(email):
    pattern = r'^[A-Za-z0-9._]+@[A-Za-z0-9.-]+\.(com|org|edu)$'
    return bool(re.match(pattern, email))


# Extract Hashtags
def extract_hashtags(text):
    return re.findall(r"#\w+", text)


# Phone Number Validation
def validate_phone(number):
    pattern = r'^(\+1-)?\d{3}-\d{3}-\d{4}$'
    return bool(re.match(pattern, number))


# Word Frequency
def word_frequency(text):
    words = re.findall(r"\w+", text)
    return Counter(words)


# Find Duplicate Words
def find_duplicate_words(text):
    return re.findall(r"\b(\w+)\s+\1\b", text)


# Extract Dates
def extract_dates(text):
    return re.findall(r"\d{4}-\d{2}-\d{2}", text)


# Mask Credit Card Number
def mask_card_number(text):
    return re.sub(r"\d(?=\d{4})", "*", text)


# Extract Programming Languages
def extract_languages(text):
    pattern = r"Python|Java|C\+\+|Ruby"
    return re.findall(pattern, text)


# TESTING
print("=== Email Validation Test ===")
emails = ["user@example.com", "bad-email", "test@domain.org"]
for e in emails:
    print(e, "->", validate_email(e))

print("\n=== Hashtag Extraction Test ===")
print(extract_hashtags("I love #Python and #AI"))

print("\n=== Phone Validation Test ===")
phones = ["+1-555-123-4567", "123-456-7890", "5551234"]
for p in phones:
    print(p, "->", validate_phone(p))

print("\n=== Word Frequency Test ===")
text = "Python, Python! AI is great; Python AI."
print(word_frequency(text))

print("\n=== Duplicate Words Test ===")
print(find_duplicate_words("This is is a test test"))

print("\n=== Date Extraction Test ===")
print(extract_dates("The events are on 2023-05-12 and 2024-01-01."))

print("\n=== Card Masking Test ===")
print(mask_card_number("Card: 1234-5678-9012-3456"))

print("\n=== Language Extraction Test ===")
print(extract_languages("I know Python, Java, and C++ but not Ruby."))
