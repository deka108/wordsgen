import click


@click.group()
def cli():
    click.echo("hello world, cli")


@cli.command()
def generate_random_words():
    click.echo("hello world, grw")
