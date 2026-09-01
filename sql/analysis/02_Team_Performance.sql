-- =============================================
-- Question 2:
-- Which team performs the best?
-- =============================================

USE GarmentProductivityDB;
GO

SELECT
    team_no,
    COUNT(*) AS Total_Records,
    AVG(actual_productivity) AS Avg_Productivity
FROM ProductionProductivity
GROUP BY team_no
ORDER BY Avg_Productivity DESC;
GO