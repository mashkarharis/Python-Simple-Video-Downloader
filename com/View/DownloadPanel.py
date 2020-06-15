import wx
import os
import sys
class DownloadPanel(wx.Panel):
    def __init__(self,mainframe):
        self.count=0
        wx.Panel.__init__(self,parent=mainframe,size=(600,800))
        text=wx.StaticText(self,label="Link (Should End As .MP4)",pos=(365,100),size=(50,-1) )
        font = wx.Font(12, wx.DECORATIVE, wx.BOLD, wx.NORMAL)
        text.SetFont(font)
        self.textCtrl = wx.TextCtrl(self, size = (200,100),pos=(365,135), style = wx.TE_MULTILINE)
        self.SetBackgroundColour("white")
        self.textCtrl.SetBackgroundColour("yellow")
        self.SetMaxSize(wx.Size(600,400))
        self.SetMinSize(wx.Size(600,400))
        path=os.path.abspath(__file__)
        path=path.split('\\')[0:-1]
        path='\\'.join(path)+"\\icons\\download.png"
        bmp = wx.Bitmap(path, wx.BITMAP_TYPE_ANY)
        wx.StaticBitmap(self, bitmap=bmp, pos=(100,100),size=(bmp.GetWidth()+10, bmp.GetHeight()+10))
        
        path=os.path.abspath(__file__)
        path=path.split('\\')[0:-1]
        path='\\'.join(path)+"\\icons\\back.ico"
        bmp = wx.Bitmap(path, wx.BITMAP_TYPE_ANY)
        self.back = wx.BitmapButton(self,-1,pos=(550,350),bitmap=bmp,size=(bmp.GetWidth()+10, bmp.GetHeight()+10))
        self.back.Bind(wx.EVT_BUTTON, self.goback)
        
        path=os.path.abspath(__file__)
        path=path.split('\\')[0:-1]
        path='\\'.join(path)+"\\icons\\quit.ico"
        bmp = wx.Bitmap(path, wx.BITMAP_TYPE_ANY)
        self.back = wx.BitmapButton(self,-1,pos=(550,5),bitmap=bmp,size=(bmp.GetWidth()+10, bmp.GetHeight()+10))
        self.back.Bind(wx.EVT_BUTTON, self.quites)
        text=wx.StaticText(self,label="Download MP4",pos =(20,12), size=(550,200), style=wx.ALIGN_CENTRE_HORIZONTAL )
        font = wx.Font(24, wx.DECORATIVE, wx.BOLD, wx.NORMAL)
        text.SetFont(font)
        self.gauge = wx.Gauge(self, range = 100, size = (300, 28),pos=(20,252), style = wx.GA_HORIZONTAL)
        self.gauge.SetValue(self.count) 
        self.downloadbutton = wx.Button(self,13,"Download",(365,250),(200,30))
        self.downloadbutton.Bind(wx.EVT_BUTTON, self.download)
        self.Update()
        
    def goback(self,event):
        from com.Controller.ViewController import ViewController
        self.Destroy()
        viewcontroller = ViewController()
        viewcontroller.gethomeview()
    def quites(self,event):
        sys.exit()
    def download(self,event):
        from com.Controller.DownloadCtrl import DownloadCtrl
        downloadcontroller =DownloadCtrl()
        downloadcontroller.downloadstart(self)
       
       
       
