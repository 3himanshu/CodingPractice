# Program to Check Prime Number using while loop

num = int(input("Enter number: "))
flag = False
i = 2 
while(i > 1 and i <= num-1):
    if num % i == 0:
        flag = True
        break
    i = i + 1
    
if flag:
    print(num,"is not a prime number")
else:
    print(num,"is a prime number")   
