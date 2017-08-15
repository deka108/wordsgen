from abc import ABCMeta, abstractmethod
from collections import OrderedDict
from enum import Enum
from wordsgen.models.word_filters import CharacterLengthFilter, \
    ResultsWordFilter, CharacterWordFilter
from wordsgen.utils.string_utils import print_array


class CorpusSource(Enum):
    NLTK = "nltk"
    RAW_TEXT = "raw_text"
    FILE = "file"

corpus_values = [corpus_src.value for corpus_src in CorpusSource]


class WordCorpus(metaclass=ABCMeta):
    def __init__(self):
        self.corpus = self._init_corpus()
        self.size = len(self.corpus)
        self.compact_corpus = self._build_compact_corpus()

    @abstractmethod
    def _get_words(self):
        """
        Initialise word corpus from source.

        :return: list of words. 
        """
        pass

    def _init_corpus(self):
        """
        Initialise word corpus and remove duplicates.

        :return: list of unique words in the corpus. 
        """
        return list(OrderedDict.fromkeys(self._get_words()))

    def _build_compact_corpus(self):
        """
        Transform corpus into a compact data structure for generating random 
        words.

        :return: the compact data structure.
        """
        len_to_sorted_to_words = {}

        for word in self.corpus:
            sorted_to_words = len_to_sorted_to_words.setdefault(len(word), {})
            words = sorted_to_words.setdefault(''.join(sorted(word)), [])
            words.append(word)

        return len_to_sorted_to_words

    def generate_random_words(self,
                              word_length=None, min_length=0, max_length=100,
                              letters=None, exact_letters=False,
                              max_result=None, sort=False,
                              print_console=False):
        """
        Random word generator.

        :param word_length: a string of the desired random words' length.
        :param max_length: the maximum length of the whole corpus.
        :param min_length: the minimum length of the whole corpus.
        The string can be a number or two comma-separated numbers.
        :param letters: a string where all the characters in the string 
        shall appear in the random words. Eg: abba or aero.
        :param exact_letters: a boolean to indicate that the random words
        must contain the same number of characters in the letters argument
        and no others.
        :param max_result: an integer to limit the random words results.
        :param sort: a boolean to indicate whether the random words
         need to be shuffled or sorted alphabetically.
        :param print_console: a boolean to indicate printing the results to
        the console.
        :return: 
        """
        filtered_corpus = self.compact_corpus

        # filtered by word length
        if word_length:
            filtered_corpus = CharacterLengthFilter(word_length,
                                                    min_length=min_length,
                                                    max_length=max_length) \
                .filter_corpus(filtered_corpus)

        # filtered by characters
        if letters:
            filtered_corpus = CharacterWordFilter(characters=letters,
                                                  exact=exact_letters)\
                .filter_corpus(filtered_corpus)

        # filtered by maximum number of result
        results = ResultsWordFilter(length=max_result, sort=sort)\
            .filter_corpus(filtered_corpus)

        if print_console:
            self.print_results(results)

        return results

    @staticmethod
    def print_results(results):
        print("=== No of Random Generator Result: {} ===".format(len(results)))
        if len(results) > 0:
            print_array(results)


class NLTKCorpus(WordCorpus):
    """
    Build word corpus using NLTK data source.
    """
    def __init__(self):
        super(NLTKCorpus, self).__init__()

    def _get_words(self):
        from nltk.corpus import words
        return words.words()


class RawTextCorpus(WordCorpus):
    """
    Build word corpus from a string.
    """
    def __init__(self, raw_text):
        """
        :param raw_text: a line of comma-separated words.
        """
        self.raw_text = raw_text
        super().__init__()

    def _get_words(self):
        try:
            corpus = [word.strip() for word in self.raw_text.split(",")]
            return corpus
        except (ValueError, AttributeError):
            raise ValueError("Raw Text Corpus must be a comma separated "
                             "string. Eg. abacus, amazing, aesthetic")


class FileCorpus(WordCorpus):
    """
    Build word corpus from a text file source.
    """
    def __init__(self, file_path):
        """
        :param file_path: the text file path which consist of line-separated
        words.
        """
        self.file_path = file_path
        super().__init__()

    def _get_words(self):
        try:
            with open(self.file_path, 'r') as fp:
                words = [word.strip() for line in fp for word in line.split()]

            return words
        except FileNotFoundError:
            raise FileNotFoundError("{} does not exist in the corpus folder"
                                    .format(self.file_path))
