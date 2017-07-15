from globals import db


class Proposal():

    def __init__(self, ticker, num_votes, num_shares, transaction_type):
        self.ticker = ticker
        self.num_votes = num_votes
        self.num_shares = num_shares
        self.transaction_type = transaction_type

    def create(self, username, fund):
        result = {
            "numVotes": self.num_votes,
            "ticker": self.ticker,
            "numShares": self.num_shares,
            "transactionType": self.transaction_type.upper()
        }
        id = db.proposals.insert_one(result).inserted_id
        db.users.update_one({'username': username}, {'$push': {'proposals': id}})
        db.funds.update_one({'fundName': fund}, {'$push': {'proposals': id}})

    def update(self):
        pass

    def delete(self):
        pass