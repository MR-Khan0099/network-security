from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    """Read the requirements.txt file and return a list of dependencies."""
    requirements_list: List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and not requirement.startswith('#') and not requirement.startswith('-e'):
                    requirements_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found.")
    return requirements_list

setup(
    name='NetworkSecurity',
    version='0.1',
    author='Rizwan',
    author_email="mohammedrizwan0909@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)










