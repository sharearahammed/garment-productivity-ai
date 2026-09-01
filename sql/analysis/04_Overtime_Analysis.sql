-- =============================================
-- Question 4:
-- What is the relationship between
-- overtime and productivity?
-- =============================================

USE GarmentProductivityDB;
GO

SELECT
    CASE
        WHEN over_time = 0 THEN 'No Overtime'
        WHEN over_time <= 1000 THEN 'Low Overtime'
        WHEN over_time <= 3000 THEN 'Medium Overtime'
        ELSE 'High Overtime'
    END AS Overtime_Category,

    COUNT(*) AS Total_Records,

    AVG(actual_productivity) AS Avg_Productivity

FROM ProductionProductivity

GROUP BY
    CASE
        WHEN over_time = 0 THEN 'No Overtime'
        WHEN over_time <= 1000 THEN 'Low Overtime'
        WHEN over_time <= 3000 THEN 'Medium Overtime'
        ELSE 'High Overtime'
    END

ORDER BY Avg_Productivity DESC;
GO