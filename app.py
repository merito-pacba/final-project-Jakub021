import os
import pyodbc
from flask import Flask, render_template, request, url_for, redirect
from dotenv import load_dotenv

load_dotenv()

port = os.environ.get("PORT", "5000")

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/query1")
def query1():
    conn_str = os.environ.get("CONN_STR")
    conn = pyodbc.connect(conn_str)
    with conn.cursor() as cursor:
        cursor.execute("SELECT TOP (10) * FROM [SalesLT].[Address]")
        rows = cursor.fetchall()
    conn.close()
    return render_template("query1result.html", rows=rows)


@app.route("/query2")
def query2():
    conn_str = os.environ.get("CONN_STR")
    conn = pyodbc.connect(conn_str)
    with conn.cursor() as cursor:
        cursor.execute("""SELECT [AddressID],
                                [AddressLine1],
                                [City]
                            FROM [SalesLT].[Address]
                            ORDER BY [AddressID] DESC""")
        rows = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
    conn.close()
    return render_template("query2result.html", rows=rows, columns=columns)


@app.route("/query3")
def query3():
    conn_str = os.environ.get("CONN_STR")
    conn = pyodbc.connect(conn_str)
    with conn.cursor() as cursor:
        cursor.execute("""SELECT [AddressID],
                                [AddressLine1],
                                [City]
                            FROM [SalesLT].[Address]
                            ORDER BY [AddressID] DESC""")
        rows = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
    conn.close()
    return render_template("query3result.html", rows=rows, columns=columns)


@app.route("/edit/<int:address_id>", methods=['POST', 'GET'])
def edit(address_id):
    conn_str = os.environ.get("CONN_STR")
    conn = pyodbc.connect(conn_str)
    if request.method == 'GET':
        with conn.cursor() as cursor:
            cursor.execute(f"""SELECT [AddressID],
                                [AddressLine1],
                                [City],
                                [StateProvince],
                                [CountryRegion],
                                [PostalCode]
                            FROM [SalesLT].[Address]
                            WHERE [AddressID]='{address_id}'""")
            row = cursor.fetchone()
            return render_template("edit.html", row=row)
    else:
        with conn.cursor() as cursor:
            cursor.execute("""UPDATE [SalesLT].[Address]
                SET [AddressLine1] = ?, [City] = ?
                WHERE [AddressID] = ?""",
                           (request.form['addressline1'], request.form['city'], address_id))
            conn.commit()
        conn.close()
        return redirect(url_for('query3'))


@app.route("/delete/<int:address_id>")
def delete_address(address_id):
    conn_str = os.environ.get("CONN_STR")
    conn = pyodbc.connect(conn_str)
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM [SalesLT].[Address] WHERE [AddressID] = ?", (address_id,))
        conn.commit()
    conn.close()
    return redirect(url_for('query2'))


@app.route("/insert", methods=['POST', 'GET'])
def insert():
    conn_str = os.environ.get("CONN_STR")
    conn = pyodbc.connect(conn_str)
    if request.method == 'GET':
        return render_template("insert.html")
    else:
        with conn.cursor() as cursor:
            cursor.execute("""INSERT INTO [SalesLT].[Address] 
                (AddressLine1, City, StateProvince, CountryRegion, PostalCode, ModifiedDate) 
                VALUES (?, ?, 'province', 'region', '0000', '2006-07-01 00:00:00.000' )""",
                           (request.form['addressline1'], request.form['city']))
            conn.commit()
        conn.close()
        return redirect(url_for('query3'))


@app.route("/search", methods=['GET'])
def search():
    query = request.args.get('query')
    conn_str = os.environ.get("CONN_STR")
    conn = pyodbc.connect(conn_str)
    with conn.cursor() as cursor:
        cursor.execute("""SELECT [AddressID], [AddressLine1], [City]
                          FROM [SalesLT].[Address]
                          WHERE [AddressLine1] LIKE ? OR [City] LIKE ?""",
                       ('%' + query + '%', '%' + query + '%'))
        rows = cursor.fetchall()
    conn.close()
    return render_template("query1result.html", rows=rows)


if __name__ == "__main__":
    app.run(debug=True, port=port)
