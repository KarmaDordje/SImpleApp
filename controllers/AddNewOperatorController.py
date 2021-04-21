import wx
from pubsub import pub
from mvc_layer.Model import Model
from db.datamodel import Operator
from views.AddNewOperatorView import AddNewOperator

class AddNewOperatorController:
    def __init__(self):
        self.model = Model()
        self.add_new_operator = AddNewOperator
        #self.operator = Operator()
        pub.subscribe(self.OnButtonAddNewUser, 'my_topic')
        pub.subscribe(self.snoop, pub.ALL_TOPICS)


    def snoop(topicObj=pub.AUTO_TOPIC, **mesgData):
        print('topic "%s": %s' % (topicObj.OnButtonAddNewUser, mesgData))

    def OnButtonAddNewUser(self,arg):
        operator = Operator()
        operator.name = arg
        self.model.add_new_user(operator)

    def user_already_exist(self, msg):
        self.add_new_operator.status.SetLabel(msg)