n = int(input("Please input an integer: "))

factorial = 1

if n < 0:
    print("You must input a non-negative number.")
elif n == 0:
    print("The factorial of 0 is 1.")
else:
    for i in range(1, n + 1):
        factorial *= i
    print(f"The factorial of {n} is {factorial}.")
