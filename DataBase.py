import pyodbc

class DataBaseMaster:

    def __init__(self):

        self.Connector = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server};"
                                        "Server=MUSGI\MYSQLSERVER;"
                                        "Database=CrawlerDB;"
                                        "Trusted_Connection=yes;")
        self.Curser = self.Connector.cursor()

    def InsertNewUrl(self,Data):
        
        try:
           self.Connector.execute("INSERT INTO Url_Container VALUES ('%s')" % (Data))
           self.Connector.commit()
        except:
          self.Connector.rollback()

    def RemoveUrl(self,Data):
        try:
           self.Connector.execute("Delete from Url_Container where FileName = ('%s')" % (Data))
           self.Connector.commit()
        except:
          self.Connector.rollback()

    def DoesExist(self,Data):

        if self.Connector.execute("Select FileName from Url_Container where FileName = ('%s')" % (Data)):
            return True
        else :
            return False

    def IsUrlVisited(self,Data):
         if self.Connector.execute("Select FileName from Visited__Urls where FileName = ('%s')" % (Data)):
            return True
         else :
            return False

    def CloseConnection(self):
        self.Connector.close()
