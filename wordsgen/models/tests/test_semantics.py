import unittest

from models.semantics import WordNetSemantics, PosTag


class TestSemantics(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.word_net_semantics = WordNetSemantics()

    def test_wordnet_semantics_synonyms(self):
        synonyms = self.word_net_semantics.find_synonyms("good")
        print(synonyms)
        self.assertIsNotNone(synonyms)
        self.assertEqual(37, len(synonyms))

        synonyms = self.word_net_semantics \
            .find_synonyms("good")
        print(synonyms)
        self.assertIsNotNone(synonyms)
        self.assertEqual(32, len(synonyms))

        synonyms = self.word_net_semantics \
            .find_synonyms("good")
        print(synonyms)

    def test_wordnet_semantics_antonyms(self):
        antonyms = self.word_net_semantics.find_antonyms("good", false)
        print(antonyms)
        self.assertIsNotNone(antonyms)
        self.assertEqual(37, len(antonyms))

        antonyms = self.word_net_semantics \
            .find_antonyms("good", false)
        print(antonyms)
        self.assertIsNotNone(antonyms)
        self.assertEqual(20, len(antonyms))

        antonyms = self.word_net_semantics \
            .find_antonyms("good", false)
        print(antonyms)

if __name__ == "__main__":
    unittest.main()