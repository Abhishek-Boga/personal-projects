-- Author: Abhishek Venkataprasad Boga
-- Date: 2025-03-06
-- Description: This SQL code is used to analyse Pet Supplies

-- Task 1
with median_sales as 
(
select 
		percentile_cont(0.5) within group(order by sales)
from public.pet_supplies
)
select
	product_id,
	replace(category,'-','Unknown') as category,
	animal,
	initcap(size) as size,
	round((case when price='unlisted' then '0'
	else price end)::numeric,2) as price,
	coalesce(sales,(select * from median_sales)) as sales,
	coalesce(rating,0) as rating,
	repeat_purchase
from public.pet_supplies;	

-- Task 2
with cte as
(
select
	animal,
	repeat_purchase,
	avg(sales) as avg_sales,
	min(sales) as min_sales,
	max(sales) as max_sales
from public.pet_supplies
group by animal, repeat_purchase
order by animal
)
select 
	animal,
	repeat_purchase,
	round(avg_sales) as avg_sales,
	round(min_sales) as min_sales,
	round(max_sales) as max_sales
from cte;

-- Task 3
select
	product_id,
	sales,
	rating
from public.pet_supplies
where repeat_purchase=1 
	and animal in ('Cat','Dog');