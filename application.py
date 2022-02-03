from flask import Flask, jsonify
application=Flask(__name__)

@application.route('/')
def main():
    #print('hello from Holland')
    person = [{'id':1,'name': 'Alice', 'username': "1986"},{'id':2,'name': 'Gerald', 'username': "Corzo"}]
    return jsonify(person) # Returns HTTP Response with {"hello": "world"}


