number = float(input("Please input a number: "))

guess = 1.0
epsilon = 1e-6

while abs(guess ** 3 - number) > epsilon:
    guess = (2 * guess + number / (guess * guess)) / 3

print(f"The cube root of {number} is: {guess}.")
