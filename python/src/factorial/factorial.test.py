from factorial import factorial

result = factorial(6)

if result == 720:
    print("\033[92mfactorial: passed\033[0m")
else:
    raise Exception("\033[91mfactorial - failed\033[91m")
