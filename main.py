from makeDirectories import directorySetup
from notify import notify

def main():
    print(directorySetup())
    file = open("text/text.txt", "r")
    print(file.readline())
    if file.readline() == "":
        notify("There is no text in text.txt!")
main()
