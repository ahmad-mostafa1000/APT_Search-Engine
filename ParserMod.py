from urllib.request import urlopen
from html.parser import HTMLParser    
from urllib import parse
import re

class Parser(HTMLParser):


    def __init__(self):
        HTMLParser.__init__(self)
        self.MyUrls = []
        self.BaseUrl = ""


    def handle_starttag(self, tag, attrs): # built in function to get sublinks 
        if tag =='a':
            for (key, value) in attrs:
                if key == 'href':
                   NewUrl = parse.urljoin(self.BaseUrl, value)
                   if NewUrl not in self.MyUrls:
                      self.MyUrls.append(NewUrl)

    #open a link and get the html data then decode it and retrive only the urls
    def GetLinksFromHtml(self,Url):
        self.BaseUrl = Url
        OpenedUrl = urlopen(Url)
        HtmlDecodedData = self.GetDecodedData(OpenedUrl)
        self.feed(HtmlDecodedData)
        SplittedHtml = re.split('"',HtmlDecodedData)
        for i in SplittedHtml:
            if str(i).startswith("http://") or str(i).startswith("https://"):
                if i not in self.MyUrls:
                    self.MyUrls.append(i)
        for i in  self.MyUrls:
            print(i)


    def GetDecodedData(self,OpenedUrl):      
        HtmlEncodedData = OpenedUrl.read()
        HeaderContents = OpenedUrl.getheader('Content-Type')
        if str(HeaderContents).count('=') < 1 :
            return str(HtmlEncodedData)
        else:
             TempStr = re.split('=',HeaderContents)
             EncodingType = TempStr[1]
             HtmlDecodedData = HtmlEncodedData.decode(EncodingType)
             return str(HtmlDecodedData)


