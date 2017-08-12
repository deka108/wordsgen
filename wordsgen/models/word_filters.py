import ast
import random

from abc import ABCMeta, abstractmethod
from collections import Counter
from numbers import Number


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
            sorted_to_words = compact_corpus.get(self.characters_length)

            if sorted_to_words.get(self.sorted_characters):
                results.setdefault(self.characters_length,
                                   {self.sorted_characters:
                                       sorted_to_words.get(
                                           self.sorted_characters)})
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
    def __init__(self, length):
        super().__init__()
        if isinstance(length, Number):
            self.lower_bound = length
            self.upper_bound = length
        else:
            try:
                length_range = ast.literal_eval(length)
                if len(length_range) != 2:
                    raise ValueError("Length must either be a number or in "
                                     "the form of two numbers eg. "
                                     "[1, 6] or 1, 6 that indicate lower and "
                                     "upper length for the words")

                self.lower_bound = length_range[0]
                self.upper_bound = length_range[1]
            except ValueError as ex:
                print(ex)

    @abstractmethod
    def filter_corpus(self, compact_corpus):
        pass


class CharacterLengthFilter(LengthWordFilter):

    def __init__(self, length):
        super().__init__(length)

    def filter_corpus(self, compact_corpus):
        results = {}

        for length in compact_corpus:
            if self.lower_bound <= length <= self.upper_bound:
                results.setdefault(length, compact_corpus[length])

        return results


class ResultsWordFilter(WordFilter):
    def __init__(self, length, shuffle):
        super().__init__()
        self.length = length
        self.shuffle = shuffle

    def filter_corpus(self, compact_corpus):
        results = []

        for length in compact_corpus:
            for sorted_word in compact_corpus[length]:
                results += compact_corpus[length][sorted_word]

        if self.shuffle:
            random.shuffle(results)
        else:
            sorted(results)

        if self.length:
            return results[:self.length]

        return results


