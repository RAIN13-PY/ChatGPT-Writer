import os

def checkIfFolderIsCreated():
    # Check if the text folder exists
    directory = os.getcwd() + "/text"
    if os.path.exists(directory) == False:
        return(False)
    else:
        return(True)

def checkIfTextFileIsCreated():
    # Check if text.txt exists in the text folder
    directory = os.getcwd() + "/text/text.txt"
    if os.path.exists(directory) == False:
        return(False)
    else:
        return(True)

def checkIfConfigFileIsCreated():
    # Check if config.txt exists in the text folder
    directory = os.getcwd() + "/text/config.txt"
    if os.path.exists(directory) == False:
        return(False)
    else:
        return(True)

def fileSetup():
    num_checks = 0
    if checkIfFolderIsCreated() == False:
        # Create the text folder if it doesn't exist
        directory = os.getcwd() + "/text"
        os.mkdir(directory, 0o666)
        num_checks += 1
    if checkIfTextFileIsCreated() == False:
        # Create the text.txt file if it doesn't exist
        with open("text/text.txt", "w") as file:
            file.close()
        num_checks += 1
    if checkIfConfigFileIsCreated() == False:
        # Create the config.txt file if it doesn't exist
        with open("text/config.txt", "w") as file:
            file.close()
        num_checks += 1
    return num_checks