x=int(input("Enter number: "))
y=int(input("Enter number: "))
while(y):
    x,y=y,x%y

print("the hcf is ",x)