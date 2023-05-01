from makeDirectories import fileSetup
from notify import notify
from config import wait_b_s, interval_b_c_m, interval_b_c_ma

def main():
    fileSetup()
    file = open("text/text.txt", "r")
    print(file.readline())
    if file.readline() == "":
        notify("There is no text in text.txt!")
        return
    #print(wait_b_s)
main()
