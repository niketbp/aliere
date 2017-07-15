from flask import Flask
from flask import request, jsonify
from flask_pymongo import PyMongo
from fund import Fund
from proposal import Proposal
from stock import get_ticker_data
from user import User

app = Flask(__name__)
mongo = PyMongo(app)


def validate_arguments(args, num_args):
    if num_args != len(request.args):
        raise Exception("Incorrect number of arguments")
    for arg in args:
        if not request.args.get(arg):
            raise Exception("Incorrect argument %s provided" % arg)


@app.route("/")
def hello():
    return("Hello World!")


@app.route("/user/create")
def user_create():
    try:
        validate_arguments('user', 1)
        user = User(request.args.get('user'))
        user.create()
    except Exception as e:
        return jsonify({'Error:', str(e)})

@app.route("/user/update")
def user_update():
    try:
        validate_arguments('user', 1)
        user = User(request.args.get('user'))
        user.update()
    except Exception as e:
        return jsonify({'Error:', str(e)})

@app.route("/user/delete")
def user_delete():
    try:
        validate_arguments('user', 1)
        user = User(request.args.get('user'))
        user.delete()
    except Exception as e:
        return jsonify({'Error:', str(e)})

@app.route("/user/data")
def user_data():
    try:
        validate_arguments('user', 1)

    except Exception as e:
        return jsonify({'Error:', str(e)})

@app.route("/proposal/add")
def proposal():
    try:
        validate_arguments()

    except Exception as e:
        return jsonify({'Error:', str(e)})


@app.route("/stock", methods=['GET'])
def stock():
    try:
        validate_arguments('ticker', 1)
        ticker = request.args.get('ticker')
        return jsonify(get_ticker_data(ticker))
    except Exception as e:
        return jsonify({'Error:', str(e)})


if __name__ == '__main__':
    app.run()