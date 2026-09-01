-- =============================================
-- Question 3:
-- What percentage of records achieved
-- the targeted productivity?
-- =============================================

USE GarmentProductivityDB;
GO

SELECT
    COUNT(*) AS Total_Records,

    SUM(
        CASE
            WHEN actual_productivity >= targeted_productivity
            THEN 1
            ELSE 0
        END
    ) AS Achieved_Records,

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
                WHEN actual_productivity >= targeted_productivity
                THEN 1
                ELSE 0
            END
        )
        / COUNT(*)
        AS DECIMAL(5,2)
    ) AS Achievement_Percentage

FROM ProductionProductivity;
GO