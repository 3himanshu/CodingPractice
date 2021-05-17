# Inverted half pyramid using *

rows = int(input("Enter number of rows for half pyramid: "))

for i in range(rows):
    for j in range(rows):
        print("* ", end = " ")
    rows = rows - 1
    print("\n")
