import os
def checkIfFolderIsCreated():
    directory = os.getcwd() + "/text"
    if os.path.exists(directory) == False:
        return(False)
    else:
        return(True)
def makeDirectory():
    directory = os.getcwd() + "/text"
    os.mkdir(directory, 0o666)
    file = open("text/text.txt", "x")
    file.close()
    return
def directorySetup():
    if checkIfFolderIsCreated() == False:
        makeDirectory()
        return("Folder created")
    else:
        return("Folder already created Aborting")
