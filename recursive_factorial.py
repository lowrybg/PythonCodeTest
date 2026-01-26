def get_factorial(n):
    if n == 1:
        return n

    return n * get_factorial(n-1)

n = int (input('Enter a number: '))
print(get_factorial(n))


#factorial
