import wx
from wx import LI_VERTICAL
import os 
import sys


class HomePanel(wx.Panel):
    def __init__(self,mainframe):
        wx.Panel.__init__(self,parent=mainframe,size=(600,800))
        self.mainframe=mainframe
        self.SetMaxSize(wx.Size(600,400))
        self.SetMinSize(wx.Size(600,400))
        

        download=wx.Button(self,-1,"Download MP4",(60,300),(100,30))
        play = wx.Button(self,13,"Watch Video",(260,300),(100,30))
        history = wx.Button(self,14,"My History",(460,300),(100,30))
        wx.StaticLine(self,-1,pos=(200,70),size=(2,295),style=LI_VERTICAL)
        wx.StaticLine(self,-1,pos=(400,70),size=(2,295),style=LI_VERTICAL)
        history.Bind(wx.EVT_BUTTON, self.clickhistory )
        play.Bind(wx.EVT_BUTTON, self.clickplaypanel )
        download.Bind(wx.EVT_BUTTON, self.clickdownloadpanel )
        path=os.path.abspath(__file__)
        path=path.split('\\')[0:-1]
        path='\\'.join(path)+"\\icons\\info.ico"
        bmp = wx.Bitmap(path, wx.BITMAP_TYPE_ANY)
        back = wx.BitmapButton(self,-1,pos=(550,350),bitmap=bmp,size=(bmp.GetWidth()+10, bmp.GetHeight()+10))
        back.Bind(wx.EVT_BUTTON, self.info)
        
        path=os.path.abspath(__file__)
        path=path.split('\\')[0:-1]
        path='\\'.join(path)+"\\icons\\quit.ico"
        bmp = wx.Bitmap(path, wx.BITMAP_TYPE_ANY)
        back = wx.BitmapButton(self,-1,pos=(550,5),bitmap=bmp,size=(bmp.GetWidth()+10, bmp.GetHeight()+10))
        back.Bind(wx.EVT_BUTTON, self.quites)
        text=wx.StaticText(self,label="Downloadable Video Player",pos =(145,12), size=(400,200) )
        font = wx.Font(20, wx.DECORATIVE, wx.BOLD, wx.NORMAL)
        text.SetFont(font)
        self.SetBackgroundColour("white")
    def info(self,event):
        wx.MessageBox('Made By Mohomed Haris Mohomed Ashkar \n Email : mashkarharis@gmail.com\n IconsBy : ICONS8.COM', 'Info', wx.OK | wx.ICON_INFORMATION)
        
    def quites(self,event):
        sys.exit()    
    
    def clickdownloadpanel(self,event):
        from com.Controller.ViewController import ViewController
        self.Destroy()
        viewcontroller = ViewController()
        viewcontroller.getdownloadview(self.mainframe)
    def clickhistory(self,event):
        from com.Controller.ViewController import ViewController
        self.Destroy()
        viewcontroller = ViewController()
        viewcontroller.gethistoryview(self.mainframe)
    def clickplaypanel(self,event):
        from com.Controller.ViewController import ViewController
        self.Destroy()
        viewcontroller = ViewController()
        viewcontroller.getplaypanel(self.mainframe)
        