USE northwind;

-- Write a query to find the price of the cheapest item that Northwind sells. Then write a second query to find the name of the product that has that price.
SELECT MIN(UnitPrice) AS 'Cheapest Price'
FROM products;

SELECT ProductName, UnitPrice
FROM products
WHERE UnitPrice = (SELECT MIN(UnitPrice) FROM products);
-- Write a query to find the average price of all items that Northwind sells. (Bonus: Once you have written a working query, try asking Claude or ChatGPT for help using the ROUND function to round the average price to the nearest cent.)
SELECT ROUND(AVG(UnitPrice),2) AS "Avergae Price"
FROM products;
-- Write a query to find the price of the most expensive item that Northwind sells. Then write a second query to find the name of the product with that price, plus the name of the supplier for that product.
SELECT MAX(UnitPrice) AS "Most Expensive"
FROM products;

SELECT p.ProductName,s.CompanyName AS "Supplier Name", p.UnitPrice
FROM prodcust p
JOIN suppliers s ON p.SupplierID = s.SupplierID
WHERE p.UnitPrice = (SELECT MAX(UnitPrice)FROM products);

-- Write a query to find total monthly payroll (the sum of all the employees’ monthly salaries).
SELECT SUM(Salary) AS "Employees Total Salary"
FROM employees;

-- Write a query to identify the highest salary and the lowest salary amounts which any employee makes. (Just the amounts, not the specific employees!)
SELECT MAX(Salary) AS "Highest Salary", MIN(Salary) AS "Lowest Salary"
FROM employees;

-- Write a query to find the name and supplier ID of each supplier and the number of items they supply. Hint: Join is your friend here.
SELECT s.SupplierID, s.CompanyName, COUNT(p.ProductID) AS "Item Count"
FROM suppliers s
LEFT JOIN products p ON s.SupplierID = p.SupplierID
GROUP BY s.SupplierID, s.CompanyName;

-- Write a query to find the list of all category names and the average price for items in each category.
SELECT c.CategoryName, AVG(p.UnitPrice) AS "Average Price"
FROM categories c
LEFT JOIN products p ON c.CategoryID = p.CategoryID
GROUP BY c.CategoryID, c.CategoryName;

-- Write a query to find, for all suppliers that provide at least 5 items to Northwind, what is the name of each supplier and the number of items they supply.
SELECT s.CompanyName, COUNT(p.ProductID)AS "Item count"
FROM suppliers s
JOIN products p ON s.SupplierID = p.SupplierID
GROUP BY s.SupplierID, s.CompanyName
HAVING COUNT(p.ProductID) >= 5;

-- Write a query to list products currently in inventory by the product id, product name, and inventory value (calculated by multiplying unit price by the number of units on hand). Sort the results in descending order by value. If two or more have the same value, order by product name. If a product is not in stock, leave it off the list.
SELECT ProductID,ProductName, (UnitPrice * UnitsInStock) AS "Inventory Value"
FROM products
WHERE UnitsInStock >0
ORDER BY "Inventory Value" DESC , ProductName ASC;
