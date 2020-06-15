class ViewController(object):
    
    def gethomeview(self):
        from com.View.Main import MainFrame
        view1 = MainFrame()
        
    def gethistoryview(self,mainframe):
        from com.View.History import HistoryPanel
        History1 = HistoryPanel(mainframe)
        
    def getplaypanel(self,mainframe):
        from com.View.PlayPanel import PlayPanel
        play = PlayPanel(mainframe)
    def getdownloadview(self,mainframe):
        from com.View.DownloadPanel import DownloadPanel
        play = DownloadPanel(mainframe)
    
