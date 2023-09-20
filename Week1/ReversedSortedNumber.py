w = float(input("Please input the first number: "))
x = float(input("Please input the second number: "))
y = float(input("Please input the third number: "))
z = float(input("Please input the fourth number: "))

numbers = [w, x, y, z]

numbers.sort(reverse=True)

print("Output: ")
for num in numbers:
    print(num, end = " ")
