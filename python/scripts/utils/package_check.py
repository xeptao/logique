#  1 - passed
#  0 - failed
def package_check(package_name, error_message):
    try:
        __import__(package_name)

        return 1
    except ImportError:
        print(error_message)

        return 0
