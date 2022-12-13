# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
#
# temp=a
# a=b
# b=temp
#
# print("The value of a after swapping: {0}".format(a))
#
# print("The value of b after swapping: {0}".format(b))

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))

a,b=b,a
print("the vale of a after swapping is {0}".format(a))
print("the vale of a after swapping is {0}".format(b))