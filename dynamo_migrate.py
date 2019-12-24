import boto3
import constant

class DynamoMigrator:

    def __init__(self, old_table_name, new_table_name, access_key=None, access_key_secret=None):
        self.old_table_name = old_table_name
        self.new_table_name = new_table_name
        self.client = __create_dynamo_client(access_key, access_key_secret)

    def __create_dynamo_client(self, access_key, access_key_secret):
        if not access_key is None and not access_key_secret is None:
            return boto3.client(constant.DYNAMODB)
        else:
            return boto3.client(constant.DYNAMODB,
                                aws_access_key_id=access_key,
                                aws_secret_access_key=access_key_secret)
    def myFunc(self):
        print("Hello my name is {}".format(self.name))

    def create_new_table(self):
        pass


# Old table name

# New table name
# Get the local indexes
# Get the global indexes