# Write your MySQL query statement below
(
    select 
        distinct u.name as results  
    from
        Users u, MovieRating m
    where 
        u.user_id = m.user_id
    group by
        m.user_id
    order by
        count(m.user_id) desc, u.name
    limit 1
)

union all

(
    select 
        distinct m.title as results  
    from
        MovieRating r, Movies m
    where 
        r.movie_id = m.movie_id and
        r.created_at like "2020-02-%"
    group by
        m.movie_id
    order by
        avg(r.rating) desc, m.title
    limit 1
)