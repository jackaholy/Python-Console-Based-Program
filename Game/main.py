"""
Created on Jan. 19, 2024

A console based game in python where a certain keyboard key will appear on the
console and the player will have to type that key as quickly as possible.
After the key appears a timer will start and stop keeping track of how much time
it took for them to press that key.

The player can play through 4 levels and must stay under a certain time in order to
proceed to the next level.

@author jackholy
"""

import time
import random

# The number of levels available
levels = [1, 2, 3, 4]
# Time required to beat the level
seconds_to_beat_level = 8


# Instructions on how to play the game
def instructions():
    print("SPEED TYPING GAME\nYou will face a series of levels attempting to type the appropriate keyboard key as "
          "fast as possible.")
    input("\nPress Enter to continue...\n")
    print(
        "Each level will have different keys that may appear: \n"
        "Easy:\t\t\tabcdefghijklmnopqrstuvwxyz\n"
        "Intermediate:\tabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ\n"
        "Hard:\t\t\tbcdfghjklmnpqrvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12345678901234567890\n"
        "Expert:\t\t\tBCDFGHJKLMNPQRSTVWXYZ1234567890!@#$%^&*()`~-_=+[]{}\\|;:\'\",.<>/?\n")
    input("Press Enter to continue...\n")
    input(
        f"Press the appropriate series of keys within {seconds_to_beat_level} seconds in order to advance to the next "
        "level.\n"
        "After pressing a key you must press Enter to submit your guess"
        "\n\nPress Enter to begin level 1...\n")


def end_game(total_game_time, level):
    median_time = total_game_time / len(levels)
    # After they complete the game tell the player how much time they took.
    print(f"Fantastic! You completed each of the {level} levels with a total time of {total_game_time:.2f} seconds")
    print(f"Average time: {median_time:.2f} seconds\n")


def game_foundation(key_options, level):
    count = 0
    time_taken_for_level = 0.00
    total_game_time = 0.00
    # The player must guess correctly 5 keys to proceed.
    while count < 5:
        target_key = random.choice(key_options)
        print(f"Press the key: {target_key}")

        # Start the timer when the target key appears on screen.
        start_time = time.time()

        user_input = input("Your guess: ")

        # After they guess stop the timer and calculate the time it took for their guess.
        end_time = time.time()
        time_taken_for_guess = end_time - start_time
        # Check and see if the player presses the correct key.
        # If they press correct key show them how much time that guess took.
        if user_input == target_key:
            count += 1
            time_taken_for_level += time_taken_for_guess
            print(f"Correct! Time taken: {time_taken_for_guess:.2f} sec")
        # If the user presses the incorrect key add to the overall level time and make them try again.
        else:
            time_taken_for_level += time_taken_for_guess
            print("Incorrect! Try again.")

        # Calculate if the player exceeded the seconds required to guess during the level.
        # If they exceed the time limit have them try again.
        if count > 4 and time_taken_for_level > seconds_to_beat_level:
            print(f"Level {level} FAILED. You exceeded the time requirement.")
            input(f"Total time taken: {time_taken_for_level:.2f} sec"
                  "\n\nPress Enter to try again...")
            # Reset level time and count
            time_taken_for_level = 0.00
            count = 0

    # After the player has finished the level calculate how much time it took them and determine if they can advance
    # to the next level.
    total_game_time += time_taken_for_level

    # If there are still levels left to be played show total level time and allow them to continue
    if level < 4:
        print(f"Level {level} COMPLETE! Total time taken: {time_taken_for_level:.2f} sec")
        input(f"\nPress Enter to begin level {level + 1}...")
    # If the user completed each of the levels just show time and allow them to continue to final screen.
    else:
        print(f"Level {level} complete! Total time taken: {time_taken_for_level:.2f} sec")
        input("\nPress Enter to continue...\n")

    return total_game_time


def easy_game(level):
    return game_foundation("abcdefghijklmnopqrstuvwxyz", level)


def intermediate_game(level):
    return game_foundation("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", level)


def hard_game(level):
    return game_foundation("bcdfghjklmnpqrvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12345678901234567890", level)


def expert_game(level):
    return game_foundation(
        "BCDFGHJKLMNPQRSTVWXYZ1234567890!@#$%^&*()`~-_=+[]{}\\|;:\'\",.<>/?!@#$%^&*()`~-_=+[]{}\\|;:\'\",.<>/?", level)


def main():
    while True:
        instructions()
        total_game_time = 0.00
        # Iterate through each of the levels in the levels list.
        for level in levels:
            if level == 1:
                total_game_time += easy_game(level)
            elif level == 2:
                total_game_time += intermediate_game(level)
            elif level == 3:
                total_game_time += hard_game(level)
            elif level == 4:
                total_game_time += expert_game(level)
            else:
                print("\nInvalid option, please try again.")
        # After the player finishes each of the levels proceed to the end game.
        end_game(total_game_time, level)
        # Allow the player to play again or quit.
        play_again = input("Do you want to play again?\nEnter 'Y' to play again, Enter any other key to quit: ")
        if play_again.lower() != 'y':
            break


if __name__ == "__main__":
    main()
