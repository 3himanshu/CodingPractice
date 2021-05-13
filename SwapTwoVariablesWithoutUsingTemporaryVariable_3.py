# Python Program to Swap Two Variables using arithmetic operator only if provided variables are number

var1 = int(input("Enter first number: "))

var2 = int(input("Enter second number: "))

var1 = var1 * var2
var2 = var1 / var2
var1 = var1 / var2

print("after swapping, var1 is: ", var1)
print("after swapping, var2 is: ", var2)
