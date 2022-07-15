import random

import yaml
from flask import Flask, request
from flask_pymongo import PyMongo
from consts import MONGO_URL, URLS
from utils import create_joke_function, update_joke_function, delete_joke_function, get_joke_function, \
    process_lmc_function

app = Flask(__name__)
app.config['MONGO_URI'] = MONGO_URL
mongo_instance = PyMongo(app)


# JOKE ENDPOINTS


# to randomize the url of the pranks
@app.route("/jokes/get/", methods=['GET'])
def get_random_joke():
    param = random.choice(list(URLS.keys()))  # Select with random dict value for search a joke in any API
    return get_joke_function(param)


@app.route("/jokes/create/", methods=['POST'])
def create_random_joke():
    param = random.choice(list(URLS.keys()))  # Select with random dict value for search a joke in any API
    return create_joke_function(param, mongo_instance)


# Principal module jokes endpoints
@app.route("/jokes/get/<string:param>", methods=['GET'])
def get_joke(param):
    return get_joke_function(param)


@app.route("/jokes/delete/<int:number>", methods=['DELETE'])
def delete_joke(number):
    return delete_joke_function(mongo_instance, number)


@app.route("/jokes/update/<string:param>/<int:number>", methods=['PUT'])
def update_joke(param, number):
    return update_joke_function(param, mongo_instance, number)


@app.route("/jokes/create/<string:param>", methods=['POST'])
def create_joke(param):
    return create_joke_function(param, mongo_instance)


# MATH ENDPOINTS
@app.route("/numbers/get_by_list/", methods=['GET'])
def get_list_num():
    list_num = eval(request.args.get('id'))
    return process_lmc_function(list_num)


@app.route("/numbers/get/", methods=['GET'])
def get_num():
    number = eval(request.args.get('id'))
    return yaml.dump({'value': number + 1})


if __name__ == '__main__':
    app.run(debug=True, port=8000)
