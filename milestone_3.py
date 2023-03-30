import random

word_list = ["apples", "blueberries", "grapes", "oranges", "strawberries"]
word = random.choice(word_list)

while True: 
    guess = input("Please enter a single letter ")
    guess = guess.lower()

    if (len(guess) == 1 and guess.isalpha() == True):
        if (guess in word):
            print(f"Good guess! {guess} is in the word.")
            break
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")
    else:
        print("Invalid letter. Please enter a single alphabetical character")
