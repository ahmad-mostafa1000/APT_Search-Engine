from nltk.stem.porter import * 
import DataBase
from urllib.request import urlopen
from bs4 import *
import os

import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='bs4')

class Indexer:
    def __init__(self):
        self.StoppingWords =  re.split('\n',open('StoppingWords.txt','r').read())
        self.Porter = PorterStemmer()
        self.DataBaseMaster = DataBase.DataBaseMaster()
        self.FilesLocation = self.GetFilesLocationDirectory()
        self.Soup = BeautifulSoup()
        self.Tags = ["h1","h2","h3","h4","h5","h6","br","p","pre"]

    def GetFilesLocationDirectory(self):
        CurrentDirectory = os.path.dirname(os.path.realpath(__file__))
        HtmlFilesDirectory = 'MyHtmlFiles'
        FilesLocation = os.path.join(CurrentDirectory, HtmlFilesDirectory)
        return FilesLocation

    def StartIndexing(self):
        while True :
            Position = 0
            TitlePosition=0
            HeaderPosition =0
            Result = self.DataBaseMaster.GetURLIDByStatus('C')
            if Result:
                File_ID = int(Result[0][0]) 
                #File_ID = '1'
                FilePath = os.path.join(self.FilesLocation,str(File_ID) + '.html')
                try:
                    #HtmlData = open(FilePath,"r")
                    HtmlData = str(self.DataBaseMaster.GetHTMLdata(File_ID))
                    l = len(HtmlData)
                except:
                    print ("EXCEPTION IN FILE " + str(File_ID) + ", CANT OPEN: DELETEING FROM DATABASE!")
                    #self.DataBaseMaster.DeleteURLbyID(File_ID);
                    self.DataBaseMaster.UpdateURLStatus('D',File_ID)
                    continue
                #HtmlData = HtmlData.replace('class="srow bigbox container mi-df-local locked-single"', 'class="row bigbox container mi-df-local single-local"') #K
                #HtmlData = open("1.txt","r")
                Title ,Headers, Paragraphs = self.GetTextFromHtml(HtmlData, File_ID)
                if Title == []:
                    continue

                for word in Title:
                    word = word.lower()
                    if word not in self.StoppingWords:
                        stemedWord = self.Porter.stem(word)
                        if not self.DataBaseMaster.KeyWordDoesExist(stemedWord):
                            self.DataBaseMaster.InsertKeyWord(stemedWord)
                        Result2 = self.DataBaseMaster.GetWordID(stemedWord)
                        Word_ID = int(Result2[0][0])
                        self.DataBaseMaster.InsertKeyWordPositionTitle(File_ID,Word_ID,TitlePosition)
                        TitlePosition = TitlePosition + 1

                for word in Headers:
                    word = word.lower()
                    if word not in self.StoppingWords:
                        stemedWord = self.Porter.stem(word)
                        if not self.DataBaseMaster.KeyWordDoesExist(stemedWord):
                            self.DataBaseMaster.InsertKeyWord(stemedWord)
                        Result2 = self.DataBaseMaster.GetWordID(stemedWord)
                        Word_ID = int(Result2[0][0])
                        self.DataBaseMaster.InsertKeyWordPositionHeaders(File_ID,Word_ID,HeaderPosition)
                        HeaderPosition = HeaderPosition + 1

                for word in Paragraphs:
                    word = word.lower()
                    if word not in self.StoppingWords:
                        stemedWord = self.Porter.stem(word)
                        if not self.DataBaseMaster.KeyWordDoesExist(stemedWord):
                            self.DataBaseMaster.InsertKeyWord(stemedWord)
                        Result2 = self.DataBaseMaster.GetWordID(stemedWord)
                        Word_ID = int(Result2[0][0])
                        self.DataBaseMaster.InsertKeyWordPositionParagraph(File_ID,Word_ID,Position)
                        Position = Position + 1


                self.DataBaseMaster.UpdateURLStatus('I', File_ID)
                print("INDEXED FILE: " + str(File_ID))
            #else :
                #print("FINISHED ALL THE SITES PLEASE ADD MORE")


    def GetTextFromHtml(self,HtmlData, File_ID):
        MySoup =  BeautifulSoup(HtmlData)
        PageTitle=[]
        Texts = []
        Headers = []
        regex = re.compile('[^a-zA-Z \n]')

        try:
            PageTitleTemp = MySoup.find('title').string
            PageTitle = regex.sub(' ',PageTitleTemp)
            PageTitle = re.split('([\t\s\n\r])|x[a-zA-Z]*', PageTitle)

        except:
            print ("EXCEPTION IN FILE " + str(File_ID) + ", NO TITLE: DELETEING FROM DATABASE!")
            #self.DataBaseMaster.DeleteURLbyID(File_ID);
            self.DataBaseMaster.UpdateURLStatus('D',File_ID)
            return PageTitle ,Headers,Texts


        for i in self.Tags:
            Paragraph = MySoup.findAll(i) 
            for j in Paragraph:
                if j.string :
                   SplittedWords = regex.sub('', j.string)
                   SplittedWords = re.split('([\t\s\n\r])|x[a-zA-Z]*', SplittedWords)
                   if len(SplittedWords) >1:
                       for k in SplittedWords:
                           if i[0] == 'h':
                               Headers.append(k)
                           else:
                               Texts.append(k)
                   else:
                        if i[0] == 'h':
                            Headers.append(j.string)
                        else:
                            Texts.append(j.string)
        PageTitle = list(filter(None, PageTitle))
        Headers = list(filter(None, Headers))
        Texts = list(filter(None, Texts))
        return PageTitle ,Headers,Texts