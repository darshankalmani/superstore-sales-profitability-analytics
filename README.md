# Superstore Sales & Profitability Analytics

## Project Overview

This project analyzes the Tableau Sample Superstore dataset to
understand sales performance, profitability, product categories,
regional performance, customer segments, and shipping modes.

The project uses **Python (Pandas)** for data inspection and exploratory
analysis, **MySQL** for database-based analysis, and **Power BI** to
build an interactive dashboard.

The goal is to turn sample retail order data into useful business
insights that can support better sales and profitability decisions.

## Project Objectives

-   Analyze overall sales, profit, and profit margin.
-   Compare sales and profitability across product categories and
    sub-categories.
-   Identify regional sales and profit patterns.
-   Understand customer-segment performance.
-   Examine monthly sales trends and shipping-mode profitability.
-   Present key metrics and trends in an interactive Power BI dashboard.

## Tools and Technologies

  Tool           Purpose
  -------------- -------------------------------------------------------
  Python         Data inspection and exploratory data analysis
  Pandas         Data loading, cleaning checks, grouping, and analysis
  MySQL          Storing and querying the dataset
  SQL            Aggregation and business analysis
  Power BI       Interactive dashboard and visualizations
  Excel (.xls)   Original sample data

## Dataset

-   **Source:** [Tableau Sample
    Data](https://public.tableau.com/app/learn/sample-data)
-   **Dataset:** Sample Superstore
-   **Records:** 10,194 rows
-   **Columns:** 21
-   **Fields include:** Order ID, Order Date, Ship Date, Ship Mode,
    Customer, Segment, Region, Category, Sub-Category, Sales, Quantity,
    Discount, and Profit.

The dataset is sample retail data and should not be interpreted as real
company transaction data. It contains records dated through December 30,
2026, including dates later than the current date. These records are
retained as supplied and are not treated as forecasts or verified future
sales.

## Project Workflow

### 1. Python -- Data Inspection and Exploratory Analysis

Used Pandas to load and inspect the dataset.

Work performed: - Checked the dataset shape and column names. - Reviewed
data types. - Checked for missing values and duplicate rows. - Examined
descriptive statistics for numerical columns. - Analyzed sales and
profit by category, sub-category, region, customer segment, and shipping
mode. - Examined discount levels and their relationship with
profitability. - Reviewed monthly sales patterns and high-value products
and customers.

**Data quality checks:** The inspected dataset contained no missing
values and no exact duplicate rows. Negative profit values were retained
because they represent loss-making transactions and are relevant to the
analysis.

### 2. MySQL -- SQL Analysis

Imported the 10,194 records into a MySQL database named `superstore_db`,
in a table named `superstore_orders`.

SQL was used to: - Calculate total sales and total profit. - Calculate
overall profit margin. - Aggregate sales and profit by product
category. - Organize results for business analysis.

SQL aggregation functions such as `SUM()` and `ROUND()` were used.

### 3. Power BI -- Interactive Dashboard

Built a one-page dashboard titled **Superstore Sales & Profitability
Dashboard**.

**KPI cards** - Total Sales - Total Profit - Profit Margin %

**Visualizations** - Monthly Sales Trend - Sales by Category - Profit by
Category - Sales by Region - Profit by Region - Profit by Sub-Category -
Sales by Customer Segment - Profit by Ship Mode

**Interactive slicers** - Region - Order Date

The slicers allow users to filter the dashboard and explore how the
selected region and date range affect the displayed metrics and charts.

## Key Results and Business Insights

The following figures are based on the full dataset as imported and
analyzed:

  Metric                          Result
  ----------------------- --------------
  Total Sales               2,326,534.35
  Total Profit                292,296.81
  Overall Profit Margin           12.56%
  Unique Orders                    5,111
  Unique Customers                   804

Selected observations:

-   **Regional profitability:** The West region had the highest total
    profit among the four regions. The Central region had the lowest
    profit margin, at approximately 7.92%.
-   **Category profitability:** Technology generated the highest total
    profit, followed by Office Supplies and Furniture.
-   **Sub-category performance:** Tables recorded an overall loss,
    making them an important area for further investigation.
-   **Customer segments:** Home Office had the highest profit margin
    among the three customer segments, at approximately 14.02%.
-   **Discounts:** Higher discount levels were associated with losses in
    several discount groups. This is an observed relationship in the
    dataset, not proof that discounts alone caused the losses.

These observations can help identify areas for further investigation,
such as discount policies, loss-making products, and regional
performance.

## Suggested Repository Structure

Organize the GitHub repository like this:

``` text
superstore-sales-profitability-analytics/
│
├── README.md
├── day1_inspection.py
├── prepare_sql_data.py
├── import_superstore_to_mysql.py
├── screenshots/
│   └── dashboard.png
└── sql/
    └── analysis_queries.sql
```

This is a suggested organization. Include only files that are actually
present in your project. Add the SQL file and dashboard screenshot if
you have saved them.

The original dataset can be downloaded from the Tableau Sample Data page
linked above. Before uploading the dataset itself, check the source's
terms for redistribution.

## How to Run the Python Scripts

1.  Download the Sample Superstore dataset from the [Tableau Sample Data
    page](https://public.tableau.com/app/learn/sample-data).
2.  Place the dataset and Python scripts in the appropriate project
    folder.
3.  Install the required Python packages:

``` bash
pip install pandas xlrd openpyxl sqlalchemy pymysql
```

4.  Run the inspection script:

``` bash
python3 day1_inspection.py
```

5.  Run the data preparation script:

``` bash
python3 prepare_sql_data.py
```

6.  Configure your own MySQL connection details securely, then run the
    import script:

``` bash
python3 import_superstore_to_mysql.py
```

The import script uses the database and table configuration defined in
the script. Review it before running, especially because an import
configured with `if_exists="replace"` replaces an existing table.

**Important:** Do not upload database passwords, API keys, or other
credentials to GitHub. Use environment variables or a local
configuration file excluded through `.gitignore`.

## Limitations

-   The dataset is sample data, not verified real-world company data.
-   The analysis describes patterns and associations; it does not
    establish causation.
-   The dataset contains dates later than the current date. These
    records should not be presented as actual completed future sales.
-   The dashboard summarizes the available fields and does not include
    external business context such as operating costs or inventory data.

## Conclusion

This project demonstrates an end-to-end data analytics workflow:
inspecting and analyzing data with Python, querying a MySQL database
using SQL, and communicating findings through an interactive Power BI
dashboard.

It provided practical experience in data handling, exploratory analysis,
SQL aggregation, business interpretation, and dashboard development.
