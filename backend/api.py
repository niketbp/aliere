from flask import Flask
from flask import request, jsonify
from flask_pymongo import PyMongo
from globals import alpha_vantage
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
    return "Hello World!"


@app.route("/user/add")
def user_add():
    validate_arguments('user', 1)
    username = request.args.get('user')
    # store user in db

#
# @app.route("/user/update")
# def user_update():
#
#
# @app.route("/user/data")
# def user_data():
#
#
# @app.route("/proposal/add")
# def proposal():


@app.route("/stock", methods=['GET'])
def stock():
    try:
        validate_arguments('ticker', 1)
        ticker = request.args.get('ticker')
        return jsonify(alpha_vantage.get_ticker_data(ticker))
    except Exception as e:
        return jsonify({'Error:', str(e)})


if __name__ == '__main__':
    app.run()