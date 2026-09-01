-- =============================================
-- Question 1:
-- Which department has the highest
-- average productivity?
-- =============================================

USE GarmentProductivityDB;
GO

SELECT
    department,
    COUNT(*) AS Total_Records,
    AVG(actual_productivity) AS Avg_Productivity
FROM ProductionProductivity
GROUP BY department
ORDER BY Avg_Productivity DESC;
GO