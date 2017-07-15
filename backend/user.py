from globals import db
from bson.json_util import dumps


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
        return dumps(db.users.find_one({"username": self.username}))
