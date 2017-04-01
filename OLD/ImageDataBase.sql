USE [CrawlerDB]
GO
/****** Object:  Table [dbo].[ImageKeyWords]    Script Date: 3/30/2017 10:02:14 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ImageKeyWords](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[ImageKeyWords] [nvarchar](max) NOT NULL,
 CONSTRAINT [PK_ImageKeyWords] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]

GO
/****** Object:  Table [dbo].[ImageNames]    Script Date: 3/30/2017 10:02:14 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ImageNames](
	[ImageFile_ID] [int] IDENTITY(1,1) NOT NULL,
	[ImageFileName] [nvarchar](max) NOT NULL,
 CONSTRAINT [PK_ImageNames] PRIMARY KEY CLUSTERED 
(
	[ImageFile_ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]

GO
/****** Object:  Table [dbo].[KeyWordLocationURL]    Script Date: 3/30/2017 10:02:14 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[KeyWordLocationURL](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[URL_ID] [int] NOT NULL,
	[ImageKeyWords_ID] [int] NOT NULL,
	[ImageURL] [nvarchar](max) NOT NULL,
 CONSTRAINT [PK_kljhklj] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]

GO
