import json
import boto3

def lambda_handler(event, context):
    # Inicializar o cliente do DynamoDB
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('AirQualityData')
    
    for record in event['Records']:
        payload = json.loads(record['body'])
        table.put_item(Item=payload)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Data processed successfully!')
    }
