x = float(input("Please input the first number: "))
y = float(input("Please input the second number: "))
z = float(input("Please input the third number: "))

numbers = [x, y, z]

numbers.sort()

print("Output: ")
for num in numbers:
    print(num, end = " ")
