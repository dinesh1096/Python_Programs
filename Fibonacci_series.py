n=int(input("Enter n terms"))

n1 , n2 = 0,1
sum=0

if n<0:
    print("please enter greater than 0")
else:
    for i in range(sum,n):
        print(sum, end=" ")
        n1=n2
        n2=sum
        sum=n1+n2