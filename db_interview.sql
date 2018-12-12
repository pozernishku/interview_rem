-- postgresql 10.0
-- https://www.db-fiddle.com

-- DDL
CREATE TABLE Sales (
  "date" TIMESTAMP,
  "customer_id" INTEGER,
  "product_id" INTEGER,
  "units_sold" INTEGER,
  "paid_amount" FLOAT
);

INSERT INTO Sales
  ("date", "customer_id", "product_id", "units_sold", "paid_amount")
VALUES
  ('2018-01-01', '1', '1', '5', '45'),
  ('2018-01-01', '2', '1', '2', '18'),
  ('2018-01-01', '3', '2', '7', '35'),
  ('2018-01-07', '1', '3', '3', '45'),
  ('2018-01-07', '2', '2', '5', '25'),
  ('2018-01-07', '4', '2', '5', '25'),
  ('2018-01-10', '1', '4', '5', '30'),
  ('2018-01-10', '2', '4', '5', '30'),
  ('2018-01-10', '4', '5', '6', '60'),
  ('2018-01-10', '4', '5', '6', '60'),
  ('2018-01-10', '4', '3', '9', '135'),
  ('2018-01-14', '3', '3', '4', '60'),
  ('2018-01-14', '2', '3', '6', '90'),
  ('2018-01-07', '2', '6', '10', '80'),
  ('2018-01-07', '3', '6', '11', '88'),
  ('2018-01-15', '5', '7', '20', '100');
  
  

CREATE TABLE products (
  "id" INTEGER,
  "name" VARCHAR(100),
  "price" FLOAT
);

INSERT INTO products
  ("id", "name", "price")
VALUES
  ('1', 'Tomato', '9'),
  ('2', 'Cucumber', '5'),
  ('3', 'Avocado', '15'),
  ('4', 'Red Pepper', '6'),
  ('5', 'Orange', '10'),
  ('6', 'Apple', '8');
  
  
  

CREATE TABLE customers (
  "id" INTEGER,
  "name" VARCHAR(100),
  "address" VARCHAR(100),
  "age" INTEGER,
  "favorite_soccer_team" VARCHAR(100)
);

INSERT INTO customers
  ("id", "name", "address", "age", "favorite_soccer_team")
VALUES
  ('1', 'Yosi', 'Tel Aviv', '35', 'Manchester United F.C.'),
  ('2', 'Liat', 'Tel Aviv', '40', 'A.S. Roma'),
  ('3', 'Ran', 'Tel Aviv', '32', 'FC Barcelona'),
  ('4', 'Moti', 'Jerusalem', '20', 'AFC Ajax');



-- SQL
-- questions

-- 1. How many tomatoes were sold during Jan 1st, 2018? (query should return a single row)
select count(s.product_id) sold_cnt

from sales s

join products p on s.product_id = p.id

where p.name = 'Tomato'
and s.date = '2018-01-01'

-- 2. How much money was paid (paid_amount) in total for each product during Jan 2018. 
-- (query should return 2 columns – Product name and the total paid_amount)
select max(p.name) product_name
, sum(s.paid_amount) total_paid_amount

from sales s

left join products p on s.product_id = p.id

where date_trunc('month', s.date) = to_date('2018-01-01','YYYY-MM-DD')

group by p.id

-- 3. Of which product did A.S. Roma fans bought the most units? (query should return a single row)
select (select p.name from products p where p.id = s.product_id) product_name
--, sum(s.units_sold) sum_units_sold

from sales s

where s.customer_id in (select c.id
	from customers c
	where c.favorite_soccer_team = 'A.S. Roma')
    
group by s.product_id

order by sum(s.units_sold) desc

limit 1

-- How many customers buy two or above different products on one of their visits (i.e. sales date)? 
-- (query should return a single row)
select row_number() over() cust_count

from sales s

group by s.date, s.customer_id

having count(distinct s.product_id) >= 2

order by cust_count desc

limit 1

-- 4. Which people bought only three products (product.name)? 
-- How many apples did these people (from the first part of the question) bought on Jan 7th, 2018?
-- (query should return a single row)
select sum(s.units_sold) sum_units_sold

from sales s

where s.date = '2018-01-07'
and s.product_id in (select p.id from products p where p.name = 'Apple')
and s.customer_id in (select s.customer_id
  from sales s
  group by s.customer_id
  -- bought only three UNIQUE products
  having count(distinct s.product_id) = 3)

-- (Bonus question)
-- 2.4	Aviv has a bug in the loading process, and notices that the sales table contains 
-- transactions for non-existing vegetables and non-existing customers. 
-- The total sales amount, however, is correct. 
-- How can he solve this issue without losing sales data?

-- We can use left join with sales table to not lose sales data:
select * 
, count(*) over() cnt

from sales s

left join products p on s.product_id = p.id
left join customers c on s.customer_id = c.id
