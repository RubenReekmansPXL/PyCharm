__author__ = 'epq_008'
# File Input/Output in Python

# Loads a text file into a single string
# Parameters:
#   fileName: a string with the name of the file to be loaded
# Returns a string
def loadTextString(fileName):
    fileHandler = open(fileName, "rt") # rt stands for read text
    text = fileHandler.read() # read the entire file into a single string
    fileHandler.close() # close the file
    return text

# Loads a text file into a list of strings. Each string is one line of text.
# Parameters:
#   fileName: a string with the name of the file to be loaded
# Returns a list of strings
def loadTextList(fileName):
    fileHandler = open(fileName, "rt") # rt stands for read text
    text = fileHandler.readlines() # read the entire file into a list
    fileHandler.close() # close the file
    return text

# Saves a string into a file.
# If the file already exists, it will be overwritten.
# Parameters:
#   fileName: a string with the name of the file to be written
# Returns None
def saveText(text, fileName):
    fileHandler = open(fileName, "wt") # wt stands for write text
    fileHandler.write(text) # write the text
    fileHandler.close() # close the file