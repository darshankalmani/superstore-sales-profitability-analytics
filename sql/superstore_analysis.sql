
USE superstore_db; -- Selects the project database

-- 1. Overall business performance
SELECT
    ROUND(SUM(Sales), 2) AS Total_Sales, -- Calculates total sales
    ROUND(SUM(Profit), 2) AS Total_Profit, -- Calculates total profit
    ROUND(SUM(Profit) / SUM(Sales) * 100, 2) AS Profit_Margin_Percent -- Calculates overall profit margin
FROM superstore_orders; -- Reads the imported orders table

-- 2. Sales and profit by product category
SELECT
    Category, -- Displays each product category
    ROUND(SUM(Sales), 2) AS Total_Sales, -- Calculates category-wise sales
    ROUND(SUM(Profit), 2) AS Total_Profit -- Calculates category-wise profit
FROM superstore_orders -- Reads the imported orders table
GROUP BY Category -- Groups records by category
ORDER BY Total_Sales DESC; -- Sorts categories by sales, highest first
