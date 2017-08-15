import click
from click import UsageError, BadParameter
from wordsgen.models.word_corpus import corpus_values, CorpusSource, \
    NLTKCorpus, RawTextCorpus, FileCorpus
from wordsgen.models.semantics import pos_tags, semantics_sources, \
    SemanticsSource, NLTKWordNetSemantics


@click.group()
def cli():
    pass


@cli.command(short_help="Generates random words based on a corpus and various "
                        "filters.")
@click.option('--corpus-src', type=click.Choice(corpus_values), required=True,
              help="The corpus source.")
@click.option('--raw-text', type=click.STRING, help="The corpus text.")
@click.option('--file', type=click.Path(exists=True, resolve_path=True),
              help="The corpus filename / filepath relative to current path.")
@click.option('--length', type=click.STRING,
              help="The desired random words' length, can be an integer or a "
                   "range. Eg: 4 or 4,7.")
@click.option('--letters', type=click.STRING,
              help="A string that consist of characters that must exist "
                   "in the random words. Eg: abba.")
@click.option('--exact-letters/--not-exact-letters', default=False,
              help="Whether the random words must match the exact number of "
                   "characters in the --letters option.")
@click.option('--max-result', type=click.INT,
              help="The desired maximum number of the random words.")
@click.option('--sort/--shuffle', default=False,
              help="Whether the results should be shuffled.")
@click.option('--interactive/--non-interactive', default=True,
              help="Interactive vs Non-interactive console.")
def random_words(corpus_src, raw_text, file, length,
                 letters, exact_letters,
                 max_result, sort, interactive):
    """Generates random words based on a corpus and various filters."""
    corpus = None
    if interactive:
        if corpus_src == CorpusSource.RAW_TEXT.value:
            raw_text = click.prompt("Enter corpus as a line of "
                                    "comma-separated words "
                                    "(eg: summer, winter, spring, rainy)",
                                    default=raw_text, show_default=True,
                                    type=click.STRING)
        elif corpus_src == CorpusSource.FILE.value:
            file = click.prompt("Enter your corpus file name and extension"
                                "(eg: oxford_adj_corpus.tsv)",
                                default=file, show_default=True,
                                type=click.Path(exists=True, resolve_path=True))
    else:
        if corpus_src == CorpusSource.FILE.value and not file:
            raise BadParameter("If corpus-src=file, file_name must be "
                               "supplied.")

    if corpus_src == CorpusSource.NLTK.value:
        corpus = NLTKCorpus()
    elif corpus_src == CorpusSource.RAW_TEXT.value:
        corpus = RawTextCorpus(raw_text=raw_text)
    elif corpus_src == CorpusSource.FILE.value:
        corpus = FileCorpus(file_path=file)

    if not corpus:
        raise UsageError("Unable to create corpus.")

    if interactive:
        length = click.prompt("Enter the desired length of the random words "
                              "(eg: 7 or 4, 5)",
                              default=length, show_default=True,
                              type=click.STRING)
        letters = click.prompt("Enter the desired characters that must exist "
                               "in the random words (eg. abba)",
                               default=letters, show_default=True,
                               type=click.STRING)
        max_result = click.prompt("Enter the number of maximum results "
                                  "(eg. 10)",
                                  default=max_result, show_default=True,
                                  type=click.INT)
        exact_letters = click.confirm("Should the random words have the same "
                                      "number of characters as in the letters?",
                                      default=exact_letters, show_default=True)
        sort = click.confirm("Should the random words results be sorted?",
                             default=sort, show_default=True)

    corpus.generate_random_words(word_length=length,
                                 letters=letters, exact_letters=exact_letters,
                                 max_result=max_result, sort=sort,
                                 print_console=True)


@cli.command()
@click.option('--semantics-src', type=click.Choice(semantics_sources),
              required=True,
              help="The semantics source. Currently only NLTK's WordNet "
                   "source is supported.")
@click.option('--word', type=click.STRING, required=True,
              help="The input word.")
@click.option('--pos-tag', type=click.Choice(pos_tags),
              help="Optional input word's POS tags.")
@click.option('--sort/--shuffle', default=True,
              help="Whether the results should be sorted.")
@click.option('--synonym/--antonym', default=True,
              help="Whether querying for synonyms or antonyms. Default to "
                   "synonym.")
def semantics(semantics_src, word, pos_tag, sort, synonym):
    """Generates synonyms or antonyms of a word."""
    semantics_corpus = None

    if semantics_src == SemanticsSource.NLTK_WORDNET.value:
        semantics_corpus = NLTKWordNetSemantics()

    if not semantics_corpus:
        raise RuntimeError("Unable to create semantics.")

    if synonym:
        semantics_corpus.find_synonyms(word=word, pos=pos_tag, sort=sort,
                                       print_console=True)
    else:
        semantics_corpus.find_antonyms(word=word, pos=pos_tag, sort=sort,
                                       print_console=True)
