from flask import Flask
from flask_restful import Resource, Api
import logging as logger

logger.basicConfig(level="DEBUG")

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        logger.debug("inside get method of task")
        details = {
            "version": "1.0.0.0",
            "owner": " Ritesh Tiwari",
            "projectName": "python flask  docker container"
        }
        return details, 200


api.add_resource(HelloWorld, '/')


@app.route("/hello")
def hello():
    return "<h1>hello World my function !</h1>"


if __name__ == '__main__':
    logger.debug("starting Flask Server from main function")
    app.run(host="localhost", port=5000, debug=True)
