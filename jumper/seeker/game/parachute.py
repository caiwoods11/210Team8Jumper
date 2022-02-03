# TODO: Implement the Seeker class as follows...
import random

from matplotlib.pyplot import draw

# 1) Add the class declaration. Use the following class comment.
class Parachute:
    """Create the layout of the parachute guy. 
    """

# 2) Create the class constructor. Use the following method comment.
    def __init__(self):

        """Constructs a new Parachute class.

        Args:
            self (Parachute): An instance of Parachute.
        """

        self.p_parts = ["_____","/","_____","\\","\\","/","\\","/","O"]

# 3) Create the get_location(self) method. Use the following method comment.
    def draw_parachute(self):
        """Gets the current location.
        Returns:
            number: The current location,
        """
        self.p_draw = f"""
      {self.p_parts[0]}
     {self.p_parts[1]}{self.p_parts[2]}{self.p_parts[3]}
     {self.p_parts[4]}     {self.p_parts[5]}
      {self.p_parts[6]}   {self.p_parts[7]}
        {self.p_parts[8]}
       /|\\
       / \\

    ^^^^^^^^^ """
        return self.p_draw


# To test Parachute        
#print(Parachute().draw_parachute())