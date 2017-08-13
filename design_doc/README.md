# Design Documentation

## Use Cases
- Random words generator
- Selective random words generator
- Random phrases generator
- Selective random words generator

## Possible Inputs
### Corpus and POS tagging
- nltk corpus
- File corpus
    - own dictionary (downloaded/open source)
    - user dictionary
- Raw Text:
    - Comma separated text

## Word Filters
- Length of Words:
    - exact
    - ranges ==> list, tuple (lower + upper)
- Letters:
    - exact
    - can be repeated
- Number of results:
    - upper bound
        - random (shuffled)
        - ordered (alphabetical)
    - all
        - ordered (alphabetical)

## Project Planning
- Develop words and selective random english & custom corpus words generator
- Develop synonyms and antonyms generator

## Future Plans
- Develop random and selective random english phrase generator + Unit Tests
