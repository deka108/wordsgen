# Design Documentation

## Use Cases
- Random words generator
- Selective random words generator
- Random phrases generator
- Selective random words generator

## Input-Output Agreement
### Possible Inputs
#### Corpus and POS tagging
- nltk corpus
- File corpus
    - own dictionary (downloaded, open source)
    - user dictionary
        - JSON
        - TSV
- Raw Text:
    - Comma separated text
    - Python list

#### Filters
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

### Possible Outputs
- python str
- write into file
    - tsv
- file stream

## Project Planning
- Phase 1 + 2: Develop words and selective random english & custom corpus words generator + unit tests
- Phase 3: Develop random and selective random english phrase generator + Unit Tests
