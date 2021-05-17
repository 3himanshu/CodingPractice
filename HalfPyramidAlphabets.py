# Program to print half pyramid using alphabets

rows = int(input("Enter number of rows for half pyramid: "))

ascii_value = 65

for i in range(rows):
    for j in range(i+1):
        print(chr(ascii_value), end=" ")
    ascii_value = ascii_value + 1
    print("\n")
