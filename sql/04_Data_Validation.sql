-- =============================================
-- Garment Production Productivity Analysis
-- Data Validation
-- =============================================

USE GarmentProductivityDB;
GO


-- =============================================
-- 1. Total Records
-- =============================================

SELECT
    COUNT(*) AS Total_Records
FROM ProductionProductivity;
GO


-- =============================================
-- 2. Missing Value Check
-- =============================================

SELECT
    COUNT(*) AS Total_Records,

    SUM(CASE WHEN production_date IS NULL THEN 1 ELSE 0 END)
        AS Missing_Date,

    SUM(CASE WHEN quarter IS NULL THEN 1 ELSE 0 END)
        AS Missing_Quarter,

    SUM(CASE WHEN department IS NULL THEN 1 ELSE 0 END)
        AS Missing_Department,

    SUM(CASE WHEN day_name IS NULL THEN 1 ELSE 0 END)
        AS Missing_Day,

    SUM(CASE WHEN team_no IS NULL THEN 1 ELSE 0 END)
        AS Missing_Team,

    SUM(CASE WHEN targeted_productivity IS NULL THEN 1 ELSE 0 END)
        AS Missing_Target,

    SUM(CASE WHEN smv IS NULL THEN 1 ELSE 0 END)
        AS Missing_SMV,

    SUM(CASE WHEN wip IS NULL THEN 1 ELSE 0 END)
        AS Missing_WIP,

    SUM(CASE WHEN over_time IS NULL THEN 1 ELSE 0 END)
        AS Missing_Overtime,

    SUM(CASE WHEN incentive IS NULL THEN 1 ELSE 0 END)
        AS Missing_Incentive,

    SUM(CASE WHEN idle_time IS NULL THEN 1 ELSE 0 END)
        AS Missing_Idle_Time,

    SUM(CASE WHEN idle_men IS NULL THEN 1 ELSE 0 END)
        AS Missing_Idle_Men,

    SUM(CASE WHEN no_of_style_change IS NULL THEN 1 ELSE 0 END)
        AS Missing_Style_Change,

    SUM(CASE WHEN no_of_workers IS NULL THEN 1 ELSE 0 END)
        AS Missing_Workers,

    SUM(CASE WHEN actual_productivity IS NULL THEN 1 ELSE 0 END)
        AS Missing_Actual_Productivity

FROM ProductionProductivity;
GO


-- =============================================
-- 3. Duplicate Check
-- =============================================

SELECT
    production_date,
    department,
    team_no,
    COUNT(*) AS Duplicate_Count
FROM ProductionProductivity
GROUP BY
    production_date,
    department,
    team_no
HAVING COUNT(*) > 1;
GO


-- =============================================
-- 4. Productivity Range Check
-- =============================================

SELECT
    MIN(actual_productivity) AS Minimum_Productivity,
    MAX(actual_productivity) AS Maximum_Productivity,
    AVG(actual_productivity) AS Average_Productivity
FROM ProductionProductivity;
GO


-- =============================================
-- 5. Target Range Check
-- =============================================

SELECT
    MIN(targeted_productivity) AS Minimum_Target,
    MAX(targeted_productivity) AS Maximum_Target,
    AVG(targeted_productivity) AS Average_Target
FROM ProductionProductivity;
GO