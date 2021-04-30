# Program to find sum of tenth of each numbers input by user. Any number user can provide and it can be of any any length

loop_value = 1
tenth_digit_sum = 0

while loop_value != 0 :
    try:
        number = input("Enter number: ")
        
        unit = int(int(number) / 10)
        tenth = unit % 10
        
        tenth_digit_sum = tenth_digit_sum + tenth
        
        loop_value = int(input("Enter 1 to continue or 0 to exit: "))
    except ValueError as err:
        print(err)
    continue
    
print("digitwise sum of numbers is: ",tenth_digit_sum)
    
            
