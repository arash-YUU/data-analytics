USE northwind;

-- Create a single query to list the product id, product name, unit price and category name of all products. Order by category name and within that, by product name.
SELECT p.ProductID, p.ProductName, p.UnitPrice, c.CategoryName
FROM products p
JOIN categories c on p.CategoryID = c.CategoryID
ORDER BY c.CategoryName asc, p.ProductName asc;

-- Create a single query to list the product id, product name, unit price and supplier name of all products that cost more than $75. Order by product name.
SELECT p.ProductID, p.ProductName, p.UnitPrice, s.SupplierID
FROM products p
JOIN suppliers s on p.SupplierID =s.SupplierID
WHERE p.UnitPrice >75
ORDER BY p.ProductName asc;

-- Create a single query to list the product id, product name, unit price, category name, and supplier name of every product. Order by product name.
SELECT p.ProductID, p.ProductName, p.UnitPrice,c.CategoryName, s.SupplierID
FROM products p
JOIN categories c on p.CategoryID = c.CategoryID
JOIN suppliers s on p.SupplierID =s.SupplierID
ORDER BY p.ProductName asc;

-- Create a single query to list the order id, ship name, ship address, and shipping company name of every order that shipped to Germany. Assign the shipping company name the alias ‘Shipper.’ Order by the name of the shipper, then the name of who itshipped to.
SELECT o.OrderID, o.ShipName, o.ShipAddress, sh.CompanyName As Shipper
FROM orders o
JOIN shippers sh on o.ShipVia = sh.ShipperID
WHERE o.ShipCountry = 'Germany'
ORDER BY Shipper ASC, o.ShipName ASC;

-- Start from the same query as above (#4), but omit OrderID and add logic to group by ship name, with a count of how many orders were shipped for that ship name.
SELECT o.ShipName, o.ShipAddress, sh.CompanyName As Shipper, COUNT(o.OrderID) AS OrderCount
FROM orders o
JOIN shippers sh on o.ShipVia = sh.ShipperID
WHERE o.ShipCountry = 'Germany'
GROUP BY o.ShipName, o.ShipAddress, Shipper
ORDER BY Shipper ASC, o.ShipName ASC;

-- Create a single query to list the order id, order date, ship name, ship address of all orders that included Sasquatch Ale.
SELECT o.OrderID, o.OrderDate, o.ShipName, o.ShipAddress
FROM orders o
JOIN `order details` od on o.OrderID = od.OrderID
JOIN products p on od.ProductID = p.ProductID
WHERE p.ProductName = 'Sasquatch Ale'
