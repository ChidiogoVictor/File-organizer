import os
import shutil


# Takes the input of the directory you want to organize
path = input("Enter path: ")

# Lists of files and directories in a specific directory
files = os.listdir(path)

for file in files:
    # This loop moves through every file from files, then split file name and extension of file
    filename, extension = os.path.splitext(file)
    # removes the dot from the extension name through slicing
    extension = extension[1:]

    # If extension directory already exist, we move the file to that directory
    if os.path.exists(path+"/"+extension):
        shutil.move(path+"/"+file, path+"/"+extension+"/"+file)
    else:
        # makes a new directory and moves the file into it
        os.makedirs(path+"/"+extension)
        shutil.move(path+"/"+file, path+"/"+extension+"/"+file)
