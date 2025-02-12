-- Author: Abhishek Venkataprasad Boga
-- Date: 2025-02-12
-- Description: This SQL code is used to analyse London's travel network

-- Question 1 Soln: most_popular_transport_types
select 
	journey_type,
	sum(journeys_millions) as TOTAL_JOURNEYS_MILLIONS
from TFL.JOURNEYS
group by journey_type
order by total_journeys_millions desc;

-- Question 2 Soln: emirates_airline_popularity
select 
	month,
	year,
	round(journeys_millions,2) as ROUNDED_JOURNEYS_MILLIONS
from TFL.JOURNEYS
where journeys_millions is not null 
	  and journey_type='Emirates Airline'
order by ROUNDED_JOURNEYS_MILLIONS desc
limit 5;

-- Question 3 Soln: least_popular_years_tube
select 
	year,
	journey_type,
	sum(journeys_millions) as TOTAL_JOURNEYS_MILLIONS
from TFL.JOURNEYS
where journey_type='Underground & DLR'
group by all
order by TOTAL_JOURNEYS_MILLIONS
limit 5;