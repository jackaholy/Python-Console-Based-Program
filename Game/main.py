# A console based game in python where a certain keyboard key will appear on the
# console and the player will have to type that key as quickly as possible.
# After the key appears a timer will start and stop keeping track of how much time
# it took for them to press that key.

# Imports
import keyboard
import time
import random

#Create a game function
def game():
    target_key = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')

    print(f"Press the key: {target_key}")

    start_time = time.time()

    # Wait for the correct key press
    keyboard.wait(target_key)

    end_time = time.time()
    # Calculate how much time it took to press the key
    time_taken = end_time - start_time
    print(f"Time taken: {time_taken:.2f} seconds")


if __name__ == "__main__":
    game()
