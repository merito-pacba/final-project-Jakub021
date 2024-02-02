# Lecture Demo 2
This sample presents how to access Azure MSSQL server using Python libraries, from Flask application. It shows some simple techniques used when programming web application.
Configuration of database connection is stored in environment variables.

If you want to test this app on your computer, you have to:

1. Set up MSSQL server database with sample DB.
2. Create `.env` file in the main folder of the project and put there environment variables with connection string to the database. Copy from Azure SQL database (Settings > Connection Strings) ODBC connection string, paste it into file, and put the correct password inside:

    ```
    CONN_STR="Driver={ODBC Driver 18 for SQL Server};Server=tcp:mydbsrv.database.windows.net,1433;Database=mydb;Uid=myadmin;Pwd=mypassword;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"
    ```

3. Create `.flaskenv` file in the main folder of the project, and paste the following content inside:

    ```
    FLASK_DEBUG=true
    FLASK_RUN_PORT=5000
    FLASK_RUN_HOST=127.0.0.1
    ```

4. Start your application locally to test the database connection: `flask run`

5. Open web application `http://127.0.0.1/query1`, then `/query2`

6. Test `/query3`. You can edit existing addresses, create new addressess, and delete addressess. Due to sample database restrictions, you will be able to delete only addresses created by you.

