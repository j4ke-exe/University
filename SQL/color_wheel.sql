-- Name: Jacob Garrison
-- Date: 10 Oct 2022
-- Class: ENTD261

-- Create Database called color_wheel and create a table called colors with character limit 15
CREATE DATABASE color_wheel;
USE color_wheel;
CREATE TABLE colors (id INT NOT NULL, NAME VARCHAR(15) );

-- (SCRIPT 1) Create a table called colors with the following items
INSERT INTO colors VALUES (1, 'red');
INSERT INTO colors VALUES (2, 'orange');
INSERT INTO colors VALUES (3, 'yellow');
INSERT INTO colors VALUES (4, 'green');
INSERT INTO colors VALUES (5, 'blue');
INSERT INTO colors VALUES (6, 'indigo');
INSERT INTO colors VALUES (7, 'violet');
INSERT INTO colors VALUES (8, 'pink');
INSERT INTO colors VALUES (9, 'purple');
INSERT INTO colors VALUES (10, 'brown');

-- (SCRIPT 2) Update the colors table to include the following
UPDATE colors SET name = 'red' WHERE id = 1;
UPDATE colors SET name = 'orange' WHERE id = 2;
UPDATE colors SET name = 'yellow' WHERE id = 3;
UPDATE colors SET name = 'green' WHERE id = 4;
UPDATE colors SET name = 'blue' WHERE id = 5;
UPDATE colors SET name = 'indigo' WHERE id = 6;
UPDATE colors SET name = 'violet' WHERE id = 7;
UPDATE colors SET name = 'pink' WHERE id = 8;
UPDATE colors SET name = 'purple' WHERE id = 9;
UPDATE colors SET name = 'brown' WHERE id = 10;

-- (SCRIPT 3a) Select all records from the colors table
SELECT * FROM colors;

-- (SCRIPT 3b) Select all records sorted descending and ascending
SELECT * FROM colors ORDER BY id DESC;
SELECT * FROM colors ORDER BY id ASC;

-- (SCRIPT 3c) Select the data from table with a condiition
SELECT * FROM colors WHERE id = 1;

-- (SCRIPT 3d) Counting number of records in a table
SELECT COUNT(*) FROM colors;

-- (SCRIPT 3e) Count all records with a condition
SELECT COUNT(*) FROM colors WHERE id = 1;

-- (SCRIPT 4) 3 delete records from the table
DELETE FROM colors WHERE id = 1;
DELETE FROM colors WHERE id = 2;
DELETE FROM colors WHERE id = 3;
