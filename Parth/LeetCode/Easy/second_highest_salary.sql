/* Write your T-SQL query statement below */
/* Runtime: 962 ms */
/* Memory: 0 B */
select max(Salary) as SecondHighestSalary 
from Employee
where Salary <
(
select max(Salary)
from Employee
)