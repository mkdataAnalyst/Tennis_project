CREATE DATABASE Tennis;
USE Tennis;


-- Create Categories Table
CREATE TABLE Categories (
    category_id VARCHAR(50) PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL
);

-- Create Competitions Table
CREATE TABLE Competitions (
    competition_id VARCHAR(50) PRIMARY KEY,
    competition_name VARCHAR(100) NOT NULL,
    parent_id VARCHAR(50),
    type VARCHAR(20) NOT NULL,
    gender VARCHAR(10) NOT NULL,
    category_id VARCHAR(50),
    FOREIGN KEY (category_id) REFERENCES Categories(category_id)
);

-- List all competitions along with their category name
SELECT c.competition_id, c.competition_name, cat.category_name
FROM Competitions c
JOIN Categories cat ON c.category_id = cat.category_id;


--- Count the number of competitions in each category
SELECT cat.category_name, COUNT(*) AS competition_count
FROM Competitions c
JOIN Categories cat ON c.category_id = cat.category_id
GROUP BY cat.category_name;


-- Find all competitions of type 'doubles'
SELECT competition_id, competition_name, type, gender
FROM Competitions
WHERE type = 'doubles';


-- Get competitions that belong to a specific category e.g., ITF Men
SELECT competition_id, competition_name
FROM Competitions
WHERE category_id = 'ITF-Men';


-- Identify parent competitions and their sub-competitions
SELECT 
    parent.competition_name AS parent_competition, 
    child.competition_name AS sub_competition
FROM Competitions child
JOIN Competitions parent ON child.parent_id = parent.competition_id;

-- Analyze the distribution of competition types by category
SELECT 
    cat.category_name, 
    c.type, 
    COUNT(*) AS type_count
FROM Competitions c
JOIN Categories cat ON c.category_id = cat.category_id
GROUP BY cat.category_name, c.type;


-- List all competitions with no parent top-level competitions
SELECT competition_id, competition_name
FROM Competitions
WHERE parent_id IS NULL;



-- complex tables

CREATE TABLE Complexes (
    complex_id VARCHAR(255) PRIMARY KEY,
    complex_name VARCHAR(255)
);

CREATE TABLE Venues (
    id VARCHAR(255) PRIMARY KEY,
	name VARCHAR(255),
    city_name VARCHAR(255),
    country_name VARCHAR(255),
    country_code VARCHAR(10),
    timezone VARCHAR(50),
    complex_id VARCHAR(255),
    FOREIGN KEY (complex_id) REFERENCES Complexes(complex_id)
);

-- List all venues along with their associated complex name
SELECT 
    Venues.name AS venue_name,
    Complexes.complex_name AS complex_name
FROM 
    Venues
INNER JOIN 
    Complexes 
ON 
    Venues.complex_id = Complexes.complex_id;
    
-- Count the number of venues in each complex
SELECT 
    Complexes.complex_name AS complex_name,
    COUNT(Venues.id) AS venue_count
FROM 
    Venues
INNER JOIN 
    Complexes 
ON 
    Venues.complex_id = Complexes.complex_id
GROUP BY 
    Complexes.complex_name;
 
 
-- Get details of venues in a specific country (e.g., Chile)
SELECT 
    Venues.id AS venue_id,
    Venues.name AS venue_name,
    Venues.city_name,
    Venues.country_name,
    Venues.timezone
FROM 
    Venues
WHERE 
    Venues.country_name = 'Chile';
    
    
    
-- Identify all venues and their timezones
SELECT 
    Venues.name AS venue_name,
    Venues.timezone
FROM 
    Venues;
    
-- Find complexes that have more than one venue
SELECT 
    Complexes.complex_name AS complex_name,
    COUNT(Venues.id) AS venue_count
FROM 
    Venues
INNER JOIN 
    Complexes 
ON 
    Venues.complex_id = Complexes.complex_id
GROUP BY 
    Complexes.complex_name
HAVING 
    COUNT(Venues.id) > 1;
    
    
-- List venues grouped by country
SELECT 
    Venues.country_name,
    GROUP_CONCAT(Venues.name SEPARATOR ', ') AS venues
FROM 
    Venues
GROUP BY 
    Venues.country_name;
    
-- Find all venues for a specific complex (e.g., Nacional)
SELECT 
    Venues.id AS venue_id,
    Venues.name AS venue_name,
    Venues.city_name,
    Venues.country_name,
    Venues.timezone
FROM 
    Venues
INNER JOIN 
    Complexes 
ON 
    Venues.complex_id = Complexes.complex_id
WHERE 
    Complexes.complex_name = 'Nacional';

--  compitetior

-- Creating the Competitors table
CREATE TABLE Competitors (
    competitor_id VARCHAR(50) PRIMARY KEY,        -- Unique ID for each competitor
    name VARCHAR(100) NOT NULL,                   -- Name of the competitor
    country VARCHAR(100) NOT NULL,                -- Competitor's country
    abbreviation VARCHAR(10) NOT NULL            -- Shortened name/abbreviation of competitor
);

-- Creating the Competitor_Rankings table
CREATE TABLE Competitor_Rankings (
    rank_id INT AUTO_INCREMENT PRIMARY KEY,      -- Unique ID for each ranking record
    `rank` INT NOT NULL,                          -- Rank of the competitor
    movement INT NOT NULL,                        -- Rank movement compared to the previous week
    points INT NOT NULL,                          -- Total ranking points
    competitions_played INT NOT NULL,             -- Number of competitions played
    competitor_id VARCHAR(50),                    -- Links to competitor details
    FOREIGN KEY (competitor_id) REFERENCES Competitors(competitor_id)
        ON DELETE CASCADE                        -- Cascade delete when competitor is deleted
        ON UPDATE CASCADE                        -- Cascade update when competitor ID is updated
);



