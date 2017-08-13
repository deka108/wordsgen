# Words Generator
Do you need to generate some words for your project? or team name or whatever-your-objective-is name?

Do you ever forgot some words that you may know some of the word details but still could not remember it?

Do you currently have a writing project? Are you planning to write a poem, or a song for your boy/girlfriend perhaps and in need to find inspiration for the words?

This project is what you need.

Some back story: this project is inspired from a word game that I love to play. But I got frustated from spending too much time thinking about the words so I made this little help :p.

## How to Install
1. Clone this project: `git clone`
2. (Optional but strongly recommended) Create a virtual environment.
3. Install this project. 
`pip install setup.py`
4. Install the dependencies: nltk, click
!! If you want to use methods that are dependent on NLTK, the NLTK corpus data must be downloaded first (size=~12MB). No need to download everything. Just the words and the WordNet corpora should be enough. There is no need to download the NLTK corpus if you're using your custom file or raw text.

## Current Features
### Random Word Generator
Random word generators + word filters: generate words based on the input characters using your own corpus or nltk corpus dictionary.

How to use: `wordsgen random_words --help`

Notes: 
- NLTK corpus require `words` corpora from nltk.
- To use your own corpus, put your words in file separated by line then copy the corpus file under the wordsgen/corpus directory.
- For a faster querying performance, add more restrictive conditions to the random word generator.

Example:
- NLTK Corpus
`wordsgen random_words --corpus-src nltk --letters love --length '4, 5' --sort`
- RawText Corpus - will ask user's input for the text corpus
`wordsgen random_words --corpus-src raw_text --letters love --length '4, 5' --sort`
- File Corpus - will ask user's input for the corpus file name


### Semantics
Retrieve synonyms or antonyms of a given word.

How to use: `wordsgen semantics --help`

Notes: requires `WordNet` corpora from nltk.

Example:
- Synonym
`wordsgen semantics --semantics-src nltk_wordnet --word happy --synonym`
- Antonym
`wordsgen semantics --semantics-src nltk_wordnet --word sad --antonym`

## Future Feature Wishes
1. Random phrase generator
2. Generate phrases given input characters and language grammars
    For example, like docker images, we can generate phrases that consist of adjective and nouns
