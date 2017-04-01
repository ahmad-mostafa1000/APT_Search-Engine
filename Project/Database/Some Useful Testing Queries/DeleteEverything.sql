delete KeyWordLocationURL
delete KeyWordsPosition_Headers
delete KeyWordsPosition_Titles
delete KeyWordsPosition_Paragraphs

delete HtmlData

use SearchEngN
go

delete ImageNames
delete ImageKeyWords
delete KeyWords
delete Url_Container

DBCC CHECKIDENT ('[ImageWordLocationURL]', RESEED, 0);
GO
DBCC CHECKIDENT ('[KeyWordsPosition_Headers]', RESEED, 0);
GO
DBCC CHECKIDENT ('[KeyWordsPosition_Titles]', RESEED, 0);
GO
DBCC CHECKIDENT ('[KeyWordsPosition_Paragraphs]', RESEED, 0);
GO
DBCC CHECKIDENT ('[HtmlData]', RESEED, 0);
GO
DBCC CHECKIDENT ('[ImageKeyWords]', RESEED, 0);
GO
DBCC CHECKIDENT ('[KeyWords]', RESEED, 0);
GO
DBCC CHECKIDENT ('[Url_Container]', RESEED, 0);
GO

insert into Url_Container values ('http://moz.com/top500','N',0)