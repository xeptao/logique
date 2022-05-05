import os
import platform
import json


def install_packages():
    try:
        import pip
    except ImportError:
        print("Pip isn't installed.")

        return Null

    user_os = platform.system()
    sudo_state = False

    # add sudo to start of command on unix-based systems
    if user_os == "Linux" or user_os == "Darwin":
        sudo_state = True

    # open packages list and install them to packages/
    with open("packages.json") as file:
        data = json.load(file)

        os.system(
            f'{"sudo" if sudo_state else None} pip install {" ".join(data)} --target "packages/"')

        print("Installed the required packages.")


if __name__ == "__main__":
    install_packages()
