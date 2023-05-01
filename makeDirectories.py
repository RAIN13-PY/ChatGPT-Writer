import os
configText = "[Main Config]\nwait_before_start = 5\ninterval_between_character_min = 0.1\ninterval_between_character_max = 0.3\nuse_default_config = false"
def checkIfFolderIsCreated():
    directory = os.getcwd() + "/text"
    if os.path.exists(directory) == False:
        return(False)
    else:
        return(True)
def checkIfTextFileIsCreated():
  directory = os.getcwd() + "/text/text.txt"
  if os.path.exists(directory) == False:
    return(False)
  else:
    return(True)
def checkIfConfigFileIsCreated():
  directory = os.getcwd() + "/config.txt"
  if os.path.exists(directory) == False:
    return(False)
  else:
    return(True)
def fileSetup():
  checks = 0
  if checkIfFolderIsCreated() == False:
    directory = os.getcwd() + "/text"
    os.mkdir(directory, 0o666)
    checks += 1
  if checkIfTextFileIsCreated() == False:
    file = open("text/text.txt", "x")
    file.close()
    checks =+ 1
  if checkIfConfigFileIsCreated() == False:
    file = open("config.txt", "x")
    file.close()
    file = open("config.txt","w")
    file.write(configText)
    file.close()
    checks += 1
  return checks

