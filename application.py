from flask import Flask, jsonify
import pandas as pd

application=Flask(__name__)

@application.route('/users')
def main():
    #print('hello from Holland')
    person = [{'id':1,'name': 'Alice2', 'username': "1986",'Site':"https://betterprogramming.pub/data-visualization-with-swiftui-radar-charts-64124aa2ac0b"},
    {'id':2,'name': 'Gerald', 'username': "Corzo",'Site':"https://bookauthority.org/books/new-swiftui-books"},
    {'id':3,'name': 'Aurelio', 'username': "Au2",'Site':"https://bookauthority.org/books/new-swiftui-books"}
    ]
    a=pd.read_csv('hilinks.csv')

    return jsonify(a.to_json()) # Returns HTTP Response with {"hello": "world"}jsonify(person)#



@application.route('/')
def PageLand():
    return "Welcome to my test stie"


#application.run() 
#export FLASK_APP