-- Author: Abhishek Venkataprasad Boga
-- Date: 2025-03-23
-- Description: This SQL code is used to analyse International Debt Statistics's

-- Question 1 Soln: num_distinct_countries
select
	count(distinct country_name) as total_distinct_countries
from public.international_debt;

-- Question 2 Soln: highest_debt_country
select
	country_name,
	sum(debt) as total_debt
from public.international_debt
group by country_name
order by total_debt desc
limit 1;

-- Question 3 Soln: lowest_principal_repayment
select 
	country_name,
	indicator_name,
	sum(debt) as lowest_repayment
from public.international_debt
where indicator_code='DT.AMT.DLXF.CD'
group by country_name, indicator_name
order by lowest_repayment
limit 1;