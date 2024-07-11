import pyodbc

# Connection string with your credentials
server = 'localhost'            #ENTER HERE LOCALHOST OR YOUR SERVER NAME
database = 'LAHORE_BOARD_STUDENT'   # ENTER HERE YOUE DATABASE NAME THAT YOUR CREATE IN SQL SERVER 
trusted_connection = 'yes'  # Use trusted connection (Windows Authentication)

try:
    # Connect to the database
    conn_string = f"""
    DRIVER={{ODBC Driver 17 for SQL Server}};
    SERVER={server};
    DATABASE={database};
    Trusted_Connection={trusted_connection};
    """
    conn = pyodbc.connect(conn_string)

    print("Connected to LAHORE_BOARD_STUDENT database successfully!")

    # You can now execute your SQL queries here using the connection object (conn)

except pyodbc.Error as ex:
    print("Error connecting to database:", ex)

finally:
    # Close the connection if opened
    if conn:
        conn.close()
        print("Connection closed.")
