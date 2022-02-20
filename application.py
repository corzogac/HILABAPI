from flask import Flask, jsonify

application=Flask(__name__)

@application.route('/users')
def main():
    #print('hello from Holland')
    person = [{'id':1,'name': 'Alice2', 'username': "1986",'Site':"https://betterprogramming.pub/data-visualization-with-swiftui-radar-charts-64124aa2ac0b"},
    {'id':2,'name': 'Gerald', 'username': "Corzo",'Site':"https://bookauthority.org/books/new-swiftui-books"}]
    return jsonify(person) # Returns HTTP Response with {"hello": "world"}



@application.route('/')
def PageLand():
    return "Welcome to my test stie"

#export FLASK_APP