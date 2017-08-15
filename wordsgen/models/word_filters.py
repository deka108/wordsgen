import random
from abc import ABCMeta, abstractmethod
from collections import Counter

from wordsgen.utils.string_utils import parse_range


class WordFilter(metaclass=ABCMeta):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def filter_corpus(self, compact_corpus):
        pass


class CharacterWordFilter(WordFilter):

    def __init__(self, include_chars, exclude_chars, exact):
        super().__init__()

        self.include_chars = include_chars
        self.include_chars_len = len(include_chars)
        self.include_chars_bag = Counter(include_chars)
        self.exclude_chars = exclude_chars
        self.exclude_chars_len = len(exclude_chars)
        self.exclude_chars_set = set(exclude_chars)
        self.sorted_include_chars = "".join(sorted(include_chars))
        self.exact = exact

    def filter_corpus(self, compact_corpus):
        results = {}

        if self.exact:
            if self.include_chars_len in compact_corpus:
                sorted_to_words = compact_corpus[self.include_chars_len]

                if self.sorted_include_chars in sorted_to_words:
                    results.setdefault(self.include_chars_len,
                                       {self.sorted_include_chars:
                                           sorted_to_words[
                                               self.sorted_include_chars]})
        else:
            for length in compact_corpus:
                if length >= self.include_chars_len:
                    for sorted_word in compact_corpus[length]:
                        sorted_word_bag = Counter(sorted_word)
                        sorted_word_bag.subtract(self.include_chars_bag)
                        if self._check_exclude(sorted_word_bag) and \
                                self._check_include(sorted_word_bag):
                            # new result
                            new_sorted_to_words = \
                                {sorted_word: compact_corpus[length][sorted_word]}

                            # create new dictionary if length does not exist
                            sorted_to_words = results.get(length, {})
                            sorted_to_words.update(new_sorted_to_words)

                            results.setdefault(length, sorted_to_words)

        return results

    def _check_exclude(self, sorted_word_bag):
        return all(ltr not in sorted_word_bag for ltr in self.exclude_chars_set)

    def _check_include(self, sorted_word_bag):
        return all(sorted_word_bag[ltr] >= 0 for ltr in self.include_chars_bag)


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
