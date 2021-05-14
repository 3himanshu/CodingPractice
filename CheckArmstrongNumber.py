# Python Program to Check Armstrong Number

try:
    num = int(input("Enter numbber: "))

    if num >= 0:
        # To check how many digits have the given number
        sum = 0
        count = 0
        temp_num = num
        while temp_num != 0:
            count = count + 1
            temp_num = int(temp_num/10)

        # Find sum as per armstrong number rule
        temp_num = num
        for i in range(count):
            rem = temp_num % 10
            temp_num = int(temp_num/10)
            sum = sum + (rem ** count)


        if sum == num:
            print("{0} is a armstrong number".format(num))
        else:
            print("{0} is not a armstrong number".format(num))
    else:
        print("Please provide only positive number !!")

except ValueError as err:
    print(err)
    print("Please enter only positive numbers !!")
    
    
