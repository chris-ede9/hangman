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

'''
#Testing purposes
word_list = ["apples", "blueberries", "grapes", "oranges", "strawberries"]
new_game = Hangman(word_list, 7)
print(new_game.word_list)
print(new_game.num_lives)
print(new_game.list_of_guesses)
print(new_game.word)
print(new_game.word_guessed)
print(new_game.num_letters)
'''