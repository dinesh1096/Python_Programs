# n=int(input("Enter a number: "))
#
# for i in range(2, n):
#     if (n % i == 0):
#         print("{0} is not a prime number".format(n))
#         print(i,"times",n//i,"is",n)
#         break
# else:
#     print("{0} is  a prime number".format(n))


#prime number with an interval

lower=int(input("Enter lower number:"))
upper=int(input("Enter Upper number"))
print("prime numbers between",lower,"and",upper,"are:" )
for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if(num%i==0):
                break
        else:
            print(num)


