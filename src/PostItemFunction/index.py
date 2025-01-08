import json
import os
import boto3
import uuid

table_name = os.environ['TESTITEMSTABLE_TABLE_NAME']
def handler(event, context):
    # Log the event argument for debugging and for use in local development.
    print(json.dumps(event))

    # Initialize DynamoDB client
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)

    # Generate random UUID for id if not provided
    item_id = event.get('id') or str(uuid.uuid4())

    # Insert item into DynamoDB table
    response = table.put_item(
        Item={
            'id': item_id,
            'data': event
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Item inserted successfully'})
    }
