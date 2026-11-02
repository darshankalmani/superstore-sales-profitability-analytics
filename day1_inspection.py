import pandas as pd

file_path = "sample_-_superstore.xls"

df = pd.read_excel(file_path, sheet_name="Orders")

print(df.head())
print("Dataset shape:", df.shape) #returns the dimensions like rows and  columns
print("Column names:", df.columns.tolist()) #the column names
print(df.dtypes)  # Displays the data type of each column
print(df.isnull().sum())  # Counts missing values in each column
print("Duplicate rows:", df.duplicated().sum())  # Counts rows that exactly repeat an earlier row
print(df[["Sales", "Quantity", "Discount", "Profit"]].describe())  # Summarizes count, mean, standard deviation, minimum, quartiles, and maximum for these numeric columns
print(df.nsmallest(5, "Profit")[["Order ID", "Product Name", "Sales", "Discount", "Profit"]])  # Displays the five rows with the lowest profit and their key details
print(df.groupby("Discount")["Profit"].agg(["mean", "sum", "count"]))  # Shows average profit, total profit, and number of records for each discount level
print(df.groupby("Category")["Profit"].agg(["sum", "mean", "count"]))  # Calculates total profit, average profit, and record count for each product category
print(df.groupby("Sub-Category")["Profit"].sum().sort_values())  # Calculates total profit for each sub-category and sorts from lowest to highest
print(df[df["Sub-Category"] == "Tables"].nsmallest(5, "Profit")[["Order ID", "Product Name", "Sales", "Discount", "Profit"]])  # Filters table products and displays the five records with the lowest profit
print(df[df["Product Name"].str.contains("Chromcraft Bull-Nose Wood Oval Conference Table", case=False, na=False)][["Order ID", "Sales", "Quantity", "Discount", "Profit"]])  # Displays all matching orders with their sales, quantity, discount, and profit
print(df[df["Product Name"].str.contains("Chromcraft Bull-Nose Wood Oval Conference Table", case=False, na=False)][["Sales", "Quantity", "Profit"]].sum())  # Calculates total sales, total quantity, and total profit across all matching orders
print(df[df["Sub-Category"] == "Tables"].groupby("Discount")["Profit"].agg(["mean", "sum", "count"]))  # Compares average profit, total profit, and number of records across discount levels for Tables
print(df.groupby("Segment")["Sales"].agg("sum").to_frame().join(df.groupby("Segment")["Profit"].sum().rename("Total Profit")))  # Compares total sales and total profit across customer segments
segment_data = df.groupby("Segment")[["Sales", "Profit"]].sum()  # Calculates total sales and profit for each customer segment
segment_data["Profit Margin (%)"] = (segment_data["Profit"] / segment_data["Sales"]) * 100  # Calculates profit as a percentage of sales for each segment
print(segment_data.round(2))  # Displays the results rounded to two decimal places
df["Order Month"] = df["Order Date"].dt.to_period("M")  # Extracts the year and month from each order date
monthly_sales = df.groupby("Order Month")["Sales"].sum()  # Calculates total sales for each month
print(monthly_sales)  # Displays monthly sales totals in chronological order
df["Order Month Number"] = df["Order Date"].dt.month  # Extracts the month number from each order date, from 1 for January to 12 for December
df["Order Year"] = df["Order Date"].dt.year  # Extracts the year from each order date
monthly_comparison = df.pivot_table(index="Order Month Number", columns="Order Year", values="Sales", aggfunc="sum")  # Arranges monthly sales by month and year for comparison
print(monthly_comparison.round(2))  # Displays a comparison of sales for each month across all years
yearly_sales = df.groupby("Order Year")["Sales"].sum()  # Calculates total sales for each year
yearly_growth = yearly_sales.pct_change() * 100  # Calculates percentage sales growth compared with the previous year
print(pd.DataFrame({"Total Sales": yearly_sales, "Growth (%)": yearly_growth}).round(2))  # Displays yearly sales and percentage growth


region_analysis = df.groupby("Region")[["Sales", "Profit"]].sum()  # Calculates total sales and profit for each region
region_analysis["Profit Margin (%)"] = (region_analysis["Profit"] / region_analysis["Sales"]) * 100  # Calculates each region's profit margin as a percentage
print(region_analysis.sort_values("Sales", ascending=False).round(2))  # Displays regions ranked from highest to lowest sales

print(df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10))  # Calculates total sales per product and displays the top 10

top_products = df.groupby("Product Name")[["Sales", "Profit"]].sum()  # Calculates total sales and profit for each product
top_products = top_products.sort_values("Sales", ascending=False).head(10)  # Selects the 10 products with the highest total sales
print(top_products.round(2))  # Displays sales and profit for the top 10 products

top_products["Profit Margin (%)"] = (top_products["Profit"] / top_products["Sales"]) * 100  # Calculates profit as a percentage of sales for each top-selling product
print(top_products.round(2))  # Displays sales, profit, and profit margin rounded to two decimal places

print(df[df["Product Name"].isin(["Cisco TelePresence System EX90 Videoconferencing Unit", "GBC DocuBind P400 Electric Binding System"])].groupby(["Product Name", "Discount"])["Profit"].agg(["sum", "mean", "count"]).round(2))  # Compares total profit, average profit, and record count by discount for the two loss-making products

print(df.groupby("Ship Mode")[["Sales", "Profit"]].sum().join(df.groupby("Ship Mode")["Order ID"].nunique().rename("Unique Orders")).round(2))  # Compares total sales, total profit, and unique order counts across shipping methods

ship_analysis = df.groupby("Ship Mode").agg(  # Groups records by shipping method
    Total_Sales=("Sales", "sum"),  # Calculates total sales for each shipping method
    Total_Profit=("Profit", "sum"),  # Calculates total profit for each shipping method
    Unique_Orders=("Order ID", "nunique")  # Counts distinct orders for each shipping method
)  # Completes the grouped summary
ship_analysis["Profit_Per_Order"] = ship_analysis["Total_Profit"] / ship_analysis["Unique_Orders"]  # Calculates total profit divided by unique orders
ship_analysis["Sales_Per_Order"] = ship_analysis["Total_Sales"] / ship_analysis["Unique_Orders"]  # Calculates total sales divided by unique orders
print(ship_analysis.round(2))  # Displays the results rounded to two decimal places

print(df.groupby(["Customer ID", "Customer Name"])["Sales"].sum().sort_values(ascending=False).head(10))  # Calculates total sales per customer and displays the top 10 customers

customer_analysis = df.groupby(["Customer ID", "Customer Name"])[["Sales", "Profit"]].sum()  # Calculates total sales and profit for each customer
customer_analysis = customer_analysis.sort_values("Sales", ascending=False).head(10)  # Selects the 10 customers with the highest total sales
customer_analysis["Profit Margin (%)"] = (customer_analysis["Profit"] / customer_analysis["Sales"]) * 100  # Calculates each customer's profit margin
print(customer_analysis.round(2))  # Displays sales, profit, and profit margin for the top 10 customers

print(df[df["Customer Name"] == "Sean Miller"][["Order ID", "Product Name", "Sales", "Discount", "Profit"]].sort_values("Profit"))  # Displays Sean Miller's orders from the largest loss to the highest profit

sean_orders = df[df["Customer Name"] == "Sean Miller"]  # Filters the dataset to include only Sean Miller's orders
print(sean_orders[["Sales", "Profit"]].sum())  # Calculates his total sales and total profit
print("Profit margin (%):", round(sean_orders["Profit"].sum() / sean_orders["Sales"].sum() * 100, 2))  # Calculates his overall profit margin as a percentage

print("Total Sales:", round(df["Sales"].sum(), 2))  # Calculates total sales across all records
print("Total Profit:", round(df["Profit"].sum(), 2))  # Calculates total profit across all records
print("Overall Profit Margin (%):", round(df["Profit"].sum() / df["Sales"].sum() * 100, 2))  # Calculates overall profit as a percentage of sales
print("Total Orders:", df["Order ID"].nunique())  # Counts distinct order IDs
print("Total Customers:", df["Customer ID"].nunique())  # Counts distinct customers

print("Earliest Order Date:", df["Order Date"].min())  # Displays the earliest order date in the dataset
print("Latest Order Date:", df["Order Date"].max())  # Displays the latest order date in the dataset
print("Earliest Ship Date:", df["Ship Date"].min())  # Displays the earliest shipping date
print("Latest Ship Date:", df["Ship Date"].max())  # Displays the latest shipping date





print("Earliest Order Date:", df["Order Date"].min())  # Finds the earliest order date in the dataset
print("Latest Order Date:", df["Order Date"].max())  # Finds the latest order date in the dataset
print(df[df["Order Date"] > pd.Timestamp("2026-10-18")][["Order ID", "Order Date", "Ship Date", "Sales", "Profit"]].head(10))  # Displays up to 10 records dated after today's date

future_records = df[df["Order Date"] > pd.Timestamp("2026-10-18")]  # Selects orders dated after October 18, 2026
print("Future-dated records:", len(future_records))  # Counts the number of future-dated records
print("Future-dated sales:", round(future_records["Sales"].sum(), 2))  # Calculates sales recorded in those future-dated rows
print("Future-dated profit:", round(future_records["Profit"].sum(), 2))  # Calculates profit recorded in those future-dated rows

future_records = df[df["Order Date"] > pd.Timestamp("2026-10-18")]  # Selects records dated after October 18, 2026

future_records["Order Month"] = future_records["Order Date"].dt.to_period("M")  # Extracts the year and month from each future-dated order

print(future_records.groupby("Order Month").agg(  # Groups future-dated records by month
    Records=("Order ID", "size"),  # Counts the number of records in each month
    Unique_Orders=("Order ID", "nunique"),  # Counts distinct orders in each month
    Sales=("Sales", "sum"),  # Calculates total sales for each month
    Profit=("Profit", "sum")  # Calculates total profit for each month
).round(2))  # Displays the monthly results rounded to two decimal places

df["Is Future Dated"] = df["Order Date"] > pd.Timestamp("2026-10-18")  # Labels each row as future-dated or not based on the current cutoff

order_sizes = df.groupby(["Is Future Dated", "Order ID"]).size()  # Counts the number of product rows in each order, separated by date group

print(order_sizes.groupby(level=0).describe().round(2))  # Summarizes the distribution of rows per order for each date group

print(df.groupby("Is Future Dated")[["Sales", "Discount", "Profit"]].agg(["mean", "median", "min", "max"]).round(2))  # Compares sales, discount, and profit distributions between earlier-dated and future-dated records

print(df.groupby("Category")["Sales"].sum().round(2))  # Recalculates total sales by category from the original DataFrame