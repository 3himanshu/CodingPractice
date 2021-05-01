# Program to Find the Largest Among Three Numbers
first_number = float(input("Entert first number: "))
second_number= float(input("Entert second number: "))
third_number = float(input("Entert third number: "))


if first_number > second_number and first_number > third_number:
    largest_number = first_number
elif second_number > first_number and second_number > third_number:
    largest_number = second_number
else:
    largest_number = third_number
    
print("Largest number is : ", largest_number)
