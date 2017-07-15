from flask import Flask
from flask import request, jsonify
from fund import Fund
from proposal import Proposal
from stock import get_ticker_data
from user import User

app = Flask(__name__)


def validate_arguments(args, num_args):
    if num_args != len(request.args):
        raise Exception("Incorrect number of arguments")
    for arg in args:
        if not request.args.get(arg):
            raise Exception("Incorrect argument %s provided" % arg)


@app.route("/user/create")
def user_create():
    try:
        validate_arguments(['user'], 1)
        user = User(request.args.get('user'), 0)
        user.create()
        return jsonify({'Status': 'User %s added successfully' % user.username})
    except Exception as e:
        return jsonify({'Error': str(e)})


@app.route("/user/data")
def user_data():
    try:
        validate_arguments(['user'], 1)

    except Exception as e:
        return jsonify({'Error': str(e)})


@app.route("/user/delete")
def user_delete():
    try:
        validate_arguments(['user'], 1)
        user = User(request.args.get('user'), 0)
        user.delete()
        return jsonify({'Status': 'User %s deleted successfully' % user.username})
    except Exception as e:
        return jsonify({'Error': str(e)})


@app.route("/user/update")
def user_update():
    try:
        validate_arguments(['user'], 1)
        user = User(request.args.get('user'), 0)
        user.update()
    except Exception as e:
        return jsonify({'Error': str(e)})


@app.route("/proposal/act")
def proposal_act():
    try:
        validate_arguments()

    except Exception as e:
        return jsonify({'Error': str(e)})


@app.route("/proposal/create")
def proposal_create():
    try:
        validate_arguments(['name', 'ticker', 'shares', 'transaction', 'user', 'fund'], 6)
        proposal = Proposal(request.args.get('name'))
        proposal.create(request.args.get('user'), request.args.get('fund'), request.args.get('ticker'), 0,
                        request.args.get('shares'), request.args.get('transaction'))
        return jsonify({'Status': 'Proposal %s added successfully' % proposal.name})
    except Exception as e:
        return jsonify({'Error': str(e)})


@app.route("/proposal/delete")
def proposal_delete():
    try:
        validate_arguments(['name'], 1)
        proposal = Proposal(request.args.get('name'))
        proposal.delete()
        return jsonify({'Status': 'Proposal %s deleted successfully' % proposal.name})
    except Exception as e:
        return jsonify({'Error': str(e)})


@app.route("/fund/add")
def fund_add():
    try:
        validate_arguments()

    except Exception as e:
        return jsonify({'Error': str(e)})


@app.route("/fund/delete")
def fund_delete():
    try:
        validate_arguments()

    except Exception as e:
        return jsonify({'Error': str(e)})


@app.route("/fund/join")
def fund_join():
    try:
        validate_arguments()

    except Exception as e:
        return jsonify({'Error': str(e)})


@app.route("/fund/leave")
def fund_leave():
    try:
        validate_arguments()

    except Exception as e:
        return jsonify({'Error': str(e)})


@app.route("/stock", methods=['GET'])
def stock():
    try:
        validate_arguments('ticker', 1)
        ticker = request.args.get('ticker')
        return jsonify(get_ticker_data(ticker))
    except Exception as e:
        return jsonify({'Error': str(e)})


if __name__ == '__main__':
    app.run()