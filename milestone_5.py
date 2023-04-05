import random

class Hangman:
    '''
    This class has the attributes and methods to play the Hangman game against the computer.

    Attributes:
        word_list: the list of words available to guess from.
        num_lives: the number of lives remaining for the user.
        list_of_guesses: the running list of all the guesses the user has picked so far.
        word: the chosen random word selected for the game.
        word_guessed: a list of the letters in the word that have been guessed so far.
        num_letters: the number of unique letters that the user needs to guess.
    '''
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.list_of_guesses = []
        self.word = self.generate_random_word(word_list)
        self.word_guessed = self.word_guessed_so_far(self.word, self.list_of_guesses)
        self.num_letters = self.unique_values_not_guessed(self.word, self.word_guessed)

    def generate_random_word(self, word_list) -> str:
        '''
        This function uses the random class to return a random word from a given list.

        Returns:
            str: a word.
        '''
        return random.choice(word_list)
    
    def word_guessed_so_far(self, word, list_of_guesses) -> list:
        '''
        This function checks which letters have been guessed so far and which letters haven't from the word.

        Returns:
            list: a list of characters from the word, showing which letters have been guessed.
        '''
        word_guessed = [''] * len(word)
        for index, char in enumerate(word):
            if (word[index] in list_of_guesses):
                word_guessed[index] = char
        return word_guessed

    def unique_values_not_guessed(self, word, word_guessed) -> int:
        '''
        This function calculates how many unique characters are still to guess in the word.

        Returns:
            int: the sum of unique letters remaining.
        '''
        remaining_letters = []
        for index, char in enumerate(word):
            if (word_guessed[index] == ''):
                remaining_letters.append(char)
        return len(set(remaining_letters))
    
    def check_guess(self, guess):
        '''
        This function checks if the guessed letter is in the word and notifies the user if it is.
        If the guess is in the word the attribute word_guessed if updated to show the letter(s) in the word.
        Else if the guess isn't the number of lives is reduced by 1.

        Returns:
            Nothing
        '''
        guess = guess.lower()
        if (guess in self.word.lower()):
            print(f"Good guess! {guess} is in the word.")
            for index, char in enumerate(self.word):
                if (char == guess):
                    self.word_guessed[index] = guess
            
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
    
    def ask_for_input(self):
        '''
        This function asks the user to input a letter to guess and validates if its a valid input or has already been chosen.

        Returns:
            Nothing
        '''
        guess = input("Please enter a single letter ")
        if not (len(guess) == 1 and guess.isalpha() == True):
            print("Invalid letter. Please enter a single alphabetical character")
        elif (guess in self.list_of_guesses):
            print("You already tried that letter!")
        else:
            self.check_guess(guess)
            self.list_of_guesses.append(guess)
    
    def play_game(self, word_list):
        '''
        This function starts a new game of Hangman with 5 lives, based on the word_list that was passed in as a parameter.

        Returns:
            Nothing
        '''
        num_lives = 5
        game = Hangman(word_list, num_lives)
        while True:
            print(game.word_guessed)
            if game.num_lives == 0:
                print(f"You lost! The word was {game.word}")
                break
            elif game.num_letters > 0:
                game.ask_for_input()
            elif game.num_lives > 0 and game.num_letters == 0:
                print("Congratulations. You won the game!")
                break
            
fruits = ["apple", "avacado", "banana", "blueberry", "cherry", "durian", "grapefruit", "grape", "guava", "kiwi", "lychee", "mango", "orange", "olive", "peach", "pomegrante", "pineapple", "strawberry", "watermelon"]
vegetables = ["asparagus", "beetroot", "broccoli", "cabbage", "carrot", "cauliflower", "celery", "garlic", "kale", "mushroom", "onion", "potato", "pea", "pepper", "spinach", "watercress"]
word_list = []
word_list.extend(fruits)
word_list.extend(vegetables)

Hangman.play_game(Hangman, word_list)