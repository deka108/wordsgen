import unittest

from models.word_corpus import NLTKCorpus, FileCorpus


class TestCorpus(unittest.TestCase):
    # @unittest.skip("Skip nltk generator")
    def test_random_word_generator_nltk(self):
        corpus = NLTKCorpus()

        res = corpus.generate_random_words(letters="cbade")
        self.assertIsNotNone(res)
        self.assertEqual(1011, len(res))

        res = corpus.generate_random_words(letters="cbade", word_length="5, 7")
        self.assertIsNotNone(res)
        self.assertEqual(25, len(res))

        res = corpus.generate_random_words(letters="cbade", max_result=10)
        self.assertIsNotNone(res)
        self.assertEqual(10, len(res))
        print(res)

        res = corpus.generate_random_words(letters="qxyz")
        self.assertEqual(0, len(res))
        print(res)

    def test_random_word_generator_file(self):
        # self.assertRaises(FileNotFoundError, FileCorpus(
        #     "cambridge_corpus.tsv"))

        corpus = FileCorpus("oxford_adj_corpus.tsv")
        self.assertEqual(64, corpus.size)

        res = corpus.generate_random_words()
        self.assertEqual(64, len(res))

        res = corpus.generate_random_words(letters="geekfest",
                                           exact_letters=True)
        self.assertIsNotNone(res)
        self.assertEqual(1, len(res))
        self.assertEqual("geekfest", res[0])

        res = corpus.generate_random_words(letters="geekfest")
        self.assertIsNotNone(res)
        self.assertEqual(1, len(res))
        self.assertEqual("geekfest", res[0])

        res = corpus.generate_random_words(letters="fest")
        self.assertIsNotNone(res)
        self.assertEqual(25, len(res))

        res = corpus.generate_random_words(letters="esft", max_result=10)
        self.assertIsNotNone(res)
        self.assertEqual(10, len(res))


if __name__ == "__main__":
    unittest.main()