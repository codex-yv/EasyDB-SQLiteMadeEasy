from setuptools import setup, find_packages

setup(
    name="Easydb",
    version='0.2',
    packages= find_packages(),
    install_requires = [

    ],
    entry_points = {
        "console_scripts": [
            "easydb = Easydb:main",
        ],
    },
)