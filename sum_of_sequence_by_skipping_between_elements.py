# find the sum of sequence by skipping the between elements without using slicing.
# Ex seq = [1, 2, 3, 4, 5, 6, 7, 8, 9] where x = 4, y = 7
# skip elements between x and y(including x and y i,e. [4, 5, 6, 7]) always y # comes after x
# output: 1+2+3+8+9 = 23

sequence = input("Enter elements of list separated by space: ")
x = input("Enter x value from where elements will be skipped: ")
y = input("Enter y value from till elements will be skipped: ")

list_sequence = sequence.split()

flag = True

Requred_list_sum = 0

for item in list_sequence:
    if item != x and flag == True:
        Requred_list_sum = Requred_list_sum + int(item)
    elif item == x:
        flag = False
    elif item == y:
        flag = True

print("\n")        
print("Requred list sum: ", Requred_list_sum)


