'''# Python program to check if the number is an Armstrong number or not

# take input from the user
num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")



#nth order
n=int(input("Enter a number:"))

length= len(str(n))

sum=0
temp=n
while temp>0:
    digit=temp % 10
    sum+=digit**length
    temp=temp//10
if(n==sum):
    print(n, "is a armstrong")
else:
    print(n, "is not  a armstrong")'''

#interval

lower=int(input("Enter a Lower number"))
upper=int(input("Enter a higher number "))

for num in range(lower,upper+1):
    order=len(str(num))

    sum=0
    temp=num
    while temp>0:
        digit=temp%10
        sum+=digit**order
        temp=temp//10
    if num==sum:
        print(num)




