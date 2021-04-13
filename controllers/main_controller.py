from views.main_view import MainWindow, AddNewOperator
from mvc_layer.Model import Model
from pubsub import pub
from views.toolbar import MainToolbarView
from views.main_munebar_view import MainManuBarView
from views.add_new_operator_view import AddNewOperator
import constants as con
import wx


class ApplicationController:
    def __init__(self):
        self.main_window_view = MainWindow(parent=None)
        self.add_new_user_view = AddNewOperator(parent=None, id=wx.ID_ANY)
        self.model = Model()

        # self.main_window_view.Bind(wx.EVT_TOOL, self.test, id=wx.ID_ANY)

        pub.subscribe(self.on_button_add_new_user_click, 'my_topic')
        pub.subscribe(self.snoop, pub.ALL_TOPICS)

    def main(self):
        self.main_window_view.main()
        print('start from controller')

    # def test(self, e):
    #     print("Hi")
    #
    #
    #
    # def CreateNewFIle(self, event):
    #     print("Button create new")
    #
    # def AddNewUser(self, e):
    #     add_new_user = self.add_new_user_view
    #     add_new_user.Show()
    #
    # def OnQuit(self, e):
    #     self.main_window_view.Close()

    def snoop(topicObj=pub.AUTO_TOPIC, **mesgData):
        print('topic "%s": %s' % (topicObj.on_button_add_new_user_click, mesgData))

    def on_button_add_new_user_click(self, arg):
        self.model.add_new_operator(arg)

        print(f'Controller get {arg}')


if __name__ == '__main__':
    app = wx.App()
    main_window = ApplicationController()
    main_window.main()


# insert into orders values (null, 3, 'ZW 58', '22Wed');
# insert into orders values (null, 2, 'ZW 100', '654');
# insert into orders values (null, 4, 'ZW 258', '111A');
# insert into orders values (null, 1, 'ZW 1', '654');
# insert into orders values (null, 3, 'ZW 25', '22Wed');
#
# insert into operator values (1, 'Sashka');
# insert into operator values (null, 'Piotr');
# insert into operator values (null, 'Piotr Tokarka');
# insert into operator values (null, 'Junior');
# insert into operator values (null, 'Ruslan');
