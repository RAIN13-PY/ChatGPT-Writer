import os
import time
# Clone the GitHub repository
print("installing ...")
directory = os.getcwd() + "\ChatGPT-Writer"
os.mkdir(directory, 0o666)
os.system("git clone https://github.com/RAIN13-PY/ChatGPT-Writer")

# Navigate to the directory of the cloned repository
os.chdir(directory)

# Install the program using pip
os.system("pip install .")
print("installed. Closing...")
time.sleep(3)
