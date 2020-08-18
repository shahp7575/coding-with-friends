/* Write your T-SQL query statement below */
/*
Problem Statement:
Write a SQL query to find all duplicate emails in a table named Person.

Runtime: 1791 ms
Memory: 0 B
*/

select Email
from Person
group by Email
having count(Email) > 1