import yaml

from consts import URLS
import requests
from datetime import datetime


def call_external_api(param):
    try:
        url = URLS.get(param)
        if url is not None:
            data = requests.get(url)
            if data.status_code == 200:
                object_data = data.json()
                joke = object_data['value']
                response = 'success'
            else:
                raise requests.exceptions.ConnectionError("Error in conection with the server")
        else:
            raise ValueError("Invalid request parameters, the url it does not exxist")

    except requests.exceptions.ConnectionError as ex:
        response = f"Error in call_external_api {ex}, the connection with server it failed"
        joke = None

    except ValueError as ex:
        response = f"Error in call_external_api {ex}"
        joke = None

    except Exception as ex:
        response = f"Unexpected error in call_external_api {ex}"
        joke = None

    return response, joke


def get_joke_function(param):
    response, joke = call_external_api(param)
    data = {'value': joke, 'response': response}
    return yaml.dump(data)


def create_joke_function(param, mongo_instance):
    try:
        response, joke = call_external_api(param)
        data = {'value': joke, 'response': response}
        if response == 'success':
            last_joke = list(mongo_instance.db.jokes.find({}))[-1]
            mongo_instance.db.jokes.insert_one(
                {'number': last_joke['number'] + 1, 'value': joke, 'created_on': datetime.now()})
            data['response'] = "Sucessfully created joke"
            return yaml.dump(data)
        else:
            return yaml.dump(data)
    except Exception as ex:
        response = f"Unexpected error in create_joke {ex}"
        data = {'value': None, 'response': response}
        return yaml.dump(data)


def update_joke_function(param, mongo_instance, number):
    try:
        response, joke = call_external_api(param)
        data = {'value': joke, 'response': response}
        if response == 'success':
            mongo_instance.db.jokes.update_one({'number': number}, {'$set': {"value": joke}})
            data['response'] = "Sucessfully update joke"
            return yaml.dump(data)
    except Exception as ex:
        response = f"Unexpected error in update_joke {ex}"
        data = {'value': None, 'response': response}
        return yaml.dump(data)


def delete_joke_function(mongo_instance, number):
    try:
        mongo_instance.db.jokes.delete_one({'number': number})
        data = {'response': f"Sucessfully update joke number {number}"}
        return yaml.dump(data)
    except Exception as ex:
        response = f"Unexpected error in update_joke {ex}"
        data = {'response': response}
        return yaml.dump(data)
