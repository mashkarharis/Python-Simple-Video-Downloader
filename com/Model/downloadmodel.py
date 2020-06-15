
import requests
class DownloadModel:
    def downloadfile(self,url,panels,length):
        from com.Controller.DownloadCtrl import DownloadCtrl
        downloadctrl = DownloadCtrl()
        local_filename = url.split('/')[-1]
        r = requests.get(url, stream=True)
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024): 
                if chunk:
                    f.write(chunk)
                    current=int(f.tell())
                    val=(current/length)*100
                    downloadctrl.setpercentage(val,panels)
        return local_filename
    
    
    #test : https://assets.mixkit.co/videos/preview/mixkit-stars-in-space-1610-large.mp4