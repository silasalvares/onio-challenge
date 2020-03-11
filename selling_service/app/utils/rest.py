from functools import wraps
from flask import Flask, request, jsonify, render_template

class JsonResponse:

    def __init__(self, success=True, message="", data=None, response_type=''):
        self.responseType = response_type
        self.success = success
        self.message = message
        self.data = data

    def jsonify(self):
        return jsonify({
            'responseType': self.responseType,
        	'success': self.success,
        	'message': self.message,
        	'data': self.data
        })

    def make_json_response(self):
        return jsonify({
            'responseType': self.responseType,
        	'success': self.success,    
        	'message': self.message,
        	'data': self.data
        }), 200 if self.success else 500

def validate_schema(schema=None):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            schema_data = None
            schema_data = schema.load(request.json)
            return f(schema_data=schema_data, *args, **kwargs)
        return decorated_function
    return decorator

def make_json_app(import_name, **kwargs):
    
    def make_json_error(ex):
        response = jsonify(message='Erro')
        # response.status_code = (ex.code
        #                         if isinstance(ex, HTTPException)
        #                         else 500)
        return response

    app = Flask(import_name, **kwargs)
    app.register_error_handler(500, make_json_error)
    # for code in default_exceptions.iterkeys():
    #     app.error_handler_spec[None][code] = make_json_error
    return app