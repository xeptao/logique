import os


def format_files():
    try:
        import pip
    except ImportError:
        print("Pip isn't installed.")

        return None

    os.system("black .")
    os.system("black ../src")


if __name__ == "__main__":
    format_files()
