# Words Generator
Do you ever forgot some words that you may know some of the letters but still 
could not remember it?

Do you ever need to generate some words for your project? or team name or 
whatever-your-objective-is name?

This project is what you need.

Some backstory: this is inspired from a game that I like to play. I got 
frustated from spending too much time thinking about the words so I made this 
little help.

## Current Features
Random word generators + word filters: Generate words based on the input 
characters using your own corpus or nltk corpus dictionary.

Note that to use your own corpus, put your words in file separated by 
line then copy the corpus file under the wordsgen/corpus directory. Example of 
the custom corpus can be seen in wordsgen/corpus/oxford_adj_corpus.tsv

### Words Filters
1. Length of the Letters
2. Ad-hoc Characters
    1. Exact-match: the generated words exactly every input characters 
    (order does not matter)
    2. In-exact: the generated words contains the input characters
    (order does not matter)

## Future Feature Wishes
1. Random phrase generator
2. Generate phrases given input characters and language grammars
    For example, like docker images, we can generate phrases that consist of 
    adjective and nouns
3. Meaningful random words and phrase generators using synonyms
