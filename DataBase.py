import pyodbc

class DataBaseMaster:

	def __init__(self):
        self.Connector = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server};"
                                        "Server=MOHAMMED\SQLEXPRESS;"
                                        "Database=CrawlerDB;"
                                        "Trusted_Connection=yes;")
        self.Curser = self.Connector.cursor()

	def InsertNewUrl(self,URL,status,freq,delay):      
        threading.Lock().acquire()       
        try:
           self.Connector.execute("insert into dbo.Url_Container (URLName,Status,Frequency,CrawlingDelay) values ('%s','%s',%d,%d)" % (Data,status,freq,delay))
           self.Connector.commit()
        except:
          self.Connector.rollback()
        threading.Lock().release
        
	def UpdateURLStatus(self,URL_ID,status):        
        try:
           self.Connector.execute("update Url_Container set Status = '%s' where URL_ID = %d" % (status,URL_ID))
           self.Connector.commit()
        except:
          self.Connector.rollback() 
		  
	def InsertKeyWord(self,Data):        
        try:
           self.Connector.execute("insert into dbo.KeyWords (KeyWords) values ('%s')" % (Data))
           self.Connector.commit()
        except:
          self.Connector.rollback()
		  
	def InsertKeyWordPositionTitle(self,URL_ID,KeyWord_ID,Position):        
        try:
           self.Connector.execute("insert into dbo.KeyWordsPosition_Titles (URL_ID,KeyWord_ID,Position) values (%d,%d,%d)" % (URL_ID,KeyWord_ID,Position))
           self.Connector.commit()
        except:
          self.Connector.rollback()
		  
	def InsertKeyWordPositionHeaders(self,URL_ID,KeyWord_ID,Position):        
        try:
           self.Connector.execute("insert into dbo.KeyWordsPosition_Headers(URL_ID,KeyWord_ID,Position) values (%d,%d,%d)" % (URL_ID,KeyWord_ID,Position))
           self.Connector.commit()
        except:
          self.Connector.rollback()
		  
	def InsertKeyWordPositionParagraph(self,URL_ID,KeyWord_ID,Position):        
        try:
           self.Connector.execute("insert into dbo.KeyWordsPosition_Paragraphs(URL_ID,KeyWord_ID,Position) values (%d,%d,%d)" % (URL_ID,KeyWord_ID,Position))
           self.Connector.commit()
        except:
          self.Connector.rollback()
		  
	def InsertImageKeyWord(self,Data):        
        try:
           self.Connector.execute("insert into dbo.ImageKeyWords (ImageKeyWords) values ('%s')" % (Data))
           self.Connector.commit()
        except:
          self.Connector.rollback()
	
	def InsertImageWordLocationURL(self,URL_ID,ImageKeyWord_ID,ImageURL):        
        try:
           self.Connector.execute("insert into dbo.ImageWordLocationURL(URL_ID,ImageKeyWord_ID,ImageURL) values (%d,%d,'%s')" % (URL_ID,ImageKeyWord_ID,ImageURL))
           self.Connector.commit()
        except:
          self.Connector.rollback()
	
	def GetURLID(self,Url):
        threading.Lock().acquire() 
        try:
            self.Curser.execute("Select File_ID from Url_Container where FileNname = ('%s')" % (Url))
            result = self.Curser.fetchall()
            self.Connector.commit()
            return result
        except:
            self.Connector.rollback()  
        threading.Lock().acquire() 
	
	def CloseConnection(self):
        self.Connector.close()
        
       #self.Curser.execute("Select u.File_ID,FileName,Position from Url_Container u,KeyWords w, KeyWord_File_Position kwp where w.Word_ID = kwp.Word_ID and u.File_ID = kwp.File_ID and Word = '%s'" % (Word))
#Get URLID given word       "select URL_ID from Url_Container where URLName = '%s'"
#Get KeyWordID given word   "select KeyWord_ID from KeyWords where KeyWords = '%s'"
#Get ImageKeyWord_ID given  "select ImageKeyWord_ID from ImageKeyWords where ImageKeyWords = '%s'"
#Update URL_Container ID    "update Url_Container set Status = '%s' where URL_ID = %d"
