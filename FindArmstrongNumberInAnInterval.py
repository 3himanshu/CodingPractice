# Python Program to Find Armstrong Number in an Interval

try:
    # get the lower and upper limit
    lower = int(input("Enter lower limit: "))
    upper = int(input("Enter upper limit: "))

    num = lower

    list_armstrong = []

    # Check if any lower or upper limit is positive then continue otherwise go to else part 
    if num >= 0 or upper >=0 :

        # Lower value should always be less than upper value
        while num <= upper :
            
            sum = 0
            count = 0
            temp_num = num
            
            # To check how many digits have the given number
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
                list_armstrong.append(num)                
            
            num = num + 1
        
        print("Armstrong number between",lower,"and",upper," is: ",str(list_armstrong)[1:-1] )  

    elif num < 0 or upper < 0 :
        print("Please provide only positive number !!")
        

except ValueError as err:
    print(err)
    print("Please enter only positive numbers !!")
