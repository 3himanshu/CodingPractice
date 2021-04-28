# Reverse a sequence of string using loop
y = input("Enter string which needs to be reverted: ")

def string(x):
    r_str = ''
    for char in x:
        r_str = char + r_str
    return r_str

reversed_str = string(y)

print("\n", "Reversed string is: ",reversed_str )
