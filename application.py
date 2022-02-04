from flask import Flask, jsonify

application=Flask(__name__)

@application.route('/users')
def main():
    #print('hello from Holland')
    person = [{'id':1,'name': 'Alice2', 'username': "1986"},{'id':2,'name': 'Gerald', 'username': "Corzo"}]
    return jsonify(person) # Returns HTTP Response with {"hello": "world"}


#export FLASK_APP