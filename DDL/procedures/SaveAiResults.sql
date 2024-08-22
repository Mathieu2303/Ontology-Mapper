CREATE PROCEDURE [dbo].[SaveAiResults] (@mrn varchar(50), @category varchar(50), @ai_result varchar(max))
AS 
BEGIN
    INSERT into results (mrn, category, ai_result,[date]) 
    values (@mrn, @category, @ai_result, getdate())
	
END
GO