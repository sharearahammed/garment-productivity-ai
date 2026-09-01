-- =============================================
-- Question 5:
-- Does higher incentive relate to
-- higher productivity?
-- =============================================

USE GarmentProductivityDB;
GO

SELECT
    CASE
        WHEN incentive = 0 THEN 'No Incentive'
        WHEN incentive <= 25 THEN 'Low Incentive'
        WHEN incentive <= 50 THEN 'Medium Incentive'
        ELSE 'High Incentive'
    END AS Incentive_Category,

    COUNT(*) AS Total_Records,

    AVG(actual_productivity) AS Avg_Productivity

FROM ProductionProductivity

GROUP BY
    CASE
        WHEN incentive = 0 THEN 'No Incentive'
        WHEN incentive <= 25 THEN 'Low Incentive'
        WHEN incentive <= 50 THEN 'Medium Incentive'
        ELSE 'High Incentive'
    END

ORDER BY Avg_Productivity DESC;
GO