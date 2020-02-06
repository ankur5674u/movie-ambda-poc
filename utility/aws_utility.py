import decimal

import boto3
import json


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if abs(o) % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)


class AwsCredential(object):
    def __init__(self):
        self.session = boto3.Session(profile_name='ankur', region_name='us-east-1')


class DynamoDB(AwsCredential):
    def __init__(self):
        AwsCredential.__init__(self)
        self.dynamo_resource = self.session.resource('dynamodb', region_name='us-west-1',
                                                     endpoint_url='arn:aws:dynamodb:us-east-1:079828730328:table/movie')

    def put_item_in_table(self, table, data):
        table = self.dynamo_resource.Table('Movies')
        response = table.put_item(
            Item=data

        )
        return json.dumps(response, indent=4, cls=DecimalEncoder)
