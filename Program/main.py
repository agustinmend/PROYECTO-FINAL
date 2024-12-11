import pyodbc
import pandas

try:
    con = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
    "Server=JORGE;"
    "Database=Residencial;"
    "Trusted_Connection=yes;")
    print("Conection Succesful!!1!")

    query = "SELECT TOP 10 * FROM dbo.Customer"

    read = pandas.read_sql_query(query, con)
    print(read)
except Exception as e:
    print("Error: ", e)