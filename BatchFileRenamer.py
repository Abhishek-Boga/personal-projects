# Author: Abhishek Boga

import os

def rename_file(filename, ext, counter):
    '''Renames a file by appending a counter to the file name.'''
    try:
        os.rename(filename, f"{counter}{ext}")
        return True  # Indicating success
    except Exception as e:
        print(f"Error renaming {filename}: {e}")
        return False  # Indicating failure

def list_files(ext):
    '''Returns the list of files with the given extension.'''
    return [file for file in os.listdir() if file.endswith(ext)]

def get_valid_directory_path():
    '''Prompt the user for a valid directory path.'''
    while True:
        filePath = input('Enter the directory where the file names need to be changed: ').strip()
        if os.path.isdir(filePath):
            return filePath
        else:
            print("Invalid directory path. Please try again.")

def get_valid_extension():
    '''Prompt the user for a valid file extension.'''
    while True:
        ext = input("Enter the file extension (including '.'): ").strip()
        if ext.startswith(".") and len(ext) > 1:
            return ext
        else:
            print("Invalid file extension. Please make sure it starts with a dot (e.g., '.txt').")

def get_confirmation(message):
    '''Asks the user for a confirmation before proceeding with a task.'''
    while True:
        response = input(f"{message} (y/n): ").strip().lower()
        if response in ['y', 'n']:
            return response == 'y'
        print("Invalid input. Please enter 'y' for yes or 'n' for no.")

def main():
    '''Main function to execute the file renaming process.'''
    # Get valid inputs from the user
    filePath = get_valid_directory_path()
    ext = get_valid_extension()

    # Change the current working directory
    try:
        os.chdir(filePath)
    except Exception as e:
        print(f"Error changing directory: {e}")
        return

    # Get the list of files with the specified extension
    fileListExt = list_files(ext)
    print('-' * 50)
    print(f'Found {len(fileListExt)} files with extension "{ext}" in the directory.')

    # If files with the extension are found, proceed with renaming
    if fileListExt:
        print('Files to be renamed: ', fileListExt)

        if get_confirmation("Do you want to proceed with renaming these files?"):
            counter = 1
            renamed_files = []
            not_renamed_files = []
            
            # Attempt renaming each file
            for item in fileListExt:
                if rename_file(item, ext, counter):
                    renamed_files.append(item)
                else:
                    not_renamed_files.append(item)
                counter += 1

            # Summary after renaming process
            print(f'Files with extension "{ext}" have been processed.')
            print(f'Successfully renamed {len(renamed_files)} files.')
            print(f'Files successfully renamed: {renamed_files}')
            print(f'Failed to rename {len(not_renamed_files)} files.')
            print(f'Files not renamed: {not_renamed_files}')

            # In case some files failed to rename, show details
            if not_renamed_files:
                print('There were errors while renaming the following files:')
                for file in not_renamed_files:
                    print(file)
        else:
            print("Renaming process canceled.")
    else:
        print(f'No files found with extension "{ext}".')

if __name__ == "__main__":
    main()
