# IDS706-Week6-Mini-Project: Complex SQL Query for a MySQL Database

This is a Python GitHub Template Repository that includes the following contents:
- A .devcontainer configuration for a Python environment
- A Makefile with commands for setup, testing, and linting
- GitHub Actions for CI/CD
- A requirements.txt for project dependencies
- A README.md with setup and usage instructions and an explanation for what the query is doing and the expected results
- A main.py file to perform a complex SQL query involving joins, aggregation, and sorting
- A test_main.py to test the main.py
  
## Prerequisites

- mysql-connector-python
- pylint
- pytest

## Report

For this project, I first created my local MySQL Database with the following tables.  

TABLE products  
mysql> SELECT * FROM products;  
  
+------------+-----------+------------+  
| product_id | name      | category   |  
+------------+-----------+------------+  
|          1 | Product A | Category 1 |  
|          2 | Product B | Category 2 |  
|          3 | Product C | Category 1 |  
|          4 | Product D | Category 1 |  
|          5 | Product E | Category 2 |  
|          6 | Product F | Category 3 |  
|          7 | Product G | Category 2 |  
|          8 | Product H | Category 3 |  
+------------+-----------+------------+  
  
TABLE sales  
mysql> SELECT * FROM sales;  
  
+---------+------------+--------------+------------+  
| sale_id | product_id | sales_amount | sale_date  |  
+---------+------------+--------------+------------+  
|       1 |          1 |       100.50 | 2023-10-01 |  
|       2 |          2 |       150.75 | 2023-10-02 |  
|       3 |          3 |        80.25 | 2023-10-03 |  
|       4 |          4 |       120.50 | 2023-10-04 |  
|       5 |          5 |        95.75 | 2023-10-05 |  
|       6 |          6 |        60.75 | 2023-10-06 |  
|       7 |          7 |        70.90 | 2023-10-07 |  
|       8 |          8 |        85.20 | 2023-10-08 |  
+---------+------------+--------------+------------+  

Then I connect to the database and perform the following SQL query involving joins, aggregation, and sorting:  
query = """  
    SELECT category, SUM(sales_amount) AS total_sales  
    FROM products  
    JOIN sales ON products.product_id = sales.product_id  
    GROUP BY category  
    ORDER BY total_sales DESC;  
    """  

This SQL query performs as group by the category, and for each category, I want to calculate the sum of the total sales amount of all products associated with specific category. I match the sale with product through a JOIN operation by specifying products.product_id = sales.product_id. Then, for the results, I order the sum of sales amount as descending order.  
  
The query result is the following:  
  
Category        Total Sales  
Category 2              317.40  
Category 1              301.25  
Category 3              145.95  
