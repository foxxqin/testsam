import json
import os
import boto3

table_name = os.environ['TESTITEMSTABLE_TABLE_NAME']



def get_all_items():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)
    
    response = table.scan()
    items = response['Items']
    
    # Handle pagination if there are more items
    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        items.extend(response['Items'])
        
    return items

def handler(event, context):
    # Log the event argument for debugging and for use in local development.
    print(json.dumps(event))
    
    items = get_all_items()
    return {
        'statusCode': 200,
        'body': json.dumps(items)
    }    # Log the event argument for debugging and for use in local development.

