# Write Fibonacci series up to n
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

fib(2000)


# Documentation Strings
def my_function():
    """Do nothing, but ducument it.

    No, really, it doesn't do anything.
    """
    pass

# print(my_function.__doc__)



# return a list containing the Fibonacci series up to n
def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

    
# f100 = fib2(100)
# print(f100)
print(fib2(100))