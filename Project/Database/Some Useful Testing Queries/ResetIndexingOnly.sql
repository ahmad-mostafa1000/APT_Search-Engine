use SearchEngN
go

delete KeyWordLocationURL
delete KeyWordsPosition_Headers
delete KeyWordsPosition_Titles
delete KeyWordsPosition_Paragraphs

delete ImageKeyWords
delete KeyWords


DBCC CHECKIDENT ('[KeyWordLocationURL]', RESEED, 0);
GO
GO
DBCC CHECKIDENT ('[KeyWordsPosition_Headers]', RESEED, 0);
GO
DBCC CHECKIDENT ('[KeyWordsPosition_Titles]', RESEED, 0);
GO
DBCC CHECKIDENT ('[KeyWordsPosition_Paragraphs]', RESEED, 0);
GO
DBCC CHECKIDENT ('[ImageKeyWords]', RESEED, 0);
GO
DBCC CHECKIDENT ('[KeyWords]', RESEED, 0);
GO

Update Url_Container set Status = 'C' where Status = 'Q' or Status = 'I'