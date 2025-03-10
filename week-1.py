# Basic Arithmetic Operations
a = 10
b = 5

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)

# String Manipulation
name = "Jussie"
greeting = "Hello, " + name + "!"
print(greeting)

# String repetition
print(name * 3)

# String slicing
print("First letter:", name[0])
print("Last letter:", name[-1])
print("Substring:", name[1:4])

# String methods
print("Uppercase:", name.upper())
print("Lowercase:", name.lower())
print("Length:", len(name))

# Experimenting with Variables and Data Types
integer_num = 25
float_num = 3.14
string_text = "Python"
boolean_value = True
complex_num = 2 + 3j

print("Integer:", integer_num, type(integer_num))
print("Float:", float_num, type(float_num))
print("String:", string_text, type(string_text))
print("Boolean:", boolean_value, type(boolean_value))
print("Complex Number:", complex_num, type(complex_num))

# Type Conversion
num_str = "100"
num_int = int(num_str)
num_float = float(num_str)

print("String to Integer:", num_int, type(num_int))
print("String to Float:", num_float, type(num_float))
print("Integer to String:", str(num_int), type(str(num_int)))

# User Input and Simple Calculation
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = num1 + num2
print("Sum:", result)

# Basic Calculator

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("Enter Operation to perform [ / - + * ]: ")

if operation == "-":
    print(f"The Subtraction of {num1} and {num2} is {num1 - num2}")

if operation == "/":
    print(f"The Division of {num1} and {num2} is {num1 / num2}")

if operation == "+":
    print(f"The Addition of {num1} and {num2} is {num1 + num2}")

if operation == "*":
    print(f"The multiplication of {num1} and {num2} is {num1 * num2}")

