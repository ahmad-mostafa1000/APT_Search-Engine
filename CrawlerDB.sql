USE [master]
GO
/****** Object:  Database [CrawlerDB]    Script Date: 28-Mar-17 2:02:21 AM ******/
CREATE DATABASE [CrawlerDB]
ALTER DATABASE [CrawlerDB] SET COMPATIBILITY_LEVEL = 120
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [CrawlerDB].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [CrawlerDB] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [CrawlerDB] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [CrawlerDB] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [CrawlerDB] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [CrawlerDB] SET ARITHABORT OFF 
GO
ALTER DATABASE [CrawlerDB] SET AUTO_CLOSE OFF 
GO
ALTER DATABASE [CrawlerDB] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [CrawlerDB] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [CrawlerDB] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [CrawlerDB] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [CrawlerDB] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [CrawlerDB] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [CrawlerDB] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [CrawlerDB] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [CrawlerDB] SET  DISABLE_BROKER 
GO
ALTER DATABASE [CrawlerDB] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [CrawlerDB] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [CrawlerDB] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [CrawlerDB] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [CrawlerDB] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [CrawlerDB] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [CrawlerDB] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [CrawlerDB] SET RECOVERY SIMPLE 
GO
ALTER DATABASE [CrawlerDB] SET  MULTI_USER 
GO
ALTER DATABASE [CrawlerDB] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [CrawlerDB] SET DB_CHAINING OFF 
GO
ALTER DATABASE [CrawlerDB] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [CrawlerDB] SET TARGET_RECOVERY_TIME = 0 SECONDS 
GO
ALTER DATABASE [CrawlerDB] SET DELAYED_DURABILITY = DISABLED 
GO
USE [CrawlerDB]
GO
/****** Object:  Table [dbo].[ImageKeyWords]    Script Date: 28-Mar-17 2:02:21 AM ******/
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
/****** Object:  Table [dbo].[ImageWordLocationURL]    Script Date: 28-Mar-17 2:02:21 AM ******/
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
/****** Object:  Table [dbo].[KeyWords]    Script Date: 28-Mar-17 2:02:21 AM ******/
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
/****** Object:  Table [dbo].[KeyWordsPosition_Headers]    Script Date: 28-Mar-17 2:02:21 AM ******/
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
/****** Object:  Table [dbo].[KeyWordsPosition_Paragraphs]    Script Date: 28-Mar-17 2:02:21 AM ******/
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
/****** Object:  Table [dbo].[KeyWordsPosition_Titles]    Script Date: 28-Mar-17 2:02:21 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[KeyWordsPosition_Titles](
	[ID] [int] NOT NULL,
	[URL_ID] [int] IDENTITY(1,1) NOT NULL,
	[KeyWord_ID] [int] NOT NULL,
	[Position] [int] NOT NULL,
 CONSTRAINT [PK_KeyWordsPosition_Titles] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
/****** Object:  Table [dbo].[Url_Container]    Script Date: 28-Mar-17 2:02:21 AM ******/
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
ALTER TABLE [dbo].[Url_Container]  WITH CHECK ADD  CONSTRAINT [FK_Url_Container_KeyWordsPosition_Titles] FOREIGN KEY([URL_ID])
REFERENCES [dbo].[KeyWordsPosition_Titles] ([ID])
GO
ALTER TABLE [dbo].[Url_Container] CHECK CONSTRAINT [FK_Url_Container_KeyWordsPosition_Titles]
GO
USE [master]
GO
ALTER DATABASE [CrawlerDB] SET  READ_WRITE 
GO
