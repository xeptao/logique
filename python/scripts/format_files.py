import os

from utils.package_check import package_check


def format_files():
    package_check("pip", "Pip isn't installed.")

    os.system("black .")
    os.system("black ../src")


if __name__ == "__main__":
    format_files()
