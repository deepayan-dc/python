# num1 = input("Enter the first number: ")
# num2 = input("Enter the second number: ")
# result = float(num1) + float(num2)
# print(result)
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
op = input("Enter the operator (+, -, *, /): ")
if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1-num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator. Please use +, -, *, or /.")

