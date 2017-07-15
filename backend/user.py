from globals import db


class User():

    def __init__(self, username, score):
        self.username = username
        self.score = score

    def create(self):
        result = {
            "username": self.username,
            "score": self.score,
            "proposals": [],
            "investorFunds": [],
            "playerFunds": []
        }
        db.users.insert_one(result)

    def update(self):
        pass

    def delete(self):
        db.users.delete_one({"username": self.username})
