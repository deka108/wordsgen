from abc import ABCMeta, abstractmethod
from enum import Enum
from nltk.corpus import wordnet as wn
from utils.string_utils import print_array


class SemanticsSource(Enum):
    NLTK_WORDNET = "nltk_wordnet"


class PosTag(Enum):
    VERB = "verb"
    NOUN = "noun"
    ADJECTIVE = "adjective"
    ADVERB = "adverb"

pos_tags = [pos_tag.value for pos_tag in PosTag]
semantics_sources = [semantics_src.value for semantics_src in SemanticsSource]


class Semantics(metaclass=ABCMeta):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def find_synonyms(self, word):
        pass

    @abstractmethod
    def find_antonyms(self, word):
        pass

    @abstractmethod
    def _get_pos_tagging(self, pos):
        pass

    @staticmethod
    def print_results(results):
        print("=== No of Semantics Result: {} ===".format(len(results)))

        if len(results) > 0:
            print_array(results)


class NLTKWordNetSemantics(Semantics):
    def __init__(self):
        super().__init__()

    def find_antonyms(self, word, pos=None, sort=False, print_console=False):
        results = set()
        antonyms = set()

        if pos:
            pos = self._get_pos_tagging(pos)

        for synset in wn.synsets(word, pos=pos):
            for lemma in synset.lemmas():
                antonyms.update([antonym.name() for antonym in lemma.antonyms()])

        for antonym in antonyms:
            results.update(self._get_word_synsets(antonym, pos))

        results = self._sort_results(results, sort)

        if print_console:
            self.print_results(results)

        return results

    def find_synonyms(self, word, pos=None, sort=False, print_console=False):
        if pos:
            pos = self._get_pos_tagging(pos)

        results = self._sort_results(self._get_word_synsets(word, pos), sort)

        if print_console:
            self.print_results(results)

        return results

    def _get_pos_tagging(self, pos):
        if pos == PosTag.VERB:
            return wn.VERB
        elif pos == PosTag.NOUN:
            return wn.NOUN
        elif pos == PosTag.ADJECTIVE:
            return wn.ADJ
        elif pos == PosTag.ADVERB:
            return wn.ADV

    @staticmethod
    def _sort_results(results, sort):
        if sort:
            return sorted(list(results))
        return list(results)

    @staticmethod
    def _get_word_synsets(word, pos):
        results = set()

        for synset in wn.synsets(word, pos=pos):
            results.update(synset.lemma_names())

        return results
