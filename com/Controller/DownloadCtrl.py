import wx
import requests
from warnings import catch_warnings
class DownloadCtrl:
    def downloadstart(self,panels):
        try:
            from com.Model.downloadmodel import DownloadModel
            from six.moves.urllib.request import urlopen
            url=panels.textCtrl.GetValue()
            response = urlopen(url)
            content = response.info()
            res=wx.MessageDialog(panels, str(content),'Details', wx.YES_NO| wx.ICON_INFORMATION).ShowModal()
            if (res==wx.ID_YES):
                downloadmodel= DownloadModel()
                length=int(response.getheader("Content-Length"))
                downloadmodel.downloadfile(url, panels,length)
        except Exception as e:
            wx.MessageDialog(panels, str(e),'Error', wx.OK| wx.ICON_WARNING).ShowModal()
            
        
    def setpercentage(self,val,panels):
        panels.gauge.SetValue(val)
        panels.Refresh()