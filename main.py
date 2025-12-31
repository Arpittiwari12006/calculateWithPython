import math

print("--------------CALCULATE_WITH_PYTHON---------------")
print("1. USE MATH FUNCTIONS DIRECTLY OR USING MATH.FUNCTION_NAME FOR SOME SPECIAL OPRATIONS.")
print("2. WANT TO QUIT TYPE EXIT.")

while True:
    expr = input("------>")

    if expr.lower() == "EXIT":
        print("CALCULATOR CLOSED")
        break

    try:
        result = eval(expr)
        print("=", result)
    except:
        print("INVALID EXPRESSION")