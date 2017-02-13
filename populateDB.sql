-- DELETE FROM ProductOrder;
-- DELETE FROM BangOrder;
-- DELETE FROM PaymentOption;
-- DELETE FROM Product;
-- DELETE FROM Customer; 

-- DROP VIEW IF EXISTS ProductPopularity;
-- DROP TABLE IF EXISTS ProductOrder;
-- DROP TABLE IF EXISTS BangOrder;
-- DROP TABLE IF EXISTS PaymentOption;
-- DROP TABLE IF EXISTS Product;
-- DROP TABLE IF EXISTS Customer;

-- Uncomment above after initial tables are created --

CREATE TABLE 'Customer' (
    'customerId' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    'name' TEXT NOT NULL,
    'address' TEXT NOT NULL,
    'city' TEXT NOT NULL,
    'state' TEXT NOT NULL,
    'postal_code' TEXT NOT NULL,
    'phone' TEXT NOT NULL,
    'email' TEXT NOT NULL
);

CREATE TABLE 'Product' (
    'productId' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    'name' TEXT NOT NULL,
    'price' INTEGER NOT NULL
);

CREATE TABLE 'PaymentOption' (
    'payment_optionId' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    'payment_type' TEXT NOT NULL,
    'account_number' 
);

CREATE TABLE 'BangOrder' (
    'bang_orderId' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    'customer' INTEGER NOT NULL,
    'payment_option' INTEGER NOT NULL,
        FOREIGN KEY('payment_option') REFERENCES 'PaymentOption'('payment_optionId'),
        FOREIGN KEY('customer') REFERENCES 'Customer' ('customerId')
);

CREATE TABLE 'ProductOrder' (
    'product_orderId' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    'product' INTEGER NOT NULL,
    'bang_order' INTEGER NOT NULL,
        FOREIGN KEY ('product') REFERENCES 'Product' ('productId'),
        FOREIGN KEY ('bang_order') REFERENCES 'BangOrder' ('bang_orderId')

);

/* 
    Below, we create a view, combining the following tables
    ProductOrder, Product, and Order
    - COUNT functions are used to count instances of orders and customers
    - SUM function adds the price of each product together
    - Data is grouped by product and ordered by product
    For example, see this post http://www.w3resource.com/sql/creating-views/create-view-with-join.php

    Author: Mark Ellis
*/

CREATE VIEW ProductPopularity
AS SELECT p.name as Product, COUNT(po.bang_order) as Orders, COUNT(DISTINCT o.customer) as Customers, SUM(p.price) as Revenue
FROM ProductOrder po, BangOrder o, Product p
WHERE po.product = p.productId
AND po.bang_order = o.bang_orderId
GROUP BY Product
ORDER BY Product;