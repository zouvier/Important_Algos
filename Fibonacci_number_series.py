from functools import lru_cache


# used cache to increase processing speed
@lru_cache(maxsize=1000)
def fibonacci(n):
    # need to check to see if n is positive integer
    # check to see if n is a whole number
    # check to see if n is a number
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)


for i in range(1,101):
    print(fibonacci(i))
