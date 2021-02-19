print('Hello World!')

# Number input  
a = input("Input a number to check if it's more than a zero ")
a = int(a)

# Checking if a number is above, equal or below zero.  
if a>0:
    print('More than zero.')
elif a == 0:
    print("Indeed, a zero.")
else:
    print('Less than zero.')