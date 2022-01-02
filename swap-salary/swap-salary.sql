# Write your MySQL query statement below
update salary
set sex =
    case sex
        when 'f' then 'm'
        when 'm' then 'f'
        else sex
    end