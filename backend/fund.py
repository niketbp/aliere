from globals import db

class Fund():

    def __init__(self, name):
        self.fund_name = name

    def create(self):
        existing_fund = db.funds.find_one({"fundName": self.fund_name})
        if existing_fund:
            raise Exception("Fund already exists")

        entry = {
            "fundName": self.fund_name,
            "proposals": []
        }
        db.funds.insert_one(entry)

    def update(self):
        pass

    def delete(self):
        db.users.delete_one({"fundName": self.fund_name})