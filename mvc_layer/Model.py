from db import db_helper
from repositories.OperatorRepository import OperatorRepository
from db.datamodel import Operator
from sqlalchemy.orm import Session

class Model:
    def __init__(self):
        self.session = Session()
        self.operator_repo = OperatorRepository(self.session)

    def add_new_user(self, operator:Operator):
        self.operator_repo.save(operator)
