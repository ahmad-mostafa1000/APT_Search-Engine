import pyodbc
import threading
import threading

class DataBaseMaster:

    def __init__(self):

        self.Connector = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server};"
                                        "Server=MUSGI\MYSQLSERVER;"
                                        "Database=SearchEngineDB;"
                                        "Trusted_Connection=yes;")
        self.Curser = self.Connector.cursor()
        self.threadLock = threading.Lock()

    def InsertNewUrl(self,URL,status,freq,delay):      
        self.threadLock.acquire()       
        try:
           self.Connector.execute("insert into dbo.Url_Container (URLName,Status,Frequency,CrawlingDelay) values ('%s','%s',%d,%d)" % (URL,status,freq,delay))
           self.Connector.commit()
        except:
          self.Connector.rollback()
        self.threadLock.release()

    def URLDoesExist(self,Data):
        self.threadLock.acquire() 
        self.Curser.execute("Select URLName from Url_Container where URLName = ('%s')" % (Data))
        data = self.Curser.fetchone()
        if data:
            return True
        else :
            return False
        self.threadLock.release() 

    def KeyWordDoesExist(self,Data):
        self.Curser.execute("Select Word from KeyWords where Word = ('%s')" % (Data))
        data = self.Curser.fetchone()
        if data:
            return True
        else :
            return False

    def GetURLIDByStatus(self,status):
        try:
            self.Curser.execute("Select URL_ID,URLName from Url_Container where Status = ('%s')" % (status))
            result = self.Curser.fetchall()
            self.Connector.commit()
            return result
        except:
            self.Connector.rollback()     
        

    def GetURLID(self,Url):
        self.threadLock.acquire() 
        try:
            self.Curser.execute("Select URL_ID from Url_Container where URLName = ('%s')" % (Url))
            result = self.Curser.fetchall()
            self.Connector.commit()
            return result
        except:
            self.Connector.rollback()  
        self.threadLock.release() 

    def UpdateURLStatus(self,status,Url):
        self.threadLock.acquire() 
        try:
            self.Curser.execute("update Url_Container set status='%s' where URLName = ('%s')" % (status,Url))
            self.Connector.commit()
        except:
            self.Connector.rollback() 
        self.threadLock.release() 

    def InsertKeyWord(self,Data):
        try:
            self.Curser.execute("Insert into KeyWords (Word) values ('%s')" % (Data))
            self.Connector.commit()
        except:
            self.Connector.rollback()

    def GetWordID(self,Data):
        try:
            self.Curser.execute("Select Word_ID from KeyWords where word = ('%s')" % (Data))
            result = self.Curser.fetchall()
            self.Connector.commit()
            return result
        except:
            self.Connector.rollback()

    def InsertKeyWordFilePosition(self,WordID,FileID,Position):
        try:
            self.Curser.execute("Insert into KeyWord_File_Position(Word_ID,File_ID,Position) values ('%d','%d','%d')" % (WordID,FileID,Position))
            self.Connector.commit()
        except:
            self.Connector.rollback()

      #self.Curser.execute("Select u.File_ID,FileName,Position from Url_Container u,KeyWords w, KeyWord_File_Position kwp where w.Word_ID = kwp.Word_ID and u.File_ID = kwp.File_ID and Word = '%s'" % (Word))
       

    

    def CloseConnection(self):
        self.Connector.close()
