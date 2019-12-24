import click
import dynamo_migrate
import constant

@click.command()
@click.option(constant.VERBOSE_FLAG_SHORT, constant.VERBOSE_FLAG_LONG, 
              is_flag=True, help=constant.VERBOSE_HELP)
@click.option(constant.FEED_AWS_CREDENTIALS_FLAG, is_flag=True, 
              help=constant.FEED_AWS_CREDENTIALS_HELP)
@click.option(constant.USING_TEMP_CREDENTIALS_FLAG, is_flag=True,
              help=constant.USING_TEMP_CREDENTIALS_HELP)
def main(verbose, feed_aws_creds, using_temp_creds):
    """Simple program that greets NAME for a total of COUNT times."""

    if feed_aws_creds:
        string = click.prompt(constant.ACCESS_KEY_PROMPT, type=str)
        string2 = click.prompt(constant.SECRET_ACCESS_KEY_PROMPT, type=str)
        if using_temp_creds:
            string3 = click.prompt(constant.SESSION_ID_PROMPT, type=str)
        click.echo("So you're access key is {} huh".format(string))
        click.echo("So you're access key is {} huh".format(string2))
    if verbose:
        click.echo("so I hear you're from {}".format("Mathewistan"))


    ckl = DynamoMigrator(thing, selp)
    ckl.myFunc(list_of_secondary_index_tuples)

if __name__ == '__main__':
    main()