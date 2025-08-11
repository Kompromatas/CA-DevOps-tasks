import boto3
import json
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Cars-SAM')

def lambda_handler(event, context):
    payload = json.loads(event['body'])
    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Headres": "*",
    }

    table.put_item(Item={
        "Cars_id": "CAR#{}".format(str(uuid.uuid1())),
        "Car_brand": payload['Car_brand'],
        "Car_model": payload['Car_model'],
        "Car_year": payload['Car_year'],
        "Car_color": payload['Car_color']
    })
    return {
        "statusCode": 200,
        "headers": headers,
        "body": "OK"
    }