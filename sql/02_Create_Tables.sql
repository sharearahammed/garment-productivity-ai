-- =============================================
-- Garment Production Productivity Analysis
-- Table Creation
-- =============================================

USE GarmentProductivityDB;
GO

-- =============================================
-- Main Production Table
-- =============================================

DROP TABLE IF EXISTS ProductionProductivity;
GO

CREATE TABLE ProductionProductivity (
    record_id INT IDENTITY(1,1) PRIMARY KEY,

    production_date DATE,
    quarter VARCHAR(20),
    department VARCHAR(50),
    day_name VARCHAR(20),
    team_no INT,

    targeted_productivity DECIMAL(6,4),
    smv DECIMAL(10,2),
    wip DECIMAL(12,2),

    over_time INT,
    incentive INT,

    idle_time DECIMAL(10,2),
    idle_men INT,

    no_of_style_change INT,
    no_of_workers DECIMAL(10,2),

    actual_productivity DECIMAL(8,6)
);
GO


-- =============================================
-- Staging Table
-- =============================================

DROP TABLE IF EXISTS ProductionProductivity_Staging;
GO

CREATE TABLE ProductionProductivity_Staging (
    date DATE,
    quarter VARCHAR(20),
    department VARCHAR(50),
    day VARCHAR(20),
    team INT,

    targeted_productivity DECIMAL(6,4),
    smv DECIMAL(10,2),
    wip DECIMAL(12,2),

    over_time INT,
    incentive INT,

    idle_time DECIMAL(10,2),
    idle_men INT,

    no_of_style_change INT,
    no_of_workers DECIMAL(10,2),

    actual_productivity DECIMAL(8,6)
);
GO