import unittest

from wordsgen.models.word_filters import CharacterWordFilter, \
    CharacterLengthFilter, ResultsWordFilter


class TestFilters(unittest.TestCase):

    def test_character_filter(self):
        filter = CharacterWordFilter(include_chars="abc", exact=False)
        self.assertFalse(filter.exact)
        self.assertEqual("abc", filter.include_chars)
        self.assertEqual(3, filter.include_chars_len)

        filter = CharacterWordFilter(include_chars="abc",
                                     exclude_chars="defg",
                                     exact=False)
        self.assertFalse(filter.exact)
        self.assertEqual("def", filter.exclude_chars)
        self.assertEqual(4, filter.exclude_chars)

        filter = CharacterWordFilter(include_chars="cab", exact=True)
        self.assertTrue(filter.exact)
        self.assertEqual("abc", filter.sorted_include_chars)

    def test_character_length_filter(self):
        filter = CharacterLengthFilter("4")
        self.assertEqual(4, filter.lower_bound)
        self.assertEqual(4, filter.upper_bound)

        filter = CharacterLengthFilter("4,")
        self.assertEqual(4, filter.lower_bound)
        self.assertEqual(100, filter.upper_bound)

        filter = CharacterLengthFilter(",4")
        self.assertEqual(0, filter.lower_bound)
        self.assertEqual(4, filter.upper_bound)

        filter = CharacterLengthFilter("4,", max_length=20)
        self.assertEqual(4, filter.lower_bound)
        self.assertEqual(20, filter.upper_bound)

        filter = CharacterLengthFilter(",4", min_length=-1)
        self.assertEqual(-1, filter.lower_bound)
        self.assertEqual(4, filter.upper_bound)

        filter = CharacterLengthFilter(",", min_length=-1, max_length=1)
        self.assertEqual(-1, filter.lower_bound)
        self.assertEqual(1, filter.upper_bound)

        filter = CharacterLengthFilter("", min_length=-1, max_length=1)
        self.assertEqual(-1, filter.lower_bound)
        self.assertEqual(1, filter.upper_bound)

        filter = CharacterLengthFilter("5, 7")
        self.assertEqual(5, filter.lower_bound)
        self.assertEqual(7, filter.upper_bound)

    def test_results_filter(self):
        filter = ResultsWordFilter(5, sort=False)
        self.assertEqual(5, filter.length)
        self.assertFalse(filter.sort)

        filter = ResultsWordFilter(4, sort=True)
        self.assertEqual(4, filter.length)
        self.assertTrue(filter.sort)

if __name__ == "__main__":
    unittest.main()