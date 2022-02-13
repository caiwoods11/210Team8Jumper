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
        
        
    def start_game(self):
        self._display_word()
        
        while self._is_playing:         
            self._display_parachute()
            self._get_input()
            self._check_end_game()

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


    def _get_input(self):
        Words().get_letter(self._word, self._hidden_word, self._wrong_guesses)
                
    def _check_end_game(self):
        Words().game_over(self._is_playing, self._hidden_word)

