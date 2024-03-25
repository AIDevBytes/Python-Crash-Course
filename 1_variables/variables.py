# assigning a value to a string variable
string_variable = "Hello there"

print(string_variable)
print(type(string_variable))

print("\n")

number_variable = 1000

print("The number stored in the number_variable is " + str(number_variable))

# example printing output formatted string literals. referred to as f-strings
print(f"The number stored in the number_variable is {number_variable}")

print("\n")

isOpen = True

isClosed = False

print(f"isOpen = {isOpen}")

print(f"isClosed = {isClosed}")

print(f"Type for isClosed and isOpen: {type(isOpen)}, {type(isClosed)}")

print("\n")

num_1 = 2

num_2 = 34

print(f"Sum of {num_1} + {num_2} is {num_1 + num_2}")

print(f"Type for num1: {type(num_1)} and num2: {type(num_1)}")

print("\n")

float_1 = 1.2343

float_2 = 3.1345

print(f"float_1: {float_1}")

print(f"float_2: {float_2:.2f}")

print("\n")
