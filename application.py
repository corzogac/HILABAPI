from flask import Flask, jsonify
application=Flask(__name__)

@application.route('/')
def main():
    #print('hello from Holland')
    person = {'name': 'Alice', 'username': "1986"}
    return jsonify(person) # Returns HTTP Response with {"hello": "world"}


