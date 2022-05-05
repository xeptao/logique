import os
import platform
import json

from utils.package_check import package_check


def install_packages():
    package_check("pip", "Pip isn't installed.")

    user_os = platform.system()
    sudo_state = False

    # add sudo to start of command on unix-based systems
    if user_os == "Linux" or user_os == "Darwin":
        sudo_state = True

    # open packages list and install them to packages/
    with open("../config/packages.json") as file:
        data = json.load(file)

        os.system(
            f'{"sudo" if sudo_state else ""} pip install {" ".join(data)} --target "../packages/"'
        )

        print("Installed the required packages.")


if __name__ == "__main__":
    install_packages()
