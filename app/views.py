from uuid import uuid4

from flask import Blueprint, jsonify, request

auth = Blueprint('auth', __name__)

TOKEN = str(uuid4())


@auth.route('/token')
def get_token():
    return jsonify(TOKEN)


@auth.route('/secure', methods=['POST'])
def secure_page():
    args = request.get_json(force=True)
    if 'token' in args:
        if args['token'] == TOKEN:
            return jsonify('This is a secure page')

    res = jsonify('Unauthorized')
    res.status_code = 401
    return res
