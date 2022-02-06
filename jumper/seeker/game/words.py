from itertools import count
import random
from re import X

class Words:
    """The person hiding from the Seeker. 
    
    The responsibility of Hider is to keep track of its location and distance from the seeker. 
    
    Attributes:
        _location (int): The location of the hider (1-1000).
        _distance (List[int]): The distance from the seeker.
    """

    def __init__(self):
        """Constructs a list of words

        Args:
            self (words): An instance of words.
        """
        self._words = ["covide", "pineapple", "sponge", "temple", "spatulae", "prophet"] # team mates add more
        self._word = random.choice(self._words)
        self._letter = []
        self.hider = []   
        

    def get_word(self):
        """Get Random Word  
        """
    
        return self._word

    def hide_word(self):
        """ Puts the _ _ _ _ _ _ _ down for the length of the random word
        """

        self._letter = list(self._word)
        #return self.letter
  
        for i in range (len(self._letter)):
            self.hider.append("_ ")
        #print(self.hider) -- to check if it is converting to _

        #return self._letter        

        hider_string = ""
        hider_string = hider_string.join(self.hider)
        print( hider_string)
           
    def display_word(self):
        """ displays the _ _ _ _ _ _ _"""
        
        Words().hide_word() # To display the _ _ _ _ _ 
        hider_string = ""
        hider_string = hider_string.join(self.hider)
        return hider_string

    def get_letters(self): #, letter_input):  find letter
        """search for a letter and return a number (number index)
        """
        Words().get_word()
        #Words()._word()
        # in director ask for the users input 
        letter_input = input("Guess a letter: ")

        # index_list = []
        # for i in range (len(self._letter)):
        #     if letter_input == self._letter[i]:
        #         index_list.append(i)
        #print (index_list)


        index_list = []
        for i in range (len(self._word)):
            if letter_input == self._word[i]:
                index_list.append(i)
                #self.hider.append(letter_input) --test
        return index_list
        # return self.hider -- test

        
    def replace_letter(self,letter_input): # replace letter
        """use the number index to place the letter in the correct index
        """
    
        letter_reveal = []
        for i in range (len(self._word)):
            if letter_input == self._word[i]:
                self.hider.append(self._letter) 
        return self.hider


print(Words().get_letters())
