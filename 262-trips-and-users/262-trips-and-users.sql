# Write your MySQL query statement below
select request_at Day, round(
    sum(
        case 
            when t.status in ('cancelled_by_driver','cancelled_by_client') 
            then 1 
            else 0 
        end
    )/count(*), 2
) "Cancellation Rate" from Trips t
join 
    Users c on (c.users_id = t.client_id)
join 
    Users d on (d.users_id = t.driver_id)
where 
    t.request_at between '2013-10-01' and '2013-10-03'
    and c.banned = 'No'
    and d.banned = 'No'
group by request_at