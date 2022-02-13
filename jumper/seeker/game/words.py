import random
import subprocess as sp

class Words:

    def __init__(self):
        """Constructs a list of words
        Args:
            self (words): An instance of words.
        """
        pass
        
    def select_word(self):
        _words = ["covid", "pineapple", "sponge", "temple", "spatula", "prophet", "flood", "flower", "python", "rhythm"]
        return random.choice(_words)

    def display_hidden_word(self, _word, _hidden_word):
        for i in range (len(_word)):
            _hidden_word.append("_ ")

        hidden_word_string = ""
        hidden_word_string = hidden_word_string.join(_hidden_word)
        print(hidden_word_string)
        return(_hidden_word)   

    def get_letter(self, _word, _hidden_word, _wrong_guesses):

        letter_input = input("\nGuess a letter [a-z]: ")

        while (len(letter_input.lower()) > 1) or not (letter_input.isalpha()):
            if (len(letter_input.lower()) > 1):
                letter_input = input("\nHow about just one letter?: ")

            if not letter_input.isalpha():
                letter_input = input("\nDo you know what a letter is? Try again: ")

        sp.call('cls', shell=True)

        for i in range (len(_word)):
            if letter_input.lower() == _word[i]:
                _hidden_word.pop(i)
                _hidden_word.insert(i, letter_input.upper() + " ")
        
        if letter_input not in _word:            
            if letter_input.lower() not in _wrong_guesses:
                print(f"\nNope, {letter_input.upper()} is not there!")
                _wrong_guesses.append(letter_input.lower())
            else:
                print(f"You have already guessed that {letter_input.lower()}!")
        
        if len(_wrong_guesses) > 0:
            print(f"Current wrong guesses: {_wrong_guesses}")
                  
        print()
        hidden_word_string = ""
        hidden_word_string = hidden_word_string.join(_hidden_word)
        print(hidden_word_string)

        return _wrong_guesses

        
       
    def game_over(self, _is_playing, _hidden_word):
        _checker = "_ "
        if _checker in _hidden_word:
            _is_playing = True
        else:
            _is_playing = False
            print("\nCongratulations! You Win!")
            exit()
        return _is_playing
