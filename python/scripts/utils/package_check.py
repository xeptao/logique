def package_check(package_name, error_message):
    try:
        __import__(package_name)
    except ImportError:
        raise error_message
