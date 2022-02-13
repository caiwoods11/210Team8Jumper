# CSE210Team8
## Week 5 &amp; 6 Jumper Game
##  Kenneth :  _kyl03001@byui.edu_   
## Cai :  _caiwoods11@byui.edu_
### 12 Feb 2022

<br>
<br>

## Creator Specs:<br>

Game Set Up 
```python 
from game.words import Words
from game.parachute import Parachute


class Director:

    def __init__(self):
        self._is_playing = True
        self._words = Words()
        self._parachute = Parachute()

        self._word = Words.select_word(self)
        self._hidden_word = []
        self._parts = Parachute.declare_parts(self)
        self._wrong_guesses = []        
        
```
Starts the Game:
```python 

    def start_game(self):
        self._display_word()
        
        while self._is_playing:         
            self._display_parachute()
            self._get_input()
            self._check_end_game()

```
The word is converted to all underscores and hides the letters
```python 

    def _display_word(self):
        Words().display_hidden_word(self._word, self._hidden_word)

    def _display_parachute(self):
        if len(self._wrong_guesses) == 0:
            Parachute().draw_parachute_full(self._parts)
        if len(self._wrong_guesses) == 1:
            Parachute().draw_parachute_1(self._parts)
        if len(self._wrong_guesses) == 2:
            Parachute().draw_parachute_2(self._parts)
        if len(self._wrong_guesses) == 3:
            Parachute().draw_parachute_3(self._parts)
        if len(self._wrong_guesses) == 4:
            Parachute().draw_parachute_4(self._parts)
        if len(self._wrong_guesses) == 5:
            Parachute().draw_parachute_5(self._parts)
            print(f"Sorry! You died... the word was {self._word.upper()}")
            exit()

```
A letter is requested from the User and the program determines if it is correct or not:
```python 

    def _get_input(self):
        Words().get_letter(self._word, self._hidden_word, self._wrong_guesses)

```
Checks if the game has been won or lost
```python 

    def _check_end_game(self):
        Words().game_over(self._is_playing, self._hidden_word)

```
from words.py
```python 
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


```
from parachute.py
```python 
class Parachute:

    def __init__(self):

        """Constructs a new Parachute class.
        Args:
            self (Parachute): An instance of Parachute.
        """
        pass

    def declare_parts(self):
        p_parts = ["_____","/","_____","\\","\\","/","\\","/","O"]
        return p_parts

    def draw_parachute_full(self, _parts):
        self.p_draw = f"""
  {_parts[0]}
 {_parts[1]}{_parts[2]}{_parts[3]}
 {_parts[4]}     {_parts[5]}
  {_parts[6]}   {_parts[7]}
    {_parts[8]}
   /|\\
   / \\
^^^^^^^^^ """
        print(self.p_draw)


    def draw_parachute_1(self, _parts):
        self.p_draw = f"""
 {_parts[1]}{_parts[2]}{_parts[3]}
 {_parts[4]}     {_parts[5]}
  {_parts[6]}   {_parts[7]}
    {_parts[8]}
   /|\\
   / \\
^^^^^^^^^ """
        print(self.p_draw)


    def draw_parachute_2(self, _parts):
        self.p_draw = f"""
 {_parts[1]}     {_parts[3]}
 {_parts[4]}     {_parts[5]}
  {_parts[6]}   {_parts[7]}
    {_parts[8]}
   /|\\
   / \\
^^^^^^^^^ """
        print(self.p_draw)


    def draw_parachute_3(self, _parts):
        self.p_draw = f"""
 {_parts[4]}     {_parts[5]}
  {_parts[6]}   {_parts[7]}
    {_parts[8]}
   /|\\
   / \\
^^^^^^^^^ """
        print(self.p_draw)


    def draw_parachute_4(self, _parts):
        self.p_draw = f"""
  {_parts[6]}   {_parts[7]}
    {_parts[8]}
   /|\\
   / \\
^^^^^^^^^ """
        print(self.p_draw)


    def draw_parachute_5(self, _parts):
        self.p_draw = f"""
    x
   /|\\
   / \\
^^^^^^^^^ """
        print(self.p_draw)



```
Run in main file 

```python
from game.director import Director

director = Director()
director.start_game()
```

<br>
<br>

## Game Play Directions:
   - The puzzle is a secret word randomly chosen from a list. <br>
   - The player guesses a letter in the puzzle. <br>
   - If the guess is correct, the letter is revealed. <br>
   - If the guess is incorrect, a line is cut on the player's parachute. <br>
   - If the puzzle is solved the game is over. <br>
   - If the player has no more parachute the game is over. <br>


