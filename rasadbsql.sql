USE ChatBot_Rasa
GO

IF OBJECT_ID(N'dbo.Major', N'U') IS NOT NULL
   DROP TABLE [dbo].Major;  
GO
IF OBJECT_ID(N'dbo.Subject', N'U') IS NOT NULL  
   DROP TABLE [dbo].Subject;  
GO

CREATE TABLE Major(
	Id nvarchar(255) NOT NULL PRIMARY KEY,
	Name nvarchar(255) NOT NULL,
	Alias nvarchar(255)
);

CREATE TABLE Subject(
	Id_Major nvarchar(255) NOT NULL FOREIGN KEY REFERENCES Major(Id),
	Id nvarchar(255) NOT NULL PRIMARY KEY,
	Name nvarchar(255) NOT NULL,
	Credit int NOT NULL,
	Condition_Subject nvarchar(255),
	Condition_Term int,
	Term int NOT NULL,
	Semester int,
	Year int,
	Alias nvarchar(255)
);