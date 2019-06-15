from flask import Flask
from flask_restful import Resource, Api, reqparse
import string
import random


app = Flask(__name__)
api = Api(app)


class Generator():
    def __init__(self, len, special, capital, numbers):
        self.len = len
        self.special = special
        self.capital = capital
        self.numbers = numbers

    def generate(self):
        password_base = string.ascii_lowercase
        if self.capital:
            password_base += string.ascii_uppercase
        if self.special:
            password_base += string.punctuation
        if self.numbers:
            password_base += string.digits
        return ''.join(random.choice(password_base) for i in range(self.len))



class Password(Resource):
    def get(self):
        return {'message': 'use POST request to generate password',
                'data': None}, 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('len', type=int, help='password length')
        parser.add_argument('special', type=bool, help='use special characters')
        parser.add_argument('capital', type=bool, help='use capital characters')
        parser.add_argument('numbers', type=bool, help='use number characters')
        args = parser.parse_args()
        password = Generator(args['len'], args['special'], args['capital'], args['numbers'])
        return {
            'password': password.generate()
        }, 201


api.add_resource(Password, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
