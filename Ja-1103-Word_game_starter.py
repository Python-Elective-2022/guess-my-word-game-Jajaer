
#On this project I have collaborated with the following student: Petch
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "word_list.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Reading word_list file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # word_list: list of strings
    word_list = line.split()
    print(len(word_list), "words found")
    return word_list

def choose_word(word_list):
    """
    word_list (list): list of words (strings)

    Returns a word from word_list at random
    """
    return random.choice(word_list)

# end of helper code
# -----------------------------------

# Load the list of words into the variable word_list
# so that it can be accessed from anywhere in the program
word_list = load_words()

def is_word_guessed(secret_word, letters_guessed):
        '''
        secret_word: string, the word the user is guessing
        letters_guessed: list, what letters have been guessed so far
        returns: boolean, True if all the i of secret_word are in letters_guessed;
        False otherwise
        '''
        # FILL IN YOUR CODE HERE...
        """
        for every i in secret word
        if i is not in the letters_guessed
            return false
        return true
        """
        for i in secret_word:
            if i not in letters_guessed:
                return False
        return True


### Testcases
# print(is_word_guessed('apple', ['a', 'e', 'i', 'k', 'p', 'r', 's']))
# print(is_word_guessed('durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u']))
# print(is_word_guessed('pineapple', []))



def get_guessed_word(secret_word, letters_guessed):
        '''
        secret_word: string, the word the user is guessing
        letters_guessed: list, what i have been guessed so far
        returns: string, comprised of i and underscores that represents
        what i in secret_word have been guessed so far.
        '''
        # FILL IN YOUR CODE HERE...
        '''
        for every i in secret_word:
            if the i is in letters_guessed:
                concatenate that i onto return_string
            otherwise
                concatenate underscore space onto return_string
        return the string
        '''
    
        full_word = ''
        for i in secret_word:
            if i in letters_guessed:
              full_word += i
            else: 
              full_word += ' _ '
        return full_word 
    
    
    
      
#Testcases
# print(get_guessed_word('apple', ['e', 'i', 'k', 'p', 'r', 's']))
# print(get_guessed_word('durian', ['a', 'c', 'd', 'h', 'i', 'm', 'n', 'r', 't', 'u']))

def get_available_letters(letters_guessed):
        '''
        letters_guessed: list, what i have been guessed so far
        returns: string, comprised of i that represents what i have not yet been guessed.
        '''

        # FILL IN YOUR CODE HERE...
        import string
        alphabet = string.ascii_lowercase
        '''
        for every i in letter_guessed
            .replace the i in the alphabet with empty string
        return the string
        '''

        for i in letters_guessed:
            alphabet = alphabet.replace(i,'')
        return alphabet



#Testcases 
# print( get_available_letters(['e', 'i', 'k', 'p', 'r', 's']) )


def game_loop(secret_word):
  guess_remaining = 8
  letter_guessed = [] 
  print ("Let the game begin!")
  print ("")
  print ("I am thinking of a word with", len(secret_word), "letters")

  while is_word_guessed(secret_word, letter_guessed) == False and guess_remaining > 0:
        print("You have", guess_remaining, "guesses remaining")
        print("Letters available to you:", get_available_letters(letter_guessed))
        guess_a_letter = input("Guess a letter:").lower()

        if (guess_a_letter in get_available_letters(letter_guessed)):
            letter_guessed.append(guess_a_letter)
            if (guess_a_letter in secret_word):
                print("Correct:", get_guessed_word(secret_word, letter_guessed))
            else:
                print("Incorrect, this letter is not in my word:", get_guessed_word(secret_word, letter_guessed))
                guess_remaining -= 1
        else:
          print("You fool", get_guessed_word(secret_word, letter_guessed))

  if (is_word_guessed(secret_word, letter_guessed)):
        print ("You WIN")
  else :
        print("GAME OVER ! The word was",(secret_word))




def main():
    secret_word = choose_word(word_list)
    game_loop(secret_word)

# Testcases
# you might want to pick your own
# secret_word while you're testing


if __name__ == "__main__":
    main()