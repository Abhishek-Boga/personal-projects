# Author: Abhishek Boga

import random
import string

def generate_random_chars(num_chars=3):
    """Generate a string of random characters with the specified length."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=num_chars))

def modify_string(original_string):
    """Append 3 random characters to the beginning and end of the original string, ensuring they are different."""
    # Generate 3 random characters for the beginning
    random_chars_beginning = generate_random_chars()   
    # Generate 3 random characters for the end, ensuring they are different from the beginning
    random_chars_end = generate_random_chars()
    while random_chars_end == random_chars_beginning:
        random_chars_end = generate_random_chars()
    return f"{random_chars_beginning}{original_string}{random_chars_end}"

def encode(word):
    """
    Encoding functionality:
    - If length < 3: reverse the string.
    - If length >= 3: remove the first letter, place it at the end, and add 3 random characters at the start and end.
    """
    if len(word) < 3:
        return word[::-1]
    return modify_string(word[1:] + word[0])

def decode(word):
    """
    Decoding functionality:
    - If length < 3: reverse the string.
    - If length >= 3: remove 3 random characters from the start and end, then move the last character to the beginning.
    """
    if len(word) < 3:
        return word[::-1]
    temp = word[3:-3]
    return temp[-1] + temp[:-1]

def process_sentence(sentence, action):
    """Process the sentence for encoding or decoding based on the specified action."""
    words = sentence.split()
    
    # Select encoding or decoding method
    process_function = encode if action == 'encode' else decode

    # Process all words in the sentence and store the result
    return ' '.join([process_function(word) for word in words])

def get_valid_input(prompt, valid_choices=None, is_numeric=False):
    """Get valid user input with the given prompt. Optionally validate for numeric input or valid choices."""
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            print("Input cannot be empty. Please try again.")
            continue
        if is_numeric and not user_input.isdigit():
            print("Please enter a valid number.")
            continue
        if valid_choices and user_input.lower() not in valid_choices:
            print(f"Invalid choice. Please choose one of the following: {', '.join(valid_choices)}")
            continue
        return user_input

def main():
    """Main function to handle user input and execute encoding/decoding."""
    # Get valid user input for sentence and action
    sentence = get_valid_input("Enter the sentence: ")
    action = get_valid_input("Enter whether to 'encode' or 'decode': ", valid_choices=['encode', 'decode'])

    try:
        result = process_sentence(sentence, action)
        print(f"Result ({action.capitalize()}d): {result}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
