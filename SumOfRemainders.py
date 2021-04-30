# program to find remainder of each number input by user and find sum of all remainders

sum_of_remainders = 0
loop_value = 1

while loop_value != 0 :
    try:
        number = input("Enter number: ")
        remainder = int(number) % 10
        sum_of_remainders = sum_of_remainders + remainder
        
        loop_value = int(input("Enter 1 to continue providing numbers or 0 to exit: "))
    except:
        print("Enter integer numbers only !!")
    continue

print("---***------***------***------***------***------***------***------***---") 
print("\n") 

print("Sum of remainder of numbers provided are: ", sum_of_remainders)

print("\n","       ************The End****************           ")
                         
        
