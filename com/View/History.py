import wx
import os
import sys
class HistoryPanel(wx.Panel):
    def __init__(self,mainframe):
        wx.Panel.__init__(self,parent=mainframe,size=(600,800))
        self.SetMaxSize(wx.Size(600,400))
        self.SetMinSize(wx.Size(600,400))
        
        path=os.path.abspath(__file__)
        path=path.split('\\')[0:-1]
        path='\\'.join(path)+"\\icons\\back.ico"
        bmp = wx.Bitmap(path, wx.BITMAP_TYPE_ANY)
        back = wx.BitmapButton(self,-1,pos=(550,350),bitmap=bmp,size=(bmp.GetWidth()+10, bmp.GetHeight()+10))
        back.Bind(wx.EVT_BUTTON, self.goback)
        
        path=os.path.abspath(__file__)
        path=path.split('\\')[0:-1]
        path='\\'.join(path)+"\\icons\\quit.ico"
        bmp = wx.Bitmap(path, wx.BITMAP_TYPE_ANY)
        back = wx.BitmapButton(self,-1,pos=(550,5),bitmap=bmp,size=(bmp.GetWidth()+10, bmp.GetHeight()+10))
        back.Bind(wx.EVT_BUTTON, self.quites)
        text=wx.StaticText(self,label="History",pos =(30,12), size=(600,200), style=wx.ALIGN_CENTRE_HORIZONTAL )
        font = wx.Font(24, wx.DECORATIVE, wx.BOLD, wx.NORMAL)
        text.SetFont(font)
        self.SetBackgroundColour("white")
       
    def goback(self,event):
        from com.Controller.ViewController import ViewController
        self.Destroy()
        viewcontroller = ViewController()
        viewcontroller.gethomeview()
    def quites(self,event):
        sys.exit()
       
       
       
       #<a target="_blank" href="https://icons8.com/icons/set/back">Back icon</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>