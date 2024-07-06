from setuptools import find_packages, setup

def get_requirements(file):
    requirements = []
    with open(file) as f:
        requirements = f.read().splitlines()
        return requirements

setup(
    name="ML Project",
    version="1.0.1",
    author="Rithish S",
    author_email="rithish.satish@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
