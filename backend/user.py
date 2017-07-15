from globals import db


class User():

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

    def update(self):
        pass

    def delete(self):
        db.users.delete_one({"username": self.username})
