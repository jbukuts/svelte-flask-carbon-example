import random
from flask import jsonify, make_response, request, Blueprint

api = Blueprint('api', __name__)

@api.route("/rand", methods = ['GET'])
def random_num():
    """Simple REST API example to be called from frontend"""
    headers = { "Content-Type": "application/json" }
    data = { "num": random.randint(0, 100) }
    return make_response(jsonify(data), 200, headers)

@api.route("/hello_get", methods = ['GET'])
def hello_get():
    """Simple REST API that can parse URL params"""
    headers = { "Content-Type": "application/json" }

    name = request.args.get('name')
    if name is None:
        return make_response('Error no name param in URL', 400, headers)

    return make_response(f"Hello, {name}!", 200, headers)

@api.route("/hello_post", methods = ['POST'])
def hello_post():
    """Simple REST API that can parse JSON body in request"""
    headers = { "Content-Type": "application/json" }
    
    name = request.get_json().get('name')
    if name is None:
        return make_response('Error no name param in request body', 400, headers)

    return make_response(f"Hello, {name}!", 200, headers)