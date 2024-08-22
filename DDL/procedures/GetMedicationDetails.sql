CREATE PROCEDURE [dbo].[GetMedicationDetails]  (@mrn VARCHAR(50), @date datetime)
AS
BEGIN
    SELECT DISTINCT 
        [ChEMBLID],
        [order_description]
    FROM [Internship].[dbo].[Medication]
    WHERE mrn = @mrn AND Order_DateTime = @date
    ORDER by [ChEMBLID]

END