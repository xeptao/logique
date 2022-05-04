# recursive formula: n x m!
# where m = n - 1
def factorial(n):
    try:
        if n > 1:
            m = n - 1

            return n * factorial(m)
        elif n == 1:
            return 1
        else:
            print("You can't enter negative values.")
    except TypeError:
        print("Please enter a number.")
