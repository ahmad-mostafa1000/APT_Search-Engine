from urllib.request import urlopen
from html.parser import HTMLParser    
from urllib import parse
import re
import os
import DataBase
try:
    from itertools import imap
except ImportError:
    imap=map

class Parser(HTMLParser):


    def __init__(self):
        HTMLParser.__init__(self)
        self.MyUrls = []
        self.BaseUrl = ""
        self.DisAllowedUrls =[]
        self.IgnoringTypes = ['.css' ,'js','.png','gif']
        self.UrlDelay = 0
        self.DataBaseMaster = DataBase.DataBaseMaster()

    def handle_starttag(self, tag, attrs): # built in function to get sublinks 
        if tag =='a':
            for (key, value) in attrs:
                if key == 'href':
                   NewUrl = parse.urljoin(self.BaseUrl, value)
                   if NewUrl not in self.MyUrls:
                       if not any(imap(NewUrl.__contains__, self.IgnoringTypes)):
                          Allowed = True
                          for j in  self.DisAllowedUrls:
                             if j not in NewUrl:
                                 Allowed = False
                                 break
                          if Allowed:
                             self.MyUrls.append(NewUrl)

    #open a link and get the html data then decode it and retrive only the urls
    def GetLinksFromHtml(self,Url):
        if self.FindDisAllowedUrls(Url) == False:
            return [],False,0
        self.BaseUrl = Url
        OpenedUrl = urlopen(Url)
        HtmlDecodedData = self.GetDecodedData(OpenedUrl)
        if not HtmlDecodedData:
            return [],False,0
        self.SaveHtmlToFile(HtmlDecodedData)
        self.feed(HtmlDecodedData)
        SplittedHtml = re.split('"',HtmlDecodedData)
        for i in SplittedHtml:
            if str(i).startswith("http://") or str(i).startswith("https://"):
                if i not in self.MyUrls:
                     if  not any(imap(i.__contains__, self.IgnoringTypes)):
                         Allowed = True
                         for j in  self.DisAllowedUrls:
                             if j in i:
                                 Allowed = False
                                 break
                         if Allowed:
                            self.MyUrls.append(i)
        return self.MyUrls,True,self.UrlDelay


    def GetDecodedData(self,OpenedUrl):     
        try:
            HtmlEncodedData = OpenedUrl.read()
        except UnicodeDecodeError as Error : 
            return False

        HeaderContents = OpenedUrl.getheader('Content-Type')
        if str(HeaderContents).count('=') < 1 :
            return str(HtmlEncodedData)
        else:
             TempStr = re.split('=',HeaderContents)
             EncodingType = TempStr[1]
             HtmlDecodedData = HtmlEncodedData.decode(EncodingType)
             return str(HtmlDecodedData)


    def  SaveHtmlToFile(self,HtmlEncodedData):
        CurrentDirectory = os.path.dirname(os.path.realpath(__file__))
        FileName = str(self.DataBaseMaster.GetURLID(self.BaseUrl)[0][0]) + '.txt'
        HtmlFilesDirectory = 'MyHtmlFiles'
        FilePath = os.path.join(CurrentDirectory, HtmlFilesDirectory, FileName)
        try:
            NewFile = open(FilePath, 'w+')
            NewFile.write(HtmlEncodedData)
            NewFile.close()
        except IOError:
            print("Wrong path provided")

    def FindDisAllowedUrls(self,Url):
        MainUrl = re.split('/',Url)
        print(MainUrl[2]+'/robots.txt')
        RobotExclusion = urlopen('http://'+MainUrl[2]+'/robots.txt')
        RobotExclusion = self.GetDecodedData(RobotExclusion)
        RobotExclusion = re.split('[\r\n]+',str(RobotExclusion))
        if len(RobotExclusion) < 3:
            return []
        i = 0
        self.DisAllowedUrls = []
        self.UrlDelay = 0
        for i in range(len(RobotExclusion)):
            if RobotExclusion[i] == 'User-Agent: *' or RobotExclusion[i] == 'User-agent: *':
                j = i+1
                while j <len(RobotExclusion):
                    if RobotExclusion[j] == 'Disallow:' or RobotExclusion[j] == 'Allow:/':
                       self.DisAllowedUrls = []
                       return
                    if 'Crawl-delay: ' in RobotExclusion[j]:
                        UrlDelay = RobotExclusion[j][13:]
                    if RobotExclusion[j] == 'Disallow:/':
                        return False
                    if 'Disallow: ' in RobotExclusion[j]:
                        self.DisAllowedUrls.append(RobotExclusion[j][10:])
                    if 'User-Agent:' in RobotExclusion[j] or 'User-agent:' in RobotExclusion[j]:
                        break
                    j = j+1
                    i = i+1
            i = i+1
        self.DisAllowedUrls = self.DisAllowedUrls[0:len(self.DisAllowedUrls)]
        return True
