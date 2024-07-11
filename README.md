Connecting to SQL Server using Python and PyODBC
This guide demonstrates how to connect to a SQL Server database using Python's PyODBC library.
Prerequisites
•	Python installed on your system (version 3.x recommended)
•	PyODBC library (pip install pyodbc)
•	SQL Server installed and running, with a database created
Steps to Connect
1.	Install PyODBC Library:
If you haven't already installed PyODBC, you can do so using pip:
Copy code
pip install pyodbc
2.	Import PyODBC:
Import the PyODBC module into your Python script:
python
Copy code
import pyodbc
3.	Set up Connection Parameters:
Define connection parameters such as server name (server), database name (database), and whether to use trusted connection (trusted_connection).
python
Copy code
server = 'localhost'  # Replace with your SQL Server hostname or IP address
database = 'LAHORE_BOARD_STUDENT'  # Replace with your database name
trusted_connection = 'yes'  # Use 'yes' for Windows Authentication
4.	Create Connection String:
Construct the connection string using the parameters defined above:
python
Copy code
conn_string = f"""
DRIVER={{ODBC Driver 17 for SQL Server}};
SERVER={server};
DATABASE={database};
Trusted_Connection={trusted_connection};
"""
5.	Connect to the Database:
Use pyodbc.connect() to establish a connection to your SQL Server database:
python
Copy code
try:
    conn = pyodbc.connect(conn_string)
    print("Connected to SQL Server database successfully!")

    # You can now execute your SQL queries using the connection object (conn)

except pyodbc.Error as ex:
    print("Error connecting to SQL Server database:", ex)

finally:
    # Close the connection if opened
    if conn:
        conn.close()
        print("Connection closed.")
Running the Example
•	Replace server and database variables with your SQL Server instance details and database name.
•	Run the script. It will attempt to connect to the specified SQL Server database and print success or failure messages.

