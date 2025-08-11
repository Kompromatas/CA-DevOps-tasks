import boto3
import json
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ.get("TABLE_NAME", "Cars-SAM"))

def lambda_handler(event, context):
    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Headres": "*",
    }
    method = event.get('httpMethod', 'POST')
    if method == "GET":
        response = table.scan()
        items = response.get('Items', [])
        return {
            "statusCode": 200,
            "headers": headers,
            "body": json.dumps(items)
        }
    elif method == "POST":
        payload = json.loads(event['body'])
        import uuid
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
    else:
        return {
            "statusCode": 405,
            "headers": headers,
            "body": json.dumps({"error": "Method not allowed"})
        }