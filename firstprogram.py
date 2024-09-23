# Basic calculator

print("Welcome to calculator")
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

choice = input("Do you want to: add, subtract, multiply, divide: ")

if choice == "add":
    print(num1 + num2)
elif choice == "subtract":
    print(num1 - num2)
elif choice == "divide":
    print(num1 / num2)
elif choice == "multiply":
    print(num1 * num2)



