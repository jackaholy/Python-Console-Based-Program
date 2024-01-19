# A console based game in python where a certain keyboard key will appear on the
# console and the player will have to type that key as quickly as possible.
# After the key appears a timer will start and stop keeping track of how much time
# it took for them to press that key.

# Imports
import time
import random


def levels():
    print(
        f"Choose a difficulty (Type '1-4'): \n Easy:         1\n Intermediate: 2\n Hard:         3\n Expert:    "
        f"   4\n")


def game_foundation(key_options):
    count = 0
    # total_time = None
    while True and count < 3:
        target_key = random.choice(key_options)
        print(f"Press the key: {target_key}")

        start_time = time.time()

        user_input = input("Your guess: ")

        end_time = time.time()

        if user_input == target_key:
            time_taken = end_time - start_time
            # total_time += time_taken
            print(f"Correct! Time taken: {time_taken:.2f} sec")
            count += 1
        else:
            print("Incorrect! Try again.")
    # After the player has finished the game calculate how much time it took them total
    # total_time = end_total_time - start_total_time

    # print(f"Total time taken: {total_time:.2f} sec")


def easy_game():
    game_foundation('abcdefghijklmnopqrstuvwxyz')


def intermediate_game():
    game_foundation('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')


def hard_game():
    game_foundation('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')


def expert_game():
    game_foundation('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ1234567890!@#$%^&*()`~-_=+[]{}\|;:'",.<>/?")


def main():
    # Allow the user to choose between 4 levels of difficulty
    selected_level = input(levels())
    # Depending on their choice they will play that game
    while True:
        if selected_level == '1':
            easy_game()
            break
        elif selected_level == '2':
            intermediate_game()
            break
        elif selected_level == '3':
            hard_game()
            break
        elif selected_level == '4':
            expert_game()
            break
        else:
            print("\nInvalid option, please try again.")
            selected_level = input(levels())


if __name__ == "__main__":
    main()
