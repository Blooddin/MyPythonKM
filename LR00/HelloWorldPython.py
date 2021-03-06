print('Hello World!')  

# Function for checking if a number is above, equal or below zero.  
def check_if_zero(a):
    if a>0:
        print('More than zero.')
    elif a == 0:
        print("Indeed, a zero.")
    else:
        print('Less than zero.')

# Number input  
a = input("Input a number to check if it's more than a zero ")
a = int(a)

check_if_zero(a)  
