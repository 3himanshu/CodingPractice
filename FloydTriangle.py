# Floyd's Triangle

rows = int(input("Enter number of rows for Floyd's triangle: "))
k = 1
for i in range(rows):
    for j in range(i+1):
        print(k, end = " ")
        k += 1
    print("\n")
       
