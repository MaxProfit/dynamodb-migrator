import click

@click.command()
@click.option('-v', '--verbose', is_flag=True, 
              help="Will print verbose messages.")
@click.option('--feed-aws-creds', is_flag=True, 
              help="Feed in aws credentials instead of system values.")
@click.option('--using-temp-creds', is_flag=True,
              help='Using temp credentials instead of permanent access keys')
def main(verbose, feed_aws_creds, using_temp_creds):
    """Simple program that greets NAME for a total of COUNT times."""

    if feed_aws_credentials:
        string = click.prompt("Access Key ID", type=str)
        string2 = click.prompt("Secret Access Key", type=str)
        if using_temp_creds:
            string3 = click.prompt("Session ID", type=str)
        click.echo("So you're access key is {} huh".format(string))
        click.echo("So you're access key is {} huh".format(string2))
    if verbose:
        click.echo("so I hear you're from {}".format("Mathewistan"))

if __name__ == '__main__':
    main()