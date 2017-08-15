import unittest

from wordsgen.models.semantics import NLTKWordNetSemantics, PosTag

DEBUG = False


class TestNLTKWordNetSemantics(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.word_net_semantics = NLTKWordNetSemantics()

    def test_wordnet_semantics_synonyms(self):
        synonyms = self.word_net_semantics.find_synonyms("good", print_console=DEBUG)
        self.assertIsNotNone(synonyms)
        self.assertEqual(37, len(synonyms))

        synonyms = self.word_net_semantics.find_synonyms("good",
                                                         pos=PosTag.ADJECTIVE.value,
                                                         print_console=DEBUG)
        self.assertIsNotNone(synonyms)
        self.assertEqual(32, len(synonyms))

        self.word_net_semantics.find_synonyms("good", print_console=DEBUG)

        synonyms = self.word_net_semantics.find_synonyms("beautiful",
                                                         print_console=True)

    def test_wordnet_semantics_antonyms(self):
        antonyms = self.word_net_semantics.find_antonyms("good", print_console=DEBUG)
        self.assertIsNotNone(antonyms)
        self.assertEqual(37, len(antonyms))

        antonyms = self.word_net_semantics.find_antonyms("good",
                                                         pos=PosTag.ADJECTIVE.value,
                                                         print_console=DEBUG)
        self.assertIsNotNone(antonyms)
        self.assertEqual(20, len(antonyms))

        self.word_net_semantics.find_antonyms("good", print_console=DEBUG)

if __name__ == "__main__":
    unittest.main()
