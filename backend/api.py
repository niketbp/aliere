from flask import Flask
from flask import request, jsonify
from flask_pymongo import PyMongo
from globals import alpha_vantage
app = Flask(__name__)
mongo = PyMongo(app)


def validate_arguments(args, num_args):
    if num_args != len(request.args):
        return jsonify({'Error': "Incorrect number of arguments"})
    for arg in args:
        if not request.args.get(arg):
            return jsonify({'Error': 'Incorrect argument provided'})

@app.route("/")
def hello():
    return("Hello World!")


@app.route("/user/add")
def user_add():
    validate_arguments('user', 1)
    username = request.args.get('user')
    # store user in db


@app.route("/user/update")
def user_update():


@app.route("/user/data")
def user_data():


@app.route("/proposal/add")
def proposal():



@app.route("/stock")
def stock():
    validate_arguments('ticker', 1)
    ticker = request.args.get('ticker')
    alpha_vantage.get_ticker_data(ticker)