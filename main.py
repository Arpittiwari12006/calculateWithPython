import math

print("calculateWithPython")
print("Use math functions directly or using math.")
print("WANT TO QUIT TYPE exit ")

while True:
    expr = input(">>> ")

    if expr.lower() == "exit":
        print("Calculator Closed")
        break

    try:
        result = eval(expr)
        print("=", result)
    except:
        print("Invalid Expression")