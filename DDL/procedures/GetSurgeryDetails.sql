CREATE PROCEDURE [dbo].[GetSurgeryDetails] 
(@mrn VARCHAR(50))
AS
BEGIN
    SELECT DISTINCT 
        [procedure]
    FROM [Internship].[dbo].[Surgery]
    WHERE mrn = @mrn

END