from email.mime import application
from flask import Flask
application=Flask(__name__)

@application.route('/')
def main():
    print('hello from Holland')
    return 'test from Gerald'


