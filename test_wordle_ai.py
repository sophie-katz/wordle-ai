import unittest
import json
from wordle_ai import *

class TestWordMask(unittest.TestCase):
    def setUp(self) -> None:
        with open("words.json", "r") as file:
            self.word_set = WordSet(json.load(file))
    
    # def test_matches(self) -> None:
    #     self.assertTrue(
    #         WordMask(
    #             global_included_letters={'e', 's', 'r', 'u'},
    #             global_excluded_letters={'a', 'd', 'e', 'c', 'r', 'u', 'i', 'l', 'o', 'p', 't', 'm'},
    #             positional_known_letters={2: 'r', 4: 's', 3: 'e', 1: 'u'},
    #             positional_excluded_letters={
    #                 0: {'a', 'd', 'c', 'l', 'p', 't', 'm'},
    #                 1: {'e', 'i', 'u'},
    #                 3: {'e', 'o'},
    #                 2: {'r'}
    #             }
    #         ).matches("naiks")
    #     )

if __name__ == "__main__":
    unittest.main()
