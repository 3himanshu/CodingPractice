# Python program to reverse string using recursion
string = input("Enter string: ")

def reverseString(x):
    if len(x) == 0:
        return x
    else:
        return reverseString(x[1:]) + x[0]

print("Reversed string is:",reverseString(string))
