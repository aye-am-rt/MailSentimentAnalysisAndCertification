from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


# method names like get and post are automatically mapped with the given function name same as get,post,delete,patch,put
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self):
        some_json = request.get_json()
        return jsonify({'you sent': some_json}), 201


class Multi(Resource):
    def get(self, num):
        return {'result': num * 10}


api.add_resource(HelloWorld, '/')
api.add_resource(Multi, '/multi/<int:num>')

if __name__ == '__main__':
    app.run(host="localhost", port=1099, debug=True, load_dotenv=True)
