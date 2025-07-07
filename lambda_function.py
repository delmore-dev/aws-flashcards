import json
import boto3
from decimal import Decimal  # DDB returns index numbers as decimals, need to be converted
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key

# Initializing DDB client
dynamodb = boto3.resource('dynamodb', region_name='REGION')
dynamodb_table = dynamodb.Table('TABLENAME')

status_check_path = '/status'
item_path = '/item'
items_path = '/items'

def lambda_handler(event, context):
    print('Request event: ', event)
    response = None
    print('HTTP Method:', event.get('httpMethod'))
    print('Path:', event.get('path'))

    try:
        http_method = event.get('httpMethod')
        path = event.get('path')

        if http_method == 'GET' and path == status_check_path:
            return {
                'statusCode': 200,
                'body': json.dumps('Service is online!')
            }
        elif http_method == 'GET' and path == items_path:
            response = dynamodb_table.scan()
            items = response['Items']
            
            # Converting decimals
            def convert_decimals(obj):
                if isinstance(obj, Decimal):
                    return float(obj) if obj % 1 != 0 else int(obj)
                if isinstance(obj, list):
                    return [convert_decimals(i) for i in obj]
                if isinstance(obj, dict):
                    return {k: convert_decimals(v) for k, v in obj.items()}
                return obj
            
            clean_items = convert_decimals(items)
            print(f'Found {len(items)} items')
            
            return {
                'statusCode': 200,
                'headers': {'Content-Type': 'application/json'},
                'body': json.dumps({
                    'count': len(items),
                    'items': clean_items
                })
            }
        else:
            print(f'Unhandled method {http_method} or path {path}')
            return {
                'statusCode': 400,
                'body': json.dumps('Error processing request')
            }
    except Exception as e:
        print('Error:', e)
        return {
            'statusCode': 400,
            'body': json.dumps('Error processing request')
        }