# n1= input("Enter the first number: ")
# n2 = input("Enter the second number: ")
# if n1.replace('.', '', 1).isdigit() and n2.replace('.', '', 1).isdigit():
#     num1 = float(n1)
#     num2 = float(n2)
#     print("Choose an operation:")
#     print("+ for Addition")
#     print("- for Subtraction")
#     print("* for Multiplication")
#     print("/ for Division")
#     operation = input("Enter your choice (+, -, *, /): ")
#     if operation == '+':
#         result = num1 + num2
#         print(f"Result: {num1} + {num2} = {result}")
#     elif operation == '-':
#         result = num1 - num2
#         print(f"Result: {num1} - {num2} = {result}")
#     elif operation == '*':
#         result = num1 * num2
#         print(f"Result: {num1} * {num2} = {result}")
#     elif operation == '/':
#         if num2 != 0:
#             result = num1 / num2
#             print(f"Result: {num1} / {num2} = {result}")
#         else:
#             print("Error: Division by zero is not allowed.")
#     else:
#         print("Invalid operation. Please enter +, -, * or /.")
# else:
#     print("Invalid input. Please enter valid numeric values.")

# 2)Fiblonaci 
n = int(input("Enter the number of terms (N): "))
a, b = 0, 1
count = 0
if n <= 0:
    print("Please enter a positive integer.")
else:
    print(f"The first {n} terms of the Fibonacci series are:")
    while count < n:
        print(a, end=' ')
        a, b = b, a + b
        count += 1

# 3)armstrong
# num = int(input("Enter a number: "))
# original = num
# sum = 0
# n = len(str(num))
# while num > 0:
#     digit = num % 10
#     sum += digit ** n
#     num //= 10
# if sum == original:
#     print(f"{original} is an Armstrong number.")
# else:
#     print(f"{original} is not an Armstrong number.")

# 4)greates number
# num = int(input("Enter a number: "))
# max_digit = 0
# while num > 0:
#     digit = num % 10
#     if digit > max_digit:
#         max_digit = digit
#     num //= 10
# print(f"The greatest digit is: {max_digit}")

# 5)greatest of three numbers
# a = float(input("Enter first number (a): "))
# b = float(input("Enter second number (b): "))
# c = float(input("Enter third number (c): "))
# if a >= b and a >= c:
#     greatest = a
# elif b >= a and b >= c:
#     greatest = b
# else:
#     greatest = c
# print(f"The greatest number among {a}, {b}, and {c} is: {greatest}")

