# Python Program to calculate the square root

# Note: change this value for a different result


# To take the input from the user
# num = float(input('Enter a number: '))
#
# num_sqrt=num**0.5
# print("The Square root of %0.3f is %0.3f"%(num,num_sqrt))

#complex
import cmath
num=eval(input("Enter number:"))

num_sqrt=cmath.sqrt(num)
print('The Square root of {0} is {1:0.3f}+{2:0.3f}'.format(num,num_sqrt.real,num_sqrt.imag))


