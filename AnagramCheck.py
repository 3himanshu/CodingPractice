# Python Program to Check If Two Strings are Anagram

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if len(str1) == len(str2):
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
    
    if sorted_str1 == sorted_str2:
        print("string {0} and {1} are anagram !!".format(str1,str2))
    else:
        print("string {0} and {1} are not anagram !!".format(str1,str2))
else:
    print("string {0} and {1} are not anagram !!".format(str1,str2))
