import ParserMod
import DataBase
import threading
class Craweler:
        
    def __init__(self):
        self.MyDataBaseMaster = DataBase.DataBaseMaster()
        self.MyParser = ParserMod.Parser() 

    def Crawel(self,ThreadLock):
        while True:
            #get the url from the container and start crawling for each thread (container is initlally  filed with few urls)
            Url =""
            ThreadLock.acquire()
            Temp = self.MyDataBaseMaster.GetURLIDByStatus('N')
            if Temp:
                Url = Temp[0][1]
                self.MyDataBaseMaster.UpdateURLStatus('C',Url)
                ThreadLock.release()
            else:
                ThreadLock.release()

            if Url:
                print(threading.current_thread().name +" has:" + Url)
                UrlsRetrived,Succes,UrlDelay = self.MyParser.GetLinksFromHtml(Url)
                if  Succes:
                    for i in UrlsRetrived:
                        self.MyDataBaseMaster.InsertNewUrl(i,'N',0,0)
                        print(i)
                    
                
