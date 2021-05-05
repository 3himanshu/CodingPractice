# Python Program to Check whether a given number is Prime or not using for else

#get number
num = int(input("Enter number: "))

# prime numbers are greater than 1
if num > 1:
    # Check for factors
    for i in range(2,num):
        if num % i == 0:
            print(num,"is not a prime number !!")
            print(i,"times",num/i, "is",num)
            break
    else:
            print(num,"is a prime number !!")

# if input is less than 1 or eqal to 1, its not a prime 
else:
    print(num,"is not a prime number !!")    
        

