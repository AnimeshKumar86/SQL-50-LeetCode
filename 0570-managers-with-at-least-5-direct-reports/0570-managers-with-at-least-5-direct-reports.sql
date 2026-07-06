# Write your MySQL query statement below
SELECT e1.name
FROM Employee e1
inner JOIN Employee e2
ON e1.id=e2.managerId
group by e2.managerid
HAVING count( e2.managerid) >=5
