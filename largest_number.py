a=int(input("Enter a first number: "))
b=int(input("Enter a second number: "))
c=int(input("Enter a three number: "))

if(a>b) and(a>c):
    print("{0} is highest number".format(a))
elif(b>a) and (b>c):
    print("{0} is highest number".format(b))
else:
    print("{0} is highest number".format(c))