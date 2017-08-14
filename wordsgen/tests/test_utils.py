import unittest

from wordsgen.utils.string_utils import parse_range


class TestStringUtils(unittest.TestCase):

    def test_parse_range(self):
        range_str = "5"
        lower, upper = parse_range(range_str)
        self.assertEqual(lower, 5)
        self.assertEqual(upper, 5)

        range_str = "1,10"
        lower, upper = parse_range(range_str)
        self.assertEqual(lower, 1)
        self.assertEqual(upper, 10)

        range_str = ",10"
        lower, upper = parse_range(range_str)
        self.assertEqual(lower, 0)
        self.assertEqual(upper, 10)

        range_str = "10,"
        lower, upper = parse_range(range_str)
        self.assertEqual(lower, 10)
        self.assertEqual(upper, 100)

        range_str = ","
        lower, upper = parse_range(range_str)
        self.assertEqual(lower, 0)
        self.assertEqual(upper, 100)

        range_str = ""
        lower, upper = parse_range(range_str)
        self.assertEqual(lower, 0)
        self.assertEqual(upper, 100)

        range_str = ""
        lower, upper = parse_range(range_str, min_val=-1, max_val=1)
        self.assertEqual(lower, -1)
        self.assertEqual(upper, 1)

        range_str = "1, 2, 3"
        self.assertRaises(ValueError, parse_range, range_str)

        range_str = "a,b"
        self.assertRaises(ValueError, parse_range, range_str)


if __name__ == "__main__":
    unittest.main()
