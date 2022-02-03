from flask import Flask, jsonify
application=Flask(__name__)

@application.route('/')
def main():
    print('hello from Holland')
    return jsonify(hello='world') # Returns HTTP Response with {"hello": "world"}


