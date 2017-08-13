import unittest

from models.word_corpus import NLTKCorpus, RawTextCorpus, FileCorpus


class TestWordCorpus(unittest.TestCase):

    def test_nltk_corpus(self):
        corpus = NLTKCorpus()

        self.assertIsNotNone(corpus)
        self.assertEqual(24, len(corpus.compact_corpus), "Wrong total length "
                                                         "of words in the "
                                                         "compact corpus")
        self.assertEqual(3868, len(corpus.compact_corpus[4]), "Wrong number of"
                                                              " words of "
                                                              " some length "
                                                              "in the corpus")

    def test_raw_text_corpus(self):
        raw_text = 'craptastic, poptastic, funktastic, fabtastic, ' \
                   'pimptastic, creeptastic, blingtastic, ego-tastic, ' \
                   'retrotastic, geektastic, blogtastic, slugfest, lovefest, '\
                   'gabfest, crapfest, talkfest, gorefest, snoozefest, ' \
                   'hatefest, bitchfest, snorefest, geekfest, gabfest, ' \
                   'bloodfest, blogfest, songfest, shitfest, screamfest, ' \
                   'filmfest, yawnfest, funfest, sobfest, plugfest, mudfest, '\
                   'fragfest, suckfest, management-speak, corporate-speak, ' \
                   'marketing-speak, geek-speak, business-speak, ' \
                   'therapy-speak, art-speak, lawyer-speak, media-speak, ' \
                   'government-speak, consultant-speak, technospeak, ' \
                   'adspeak, PR-speak, science-speak, politispeak, ' \
                   'military-speak, computer-speak, BBC-speak, tech-speak, ' \
                   'legal-speak, left-speak, dumpsville, dullsville, ' \
                   'squaresville,hicksville, smallville, stupidville, ' \
                   'shitsville'

        corpus = RawTextCorpus("")
        self.assertIsNotNone(corpus)

        corpus = RawTextCorpus("10")
        self.assertIsNotNone(corpus)

        self.assertRaises(ValueError, RawTextCorpus, 10)

        corpus = RawTextCorpus(raw_text=raw_text)
        self.assertIsNotNone(corpus)
        self.assertEqual(10, len(corpus.compact_corpus))
        self.assertEqual(16, len(corpus.compact_corpus[8]))

    def test_file_corpus(self):
        corpus = FileCorpus("oxford_adj_corpus.tsv")
        self.assertIsNotNone(corpus)
        self.assertEqual(10, len(corpus.compact_corpus))
        self.assertEqual(7, len(corpus.compact_corpus[9]))


if __name__ == "__main__":
    unittest.main()
