# Taking kilometers input from the user
kilometers = float(input("Enter value in kilometers: "))

# conversion factor
conv_fac = 0.621371

# calculate miles
miles = kilometers * conv_fac
print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))

#Miles to kilometers
# Miles=float(input("Enter Miles: "))
#
# num=0.621371
#
# kilometers= Miles / num
#
# print("%0.2f miles is equal to %0.2f kilometers"%(Miles,kilometers) )