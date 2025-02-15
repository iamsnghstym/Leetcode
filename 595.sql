# Write your MySQL query statement below
WITH big_countries AS (
    SELECT * FROM World
    WHERE area >= 3000000 OR population >= 25000000
)

SELECT name, population, area
FROM big_countries
