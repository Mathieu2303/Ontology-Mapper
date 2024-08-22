CREATE PROCEDURE [dbo].[GetTumorDetailsByMRN] (@mrn VARCHAR(50))
AS

    SELECT 
        [Histology_Text],
		[Behavior_Description],
		[Laterality_Description],
		[Primary_Site_Text],
		[Primary_Site_ICDO3],
		[Histology_ICDO3]
    FROM [Internship].[dbo].[Tumor]
    WHERE mrn = @mrn
GO