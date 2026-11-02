import pandas as pd  # Imports Pandas to work with Excel and tabular data

file_path = "sample_-_superstore.xls"  # Specifies the original Superstore Excel file

orders_df = pd.read_excel(file_path, sheet_name="Orders")  # Loads the original Orders worksheet into a DataFrame

orders_df.to_csv("superstore_orders.csv", index=False)  # Exports the worksheet to CSV without adding an unnecessary row-number column

print("CSV file created successfully!")  # Confirms that the export completed
print("Rows and columns:", orders_df.shape)  # Displays the number of rows and columns exported

