# Program to add as many numbers as user wants
list_of_numbers =[]
entered_value = 1
sum_of_numbers = 0
count = 0

while entered_value != 0 :
    try:
        num = float(input("Enter number which needs to be added: "))
        sum_of_numbers = sum_of_numbers + num
        list_of_numbers.append(num)
        entered_value = float(input("Enter 1 (or, any non-zero number) to continue or 0 to exit: "))
        print("\n")
            
    except:
        print("\n","****** oops! looks like you have entered a value which is not a number. Please enter only numbers!!! *****")
    count = count + 1
    continue

print("---***------***------***------***------***------***------***------***---")   

print("Sum of numbers",end = " ")
for item in list_of_numbers:
    print(item,end = ", ")
print("is:", sum_of_numbers,"\n")

print("---***------***------***------***------***------***------***------***---") 

print("There are",count, "numbers provided by user for addition")
print("---***------***------***------***------***------***------***------***---") 

print("Numbers provided for addition are", list_of_numbers)

print("\n","       ************The End****************           ")
