create table cat_reg as

select	category,
    	round(max(case when region = 'East' then sum_total_price end),0) as "East",
    	round(max(case when region = 'West' then sum_total_price end),0) as "West",
    	round(sum(sum_total_price),0) AS "Grand Total"
from 	(
    	select	category,
        		region,
        		sum(totalprice) AS sum_total_price
    	from	public.food_sales
    	GROUP by category, region
    	order by category
		) as A
group by category

union all

select	'Grand Total' as "category",
		round(sum(case when region = 'East' then totalprice else 0 end),0) as "East",
		round(sum(case when region = 'West' then totalprice else 0 end),0) as "West",
		round(sum(totalprice),0) AS "Grand Total"
from	public.food_sales