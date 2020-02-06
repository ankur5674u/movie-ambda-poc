import requests
import json
from utility import aws_utility


def FETCHING_DATA_FROM_INTERNET(event, lambda_context):
    data_url = "https://raw.githubusercontent.com/prust/wikipedia-movie-data/master/movies.json"
    data = requests.get(data_url)
    # Creating Aws resources
    dynamo_db = aws_utility.DynamoDB()
    for item in data.json():
        movie_data = dict(item)
        data = dict(
            title=movie_data.get('title'),
            year=movie_data.get('year'),
            cast=json.dumps(movie_data.get('cast')),
            genres=json.dumps(movie_data.get('genres')),

        )
        dynamo_db.put_item_in_table(table='movie', data=data)


def unhandled_exceptions(e, event, context):
    return True
