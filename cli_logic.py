import click

@click.command()
@click.argument('country')
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
@click.option('--verbose', is_flag=True, help="Will print verbose messages.")
def main(country, verbose, count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    if verbose:
        click.echo("so I hear you're from {}".format(country))
    for x in range(count):
        click.echo('Hello %s!' % name)

if __name__ == '__main__':
    main()