import pandas as pd  # Imports Pandas to read and transfer tabular data
from getpass import getpass  # Allows you to enter your MySQL password without displaying it
from sqlalchemy import create_engine  # Creates a connection to MySQL
from sqlalchemy.engine import URL  # Builds the database connection URL safely

from pathlib import Path  # Imports tools to handle file paths across operating systems

csv_path = Path(__file__).parent / "superstore_orders.csv"  # Finds the CSV in the same folder as this Python script
username = input("Enter your MySQL username: ").strip()  # Asks for your MySQL username, often root
password = getpass("Enter your MySQL password: ")  # Asks for your MySQL password without showing it

df = pd.read_csv(csv_path, parse_dates=["Order Date", "Ship Date"])  # Loads the CSV and parses the two date columns

connection_url = URL.create(  # Builds the connection details for your MySQL database
    drivername="mysql+pymysql",  # Uses PyMySQL as the MySQL connection driver
    username=username,  # Supplies the username entered above
    password=password,  # Supplies the password entered above
    host="localhost",  # Connects to MySQL running on your Mac
    port=3306,  # Uses the usual MySQL port
    database="superstore_db"  # Selects your project database
)

engine = create_engine(connection_url)  # Creates the database connection engine

with engine.connect() as connection:  # Opens a connection to verify MySQL is reachable
    connection.exec_driver_sql("SELECT 1")  # Runs a simple query to test the connection

print("MySQL connection successful!")  # Confirms the connection works

df.to_sql(  # Transfers the DataFrame into a MySQL table
    name="superstore_orders",  # Sets the destination table name
    con=engine,  # Uses the MySQL connection created above
    if_exists="replace",  # Creates the table or replaces an existing table with this name
    index=False,  # Prevents Pandas from adding an unnecessary index column
    chunksize=500  # Transfers the data in batches of 500 rows
)

with engine.connect() as connection:  # Opens a connection to verify the imported table
    result = connection.exec_driver_sql("SELECT COUNT(*) FROM superstore_orders")  # Counts the rows in the table
    row_count = result.scalar_one()  # Retrieves the row count as a single number

print("Rows imported into MySQL:", row_count)  # Displays the number of imported rows

engine.dispose()  # Closes the database engine and releases its resources


