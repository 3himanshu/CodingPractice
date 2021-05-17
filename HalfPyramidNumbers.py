# Program to print half pyramid using numbers

rows = int(input("Enter number of rows for half pyramid: "))

for i in range(rows):
    for j in range(i + 1):
        print(j+1," ", end="")
    print("\n")
