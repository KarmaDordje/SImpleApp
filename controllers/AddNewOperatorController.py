import wx
from pubsub import pub
from mvc_layer.Model import Model
from db.datamodel import Operator

class AddNewOperatorController:
    def __init__(self):
        self.model = Model()
        self.operator = Operator()
        pub.subscribe(self.OnButtonAddNewUser, 'my_topic')
        pub.subscribe(self.snoop, pub.ALL_TOPICS)


    def snoop(topicObj=pub.AUTO_TOPIC, **mesgData):
        print('topic "%s": %s' % (topicObj.OnButtonAddNewUser, mesgData))

    def OnButtonAddNewUser(self, arg):
        self.operator.name = arg
        self.model.add_new_user(self.operator.name)
        print(self.operator.name)
