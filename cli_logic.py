import click
import dynamo_migrate
import constant
import json

@click.command()
@click.option(constant.VERBOSE_FLAG_SHORT, constant.VERBOSE_FLAG_LONG, 
              is_flag=True, help=constant.VERBOSE_HELP)
@click.option(constant.FEED_AWS_CREDENTIALS_FLAG, is_flag=True, 
              help=constant.FEED_AWS_CREDENTIALS_HELP)
@click.option(constant.USING_TEMP_CREDENTIALS_FLAG, is_flag=True,
              help=constant.USING_TEMP_CREDENTIALS_HELP)
def main(verbose, feed_aws_creds, using_temp_creds):
    """Simple program that greets NAME for a total of COUNT times."""

    aws_access_key_id = None
    aws_secret_access_key = None
    aws_session_token = None

    if feed_aws_creds:
        aws_access_key_id = click.prompt(constant.ACCESS_KEY_PROMPT, type=str)
        aws_secret_access_key = click.prompt(constant.SECRET_ACCESS_KEY_PROMPT, 
                                             type=str)
        if using_temp_creds:
            aws_session_token = click.prompt(constant.SESSION_ID_PROMPT, 
                                             type=str)
    # if verbose:
    #     click.echo("so I hear you're from {}".format("Ireland"))

    old_name = click.prompt(constant.OLD_NAME_PROMPT, type=str)
    new_name = click.prompt(constant.NEW_NAME_PROMPT, type=str)

    dynamo_migrator = dynamo_migrate.DynamoMigrator(old_name, 
                                                    new_name, 
                                                    aws_access_key_id,
                                                    aws_secret_access_key,
                                                    aws_session_token)

    secondary_indexes = dynamo_migrator.get_old_table_configuration()
    print(json.dumps(secondary_indexes, indent=4, sort_keys=True, default=str))

    lsi = click.prompt("Which LSI would you like to modify today?", type=str)
    obj_to_modify = None
    for lsi_obj in secondary_indexes:
        if lsi == lsi_obj["IndexName"]:
            obj_to_modify = lsi_obj
            break
        else:
            for key in lsi_obj["KeySchema"]:
                if key["AttributeName"] == lsi:
                    obj_to_modify = lsi_obj
                    break
    
    action = None
    if obj_to_modify is None:
        if click.confirm("Would you like to create a new index for that?"):
            action = dynamo_migrate.Action.CREATE
    else:
        json.dumps(obj_to_modify, indent=4, sort_keys=True, default=str)
        if click.confirm("Would you like to delete this index?"):
            action = dynamo_migrate.Action.DELETE
    
    if action is dynamo_migrate.Action.CREATE:
        click.echo("CREATING!")
    elif action is dynamo_migrate.Action.DELETE:
        click.echo("DELETING!")



if __name__ == '__main__':
    main()