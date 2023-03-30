import random

def check_guess(guess):
    guess = guess.lower()
    if (guess in word.lower()):
        print(f"Good guess! {guess} is in the word.")
        return True
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")
        return False

def ask_for_input():
    while True:
        guess = input("Please enter a single letter ")
        if (len(guess) == 1 and guess.isalpha() == True):
            if check_guess(guess) == True:
                break
        else:
            print("Invalid letter. Please enter a single alphabetical character")

word_list = ["apples", "blueberries", "grapes", "oranges", "strawberries"]
word = random.choice(word_list)

ask_for_input()