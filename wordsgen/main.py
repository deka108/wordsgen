import click
from models.word_corpus import corpus_values, CorpusSource, NLTKCorpus, \
    RawTextCorpus, FileCorpus
from models.semantics import pos_tags, semantics_sources, SemanticsSource, \
    NLTKWordNetSemantics


@click.group()
def cli():
    pass


@cli.command(short_help="Generates random words based on a corpus and various "
                        "filters.")
@click.option('--corpus-src', type=click.Choice(corpus_values), required=True,
              help="The corpus source.")
@click.option('--word-length', type=click.STRING,
              help="The desired random words' length, can be an integer or a "
                   "range. Eg: 4 or 4,7")
@click.option('--letters', type=click.STRING,
              help="A string that consist of characters that must exist "
                   "in the random words. Eg: abba")
@click.option('--exact-letters/--not-exact-letters', default=False,
              help="Flag for requiring the exact number of characters in the "
                   "--letters option in the random words.")
@click.option('--max-result', type=click.INT,
              help="The desired maximum number of the random words.")
@click.option('--shuffle/--no-shuffle', default=True,
              help="Flag for shuffling the results.")
def random_words(corpus_src, word_length,
                 letters, exact_letters,
                 max_result, shuffle):
    """Generates random words based on a corpus and various filters."""
    corpus = None

    if corpus_src == CorpusSource.NLTK.value:
        corpus = NLTKCorpus()
    elif corpus_src == CorpusSource.RAW_TEXT.value:
        raw_text = click.prompt("Enter corpus as a line of comma-separated "
                                "words")
        corpus = RawTextCorpus(raw_text=raw_text)
    elif corpus_src == CorpusSource.FILE.value:
        file_name = click.prompt("Enter your corpus file name and extension")
        corpus = FileCorpus(file_name=file_name)

    if not corpus:
        raise RuntimeError("Unable to create corpus.")

    corpus.generate_random_words(word_length=word_length,
                                 letters=letters, exact_letters=exact_letters,
                                 max_result=max_result, shuffle_result=shuffle,
                                 print_console=True)


@cli.command()
@click.option('--semantic-src', type=click.Choice(semantics_sources),
              required=True)
@click.option('--word', type=click.STRING, required=True)
@click.option('--pos-tag', type=click.Choice(pos_tags))
@click.option('--sort/--no-sort', default=False)
@click.option('--synonym/--antonym', default=True)
def semantics(semantic_src, word, pos_tag, sort, synonym):
    """Generates synonyms or antonyms of a word."""
    semantics_corpus = None

    if semantic_src == SemanticsSource.NLTK_WORDNET.value:
        semantics_corpus = NLTKWordNetSemantics()

    if not semantics_corpus:
        raise RuntimeError("Unable to create semantics.")

    if synonym:
        semantics_corpus.find_synonyms(word=word, pos=pos_tag, sort=sort,
                                       print_console=True)
    else:
        semantics_corpus.find_antonyms(word=word, pos=pos_tag, sort=sort,
                                       print_console=True)


