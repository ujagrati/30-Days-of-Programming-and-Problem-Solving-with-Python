select max(salary) AS SecondHighestSalary
from Employee
where salary not in (
    select max(salary) from employee
)
