import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('NotesTable')

def lambda_handler(event, context):
    note_id = event['pathParameters']['id']
    response = table.get_item(Key={'noteId': note_id})
    
    item = response.get('Item')
    if not item:
        return {'statusCode': 404, 'body': json.dumps({'message': 'Note not found'})}
    
    return {
        'statusCode': 200,
        'body': json.dumps(item)
    }