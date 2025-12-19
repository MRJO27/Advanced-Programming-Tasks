# 1. Bytecode Inspection
import dis

def square(x):
  return x * x

def multiply(a, b):
  return a * b

print("Bytecode for square():")
dis.dis(square)
print("\nBytecode for multiply():")
dis.dis(multiply)

# 2. Dynamic Typing Test
def my_func():
  pass

data = 4
print(f"\ndata = 4: {type(data)}")

data = [1, 2, 3, 4]
print(f"data = [1,2,3,4]: {type(data)}")

data = my_func
print(f"data = my_func: {type(data)}")

# 3. AST Exploration
import ast

code = "y = (4 * 5) - 3"
tree = ast.parse(code)
print("\nAST dump:")
print(ast.dump(tree, indent=4))

# 4. Mutability and Object Identity Test
my_list = [10, 20, 30]
print(f"\nInitial list ID: {id(my_list)}")

my_list.append(40)
print(f"After append, list ID: {id(my_list)}")
print(f"Same ID? {id(my_list) == id(my_list)}")