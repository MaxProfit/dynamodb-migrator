import boto3
import constant
from enum import Enum

class Action(Enum):
    CREATE = 1
    DELETE = 2

class DynamoMigrator:
    def __create_dynamo_client(self, access_key, 
                               access_key_secret, session_token):
        if access_key is None or access_key_secret is None:
            return boto3.client(constant.DYNAMODB)
        elif session_token is None:
            return boto3.client(constant.DYNAMODB,
                                aws_access_key_id=access_key,
                                aws_secret_access_key=access_key_secret)
        else:
            return boto3.client(constant.DYNAMODB,
                                aws_access_key_id=access_key,
                                aws_secret_access_key=access_key_secret,
                                aws_session_token=session_token)

    def __init__(self, old_table_name: str, new_table_name: str, 
                 aws_access_key_id, aws_secret_access_key, aws_session_token):
        self.old_table_name = old_table_name
        self.new_table_name = new_table_name
        self.client = self.__create_dynamo_client(aws_access_key_id, 
                                                  aws_secret_access_key,
                                                  aws_session_token)

    def get_old_table_configuration(self):
        old_table_desc = self.client.describe_table(
            TableName=self.old_table_name
        )
        
        local_secondary_indexes = old_table_desc["Table"]["LocalSecondaryIndexes"]
        # key_schema = old_table_desc["Table"]["KeySchema"]
        # return local_secondary_indexes, key_schema
        return local_secondary_indexes

    def create_new_table(self):
        return self.client.create_table(
            AttributeDefinitions=[
                {
                    'AttributeName': 'string',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'string2',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'string3',
                    'AttributeType': 'S'
                }
            ],
            TableName='string',
            KeySchema=[
                {
                    'AttributeName': 'string',
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': 'string2',
                    'KeyType': 'RANGE'
                },
            ],
            LocalSecondaryIndexes=[
                {
                    'IndexName': 'string',
                    'KeySchema': [
                        {
                            'AttributeName': 'string',
                            'KeyType': 'HASH'
                        },
                        {
                            'AttributeName': 'string3',
                            'KeyType': 'RANGE'
                        }
                    ],
                    'Projection': {
                        'ProjectionType': 'ALL'
                    }
                },
            ],
            BillingMode='PROVISIONED',
            ProvisionedThroughput={
                'ReadCapacityUnits': 1,
                'WriteCapacityUnits': 1
            },
        )