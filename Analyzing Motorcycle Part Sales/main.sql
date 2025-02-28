-- Author: Abhishek Venkataprasad Boga
-- Date: 2025-02-28
-- Description: This SQL code is used to analyse Motorcycle Part Sales's

select
	product_line,
	to_char(date,'Month') as month,
	warehouse,
	sum(total)-sum(payment_fee) as net_revenue
from public.sales
where client_type='Wholesale'
group by product_line, month, warehouse
order by product_line, month, net_revenue desc;