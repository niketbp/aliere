from globals import db


class Proposal():

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

    def update(self):
        pass

    def delete(self):
        db.proposals.delete_one({"proposalName": self.name})
