# Write your MySQL query statement below

with same_tiv_2015 as (
    select tiv_2015
    from insurance
    group by tiv_2015
    having count(distinct pid) > 1
), 
unique_locations as (
    select lat, lon
    from insurance
    group by lat, lon
    having count(distinct pid) = 1
)
select 
    round(sum(tiv_2016), 2) as tiv_2016
from 
    insurance
where
    tiv_2015 in (
        select tiv_2015 from same_tiv_2015
    ) and
    (lat, lon) in (
        select lat, lon from unique_locations
    ) 
