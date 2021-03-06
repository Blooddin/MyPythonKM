def GCD(a, b: int) -> int:
    '''Finding greatest common divisor for a,b'''
    if b>a: 
        a, b = b, a
    while b!=0:
        r = a%b
        a = b
        b = r
    return a

def LCM(a, b: int) -> int:
    '''Finding least common multiple for a,b'''
    return (int)((a*b)/GCD(a,b))


if __name__ == '__main__':
    a, b = input().split(' ')

    if a[0] == '-': #If a is less than zero
        a = a[1:]
    if b[0] == '-': #If b is less than zero
    	b = b[1:]

    if a.isdigit() and b.isdigit() and a!='0' and b!='0':
        a = int(a)
        b = int(b)
        print(GCD(a,b),LCM(a,b))
    else:
        print('Input Error')