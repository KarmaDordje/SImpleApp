from DB import db_helper
class Model:
    def __init__(self):
        self.text = ''


    def add_new_operator(self, text):
        db_helper.create_new_operator(text)