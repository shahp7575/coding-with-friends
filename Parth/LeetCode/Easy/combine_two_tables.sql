/*
Write a SQL query for a report that provides the following information for each person in the Person table, 
regardless if there is an address for each of those people:

Runtime: 1400 ms
Memory: 0 B
*/

select p.FirstName, p.LastName, a.City, a.State
from Person p
left join Address a
on p.PersonId = a.PersonId