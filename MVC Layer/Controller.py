from View import MainWindow,AddNewOperator
from Model import Model


class ApplicationController:
    def __init__(self):
        self.main_window_view = MainWindow(self)
        self.add_new_user_view = AddNewOperator()
        self.model = Model()

    def main(self):
        self.main_window_view.main()

    def on_button_add_new_user_click(self, text):
        self.model.add_new_operator(text)





if __name__ == '__main__':
    MainWindow.main()



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

