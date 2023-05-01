from setuptools import setup

setup(
    name="my_package",
    version="0.1",
    author="Your Name",
    author_email="your.email@example.com",
    description="My package description",
    install_requires=[
        "os",
        "pyautogui",
        "win10toast"
    ],
    packages=["my_package"],
    entry_points={
        "console_scripts": [
            "my_script = my_package.my_module:main"
        ]
    }
)
