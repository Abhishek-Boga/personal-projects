# Author: Abhishek Boga

import random

def select_random_choice(choices):
    '''Select a random item from the list of choices.'''
    return random.choice(choices)

def get_choice_name(choice, choice_map):
    '''Get the name of a choice based on its value.'''
    return choice_map.get(choice, 'Unknown')

def determine_result(player_choice, computer_choice):
    '''Determine the game result based on player and computer choices.'''
    if player_choice == computer_choice:
        return 'Draw'
    elif (player_choice == 1 and computer_choice == 2) or \
         (player_choice == 2 and computer_choice == 3) or \
         (player_choice == 3 and computer_choice == 1):
        return 'Win'
    else:
        return 'Loss'

def get_valid_player_choice(choice_map):
    '''Prompt the user for a valid choice with validation.'''
    while True:
        print("Please choose an option:")
        for key, value in choice_map.items():
            print(f"{key}) {value}")

        try:
            player_choice = int(input("Enter the option number: ").strip())
            if player_choice in choice_map:
                return player_choice
            else:
                print(f"Invalid choice. Please select a number between 1 and {len(choice_map)}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    '''Main function for the Snake-Water-Gun game.'''
    # Mapping of choices
    choice_map = {
        1: 'Snake',
        2: 'Water',
        3: 'Gun'
    }

    # Generate computer choice
    comp_choice = select_random_choice(list(choice_map.keys()))

    # Get player's choice with validation
    player_choice = get_valid_player_choice(choice_map)

    # Display choices
    print(f"\nPlayer's Choice: {get_choice_name(player_choice, choice_map)}")
    print(f"Computer's Choice: {get_choice_name(comp_choice, choice_map)}")

    # Determine and display the result
    result = determine_result(player_choice, comp_choice)
    print(f"\n{' Result: ' + result + ' ':=^50}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGame interrupted. Exiting...")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")