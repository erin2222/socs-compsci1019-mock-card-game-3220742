import unittest
from unittest.mock import patch
from card_game.communication.ConsoleInOut import *
from card_game.card.entity.Deck import *
from card_game.Game import *
from card_game.LoadCSV import *

class test_task(unittest.TestCase):

    @patch('card_game.communication.ConsoleInOut.get_string')
    def test_get_input_integer(self,mock):
        mock.return_value = "18"
        self.assertEqual(18,get_input_integer(""))

    def test_get_game_info(self):
        #Sub-task 2 – Mock Console Game Info
        pass

    def test_get_integer_max_attempts(self):
        #Sub-task 3 – Mock Console Input With Built In
        pass

    def test_get_csv_rows(self):
        #Sub-task 4 – Mock File Load
        pass

    def test_play_a_card_from_deck_random(self):
        #Sub-task 5 – Mock Get Player Names
        pass