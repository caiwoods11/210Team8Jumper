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

