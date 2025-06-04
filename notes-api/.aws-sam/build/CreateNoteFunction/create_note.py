import json
import uuid
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('NotesTable')

def lambda_handler(event, context):
    body = json.loads(event['body'])
    note_id = str(uuid.uuid4())
    content = body.get('content', '')
    
    table.put_item(Item={
        'noteId': note_id,
        'content': content
    })
    
    return {
        'statusCode' : 200,
        'body' : json.dumps({'noteId' : note_id, 'message': 'Note created'})
    }