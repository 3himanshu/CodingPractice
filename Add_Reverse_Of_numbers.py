# Python Program to Add reverse of two Numbers
try:
    number_1 = int(input("Enter first number: "))
    number_2 = int(input("Enter second number: "))
    
    reversed_number_1 = str(number_1)[::-1]
    reversed_number_2 = str(number_2)[::-1]
    
    print("\n")
    print("Reverse of", number_1, "is: ", reversed_number_1)
    print("Reverse of", number_2, "is: ", reversed_number_2)

    sum_of_reversed_numbers = int(reversed_number_1) + float(reversed_number_2)
    print("\n")
    print("sum of reverse of numbers provided is:", sum_of_reversed_numbers)

except:
    print("\n","Please enter only integer value!!!")





