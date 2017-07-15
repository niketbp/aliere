from globals import db


class Fund:

    def __init__(self, name):
        self.fund_name = name

    def create(self, username):
        existing_fund = db.funds.find_one({"fundName": self.fund_name})
        if existing_fund:
            raise Exception("Fund already exists")

        entry = {
            "fundName": self.fund_name,
            "proposals": []
        }
        id = db.funds.insert_one(entry).inserted_id
        db.users.update_one({'username': username}, {'$push': {'investorFunds': id}})

    def update(self):
        pass

    def delete(self):
        id = db.funds.find_one({'fundName': self.fund_name})['_id']
        db.users.update_all({}, {'$pop': {'investorFunds': id}})
        db.users.update_all({}, {'$pop': {'playerFunds': id}})
        db.funds.delete_one({"fundName": self.fund_name})

    def join(self, username):
        id = db.funds.find_one({'fundName': self.fund_name})['_id']
        db.users.update_one({'username': username}, {'$push': {'playerFunds': id}})

    def leave(self, username):
        id = db.funds.find_one({'fundName': self.fund_name})['_id']
        db.users.update_one({'username': username}, {'$pop': {'playerFunds': id}})

    def get_data(self):
        results = db.funds.find_one({"fundName": self.fund_name})
        for i in range(len(results['proposals'])):
            results['proposals'][i] = db.proposals.find_one({"_id": results['proposals'][i]})
        if not results:
            raise Exception('Invalid fund name')
        return results
