-- # Write your MySQL query statement below
select employee_id,
    CASE
        when employee_id % 2 = 1 
            and name NOT REGEXP '^M'
        THEN salary
        ELSE 0
    END as bonus
from employees
order by employee_id