/* Write your T-SQL query statement below */
/*
Problem Statement:
Given the Employee table, write a SQL query that finds out employees who earn more than their managers.
*/

/**
Runtime: 866 ms
Memory: 0B
**/

select e1.Name as Employee
from Employee e1
inner join Employee e2
on e2.Id = e1.ManagerId
where e1.Salary > e2.Salary
