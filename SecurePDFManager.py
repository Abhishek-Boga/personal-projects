# Author: Abhishek Boga

from PyPDF2 import PdfReader, PdfWriter
import os
import re

def format_file_path(file_path):
    '''Format the file path for compatibility'''
    return os.path.normpath(file_path)

def validate_password_strength(password):
    '''Validate the strength of the password'''
    if len(password) < 6:
        return "Password must be at least 6 characters long."
    if not any(char.isdigit() for char in password):
        return "Password must include at least one number."
    if not any(char.isupper() for char in password):
        return "Password must include at least one uppercase letter."
    if not any(char.islower() for char in password):
        return "Password must include at least one lowercase letter."
    if not any(char in "!@#$%^&*()-_+=" for char in password):
        return "Password must include at least one special character (!@#$%^&*()-_+=)."
    return None

def encrypt_pdf(file_path, password, output_path):
    '''Encrypt a PDF file'''
    try:
        reader = PdfReader(file_path)
        writer = PdfWriter()

        if reader.is_encrypted:
            return f'Error: {os.path.basename(file_path)} is already encrypted. Encryption skipped.'

        for page in reader.pages:
            writer.add_page(page)

        writer.encrypt(password)

        with open(output_path, "wb") as f:
            writer.write(f)

        return f'Success: File has been encrypted and saved as {output_path}.'

    except FileNotFoundError:
        return f'Error: File not found at {file_path}. Please check the path and try again.'
    except PermissionError:
        return f'Error: Permission denied. Ensure you have write access to save the encrypted file in the specified directory.'
    except Exception as e:
        return f'Error: An unexpected issue occurred while encrypting the file: {e}'

def decrypt_pdf(file_path, password, output_path):
    '''Decrypt a PDF file'''
    try:
        reader = PdfReader(file_path)
        writer = PdfWriter()

        if reader.is_encrypted:
            if not reader.decrypt(password):
                return "Error: Incorrect password. Unable to decrypt the file."
        else:
            return f'Error: {os.path.basename(file_path)} is not encrypted. Decryption skipped.'

        for page in reader.pages:
            writer.add_page(page)

        with open(output_path, "wb") as f:
            writer.write(f)

        return f'Success: File has been decrypted and saved as {output_path}.'

    except FileNotFoundError:
        return f'Error: File not found at {file_path}. Please check the path and try again.'
    except PermissionError:
        return f'Error: Permission denied. Ensure you have write access to save the decrypted file in the specified directory.'
    except Exception as e:
        return f'Error: An unexpected issue occurred while decrypting the file: {e}'

def get_valid_file_path(prompt):
    '''Prompt the user for a valid file path'''
    while True:
        file_path = input(prompt).strip()
        file_path = format_file_path(file_path)
        if not os.path.isfile(file_path):
            print('Error: File not found at the provided path. Please enter a valid file path.')
        elif not file_path.lower().endswith('.pdf'):
            print('Error: The selected file is not a PDF. Please select a valid PDF file.')
        else:
            return file_path

def get_valid_directory(prompt):
    '''Prompt the user for a valid directory path'''
    while True:
        directory = input(prompt).strip()
        directory = format_file_path(directory)
        if os.path.isdir(directory):
            return directory
        else:
            print('Error: Invalid directory path. Please enter a valid directory.')

def get_valid_password(prompt):
    '''Prompt the user for a valid password'''
    while True:
        password = input(prompt).strip()
        validation_error = validate_password_strength(password)
        if validation_error:
            print(f'Error: {validation_error}')
        else:
            return password

def get_output_filename(default_name):
    '''Prompt the user for an output filename'''
    while True:
        filename = input(f"Enter the name for the output file (default: {default_name}): ").strip()
        if not filename:  # If blank, use the default name
            return default_name
        if not re.match(r'^[\w\-. ]+$', filename):
            print("Error: Invalid filename. Please avoid special characters like /, \\,:, *, ?, \", <, >, |.")
        else:
            return filename

def get_valid_choice():
    '''Prompt the user for a valid choice (1 or 2)'''
    while True:
        try:
            choice = int(input('Enter your choice (1 or 2): ').strip())
            if choice in [1, 2]:
                return choice
            else:
                print('Error: Invalid choice. Please enter either 1 or 2.')
        except ValueError:
            print('Error: Invalid input. Please enter a number (1 or 2).')

def main():
    '''Main function to handle user input and encryption/decryption'''
    print('PDF Encryption and Decryption Tool')
    print('-' * 50)
    
    file_path = get_valid_file_path('Enter the full path of the PDF file: ')

    print('''Select your choice:
    1) Encrypt the PDF
    2) Decrypt the PDF''')

    choice = get_valid_choice()

    if choice == 1:
        password = get_valid_password('Enter encryption password: ')
        default_name = os.path.splitext(os.path.basename(file_path))[0] + "_encrypted"
        output_directory = get_valid_directory('Enter the directory where the encrypted file should be saved: ')
        output_filename = get_output_filename(default_name)
        output_path = os.path.join(output_directory, f'{output_filename}.pdf')

        result = encrypt_pdf(file_path, password, output_path)
        print(result)

    elif choice == 2:
        password = input('Enter decryption password: ').strip()
        original_name = os.path.splitext(os.path.basename(file_path))[0]
        if original_name.endswith("_encrypted"):
            default_name = original_name[:-10]  # Remove '_encrypted'
        else:
            default_name = original_name + "_decrypted"
        output_directory = get_valid_directory('Enter the directory where the decrypted file should be saved: ')
        output_filename = get_output_filename(default_name)
        output_path = os.path.join(output_directory, f'{output_filename}.pdf')

        result = decrypt_pdf(file_path, password, output_path)
        print(result)

if __name__ == '__main__':
    main()