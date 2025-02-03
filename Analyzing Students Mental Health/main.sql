-- Author: Abhishek Venkataprasad Boga
-- Date: 2024-12-30
-- Description: This SQL code is used to analyse the students mental health data

-- To see data in the students table
-- SELECT * 
-- FROM students;

-- main query
select stay, count(inter_dom) as count_int, round(avg(todep),2) as average_phq, round(avg(tosc),2) as average_scs, round(avg(toas),2) as average_as
from students
where inter_dom='Inter'
group by stay
order by stay desc;