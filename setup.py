from setuptools import setup,find_packages
from typing import List

# Declaring variables for setup function
PROJECT_NAME = "Creadit-card-project"
VERSION = "0.0.1"
AUTHOR = "Swinal"
DESCRIPTION = "This is a creadit card detection"
PACKAGES = ["Creadit_card"]
REQUIREMENT_FILE_NAME = "requirements.txt"

def get_requirements_list()->List[str]:
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires = get_requirements_list()
)

if __name__ == "__main__":
    print(get_requirements_list())
    