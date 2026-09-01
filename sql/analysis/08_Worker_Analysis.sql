-- =============================================
-- Question 8:
-- Which department has the highest
-- average number of workers?
-- =============================================

USE GarmentProductivityDB;
GO

SELECT
    department,

    COUNT(*) AS Total_Records,

    AVG(no_of_workers) AS Avg_Workers,

    MAX(no_of_workers) AS Max_Workers

FROM ProductionProductivity

GROUP BY department

ORDER BY Avg_Workers DESC;
GO