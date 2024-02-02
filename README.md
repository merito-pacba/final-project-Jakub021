# Lecture Demo 2
This sample presents how to access Azure MSSQL server using Python libraries, from Flask application. It shows some simple techniques used when programming web application.
Configuration of database connection is stored in environment variables.

If you want to test this app on your computer, you have to:

1. Set up MSSQL server database with sample DB.
2. Create virtual Python environment and install requirements inside:

   ```sh
   python -m venv .venv
   .venv\Source\Activate.ps1  # for Powershell
   source .venv/bin/activate  # for Linux/Mac
   pip install -r requirements.txt
   ```
4. Create `.env` file in **the main folder of the project** and put there environment variables with connection string to the database. Copy from Azure SQL database (Settings > Connection Strings) ODBC connection string, paste it into file, and put the correct password inside:

    ```
    CONN_STR="Driver={ODBC Driver 18 for SQL Server};Server=tcp:mydbsrv.database.windows.net,1433;Database=mydb;Uid=myadmin;Pwd=mypassw23!;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"
    ```

    *Warning:* If you get an error stating lack of SQL driver, you can find the driver available in your system in the following way:

    ```
    python
    >>> import pyodbc
    >>> pyodbc.drivers()
    ['SQL Server', 'Microsoft Access Driver (*.mdb, *.accdb)', 'Microsoft Excel Driver (*.xls, *.xlsx, *.xlsm, *.xlsb)', 'Microsoft Access Text Driver (*.txt, *.csv)']
    >>> exit()
    ```
    
    In such a case, replace `Driver={ODBC Driver 18 for SQL Server}` with `Driver={SQL Server}`

5. Create `.flaskenv` file in the main folder of the project, and paste the following content inside:

    ```
    FLASK_DEBUG=true
    FLASK_RUN_PORT=5000
    FLASK_RUN_HOST=127.0.0.1
    ```

6. Start your application locally to test the database connection: `flask run`

7. Open web application `http://127.0.0.1/query1`, then `/query2`

8. Test `/query3`. You can edit existing addresses, create new addressess, and delete addressess. Due to sample database restrictions, you will be able to delete only addresses created by you.

