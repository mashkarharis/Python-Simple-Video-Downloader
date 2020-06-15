import wx
from wx import NO_BORDER



class MainFrame(wx.Frame):
    def __init__(self):
        app=wx.App()
        wx.Frame.__init__(self, parent=None, title= "Downloadable Media Player",size=(600,400) ,style=NO_BORDER | wx.RAISED_BORDER)
        from com.View.Homepanel import HomePanel
        self.Center()
        self.SetBackgroundColour("white")
        self.SetMaxSize(wx.Size(600,400))
        self.SetMinSize(wx.Size(600,400))
        homepanel = HomePanel(self)
        self.Show(show=True)
        app.MainLoop()
        

 
