import boto3
import json
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Cars-SAM')

def lambda_handler(event, context):
    method = event.get('httpMethod', 'POST')
    payload = json.loads(event['body'])
    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Headres": "*",
    }
    if method == "POST":

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
    if method == "PUT":
        car_id = payload.get('Cars_id')
        if not car_id:
            return {
                "statusCode": 400,
                "headers": headers,
                "body": json.dumps({"error": "Cars_id is required"})
            }
        update_expression = "SET Car_brand = :brand, Car_model = :model, Car_year = :year, Car_color = :color"
        expression_values = {
            ":brand": payload['Car_brand'],
            ":model": payload['Car_model'],
            ":year": payload['Car_year'],
            ":color": payload['Car_color']
        }
        table.update_item(
            Key={"Cars_id": car_id},
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_values
        )
        return {
            "statusCode": 200,
            "headers": headers,
            "body": "Car updated successfully"
        }
    elif method == "GET":
        import os
        tableget = dynamodb.Table(os.environ.get("TABLE_NAME", "Cars-SAM"))
        response = tableget.scan()
        items = response.get('Items', [])
        return {
            "statusCode": 200,
            "headers": headers,
            "body": json.dumps(items)
        }
    else:
        return {
            "statusCode": 405,
            "headers": headers,
            "body": json.dumps({"error": "Method not allowed"})
        }