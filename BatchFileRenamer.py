# Author: Abhishek Boga

import os

def rename_file(filename,ext,counter):
    ''' Renames a file'''
    os.rename(filename,str(counter)+f"{ext}")

def list_files(ext):
    ''' Returns the List of files with the given extension'''
    newListFiles=[]
    for file in os.listdir():
        if(file.endswith(ext)):
            newListFiles.append(file)
    return newListFiles

# Taking input from user for filePath and extension
filePath=input('Enter the directory where the file names need to be changed: ')
ext=input("Enter the file extension (along with '.'): ")

# Formatting filePath
newFilePath=filePath.replace('\\','/')
os.chdir(newFilePath)

# Calling method to fetch list of files from the directory based on the specified extension
fileListExt=list_files(ext)
print(''.center(50,'-'))
print(f'Count of files with extension "{ext}" in the directory: {len(fileListExt)}')

# Checking if the files are present with given extension after which only rename functionalities will work
if(len(fileListExt)!=0):
    print('Start of File Rename Functionality'.center(50,'-'))
    print(f'List of files with extension "{ext}" in the directory: ',fileListExt)
    counter=0
    for item in fileListExt:
        counter+=1
        rename_file(item,ext,counter)
    print(f'Files with extension "{ext}" that have been renamed successfully: {counter}')
    print(f'Renamed List of files with extension "{ext}" in the directory: ',list_files(ext))
    print("End of File Rename Functionality".center(50,'-'))
else:
    print(''.center(50,'-'))
    print(f'No files found with extension "{ext}"')
