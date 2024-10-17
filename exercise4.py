num1 = int(input("input a number of your choice"))
counter = 0
i = 1
while i < num1:
    if num1 % i ==0:
        counter+=1
    i+=1

print(f"Amount of factors: {counter}")