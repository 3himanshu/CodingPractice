# Find the square root of real or complex number

num = eval(input("Enter number:"))

sqrt_num = cmath.sqrt(num)

print("Square root of {0} is {1:0.3f} + {2:0.3f}j".format(num,sqrt_num.real,sqrt_num.imag))
