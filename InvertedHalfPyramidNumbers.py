# Inverted half pyramid using numbers

rows = int(input("Enter number of rows for inverted half pyramid: "))

for i in range(rows):
    for j in range(rows):
        print(j+1, end = " ")
    rows = rows -1 
    print("\n")
