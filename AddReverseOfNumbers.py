# Program to add reverse of as many numbers as user wants
loop_number = 1
reversed_number_list = []
sum_of_reversed_number = 0

while loop_number != 0 :
    try:
        entered_number = input("Enter number which needs to be added after reversing it: ")
            
        reversed_number = entered_number[::-1]
        sum_of_reversed_number = sum_of_reversed_number + int(reversed_number)
        
        loop_number = int(input("Enter 1 to continue or 0 to exit: "))
    except ValueError :
        print("Enter ony integers !!")
    continue

print("---***------***------***------***------***------***------***------***---") 
print("\n") 

print("sum of reversed of all given number is: ", sum_of_reversed_number)
print("\n","       ************The End****************           ")
