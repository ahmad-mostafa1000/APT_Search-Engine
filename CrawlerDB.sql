USE [CrawlerDB]
GO
/****** Object:  Table [dbo].[ImageKeyWords]    Script Date: 28-Mar-17 3:55:05 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ImageKeyWords](
	[ImageKeyWord_ID] [int] IDENTITY(1,1) NOT NULL,
	[ImageKeyWords] [nvarchar](max) NOT NULL,
 CONSTRAINT [PK_ImageKeyWords] PRIMARY KEY CLUSTERED 
(
	[ImageKeyWord_ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]

GO
/****** Object:  Table [dbo].[ImageWordLocationURL]    Script Date: 28-Mar-17 3:55:05 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ImageWordLocationURL](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[URL_ID] [int] NOT NULL,
	[ImageKeyWord_ID] [int] NOT NULL,
	[ImageURL] [nvarchar](max) NOT NULL,
 CONSTRAINT [PK_ImageWordLocationURL] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]

GO
/****** Object:  Table [dbo].[KeyWords]    Script Date: 28-Mar-17 3:55:05 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[KeyWords](
	[KeyWord_ID] [int] IDENTITY(1,1) NOT NULL,
	[KeyWords] [nvarchar](max) NOT NULL,
 CONSTRAINT [PK_KeyWords] PRIMARY KEY CLUSTERED 
(
	[KeyWord_ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]

GO
/****** Object:  Table [dbo].[KeyWordsPosition_Headers]    Script Date: 28-Mar-17 3:55:05 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[KeyWordsPosition_Headers](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[URL_ID] [int] NOT NULL,
	[KeyWord_ID] [int] NOT NULL,
	[Position] [int] NOT NULL,
 CONSTRAINT [PK_KeyWordsPosition_Headers] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
/****** Object:  Table [dbo].[KeyWordsPosition_Paragraphs]    Script Date: 28-Mar-17 3:55:05 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[KeyWordsPosition_Paragraphs](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[URL_ID] [int] NOT NULL,
	[KeyWord_ID] [int] NOT NULL,
	[Position] [int] NOT NULL,
 CONSTRAINT [PK_KeyWordsPosition_Paragraphs] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
/****** Object:  Table [dbo].[KeyWordsPosition_Titles]    Script Date: 28-Mar-17 3:55:05 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[KeyWordsPosition_Titles](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[URL_ID] [int] NOT NULL,
	[KeyWord_ID] [int] NOT NULL,
	[Position] [int] NOT NULL,
 CONSTRAINT [PK_KeyWordsPosition_Titles] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
/****** Object:  Table [dbo].[Url_Container]    Script Date: 28-Mar-17 3:55:05 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [dbo].[Url_Container](
	[URL_ID] [int] IDENTITY(1,1) NOT NULL,
	[URLName] [nvarchar](max) NOT NULL,
	[Status] [char](1) NOT NULL,
	[Frequency] [int] NOT NULL,
 CONSTRAINT [PK_Url_Container] PRIMARY KEY CLUSTERED 
(
	[URL_ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]

GO
SET ANSI_PADDING OFF
GO
ALTER TABLE [dbo].[Url_Container] ADD  CONSTRAINT [DF_Url_Container_Status]  DEFAULT ('N') FOR [Status]
GO
ALTER TABLE [dbo].[ImageWordLocationURL]  WITH CHECK ADD  CONSTRAINT [FK_ImageWordLocationURL_ImageKeyWords] FOREIGN KEY([ImageKeyWord_ID])
REFERENCES [dbo].[ImageKeyWords] ([ImageKeyWord_ID])
GO
ALTER TABLE [dbo].[ImageWordLocationURL] CHECK CONSTRAINT [FK_ImageWordLocationURL_ImageKeyWords]
GO
ALTER TABLE [dbo].[ImageWordLocationURL]  WITH CHECK ADD  CONSTRAINT [FK_ImageWordLocationURL_Url_Container] FOREIGN KEY([URL_ID])
REFERENCES [dbo].[Url_Container] ([URL_ID])
GO
ALTER TABLE [dbo].[ImageWordLocationURL] CHECK CONSTRAINT [FK_ImageWordLocationURL_Url_Container]
GO
ALTER TABLE [dbo].[KeyWordsPosition_Headers]  WITH CHECK ADD  CONSTRAINT [FK_KeyWordsPosition_Headers_KeyWords] FOREIGN KEY([KeyWord_ID])
REFERENCES [dbo].[KeyWords] ([KeyWord_ID])
GO
ALTER TABLE [dbo].[KeyWordsPosition_Headers] CHECK CONSTRAINT [FK_KeyWordsPosition_Headers_KeyWords]
GO
ALTER TABLE [dbo].[KeyWordsPosition_Headers]  WITH CHECK ADD  CONSTRAINT [FK_KeyWordsPosition_Headers_Url_Container] FOREIGN KEY([URL_ID])
REFERENCES [dbo].[Url_Container] ([URL_ID])
GO
ALTER TABLE [dbo].[KeyWordsPosition_Headers] CHECK CONSTRAINT [FK_KeyWordsPosition_Headers_Url_Container]
GO
ALTER TABLE [dbo].[KeyWordsPosition_Paragraphs]  WITH CHECK ADD  CONSTRAINT [FK_KeyWordsPosition_Paragraphs_KeyWords] FOREIGN KEY([KeyWord_ID])
REFERENCES [dbo].[KeyWords] ([KeyWord_ID])
GO
ALTER TABLE [dbo].[KeyWordsPosition_Paragraphs] CHECK CONSTRAINT [FK_KeyWordsPosition_Paragraphs_KeyWords]
GO
ALTER TABLE [dbo].[KeyWordsPosition_Paragraphs]  WITH CHECK ADD  CONSTRAINT [FK_KeyWordsPosition_Paragraphs_Url_Container] FOREIGN KEY([URL_ID])
REFERENCES [dbo].[Url_Container] ([URL_ID])
GO
ALTER TABLE [dbo].[KeyWordsPosition_Paragraphs] CHECK CONSTRAINT [FK_KeyWordsPosition_Paragraphs_Url_Container]
GO
ALTER TABLE [dbo].[KeyWordsPosition_Titles]  WITH CHECK ADD  CONSTRAINT [FK_KeyWordsPosition_Titles_KeyWords] FOREIGN KEY([KeyWord_ID])
REFERENCES [dbo].[KeyWords] ([KeyWord_ID])
GO
ALTER TABLE [dbo].[KeyWordsPosition_Titles] CHECK CONSTRAINT [FK_KeyWordsPosition_Titles_KeyWords]
GO
ALTER TABLE [dbo].[KeyWordsPosition_Titles]  WITH CHECK ADD  CONSTRAINT [FK_KeyWordsPosition_Titles_Url_Container] FOREIGN KEY([URL_ID])
REFERENCES [dbo].[Url_Container] ([URL_ID])
GO
ALTER TABLE [dbo].[KeyWordsPosition_Titles] CHECK CONSTRAINT [FK_KeyWordsPosition_Titles_Url_Container]
GO
