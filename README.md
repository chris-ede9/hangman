# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.

## Milestone 1

- The first milestone was learning about how Git works, the best practices to use and hooking up to GitHub so that the code is stored remotely and securely to be worked on through the course of the project tasks.

- A branch strategy is used whereby all development is done on a dev branch for each task and once verfied is correct, this is then merged to the main branch and synced back to GitHub.

## Milestone 2

- This milestone was the start of the implementation of the hangman solution. Firstly we were required to store a list of favourite fruits. This was enhanced by importing the random module, which is a 3rd party module which allows for selecting a random value from a passed in list. This would therefore select a random fruit from the list.

- Next we added user interction and validation, requesting that the user entered a single letter and checking that the input enter was an alphabetic single character. Depending on the input the user will be notified if it was valid or not.

- Below is the code done for milestone 2:

```bash
import random

word_list = ["apples", "blueberries", "grapes", "oranges", "strawberries"]
print(word_list)

word = random.choice(word_list)
print(word)

guess = input("Please enter a single letter ")

if (len(guess) == 1 and guess.isalpha() == True):
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
```

## Milestone 3

- This milestone first concentrated on checking whether the input provided by the user was in the random fruit word that was selected. It would keep repeating the request until the user selected a letter that was a match.

- However as the code was becoming one long script, the milestone also specified that it should be more readable and functions should be applied. The code was refactored to contain 2 functions:
    - check_guess
    - ask_for_input
<br/><br/>
- Below is the code done for milestone 3:

```bash
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
```

## Milestone n

- Continue this process for every milestone, making sure to display clear understanding of each task and the concepts behind them as well as understanding of the technologies used.

- Also don't forget to include code snippets and screenshots of the system you are building, it gives proof as well as it being an easy way to evidence your experience!

## Conclusions

- Maybe write a conclusion to the project, what you understood about it and also how you would improve it or take it further.

- Read through your documentation, do you understand everything you've written? Is everything clear and cohesive?
