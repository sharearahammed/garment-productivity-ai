-- =============================================
-- Question 7:
-- Which team has the highest average idle time?
-- =============================================

USE GarmentProductivityDB;
GO

SELECT
    team_no,

    COUNT(*) AS Total_Records,

    AVG(idle_time) AS Avg_Idle_Time,

    MAX(idle_time) AS Max_Idle_Time

FROM ProductionProductivity

GROUP BY team_no

ORDER BY Avg_Idle_Time DESC;
GO