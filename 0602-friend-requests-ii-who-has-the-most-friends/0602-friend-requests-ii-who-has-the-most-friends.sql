# Write your MySQL query statement below
with people_with_most_friends as (
    select requester_id as id, accepter_id
    from RequestAccepted

    union all

    select accepter_id as id, requester_id
    from RequestAccepted
)

select 
    id, count(accepter_id) as num 
from 
    people_with_most_friends
group by
    id
order by 
    num desc
limit 1