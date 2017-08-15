# Words Generator
Do you love anagrams?

Do you need to generate some words for your project? or team name or whatever-your-objective-is name?

Do you ever forgot some words that you may know some of the word details but still could not remember it?

Do you have a writing project? Are you planning to write a poem, or a song for your boy/girlfriend perhaps and in need of inspiration for the words?

This project is what you need.

Some back story: this project is inspired from a word game that I love to play. But I got frustated from spending too much time thinking about the words so I made this little help :p

## How to Install...
= This project supports **python3** and not python2 =

1. (Optional but strongly recommended) Create a virtual environment for python 3.
```
python3 -m venv env
source env/bin/activate
```
2. Install this project and its dependencies
```
pip install git+https://github.com/deka108/wordsgen.git
```

3. Download the required data for NLTK (only when using NLTK corpus).

!! There is no need to download the NLTK corpus if you're using your custom file or raw text corpora.

!! If you want to use methods that are dependent on NLTK, the NLTK corpus data (size=~12MB) must be downloaded first. No need to download everything. Just the `words` and the `WordNet` corpora should be enough. 

```
import nltk
nltk.download()
```

## Current Features
### Random Word Generator
Random word generators + word filters: generate words based on the input characters using your own corpus or nltk corpus dictionary.

#### How to use: 
```
wordsgen random_words --help
```

#### Notes: 
- To use your own corpus, put your words in file separated by line and then use the filepath relative to the current directory where you run the `wordsgen` command. Also, choose file as the `--corpus-src` value.
- For a faster querying performance, add more restrictive conditions to the random word generator.
- NLTK corpus require `words` corpora from nltk.


#### Example:
- Interactive random_words --> With this command only corpus source is required, and the rest will be prompted interactively.
```
wordsgen random_words --corpus-src raw_text --interactive
```
- NLTK Corpus
```
wordsgen random_words --corpus-src nltk --letters love --length '4, 5' --sort
```
- RawText Corpus - requires the raw text corpus
```
wordsgen random_words --corpus-src raw_text --raw-text leave, volley, basket, woven, clove, valley --letters love --length '4, 5' --sort
```
- File Corpus - requires the corpus file path (in this example, `oxford_adj_corpus.tsv` exists in the cwd)
```
wordsgen random_words --corpus-src file --file oxford_adj_corpus.tsv --letters love --length '4, 5' --sort
```

### Semantics
Retrieve synonyms or antonyms of a given word.

#### How to use: 
```wordsgen semantics --help```

#### Notes: 
- Requires `WordNet` corpora from nltk.

#### Example:
- Synonym
```
wordsgen semantics --semantics-src nltk_wordnet --word happy --synonym
```
- Antonym
```
wordsgen semantics --semantics-src nltk_wordnet --word sad --antonym
```

## Future Feature Wishes
1. Random phrase generator
2. Generate phrases given input characters and language grammars
    For example, like docker images, we can generate phrases that consist of adjective and people's names
