import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import torch

print("Array:", arr)
print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", round(std, 3))

data = {
    "Name": ["Ahmed", "Sara", "Mohamed", "Lalla"],
    "Age": [20, 21, 22, 20],
    "Score": [75, 88, 90, 79]
}

df = pd.DataFrame(data)
filtered_students = df[df["Score"] > 80]
print(filtered_students)

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y)
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Line Graph Example")
plt.show()

tensor1 = torch.tensor([1, 2, 3])
tensor2 = torch.tensor([4, 5, 6])

dot_product = torch.dot(tensor1, tensor2)
element_wise = tensor1 * tensor2

print("Dot Product:", dot_product)
print("Element-wise Multiplication:", element_wise)