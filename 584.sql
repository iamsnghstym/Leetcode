# Write your MySQL query statement below
SELECT name
FROM Customer
WHERE referee_id <> 2
OR referee_id IS NULL;



# OR

# Write your MySQL query statement below
SELECT name
FROM Customer
WHERE IFNULL(referee_id, -1) <> 2;