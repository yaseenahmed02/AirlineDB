from flask import Flask, render_template, request, jsonify
import mysql.connector
from mysql.connector import pooling

app = Flask(__name__)

# Create a database connection pool
dbconfig = {
  "host": "sql9.freemysqlhosting.net",
  "user": "sql9610598",
  "password": "1Fpa25RFZ1",
  "database": "sql9610598"
}
pool = pooling.MySQLConnectionPool(pool_name="mypool", pool_size=5, **dbconfig)

@app.route("/")
def home():
    # Get a connection from the pool
    cnx = pool.get_connection()

    # Get the customer data
    cursor = cnx.cursor()
    cursor.execute("SHOW TABLES")
    tables = [table[0] for table in cursor.fetchall()]

    # Release the connection back to the pool
    cnx.close()

    # Render the template with the tables data
    return render_template("index.html", tables=tables)

@app.route("/<selected_table>")
def display_table(selected_table):
    return render_template(f"{selected_table}.html")

@app.route('/add_customer_data', methods=['POST'])
def add_customer_data():
    print(request.form)

    # Extract the data from the request
    first = request.form['First']
    middle = request.form['Middle']
    last = request.form['Last']
    dob = request.form['DOB']
    gender = request.form['Gender']
    passport_number = request.form['Passport_Number']
    phone_number = request.form['Phone_Number']
    email_address = request.form['Email_Address']

    # Print the data received
    print(f"Received data: {first}, {middle}, {last}, {dob}, {gender}, {passport_number}, {phone_number}, {email_address}")

    # Get a connection from the pool
    cnx = pool.get_connection()

    # Insert the customer data into the database
    cursor = cnx.cursor()
    query = "INSERT INTO Customer (First, Middle, Last, DOB, Gender, Passport_Number, Phone_Number, Email_Address) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    values = (first, middle, last, dob, gender, passport_number, phone_number, email_address)
    cursor.execute(query, values)
    cnx.commit()

    # Release the connection back to the pool
    cnx.close()

    # Return a success message
    return jsonify({'status': 'success'})

if __name__ == "__main__":
    app.run(debug=True)
