# Create a calculator program for addition, substraction, multiplication, and floor division.
# Take the inputs from the user, and based on the choice of operation, return the resutls.

def addition(a, b):
    return a+b
def substraction(a, b):
    return a-b

def multiplication(a, b):
    return a*b

def divide(a, b):
    return a/b

a = int(input("Enter your first number -> "))
b = int(input("Enter your second number -> "))
choice = int(input(
    "Operation 1 = Addition\nOperation 2 = Substraction\nOperation 3 = Multiplication\nOperation 4 = division\n Select an Operation: "))
if (choice == 1):
    print(addition(a, b))
elif (choice == 2):
    print(substraction(a, b))
elif (choice == 3):
    print(multiplication(a, b))
elif (choice == 4):
    print(divide(a, b))
else:
    print("Wrong choice")
