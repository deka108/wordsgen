import unittest

from models.word_corpus import NLTKCorpus, FileCorpus, RawTextCorpus, \
    CorpusSource


def run_test(corpus):
    if corpus == CorpusSource.NLTK:
        return True
    elif corpus == CorpusSource.FILE:
        return True
    elif corpus == CorpusSource.RAW_TEXT:
        return True


@unittest.skipUnless(run_test(CorpusSource.NLTK), "Skipping nltk corpus test")
class TestNLTKWordGenerator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.corpus = NLTKCorpus()

    def test_random_word_generator(self):
        self.assertEqual(235892, self.corpus.size)

        res = self.corpus.generate_random_words()
        self.assertEqual(235892, len(res))

    def test_filter_letters(self):
        res = self.corpus.generate_random_words(letters="cbade")
        self.assertIsNotNone(res)
        self.assertEqual(1011, len(res))

        res = self.corpus.generate_random_words(letters="cbade",
                                                exact_letters=True)
        self.assertIsNotNone(res)
        self.assertEqual(0, len(res))

    def test_filter_word_length(self):
        res = self.corpus.generate_random_words(letters="cbade",
                                                word_length="5, 7")
        self.assertIsNotNone(res)
        self.assertEqual(25, len(res))

    def test_filter_max_result(self):
        res = self.corpus.generate_random_words(letters="cbade", max_result=10)
        self.assertIsNotNone(res)
        self.assertEqual(10, len(res))

    def test_no_result(self):
        res = self.corpus.generate_random_words(letters="qxyz")
        self.assertEqual(0, len(res))


@unittest.skipUnless(run_test(CorpusSource.FILE), "Skipping file corpus test")
class TestFileWordGenerator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.corpus = FileCorpus("oxford_adj_corpus.tsv")

    def test_file_word_generator_exception(self):
        self.assertRaises(FileNotFoundError, FileCorpus,
                          "cambridge_corpus.tsv")

    def test_random_word_generator(self):
        self.assertEqual(64, self.corpus.size)

        res = self.corpus.generate_random_words()
        self.assertEqual(64, len(res))

    def test_filter_exact_letters(self):
        res = self.corpus.generate_random_words(letters="geekfest",
                                                exact_letters=True)
        self.assertIsNotNone(res)
        self.assertEqual(1, len(res))
        self.assertEqual("geekfest", res[0])

        res = self.corpus.generate_random_words(letters="geekfest")
        self.assertIsNotNone(res)
        self.assertEqual(1, len(res))
        self.assertEqual("geekfest", res[0])

        res = self.corpus.generate_random_words(letters="fest",
                                                exact_letters=True)
        self.assertIsNotNone(res)
        self.assertEqual(0, len(res))

    def test_filter_nonexact_letters(self):
        res = self.corpus.generate_random_words(letters="fest")
        self.assertIsNotNone(res)
        self.assertEqual(25, len(res))

        res = self.corpus.generate_random_words(letters="esft", max_result=10)
        self.assertIsNotNone(res)
        self.assertEqual(10, len(res))


@unittest.skipUnless(run_test(CorpusSource.RAW_TEXT), "Skipping raw text "
                                                      "corpus test")
class TestRawTextWordGenerator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
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
        cls.corpus = RawTextCorpus(raw_text)

    def test_random_word_generator(self):
        self.assertEqual(64, self.corpus.size)
        res = self.corpus.generate_random_words()
        self.assertEqual(64, len(res))

    def test_sort_words(self):
        res = self.corpus.generate_random_words(letters="fest", sort=True)
        self.assertTrue(all([res[i] <= res[i+1] for i in range(len(res) - 1)]))

    def test_filter_letters(self):
        res = self.corpus.generate_random_words(letters="")
        self.assertEqual(64, len(res))

        res = self.corpus.generate_random_words(letters="u")
        self.assertEqual(13, len(res))


if __name__ == "__main__":
    unittest.main()