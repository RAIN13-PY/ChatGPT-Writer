from setuptools import setup

setup(
    name="ChatGPT-Writer",
    version="0.1",
    author="Your Name",
    author_email="Not Included",
    description="To do",
    install_requires=[
        "os",
        "pyautogui",
        "win10toast"
    ],
    packages=["main", "main.makeDirectories", "main.notify"]
)
