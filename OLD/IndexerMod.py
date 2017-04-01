from nltk.stem.porter import * 
import DataBase
from urllib.request import urlopen
from bs4 import *
import os
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
                #File_ID = int(Result[0][0]) 
                File_ID = '1'
                FilePath = os.path.join(self.FilesLocation,File_ID + '.txt') 
                HtmlData = open(FilePath,"r")
                #HtmlData = open("1.txt","r")
                Title ,Headers, Paragraphs = self.GetTextFromHtml(HtmlData)

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
                        self.DataBaseMaster.InsertKeyWordPositionTitle(File_ID,Word_ID,HeaderPosition)
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
            else :
                break


    def GetTextFromHtml(self,HtmlData):
        MySoup =  BeautifulSoup(HtmlData, 'html.parser')
        PageTitleTemp = MySoup.find('title').string
        PageTitle = re.split('[ \'.,;]',j.PageTitleTemp)
        Texts = []
        Headers = []
        for i in self.Tags:
            Paragraph = MySoup.findAll(i) 
            for j in Paragraph:
                if j.string :
                   SplittedWords = re.split('[ \'.,;]',j.string)
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
        return PageTitle ,Headers,Texts



