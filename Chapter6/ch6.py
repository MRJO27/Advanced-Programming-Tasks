# 1) CSV Reading
import csv
with open("students.csv", newline='', encoding="utf-8") as file:
  reader = csv.DictReader(file)
  print("Students with score > 80:")
  for row in reader:
    score = int(row["Score"])
    if score > 80:
      print(row["Name"])

# 2) JSON Handling
import json
data = {
  "Employee": [
    {"name": "Ali", "course": "Python", "fees": 300},
    {"name": "Mona", "course": "Networking", "fees": 250},
    {"name": "Omar", "course": "WebData", "fees": 350}
  ]
}
with open("course.json", "w") as f:
  json.dump(data, f, indent=4)

with open("course.json", "r") as f:
  content = json.load(f)
names = [emp["name"] for emp in content["Employee"]]
print("Employee names:", names)

# 3) Pandas to CSV
import pandas as pd
data = {
  "people": [
    {"Name": "Ali", "Age": 25, "City": "Riyadh", "Class": "A"},
    {"Name": "Mona", "Age": 30, "City": "Jeddah", "Class": "B"},
    {"Name": "Omar", "Age": 22, "City": "Cairo", "Class": "A"}
  ]
}
df = pd.DataFrame(data['people'])
df.to_csv('people.csv', index=False)
print("CSV file 'people.csv' has been created successfully!")