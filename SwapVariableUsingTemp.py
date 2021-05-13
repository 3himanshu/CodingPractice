# Python Program to Swap Two Variables by using a temporary variable 

var1 = input("Enter first number: ")

var2 = input("Enter second number: ")

temp1 = var1
var1 = var2
var2 = temp1

print("\n")

print("after swapping, var1 is: ", var1)
print("after swapping, var2 is: ", var2)
