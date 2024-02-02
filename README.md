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

    ```sh
    CONN_STR="Driver={ODBC Driver 18 for SQL Server};Server=tcp:mydbsrv.database.windows.net,1433;Database=mydb;Uid=myadmin;Pwd=mypassw23!;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"
    ```

    *Warning:* If you get an error stating lack of SQL driver, you can find the driver available in your system in the following way:

    ```python
    $ python
    >>> import pyodbc
    >>> pyodbc.drivers()
    ['SQL Server', 'Microsoft Access Driver (*.mdb, *.accdb)', 'Microsoft Excel Driver (*.xls, *.xlsx, *.xlsm, *.xlsb)', 'Microsoft Access Text Driver (*.txt, *.csv)']
    >>> exit()
    ```

    In such a case, replace `Driver={ODBC Driver 18 for SQL Server}` with `Driver={SQL Server}`

5. Create `.flaskenv` file in the main folder of the project, and paste the following content inside:

    ```sh
    FLASK_DEBUG=true
    FLASK_RUN_PORT=5000
    FLASK_RUN_HOST=127.0.0.1
    ```

6. Start your application locally to test the database connection: `flask run`

7. Open web application `http://127.0.0.1/query1`, then `/query2`. In both cases the page is created by function.

8. Test `/query3`. You can edit existing addresses, create new addressess, and delete addresses. In this case the table with addresses is created using template.

   *Warning:* Due to sample database constrains, you will be able to delete only addresses created by you.

## Advice

If you want to better understand the code, try to extend this application.

1. Start with `insert()` function and `insert.html` template. In the template, add the `input` field to enter State or Province. Then modify command `INSERT` in `insert()` function to store the State name in the database. Then you can add country region or postal code.

2. Modify `query3()` function, and `query3restult.html` template to display the full address (including state, province, and code).

3. Modify `edit()` function, and `edit.html` template to edit the full code.

