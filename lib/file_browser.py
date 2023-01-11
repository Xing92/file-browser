from os import walk
from os import listdir

def getDirectoryContent(path):
    #filenames = next(walk(directory), (None, None, []))[2]  # [] if no file
    filenames = [f for f in listdir(path)]
    return filenames


#content = getDirectoryContent("..")
#for file in content:
#    print(file)
