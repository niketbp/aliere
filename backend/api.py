from flask import Flask
from flask import request, jsonify
from flask_cors import cross_origin
import json
from bson import ObjectId
from fund import Fund
from proposal import Proposal
from stock import get_ticker_data
from user import User


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

app = Flask(__name__)
app.json_encoder = JSONEncoder


def validate_arguments(args, num_args):
    if num_args != len(request.args):
        raise Exception("Incorrect number of arguments")
    for arg in args:
        if not request.args.get(arg):
            raise Exception("Incorrect argument %s provided" % arg)


@app.route("/user/create", methods=['GET'])
def user_create():
    try:
        validate_arguments(['user'], 1)
        user = User(request.args.get('user'))
        user.create(0)
        return jsonify({'Status': 'User %s added successfully' % user.username})
    except Exception as e:
        return jsonify({'Error': str(e)})


@app.route("/user/data", methods=['GET'])
@cross_origin()
def user_data():
    try:
        validate_arguments(['user'], 1)
        user = User(request.args.get('user'))
        return jsonify(user.get_data())
    except Exception as e:
        return jsonify({'Error': str(e)})


@app.route("/user/delete", methods=['DELETE'])
def user_delete():
    try:
        validate_arguments(['user'], 1)
        user = User(request.args.get('user'))
        user.delete()
        return jsonify({'Status': 'User %s deleted successfully' % user.username})
    except Exception as e:
        return jsonify({'Error': str(e)})


@app.route("/user/update", methods=['GET'])
def user_update():
    try:
        user = User(request.args.get('user'))
        if len(request.args) == 1:
            return jsonify({'Error': 'Need to provide at least two arguments, one being user'})
        elif len(request.args) > 3:
            return jsonify({'Error': 'Too many arguments provided'})
        else:
            for arg in request.args:
                if arg == 'user':
                    continue
                elif arg == 'new_user':
                    user.update_username(request.args.get('new_user'))
                elif arg == 'score':
                    user.update_score(int(request.args.get('score')))
                else:
                    return jsonify({'Error': 'Incorrect parameter %s' % arg})
        return jsonify({'Status': 'User %s updated successfully' % request.args.get('user')})

    except Exception as e:
        return jsonify({'Error': str(e)})


@app.route("/proposal/act", methods=['GET'])
def proposal_act():
    try:
        validate_arguments(['name', 'username', 'fund_name'], 3)
        proposal = Proposal(request.args.get('name'))
        proposal.act(request.args.get('username'), request.args.get('fund_name'))
        return jsonify({'Status': 'Proposal %s acted successfully' % proposal.name})
    except Exception as e:
        return jsonify({'Error': str(e)})


@app.route("/proposal/create", methods=['GET'])
def proposal_create():
    try:
        validate_arguments(['name', 'ticker', 'shares', 'transaction', 'user', 'fund'], 6)
        proposal = Proposal(request.args.get('name'))
        proposal.create(request.args.get('user'), request.args.get('fund'), request.args.get('ticker'), 0,
                        request.args.get('shares'), request.args.get('transaction'))
        return jsonify({'Status': 'Proposal %s added successfully' % proposal.name})
    except Exception as e:
        return jsonify({'Error': str(e)})


@app.route("/proposal/data", methods=['GET'])
def proposal_data():
    try:
        validate_arguments(['name'], 1)
        proposal = Proposal(request.args.get('name'))
        return jsonify(proposal.get_data())
    except Exception as e:
        return jsonify({'Error': str(e)})


@app.route("/proposal/delete", methods=['DELETE'])
def proposal_delete():
    try:
        validate_arguments(['name', 'username', 'fund_name'], 3)
        proposal = Proposal(request.args.get('name'))
        proposal.delete(request.args.get('username'), request.args.get('fund_name'))
        return jsonify({'Status': 'Proposal %s deleted successfully' % proposal.name})
    except Exception as e:
        return jsonify({'Error': str(e)})


@app.route("/proposal/downvote", methods=['GET'])
def proposal_downvote():
    try:
        validate_arguments(['name'], 1)
        proposal = Proposal(request.args.get('name'))
        proposal.downvote()
        return jsonify({'Status': 'Proposal %s: Vote removed successfully' % proposal.name})
    except Exception as e:
        return jsonify({'Error': str(e)})


@app.route("/proposal/upvote", methods=['GET'])
def proposal_upvote():
    try:
        validate_arguments(['name'], 1)
        proposal = Proposal(request.args.get('name'))
        proposal.upvote()
        return jsonify({'Status': 'Proposal %s upvoted successfully' % proposal.name})
    except Exception as e:
        return jsonify({'Error': str(e)})


@app.route("/fund/create", methods=['GET'])
def fund_create():
    try:
        validate_arguments(['name', 'username'], 1)
        fund = Fund(request.args.get('name'))
        fund.create(request.args.get('username'))
        return jsonify({'Status': 'Fund %s created successfully' % fund.fund_name})
    except Exception as e:
        return jsonify({'Error': str(e)})


@app.route("/fund/data", methods=['GET'])
@cross_origin()
def fund_data():
    try:
        validate_arguments(['name'], 1)
        fund = Fund(request.args.get('name'))
        return jsonify(fund.get_data())
    except Exception as e:
        return jsonify({'Error': str(e)})


@app.route("/fund/delete", methods=['DELETE'])
def fund_delete():
    try:
        validate_arguments(['name'], 1)
        fund = Fund(request.args.get('name'))
        fund.delete()
        return jsonify({'Status': 'Fund %s deleted successfully' % fund.fund_name})

    except Exception as e:
        return jsonify({'Error': str(e)})


@app.route("/fund/join", methods=['GET'])
def fund_join():
    try:
        validate_arguments(['name', 'username'], 2)
        fund = Fund(request.args.get('name'))
        fund.join(request.args.get('username'))
        return jsonify({'Status': 'Fund %s joined successfully' % fund.fund_name})
    except Exception as e:
        return jsonify({'Error': str(e)})


@app.route("/fund/leave", methods=['GET'])
def fund_leave():
    try:
        validate_arguments(['name', 'username'], 2)
        fund = Fund(request.args.get('name'))
        fund.leave(request.args.get('username'))
        return jsonify({'Status': 'Fund %s left successfully' % fund.fund_name})
    except Exception as e:
        return jsonify({'Error': str(e)})


@app.route("/stock", methods=['GET'])
def stock():
    try:
        validate_arguments(['ticker'], 1)
        ticker = request.args.get('ticker')
        return jsonify(get_ticker_data(ticker))
    except Exception as e:
        return jsonify({'Error': str(e)})


if __name__ == '__main__':
    app.run()
