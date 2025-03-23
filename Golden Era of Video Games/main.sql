-- Author: Abhishek Venkataprasad Boga
-- Date: 2025-03-23
-- Description: This SQL code is used to analyse the Golden Era of Video Games

-- Question 1 Soln: best_selling_games
select *
from public.game_sales
order by games_sold desc
limit 10;

-- Question 2 Soln: critics_top_ten_years
with critics_by_year as 
(
select 	
	gs.year,
	count(gs.name) as num_games,
	avg(r.critic_score) as avg_critic_score
from game_sales as gs
inner join reviews as r
using (name)
group by gs.year
)
select
	year,
	num_games,
	round(avg_critic_score,2) as avg_critic_score
from critics_by_year
where num_games>=4
order by avg_critic_score desc
limit 10;

-- Question 3 Soln: golden_years
select 
	c.year,
	c.num_games,
	c.avg_critic_score,
	u.avg_user_score,
	(c.avg_critic_score-u.avg_user_score) as diff
from public.critics_avg_year_rating as c
inner join public.users_avg_year_rating as u
using (year)
where c.avg_critic_score>9 or u.avg_user_score>9
order by year; 