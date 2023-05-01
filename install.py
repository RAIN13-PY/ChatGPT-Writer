import os

# Clone the GitHub repository
directory = os.getcwd() + "ChatGPT-Writer"
os.mkdir(directory, 0o666)
os.system("git clone https://github.com/RAIN13-PY/ChatGPT-Writer")

# Navigate to the directory of the cloned repository
os.chdir("Chat")

# Install the program using pip
os.system("pip install .")
