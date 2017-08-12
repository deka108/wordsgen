import unittest

from models.word_corpus import NLTKCorpus, FileCorpus, RawTextCorpus


class TestWordGenerator(unittest.TestCase):
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
        self.assertRaises(FileNotFoundError, FileCorpus,
                          "cambridge_corpus.tsv")

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

    def test_random_word_generator_rawtext(self):
        raw_text = 'craptastic, poptastic, funktastic, fabtastic, ' \
                   'pimptastic, creeptastic, blingtastic, ego-tastic, ' \
                   'retrotastic, geektastic, blogtastic, slugfest, lovefest, ' \
                   'gabfest, crapfest, talkfest, gorefest, snoozefest, ' \
                   'hatefest, bitchfest, snorefest, geekfest, gabfest, ' \
                   'bloodfest, blogfest, songfest, shitfest, screamfest, ' \
                   'filmfest, yawnfest, funfest, sobfest, plugfest, mudfest, ' \
                   'fragfest, suckfest, management-speak, corporate-speak, ' \
                   'marketing-speak, geek-speak, business-speak, ' \
                   'therapy-speak, art-speak, lawyer-speak, media-speak, ' \
                   'government-speak, consultant-speak, technospeak, ' \
                   'adspeak, PR-speak, science-speak, politispeak, ' \
                   'military-speak, computer-speak, BBC-speak, tech-speak, ' \
                   'legal-speak, left-speak, dumpsville, dullsville, ' \
                   'squaresville,hicksville, smallville, stupidville, ' \
                   'shitsville'
        corpus = RawTextCorpus(raw_text)


if __name__ == "__main__":
    unittest.main()