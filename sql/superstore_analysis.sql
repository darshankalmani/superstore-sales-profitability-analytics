-- SUPERSTORE SALES & PROFITABILITY ANALYTICS
-- Consolidated SQL queries from the project's working SQL files.

-- SECTION 1: DATABASE AND DATA VALIDATION
CREATE DATABASE IF NOT EXISTS superstore_db; -- Creates a database for your Superstore analytics project if it does not already exist

USE superstore_db; -- Selects the database for your project

SELECT COUNT(*) AS total_rows FROM superstore_orders; -- Counts the number of imported records

SELECT * FROM superstore_orders LIMIT 5; -- Displays the first five rows to verify the imported data

SELECT
    ROUND(SUM(Sales), 2) AS Total_Sales, -- Adds sales across all records
    ROUND(SUM(Profit), 2) AS Total_Profit, -- Adds profit across all records
    ROUND(SUM(Profit) / SUM(Sales) * 100, 2) AS Profit_Margin_Percent -- Calculates overall profit as a percentage of sales
FROM superstore_orders; -- Reads the data from our imported table

-- SECTION 2: BUSINESS ANALYSIS QUERIES
SELECT
    Category, -- Displays each product category
    ROUND(SUM(Sales), 2) AS Total_Sales, -- Calculates total sales for each category
    ROUND(SUM(Profit), 2) AS Total_Profit -- Calculates total profit for each category
FROM superstore_orders -- Reads data from your imported Superstore table
GROUP BY Category -- Groups all records belonging to the same category
ORDER BY Total_Sales DESC; -- Sorts categories from highest to lowest sales

SELECT
    Category, -- Shows each product category
    ROUND(SUM(Sales), 2) AS Total_Sales, -- Calculates total sales
    ROUND(SUM(Profit), 2) AS Total_Profit, -- Calculates total profit
    ROUND(SUM(Profit) / SUM(Sales) * 100, 2) AS Profit_Margin_Percent -- Calculates profit as a percentage of sales
FROM superstore_orders -- Reads the imported data
GROUP BY Category -- Calculates results separately for each category
ORDER BY Profit_Margin_Percent DESC; -- Ranks categories by profit margin

SELECT
    `Sub-Category`, -- Displays each product subcategory
    ROUND(SUM(Sales), 2) AS Total_Sales, -- Calculates total sales
    ROUND(SUM(Profit), 2) AS Total_Profit -- Calculates total profit
FROM superstore_orders -- Reads the imported data
GROUP BY `Sub-Category` -- Groups records by subcategory
ORDER BY Total_Profit ASC; -- Shows the lowest-profit subcategories first

SELECT
    Discount, -- Shows the discount applied
    COUNT(*) AS Number_Of_Records, -- Counts records at each discount level
    ROUND(SUM(Sales), 2) AS Total_Sales, -- Calculates total sales
    ROUND(SUM(Profit), 2) AS Total_Profit, -- Calculates total profit
    ROUND(AVG(Profit), 2) AS Average_Profit -- Calculates average profit per record
FROM superstore_orders -- Reads the imported data
WHERE `Sub-Category` = 'Tables' -- Includes only Tables records
GROUP BY Discount -- Groups records by discount level
ORDER BY Discount ASC; -- Sorts from lowest to highest discount

SELECT
    `Sub-Category`, -- Displays the product subcategory
    `Product Name`, -- Displays the individual product name
    COUNT(*) AS Number_Of_Records, -- Counts records for each product
    ROUND(SUM(Sales), 2) AS Total_Sales, -- Calculates total sales
    ROUND(SUM(Profit), 2) AS Total_Profit -- Calculates total profit
FROM superstore_orders -- Reads the imported data
WHERE `Sub-Category` = 'Tables' -- Filters for tables only
GROUP BY `Sub-Category`, `Product Name` -- Groups records by product
HAVING SUM(Profit) < 0 -- Keeps products with an overall loss
ORDER BY Total_Profit ASC; -- Lists the biggest losses first

SELECT
    `Order ID`, -- Identifies each order
    `Order Date`, -- Shows when the order was placed
    Sales, -- Shows sales value for the record
    Quantity, -- Shows the number of units
    Discount, -- Shows the discount applied
    Profit -- Shows the profit or loss
FROM superstore_orders -- Reads the imported data
WHERE `Product Name` = 'Chromcraft Bull-Nose Wood Oval Conference Tables & Bases' -- Filters for the selected product
ORDER BY Profit ASC; -- Shows the most loss-making records first

SELECT
    Category, -- Displays the product category
    `Sub-Category`, -- Displays the product subcategory
    `Product Name`, -- Displays the product name
    COUNT(*) AS Number_Of_Records, -- Counts records for each product
    ROUND(SUM(Sales), 2) AS Total_Sales, -- Calculates total sales
    ROUND(SUM(Profit), 2) AS Total_Profit -- Calculates total profit
FROM superstore_orders -- Reads the imported data
GROUP BY Category, `Sub-Category`, `Product Name` -- Summarizes each product
HAVING SUM(Profit) < 0 -- Keeps products with an overall loss
ORDER BY SUM(Profit) ASC -- Places the largest losses first
LIMIT 10; -- Returns only the 10 biggest loss-making products

SELECT
    Region, -- Displays each sales region
    ROUND(SUM(Sales), 2) AS Total_Sales, -- Calculates total sales by region
    ROUND(SUM(Profit), 2) AS Total_Profit, -- Calculates total profit by region
    ROUND(SUM(Profit) / SUM(Sales) * 100, 2) AS Profit_Margin_Percent -- Calculates regional profit margin
FROM superstore_orders -- Reads the imported data
GROUP BY Region -- Groups records by region
ORDER BY Total_Profit DESC; -- Ranks regions from highest to lowest total profit

SELECT
    Segment, -- Displays the customer segment
    COUNT(DISTINCT `Customer ID`) AS Unique_Customers, -- Counts different customers in each segment
    ROUND(SUM(Sales), 2) AS Total_Sales, -- Calculates total sales
    ROUND(SUM(Profit), 2) AS Total_Profit, -- Calculates total profit
    ROUND(SUM(Profit) / SUM(Sales) * 100, 2) AS Profit_Margin_Percent -- Calculates profit margin
FROM superstore_orders -- Reads the imported data
GROUP BY Segment -- Groups records by customer segment
ORDER BY Total_Sales DESC; -- Ranks segments by total sales

SELECT
    `Customer Name`, -- Displays the customer's name
    COUNT(DISTINCT `Order ID`) AS Total_Orders, -- Counts unique orders
    ROUND(SUM(Sales), 2) AS Total_Sales, -- Calculates customer sales
    ROUND(SUM(Profit), 2) AS Total_Profit, -- Calculates customer profit
    ROUND(SUM(Profit) / SUM(Sales) * 100, 2) AS Profit_Margin_Percent -- Calculates customer profit margin
FROM superstore_orders -- Reads the imported data
GROUP BY `Customer ID`, `Customer Name` -- Groups records by individual customer
ORDER BY Total_Sales DESC -- Ranks customers by sales
LIMIT 10; -- Returns the top 10 customers

SELECT
    `Ship Mode`, -- Displays the shipping method
    COUNT(DISTINCT `Order ID`) AS Total_Orders, -- Counts unique orders
    ROUND(SUM(Sales), 2) AS Total_Sales, -- Calculates total sales
    ROUND(SUM(Profit), 2) AS Total_Profit, -- Calculates total profit
    ROUND(SUM(Profit) / SUM(Sales) * 100, 2) AS Profit_Margin_Percent -- Calculates profit margin
FROM superstore_orders -- Reads the imported data
GROUP BY `Ship Mode` -- Groups records by shipping method
ORDER BY Total_Profit DESC; -- Ranks shipping methods by total profit

SELECT
    YEAR(`Order Date`) AS Order_Year, -- Extracts the year from each order date
    MONTH(`Order Date`) AS Order_Month, -- Extracts the month number
    ROUND(SUM(Sales), 2) AS Total_Sales, -- Calculates monthly sales
    ROUND(SUM(Profit), 2) AS Total_Profit -- Calculates monthly profit
FROM superstore_orders -- Reads the imported data
GROUP BY YEAR(`Order Date`), MONTH(`Order Date`) -- Groups records by year and month
ORDER BY Order_Year, Order_Month; -- Sorts chronologically

WITH yearly_sales AS ( -- Creates a temporary result containing yearly sales
    SELECT
        YEAR(`Order Date`) AS Order_Year, -- Extracts the order year
        SUM(Sales) AS Total_Sales -- Calculates sales for each year
    FROM superstore_orders -- Reads the imported data
    GROUP BY YEAR(`Order Date`) -- Groups records by year
)
SELECT
    Order_Year, -- Displays the year
    ROUND(Total_Sales, 2) AS Total_Sales, -- Displays annual sales
    ROUND(LAG(Total_Sales) OVER (ORDER BY Order_Year), 2) AS Previous_Year_Sales, -- Retrieves the previous year's sales
    ROUND((Total_Sales - LAG(Total_Sales) OVER (ORDER BY Order_Year))
        / LAG(Total_Sales) OVER (ORDER BY Order_Year) * 100, 2) AS Growth_Percent -- Calculates year-over-year growth
FROM yearly_sales -- Reads the temporary yearly summary
ORDER BY Order_Year; -- Sorts years chronologically

SELECT
    Discount, -- Shows the discount rate
    COUNT(*) AS Number_Of_Records, -- Counts records at each discount level
    ROUND(SUM(Sales), 2) AS Total_Sales, -- Calculates total sales
    ROUND(SUM(Profit), 2) AS Total_Profit, -- Calculates total profit
    ROUND(AVG(Profit), 2) AS Average_Profit -- Calculates average profit per record
FROM superstore_orders -- Reads the imported data
GROUP BY Discount -- Groups records by discount rate
ORDER BY Discount ASC; -- Sorts from lowest to highest discount

SELECT
    Discount, -- Shows the discount rate
    ROUND(SUM(Sales), 2) AS Total_Sales, -- Calculates total sales
    ROUND(SUM(Profit), 2) AS Total_Profit, -- Calculates total profit
    ROUND(SUM(Profit) / SUM(Sales) * 100, 2) AS Profit_Margin_Percent -- Calculates profit as a percentage of sales
FROM superstore_orders -- Reads the imported data
GROUP BY Discount -- Groups records by discount rate
ORDER BY Discount ASC; -- Sorts from lowest to highest discount

SELECT
    Category, -- Displays the product category
    `Sub-Category`, -- Displays the product subcategory
    `Product Name`, -- Displays the individual product
    ROUND(SUM(Sales), 2) AS Total_Sales, -- Calculates total sales per product
    ROUND(SUM(Profit), 2) AS Total_Profit, -- Calculates total profit per product
    ROUND(SUM(Profit) / SUM(Sales) * 100, 2) AS Profit_Margin_Percent -- Calculates profit margin
FROM superstore_orders -- Reads the imported data
GROUP BY Category, `Sub-Category`, `Product Name` -- Summarizes each product
HAVING SUM(Profit) > 0 -- Keeps profitable products
ORDER BY SUM(Profit) DESC -- Ranks products by total profit
LIMIT 10; -- Returns the top 10 most profitable products

SELECT
    `Sub-Category`, -- Displays each product subcategory
    ROUND(SUM(Sales), 2) AS Total_Sales, -- Calculates total sales
    ROUND(SUM(Profit), 2) AS Total_Profit, -- Calculates total profit
    ROUND(SUM(Profit) / SUM(Sales) * 100, 2) AS Profit_Margin_Percent -- Calculates profit margin
FROM superstore_orders -- Reads the imported data
GROUP BY `Sub-Category` -- Summarizes each subcategory
ORDER BY Total_Profit ASC; -- Shows the lowest-profit subcategories first

SELECT
    ROUND(SUM(Sales), 2) AS Total_Sales, -- Calculates total sales across the dataset
    ROUND(SUM(Profit), 2) AS Total_Profit, -- Calculates total profit across the dataset
    ROUND(SUM(Profit) / SUM(Sales) * 100, 2) AS Profit_Margin_Percent, -- Calculates overall profit margin
    COUNT(DISTINCT `Order ID`) AS Total_Orders, -- Counts unique orders
    COUNT(DISTINCT `Customer ID`) AS Total_Customers, -- Counts unique customers
    COUNT(DISTINCT `Product ID`) AS Unique_Products -- Counts different products
FROM superstore_orders; -- Reads the imported Superstore table
