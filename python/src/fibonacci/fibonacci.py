from functools import lru_cache


@lru_cache(maxsize=5)
def fibonacci(n):
    try:
        if n > 2:
            return fibonacci(n - 1) + fibonacci(n - 2)
        elif n == 1 or n == 2:
            return 1
        else:
            print("Do not enter negative values.")
    except TypeError:
        print("Please enter a number.")
