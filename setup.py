
from setuptools import setup, find_packages

# Read the README.md for the long description
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pyhotkey',
    version='0.1',
    description='A hotkey manager with a pyhotkey modifier system',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Cary Carter',
    author_email='ccarterdev@gmail.com',
    url='https://github.com/cc-d/pyhotkey',
    packages=find_packages(),
    install_requires=[
        'keyboard>=0.13.5',
        'pyautogui>=0.9.52',
    ],
    entry_points={
        'console_scripts': [
            'pyhotkey=pyhotkey.main:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
