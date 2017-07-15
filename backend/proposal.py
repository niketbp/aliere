from globals import db


class Proposal:

    def __init__(self, name):
        self.name = name

    def create(self, username, fund, ticker, num_votes, num_shares, transaction_type):
        existing_proposal = db.proposals.find_one({"proposalName": self.name})
        if existing_proposal:
            raise Exception("Proposal already exists")

        entry = {
            "proposalName": self.name,
            "numVotes": num_votes,
            "ticker": ticker,
            "numShares": num_shares,
            "transactionType": transaction_type.upper()
        }
        id = db.proposals.insert_one(entry).inserted_id
        db.users.update_one({'username': username}, {'$push': {'proposals': id}})
        db.funds.update_one({'fundName': fund}, {'$push': {'proposals': id}})

    def upvote(self):
        update_result = db.proposals.update_one({'proposalName': self.name}, {'$inc': {'numVotes': 1}})
        if update_result.modified_count == 0:
            raise Exception("Unable to cast vote. Please try again!")

    def downvote(self):
        update_result = db.proposals.update_one({'proposalName': self.name}, {'$inc': {'numVotes': -1}})
        if update_result.modified_count == 0:
            raise Exception("Unable to cast vote. Please try again!")

    def act(self, username, fund_name):
        self.delete(username, fund_name)

    def delete(self, username, fund_name):
        id = db.proposals.find_one({'proposalName': self.name})['_id']
        db.users.update_one({'username': username}, {'$pop': {'proposals': id}})
        db.funds.update_one({'fundName': fund_name}, {'$pop': {'proposals': id}})
        db.proposals.delete_one({"proposalName": self.name})
