from game.words import Words
from game.parachute import Parachute


class Director:

    def __init__(self):
        self._is_playing = True
        self._words = Words()
        self._parachute = Parachute()
        
    def start_game(self):
        while self._is_playing:
            self._get_word()
            self._display_hidden_word()
            self._display_parachute()
            self._letter_input()

            self._end_game()

    def _get_word(self):
        new_word = self._words.get_word()
        print(f"The new word is {new_word}")  # DELETE THIS WHE COMPLETE

    def _display_hidden_word(self):
        Words().hide_word()

    def _display_parachute(self):
        print(Parachute().draw_parachute())
        
    def _letter_input(self):
        Words().get_letters()

    def _end_game(self):
        self._is_playing = False
