# Python Program to Make a Simple Calculator
global_loop_value = 1
add_loop_value = 1
mul_loop_value = 1 
div_loop_value = 1 
entered_value = 1 
sum_number = 0
mul_number = 1

while global_loop_value != 0:
    try:
        entered_value = int(input("Enter 1 for addtion, 2 for subtraction, 3 for multiply and 4 for division: "))

        if entered_value == 1:
            while add_loop_value != 0:
                add_entered_value = int(input("Enter number for addition: "))

                sum_number = sum_number + int(add_entered_value)

                add_loop_value = int(input("Enter 1 to continue adding number or 0 to exit: "))
                continue

            print("Sum of given number is: ", sum_number)

        elif entered_value == 2:
            minuend  = int(input("Enter Minuend number : "))
            subtrahend   = int(input("Enter Subtrahend number : "))

            subtraction = minuend - subtrahend 

            print("Result of subtraction is: ", subtraction)

        elif entered_value == 3:
            while mul_loop_value != 0:
                mul_entered_value = int(input("Enter number for multiplication: "))

                mul_number = mul_number * int(mul_entered_value)

                mul_loop_value = int(input("Enter 1 to continue adding number or 0 to exit: "))
                continue

            print("multiply of given number is: ", mul_number)

        elif entered_value == 4:
            dividend  = int(input("Enter Dividend number : "))
            divisor   = int(input("Enter Divisor number : "))

            Quotient = dividend/divisor 

            print("Result of division is: ", Quotient)
        else:
            print("Please enter valid operation number !!")


        global_loop_value = int(input("Enter 1 to continue using calculator or 0 to exit: "))
    
    except ValueError as err:
        print(err)

            
            
            
