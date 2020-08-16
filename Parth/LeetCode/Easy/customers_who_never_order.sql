-- MySQL
-- Suppose that a website contains two tables, the Customers table and the Orders table. 
-- Write a SQL query to find all customers who never order anything.
-- Runtime: 552 ms
-- Memory: 0 B

select c.Name as Customers from Customers c
where c.Id not in
(
select c.Id from Customers c
inner join Orders o
on c.Id = o.CustomerId
) 