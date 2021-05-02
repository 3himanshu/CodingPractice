# Simple Calculator by Using Functions

# This function adds two numbers
def add(x,y):
    return x+y

# This function subtracts two numbers
def sub(x,y):
    return x-y

# This function multiply two numbers
def mul(x,y):
    return x*y

# This function divide two numbers
def div(x,y):
    return x/y

print("Select operation: ")
print("1 for addition")
print("2 for subtraction")
print("3 for multiplication")
print("4 for division")

while True:
    #Take into from the user
    choice = input("Enter choice (1/2/3/4): ")
    
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1':
            print(num1, "+", num2, "is: ", add(num1,num2))
        
        elif choice == '2':
            print(num1, "-", num2, "is: ", sub(num1,num2))
        
        elif choice == '3':
            print(num1, "*", num2, "is: ", mul(num1,num2))
        
        elif choice == '4':
            print(num1, "/", num2, "is: ", div(num1,num2))
        break
    else:
        print("Invalid input !!!")
    



