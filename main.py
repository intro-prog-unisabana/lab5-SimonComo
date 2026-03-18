from utils import *

while True:
    op = input("Which calculation would you like to perform? (add, subtract, multiply, divide, exponent, modulo, floor_divide, absolute, exit):\n").lower()

    if op == "exit":
        break

    if op not in ["add", "subtract", "multiply", "divide", "exponent", "modulo", "floor_divide", "absolute"]:
        print("Invalid option!")
        continue

    if op == "absolute":
        num = float(input("Enter the number:\n"))
        print("The result is:", absolute(num))
    else:
        num1 = float(input("Enter the first number:\n"))
        num2 = float(input("Enter the second number:\n"))

        if op == "add":
            print("The result is:", add(num1, num2))
        elif op == "subtract":
            print("The result is:", sub(num1, num2))
        elif op == "multiply":
            print("The result is:", multiply(num1, num2))
        elif op == "divide":
            print(divide(num1, num2))
        elif op == "exponent":
            print("The result is:", exponent(num1, num2))
        elif op == "modulo":
            print(modulo(num1, num2))
        elif op == "floor_divide":
            print(floor_divide(num1, num2))