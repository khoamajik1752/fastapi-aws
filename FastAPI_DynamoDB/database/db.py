from boto3 import resource
from os import getenv
from dotenv import load_dotenv
load_dotenv()
# print(getenv("AWS_ACCES_KEY_ID"),getenv("AWS_SECRET_ACCES_KEY"),getenv("REGION_NAME"))
dynamodb = resource("dynamodb",
        aws_access_key_id=getenv("AWS_ACCESS_KEY"),
        aws_secret_access_key=getenv("AWS_SECRET"),
        region_name=getenv("REGION_NAME"))


tables = [
    {
        "TableName": "Song",
        
        "AttributeDefinitions": [
            {
                'AttributeName': 'LoaderId',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'SongId',
                'AttributeType': 'S'
            }
        ],

        "KeySchema": [
            {
                'AttributeName': 'LoaderId',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'SongId',
                'KeyType': 'RANGE'
            },

        ],
    },
]


def create_tables():

    try:
        for table in tables:
            dynamodb.create_table(
                TableName=table["TableName"],
                KeySchema=table["KeySchema"],
                AttributeDefinitions=table["AttributeDefinitions"],
                BillingMode="PAY_PER_REQUEST"
            )
    except Exception as e:

        print(e)
