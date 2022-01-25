from flask import jsonify


def get_response(code, message, data):
    response = jsonify({
        'code': code,
        'message': message,
        'data': data,
    })
    response.status_code = code
    return response
