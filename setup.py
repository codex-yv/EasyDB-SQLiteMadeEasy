from setuptools import setup, find_packages

setup(
    name="Easydb",
    version='0.7',
    packages= find_packages(),
    include_package_data=True,
    package_data={
        'Easydb': ['assets/logo/*.ico'],
    },
    install_requires = [
        "backports.tarfile==1.2.0",
        "certifi==2025.8.3",
        "charset-normalizer==3.4.3",
        "customtkinter==5.2.2",
        "darkdetect==0.8.0",
        "docutils==0.22",
        "engineering-notation==0.10.0",
        "id==1.5.0",
        "idna==3.10",
        "importlib_metadata==8.7.0",
        "jaraco.classes==3.4.0",
        "jaraco.context==6.0.1",
        "jaraco.functools==4.2.1",
        "keyring==25.6.0",
        "markdown-it-py==4.0.0",
        "mdurl==0.1.2",
        "more-itertools==10.7.0",
        "nh3==0.3.0",
        "packaging==25.0",
        "pillow==11.3.0",
        "Pygments==2.19.2",
        "pyttk==0.3.2",
        "pywin32-ctypes==0.2.3",
        "readme_renderer==44.0",
        "requests==2.32.4",
        "requests-toolbelt==1.0.0",
        "rfc3986==2.0.0",
        "rich==14.1.0",
        "tk-tools==0.16.0",
        "twine==6.1.0",
        "urllib3==2.5.0",
        "zipp==3.23.0"
    ],
    entry_points = {
        "console_scripts": [
            "easydb = Easydb:main",
        ],
    },
)

# py setup.py sdist bdist_wheel