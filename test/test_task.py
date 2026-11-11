import unittest
from unittest.mock import patch
from unittest.mock import MagicMock
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
        with patch('card_game.communication.ConsoleInOut.get_string') as mock:
            mock.side_effect = ["Derek", "3"]
            self.assertEqual(("Derek",3),get_game_info())

    def test_get_integer_max_attempts(self):
        with patch('card_game.communication.ConsoleInOut.get_string') as mock:
            mock.return_value = "abc"
            result = get_integer()
            self.assertEqual(result,-1)
            self.assertEqual(mock.call_count, 5)
        

    def test_get_csv_rows(self):
        with patch('card_game.LoadCSV.create_csv_reader') as mock:
            mock.return_value = "Derek\nXi"
            result = get_csv_rows("randomfile.csv")
            self.assertEqual(result[1][0],"Xi")

    def test_play_a_card_from_deck_random(self):
        with patch('card_game.card.entity.Deck.random.randint') as mock:
            mock.return_value = 0
            deck = create_deck()
            firstCard= deck[0]
            playedCard = play_a_card_from_deck(deck)
            self.assertEqual(playedCard,firstCard)
