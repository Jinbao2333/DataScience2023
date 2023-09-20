s = input("Please input a string: ")
count = 1

for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        count += 1
        if count >= 2:
            print("The input string contains two or more consecutive identical characters.")
            break
    else:
        count = 1

if count < 2:
    print("The input string does not contain two or more consecutive identical characters.")
