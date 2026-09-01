-- =============================================
-- Question 6:
-- Which department has the most
-- below-target records?
-- =============================================

USE GarmentProductivityDB;
GO

SELECT
    department,

    COUNT(*) AS Total_Records,

    SUM(
        CASE
            WHEN actual_productivity < targeted_productivity
            THEN 1
            ELSE 0
        END
    ) AS Below_Target_Records,

    CAST(
        100.0 *
        SUM(
            CASE
                WHEN actual_productivity < targeted_productivity
                THEN 1
                ELSE 0
            END
        )
        / COUNT(*)
        AS DECIMAL(5,2)
    ) AS Below_Target_Percentage

FROM ProductionProductivity

GROUP BY department

ORDER BY Below_Target_Percentage DESC;
GO