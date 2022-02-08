class Parachute:

    def __init__(self):

        """Constructs a new Parachute class.
        Args:
            self (Parachute): An instance of Parachute.
        """

        self.p_parts = ["_____","/","_____","\\","\\","/","\\","/","O"]

    def draw_parachute(self):
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
