import config

from abc import ABCMeta, abstractmethod
from collections import OrderedDict
from enum import Enum
from models.word_filters import CharacterLengthFilter, ResultsWordFilter, \
    CharacterWordFilter


class CorpusSource(Enum):
    NLTK = "nltk"
    RAW_TEXT = "raw_text"
    FILE = "file"


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
        Initialise word corpus and removing corpus duplicate.

        :return: list of unique words in the corpus. 
        """
        return list(OrderedDict.fromkeys(self._get_words()))

    def _build_compact_corpus(self):
        """
        Transform corpus into a compact data structure for generating random 
        words.
         
        :param corpus: list of words in the corpus.
        :return: the compact data structure.
        """
        len_to_sorted_to_words = {}

        for word in self.corpus:
            sorted_to_words = len_to_sorted_to_words.setdefault(len(word), {})
            words = sorted_to_words.setdefault(''.join(sorted(word)), [])
            words.append(word)

        return len_to_sorted_to_words

    def generate_random_words(self, word_length=None,
                              letters=None, exact_letters=False,
                              max_result=None, shuffle_result=False,
                              print=False):
        """
        Random word generator.
        
        :param word_length: a range of the desired random words. Can be a 
        number or tuple of two numbers. Eg: [lower_bound, upper_bound].
        :param letters: a string where all the characters in the string 
        shall appear in the random words. Eg: abba or aero.
        :param exact_letters: a boolean to indicate whether the random words 
        must contain exactly all the characters in the letters and no others.  
        :param max_result: an integer to limit the random words results.
        :param shuffle_result: a boolean to indicate whether the random words
         need to be shuffled or sorted alphabetically.
        :return: 
        """
        filtered_corpus = self.compact_corpus

        # filtered by word length
        if word_length:
            filtered_corpus = CharacterLengthFilter(word_length) \
                .filter_corpus(filtered_corpus)

        # filtered by characters
        if letters:
            filtered_corpus = CharacterWordFilter(characters=letters,
                                                  exact=exact_letters)\
                .filter_corpus(filtered_corpus)

        # filtered by maximum characters
        results = ResultsWordFilter(length=max_result, shuffle=shuffle_result)\
            .filter_corpus(filtered_corpus)

        if print:
            self.print_results(results)

        return results

    @staticmethod
    def print_results(results):
        for result in results:
            print(result)


class NLTKCorpus(WordCorpus):
    """
    Word corpus with NLTK data source.
    """
    def __init__(self):
        super(NLTKCorpus, self).__init__()

    def _get_words(self):
        from nltk.corpus import words
        return words.words()


class RawTextCorpus(WordCorpus):
    """
    Word corpus with comma separated word text source.
    """
    def __init__(self, raw_text):
        """
        
        :param raw_text: 
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
    Word corpus with newline separated word text file source.
    """
    def __init__(self, file_name):
        """
        
        :param file_name: 
        """
        self.file_name = file_name
        super().__init__()

    def _get_words(self):
        try:
            path = "{root_dir}/corpus/{file_name}"\
                .format(root_dir=config.ROOT_DIR, file_name=self.file_name)

            with open(path, 'r') as fp:
                words = [word for line in fp for word in line.split()]

            return words
        except FileNotFoundError:
            raise FileNotFoundError("{} does not exist in the corpus folder"
                                    .format(self.file_name))
