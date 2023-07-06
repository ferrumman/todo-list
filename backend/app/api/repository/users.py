from .mongo import get_mongo_client
from fastapi.encoders import jsonable_encoder

class Users:
    db = None

    def __init__(self, db):
        try:
            self.db = db
            pass
        except Exception as e:
            print(e)

    def sign_up(self, user):
        # jsonable_encoder(user)
        print('Sign up ', jsonable_encoder(user))
        self.db.insert_one('users', jsonable_encoder(user))

    def login(self):
        # self.db.insert_one()
        pass


def get_user_controller():
    return Users(get_mongo_client())