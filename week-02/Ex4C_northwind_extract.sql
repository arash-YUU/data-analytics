USE northwind; 

-- a) What is the name of the table that holds the items Northwind sells? 

-- Answer: The table that holds the items Northwind sells is the products table. 

  
-- b) What is the name of the table that holds the types/categories of the items Northwind sells? 

-- Answer: The table that holds the types/categories of the items Northwind sells is the categories table. 


-- 5. Create a SELECT statement to retrieve all columns from the employees table. 

SELECT * FROM employees; 

  
-- a) Who is the Northwind employee whose name makes it look like she’s a bird? A 

-- Answer: Nancy Davolio sounds like "dove-olio".


-- 6. Create a SELECT statement to retrieve all columns from the products table. 

SELECT * FROM products; 


-- a) How many records does your query return? Using the toolbar options at the top of the query pane, how can you change your query to retrieve only 10 rows?  

-- Answer: It returns 77 records. Using the toolbar options at the top of the query pane, you can change the Limit to 1000 rows dropdown selector to Limit to 10 rows. 

  
-- b) BONUS: How could you write the query to limit the number of rows returned? This isn’t covered in the Week 2 Student Guide, so if you tackle this bonus question, you’ll need to do a little independent research. Add the answer as a comment in your script with a note on what source you used to find the answer. 

-- Answer: You can use the LIMIT clause in SQL, for example: SELECT * FROM products LIMIT 10; (Source: MySQL official documentation). 

  
-- 7. Create another SELECT statement to retrieve all columns from the categories table. 

SELECT * FROM categories; 

-- c) What is the category id of seafood?  

-- Answer: The category ID of seafood is 8. 

-- 8. Create a final SELECT statement to retrieve the top 50 records from orders, including only the OrderID, OrderDate, ShipName, and ShipCountry columns. 

SELECT OrderID, OrderDate, ShipName, ShipCountry  
FROM orders  LIMIT 50; 