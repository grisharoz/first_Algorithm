from os import listdir
from os.path import isfile, join


#finding certain file
def printnames(dir):
        for file in sorted(listdir(dir)):
            fullpath=join(dir,file)
            if isfile(fullpath):
              print(file)
            else:
                printnames(fullpath) #recursion function

printnames('pics')
