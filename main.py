import art
from art import *
from data import *
import random

def compare(A, B):
    """Returns A if A has more followers, otherwise returns B."""
    if A["follower_count"] > B["follower_count"]:
        return 'A'
    else:
        return 'B'

def format(person):
    """Formats account data into a printable string."""
    name = person["name"]
    description = person["description"]
    country = person["country"]
    follower_count = person["follower_count"]
    return f"{name}, a {description}, from {country}"

def play():
    # Variables
    score = 0
    lives = 3
    more_game = True

    while more_game:
        print(logo)

        person_one = random.choice(data)
        person_two = random.choice(data)

        # Make sure they are different
        while person_one == person_two:
            person_two = random.choice(data)

        print(f"Compare A: {format(person_one)}")
        print(vs)
        print(f"Against B: {format(person_two)}")

        answer = input("Who has more followers? Type 'A' or 'B': ?")

        result = compare(person_one, person_two)

        if result == answer:
            score += 1
            print("Correct!")
        else:
            lives -= 1
            print("Wrong!")

        if lives == 0:
            more_game = False
            print("Game Over")

        print(f"Score: {score}")
        print(f"Lives: {lives}")

play_again = input("Would you like to play a game of Higher Lower? Type 'y' or 'n': ").lower()
if play_again == "n":
    more_game = False
if play_again == "y":
    play()