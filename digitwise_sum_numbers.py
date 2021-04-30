# program to find digitwise sum of numbers input by user..user can provide as many numbers as he wants and it can be of any length. Ex: numbers 123 and 456 are provided by user then sum will be 21
loop_value = 1
digitwise_sum = 0
while loop_value != 0 :
    try:
        number = input("Enter number: ")
        
        for character in number:
            digitwise_sum = digitwise_sum + int(character)
        
        loop_value = int(input("Enter 1 to continue or 0 to exit: "))
    except ValueError as err:
        print(err)
    continue
    
print("digitwise sum of numbers is: ",digitwise_sum)
    
            
