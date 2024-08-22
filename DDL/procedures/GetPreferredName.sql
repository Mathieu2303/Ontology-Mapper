CREATE PROCEDURE [dbo].[GetPreferredName]
(@prefered_term  VARCHAR(50))
AS
BEGIN
    SELECT DISTINCT 
        [chembl_id]
    FROM [Internship].[dbo].[medication_Ontology]
    WHERE prefered_term = @prefered_term

END