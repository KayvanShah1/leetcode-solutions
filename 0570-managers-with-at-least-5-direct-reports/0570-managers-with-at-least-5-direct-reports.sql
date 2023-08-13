# Write your MySQL query statement below
with manager_direct_reports as (
    select 
        managerId 
    from 
        employee
    group by 
        managerId
    having 
        count(managerId) >= 5
)
select 
    name 
from employee
where id in (
    select managerId from manager_direct_reports
)