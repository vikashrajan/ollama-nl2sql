-- Use your target database
USE weather;
GO

-- Drop if exists (optional)
IF OBJECT_ID('dbo.WeatherData', 'U') IS NOT NULL
    DROP TABLE dbo.WeatherData;
GO

-- Create WeatherData table
CREATE TABLE WeatherData (
    ID INT IDENTITY PRIMARY KEY,
    City NVARCHAR(100),
    Country NVARCHAR(100),
    Temperature FLOAT,
    Humidity INT,
    Pressure INT,
    WeatherDescription NVARCHAR(100),
    ObservationTime DATETIME
);
GO
