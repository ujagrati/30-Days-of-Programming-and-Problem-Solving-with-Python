# Write your MySQL query statement below
select Employee.name , Bonus.bonus from Employee 
left join Bonus ON Employee.empId = Bonus.empId
where bonus<1000 OR bonus is null;