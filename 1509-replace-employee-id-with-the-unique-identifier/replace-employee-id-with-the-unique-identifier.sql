# Write your MySQL query statement below
 select name, unique_id from Employees
 left join EmployeeUNI ON Employees.id = EmployeeUNI.id
