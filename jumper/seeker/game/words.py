from itertools import count
import random

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
        self._words = ["covid", "pineapple", "sponge", "temple", "spatula", "prophet"] # team mates add more
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

        hider_string = ""
        hider_string = hider_string.join(self.hider)
        return hider_string
           


    def get_letters(self): # find letter
        """search for a letter and return a number (number index)
        """
        return (self._distance[-1] == 0)
        
    def replace_letter(self, seeker): # replace letter
        """use the number index to place the letter in the correct index
        """
        distance = abs(self._location - seeker.get_location())
        self._distance.append(distance)


print(Words().hide_word())