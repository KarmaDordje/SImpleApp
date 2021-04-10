from mvc_layer.Controller import ApplicationController
import wx

if __name__ == '__main__':
    app = wx.App()
    main_window = ApplicationController()
    main_window.main()
