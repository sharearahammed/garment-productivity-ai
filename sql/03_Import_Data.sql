-- =============================================
-- Garment Production Productivity Analysis
-- Import / Transform Data
-- =============================================

USE GarmentProductivityDB;
GO


-- Check raw data
SELECT COUNT(*) AS Raw_Row_Count
FROM [Garments_Production_Raw.csv];
GO


-- =============================================
-- Insert Raw Data into Main Production Table
-- =============================================

INSERT INTO ProductionProductivity (
    production_date,
    quarter,
    department,
    day_name,
    team_no,
    targeted_productivity,
    smv,
    wip,
    over_time,
    incentive,
    idle_time,
    idle_men,
    no_of_style_change,
    no_of_workers,
    actual_productivity
)
SELECT
    date,
    quarter,
    department,
    day,
    team,
    targeted_productivity,
    smv,
    wip,
    over_time,
    incentive,
    idle_time,
    idle_men,
    no_of_style_change,
    no_of_workers,
    actual_productivity
FROM [Garments_Production_Raw.csv];
GO


-- =============================================
-- Verify Import
-- =============================================

SELECT COUNT(*) AS Production_Row_Count
FROM ProductionProductivity;
GO