import unittest

from models.filters import CharacterFilter, CharacterLengthFilter, \
    ResultsFilter


class TestFilters(unittest.TestCase):

    def test_character_filter(self):
        filter = CharacterFilter("abc", exact=False)
        self.assertFalse(filter.exact)
        self.assertEqual("abc", filter.characters)
        self.assertEqual(3, filter.characters_length)

        filter = CharacterFilter("cab", exact=True)
        self.assertTrue(filter.exact)
        self.assertEqual("abc", filter.sorted_characters)

    def test_character_legnth_filter(self):
        filter = CharacterLengthFilter(4)
        self.assertEqual(4, filter.upper_bound)
        self.assertEqual(4, filter.lower_bound)

        filter = CharacterLengthFilter("5, 7")
        self.assertEqual(5, filter.lower_bound)
        self.assertEqual(7, filter.upper_bound)

        filter = CharacterLengthFilter("[3, 6]")
        self.assertEqual(3, filter.lower_bound)
        self.assertEqual(6, filter.upper_bound)

    def test_results_filter(self):
        filter = ResultsFilter(5, shuffle=False)
        self.assertEqual(5, filter.length)
        self.assertFalse(filter.shuffle)

        filter = ResultsFilter(4, shuffle=True)
        self.assertEqual(4, filter.length)
        self.assertTrue(filter.shuffle)

if __name__ == "__main__":
    unittest.main()