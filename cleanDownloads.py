# -*- coding: utf-8 -*-

import os

numberOfFilesMoved=0
movedFilesList=[]

numberOfFilesAlreadyExisting=0
alreadyExistingFilesList=[]

downloadsFolder="C:/Users/Enzo/Downloads"
downloadsFolderPath="C:/Users/Enzo/Downloads/"

dlFolder="C:/Users/Enzo/Desktop/dl"
dlFolderPath="C:/Users/Enzo/Desktop/dl/"

print("Downloads folder cleaner")
print("This script is running from : " + os.getcwd())
print("----------")

# parse files in C:/Users/Enzo/Downloads
for filename in os.listdir(downloadsFolder):
    # if the file isn't a zip or rar or exe or msi or ini file or a folder
    if not(filename.endswith(".zip") or filename.endswith(".rar") or filename.endswith(".exe") or filename.endswith(".msi") or filename.endswith(".ini") or os.path.isdir("C:/Users/Enzo/Downloads/" + filename)):
        # if the file doesn't exist in C:/Users/Enzo/Desktop/dl
        if not(os.path.isfile(dlFolderPath + filename)):
            # cut files from C:/Users/Enzo/Downloads to C:/Users/Enzo/Desktop/dl
            os.rename(downloadsFolderPath + filename, dlFolderPath + filename)
            numberOfFilesMoved+=1
            movedFilesList.append(filename)
        else:
            numberOfFilesAlreadyExisting+=1
            alreadyExistingFilesList.append(filename)

print(f"{numberOfFilesMoved} file(s) moved")
for filename in movedFilesList:
    print(f"{filename}\n")

print("-----------")

print(f"{numberOfFilesAlreadyExisting} file(s) already in C:/Users/Enzo/Desktop/dl :")
for filename in alreadyExistingFilesList:
    print(f"{filename}\n")

