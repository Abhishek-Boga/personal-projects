-- Author: Abhishek Venkataprasad Boga
-- Date: 2025-03-22
-- Description: This SQL code is used to analyse GoodThought NGO's initiatives

-- Question 1 Soln: highest_donation_assignments
with donation_donnor_summary as 
(
select
	assignment_id,
	d.amount,
	d.donor_id,
	don.donor_type
from public.donations as d
inner join public.donors as don
using(donor_id)
),
donation_assignments as (
select 
	a.assignment_name,
	a.region,
	c.donor_type,
	sum(c.amount) as totat_donation_amount
from public.assignments as a
inner join donation_donnor_summary as c
using(assignment_id)
group by a.assignment_id, a.region, c.donor_type
)
select 
	assignment_name,
	region,
	round(totat_donation_amount,2) as rounded_total_donation_amount,
	donor_type
from donation_assignments
order by rounded_total_donation_amount desc
limit 5;

-- Question 2 Soln: top_regional_impact_assignments
with num_assignment_donations as 
(
select
	a.assignment_name,
	a.region,
	a.impact_score,
	count(d.donation_id) over(partition by a.assignment_name order by region asc) as num_total_donations
from public.assignments as a
left join public.donations as d
using(assignment_id)
),
region_rank as
(
select
	distinct assignment_name,
	region,
	impact_score,
	num_total_donations,
	rank() over(partition by region order by impact_score desc) as rank_region_wise
from num_assignment_donations
where num_total_donations>=1
order by rank_region_wise
)
select
	assignment_name,
	region,
	impact_score,
	num_total_donations
from region_rank
where rank_region_wise=1
order by region
limit 4;