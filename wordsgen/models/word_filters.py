import random
from abc import ABCMeta, abstractmethod
from collections import Counter

from utils.string_utils import parse_range


class WordFilter(metaclass=ABCMeta):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def filter_corpus(self, compact_corpus):
        pass


class CharacterWordFilter(WordFilter):

    def __init__(self, characters, exact):
        super().__init__()

        if not isinstance(characters, str):
            raise ValueError("Characters must be a string Eg. abc")
        self.characters = characters
        self.characters_length = len(characters)
        self.characters_bag = Counter(characters)
        self.sorted_characters = "".join(sorted(characters))
        self.exact = exact

    def filter_corpus(self, compact_corpus):
        results = {}

        if self.exact:
            if self.characters_length in compact_corpus:
                sorted_to_words = compact_corpus[self.characters_length]

                if self.sorted_characters in sorted_to_words:
                    results.setdefault(self.characters_length,
                                       {self.sorted_characters:
                                           sorted_to_words[
                                               self.sorted_characters]})
        else:
            for length in compact_corpus:
                if length >= self.characters_length:
                    for sorted_word in compact_corpus[length]:
                        sorted_word_bag = Counter(sorted_word)
                        sorted_word_bag.subtract(self.characters_bag)
                        if all(sorted_word_bag[ltr] >= 0
                               for ltr in self.characters_bag):
                            # new result
                            new_sorted_to_words = \
                                {sorted_word: compact_corpus[length][sorted_word]}

                            # length did not exist
                            sorted_to_words = results.get(length, {})
                            sorted_to_words.update(new_sorted_to_words)

                            results.setdefault(length, sorted_to_words)

        return results


class LengthWordFilter(WordFilter):
    def __init__(self, length, min_length, max_length):
        super().__init__()
        self.lower_bound, self.upper_bound = parse_range(length,
                                                         min_val=min_length,
                                                         max_val=max_length)

    @abstractmethod
    def filter_corpus(self, compact_corpus):
        pass


class CharacterLengthFilter(LengthWordFilter):

    def __init__(self, length, min_length=0, max_length=100):
        super().__init__(length, min_length, max_length)

    def filter_corpus(self, compact_corpus):
        results = {}

        for length in compact_corpus:
            if self.lower_bound <= length <= self.upper_bound:
                results.setdefault(length, compact_corpus[length])

        return results


class ResultsWordFilter(WordFilter):
    def __init__(self, length, sort):
        super().__init__()
        self.length = length
        self.sort = sort

    def filter_corpus(self, compact_corpus):
        results = []

        for length in compact_corpus:
            for sorted_word in compact_corpus[length]:
                results += compact_corpus[length][sorted_word]

        if self.sort:
            results = sorted(results)
        else:
            random.shuffle(results)

        if self.length:
            return results[:self.length]

        return results
