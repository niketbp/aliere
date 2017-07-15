from globals import db
from fund import Fund


class User:

    def __init__(self, username):
        self.username = username

    def create(self, score):
        existing_user = db.users.find_one({"username": self.username})
        if existing_user:
            raise Exception("Username already exists")

        entry = {
            "username": self.username,
            "score": score,
            "proposals": [],
            "investorFunds": [],
            "playerFunds": []
        }
        db.users.insert_one(entry)

    def update_username(self, new_username):
        update_result = db.users.update_one({'username': self.username}, {'$set': {'username': new_username}})
        if update_result.modified_count == 0:
            raise Exception("Unable to update username. Please make sure it is spelled correctly!")
        self.username = new_username

    def update_score(self, score):
        update_result = db.users.update_one({'username': self.username}, {'$set': {'score': score}})
        if update_result.modified_count == 0:
            raise Exception("Unable to update username. Please make sure it is spelled correctly!")

    def delete(self):
        db.users.delete_one({"username": self.username})

    def get_data(self):
        results = db.users.find_one({"username": self.username})
        for i in range(len(results['proposals'])):
            results['proposals'][i] = db.proposals.find_one({"_id": results['proposals'][i]})
        for i in range(len(results['investorFunds'])):
            fund = db.funds.find_one({"_id": results['investorFunds'][i]})
            fund_obj = Fund(fund['fundName'])
            results['investorFunds'][i] = fund_obj.get_data()
        for i in range(len(results['playerFunds'])):
            fund = db.funds.find_one({"_id": results['playerFunds'][i]})
            fund_obj = Fund(fund['fundName'])
            results['playerFunds'][i] = fund_obj.get_data()
        if not results:
            raise Exception('Invalid username')
        return results
