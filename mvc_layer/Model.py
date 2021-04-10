from DB import db_helper


class Model:

    @staticmethod
    def add_new_operator(name):
        db_helper.create_new_operator(name)