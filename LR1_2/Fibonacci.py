import sys


def fibonacci(n: int) -> int:
    '''Finding the n number of Fibonacci'''
    if n == 1:
        return 0
    if n == 2:
        return 1
    a = 0
    b = 1
    for x in range(2, n):
        temp = b
        b = a + b
        a = temp
    return b


if __name__ == '__main__':
    if len(sys.argv) == 2:
        if sys.argv[1].isdigit() and sys.argv[1] != '0':
            a = int(sys.argv[1])
            print("The "+str(a)+"'s number is "+str(fibonacci(a)))
        else:
            print('Input Error')
    else:
        print('Enter the number of Fibonacci')
        a = input()
        if a.isdigit() and a != '0':
            a = int(a)
            print("The "+str(a)+"'s number is "+str(fibonacci(a)))
        else:
            print('Input Error')
