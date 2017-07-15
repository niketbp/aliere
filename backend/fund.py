from globals import db

class Fund():

    def __init__(self, name):
        self.fund_name = name

    def create(self):
        entry = {
            "fundName": self.fund_name,
            "proposals": []
        }
        db.funds.insert_one(entry)

    def update(self):
        pass

    def delete(self):
        db.users.delete_one({"fundName": self.fund_name})