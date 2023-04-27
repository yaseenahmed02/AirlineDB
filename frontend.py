import email
from flask import Flask, render_template, request, jsonify
import mysql.connector
from mysql.connector import pooling, Error

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
    return render_template(f"{selected_table}")

def encrypt(data):
  key = "secret"
  encrypted_data = []
  for i, char in enumerate(data):
      key_char = key[i % len(key)]
      encrypted_char = chr(ord(char) ^ ord(key_char))
      encrypted_data.append(encrypted_char)
  encrypted_string = ''.join(encrypted_data)
  return encrypted_string

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
    password = encrypt(request.form['Password'])

    # Get a connection from the pool
    cnx = pool.get_connection()

    # Insert the customer data into the database
    cursor = cnx.cursor()
    query = "INSERT INTO Customer (First, Middle, Last, DOB, Gender, Passport_Number, Phone_Number, Email_Address, Password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (first, middle, last, dob, gender, passport_number, phone_number, email_address, password)
    print(f"Received data: {first}, {middle}, {last}, {dob}, {gender}, {passport_number}, {phone_number}, {email_address}, {password}")
    cursor.execute(query, values)

    cnx.commit()

    # Release the connection back to the pool
    cursor.close()
    cnx.close()

    # Return a success message
    return jsonify({'status': 'success'})

@app.route('/add_employee_data', methods=['POST'])
def add_employee_data():
    print(request.form)
    # Extract the data from the request
    first = request.form['First']
    middle = request.form['Middle']
    last = request.form['Last']
    dob = request.form['DOB']
    gender = request.form['Gender']
    role = request.form['Role']
    wage = request.form['Wage']
    hire_date = request.form['Hire_Date']
    email_address = request.form['Email_Address']
    airport_code = encrypt(request.form['Airport_Code'])

    # Get a connection from the pool
    cnx = pool.get_connection()

    # Insert the customer data into the database
    cursor = cnx.cursor()
    query = "INSERT INTO Employee (First, Middle, Last, DOB, Gender, Role, Wage, Hire_Date, Email_Address, Airport_Code) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (first, middle, last, dob, gender, role, wage, hire_date, email_address, airport_code)
    print(f"Received data: {first}, {middle}, {last}, {dob}, {gender}, {role}, {wage}, {hire_date}, {email_address}, {airport_code}")
    cursor.execute(query, values)

    cnx.commit()

    # Release the connection back to the pool
    cursor.close()
    cnx.close()

    # Return a success message
    return jsonify({'status': 'success'})

@app.route("/customer_login", methods=["POST"])
def customer_login():
    email = request.json.get("email")
    password = encrypt(request.json.get("password"))
    print("LOGIN FUNCTION CALLED")
    try:
        cnx = pool.get_connection()

        cursor = cnx.cursor()
        query = f"SELECT * FROM Customer WHERE Email_Address='{email}' AND Password='{password}'"
        cursor.execute(query)
        customer = cursor.fetchone()

        if customer:
            return jsonify({"success": True})
        else:
            return jsonify({"success": False, "message": "Incorrect credentials"})
    except Error as e:
        print("Error while connecting to MySQL using Connection pool ", e)
    finally:
        # Release the connection back to the pool
        cnx.close()

@app.route('/admin_login', methods=["POST"])
def admin_login():
    email = request.json.get("email")
    password = encrypt(request.json.get("password"))
    print("ADMIN LOGIN FUNCTION CALLED")
    try:
        cnx = pool.get_connection()

        cursor = cnx.cursor()
        query = f"SELECT * FROM Employee WHERE Email_Address='{email}' AND Password='{password}' AND Role='Admin'"
        cursor.execute(query)
        customer = cursor.fetchone()

        if customer:
            return jsonify({"success": True})
        else:
            return jsonify({"success": False, "message": "Incorrect credentials"})
    except Error as e:
        print("Error while connecting to MySQL using Connection pool ", e)
    finally:
        # Release the connection back to the pool
        cnx.close()

@app.route('/customer_data')
def get_customer_data():
    cnx = pool.get_connection()
    cursor = cnx.cursor()
    query = ("SELECT * FROM Customer")
    cursor.execute(query)
    data = cursor.fetchall()
    column_names = [desc[0] for desc in cursor.description]  # Get column names
    cursor.close()
    cnx.close()

    # Convert tuples to list of dictionaries
    data = [dict(zip(column_names, row)) for row in data]

    return jsonify(data)

@app.route('/employee_data')
def get_employee_data():
    cnx = pool.get_connection()
    cursor = cnx.cursor()
    query = ("SELECT * FROM Employee")
    cursor.execute(query)
    data = cursor.fetchall()
    column_names = [desc[0] for desc in cursor.description]  # Get column names
    cursor.close()
    cnx.close()

    # Convert tuples to list of dictionaries
    data = [dict(zip(column_names, row)) for row in data]

    return jsonify(data)


@app.route('/delete_customer', methods=['POST'])
def delete_customer():
    customer_id = request.form['customerId']
    print(customer_id)
    cnx = pool.get_connection()
    cursor = cnx.cursor()
    query = "DELETE FROM Customer WHERE ID = %s"
    cursor.execute(query, (customer_id,))
    cnx.commit()
    cursor.close()
    cnx.close()
    return "Customer deleted successfully"

@app.route('/delete_employee', methods=['POST'])
def delete_employee():
    employee_id = request.form['employeeId']
    print(employee_id)
    cnx = pool.get_connection()
    cursor = cnx.cursor()
    query = "DELETE FROM Employee WHERE ID = %s"
    cursor.execute(query, (employee_id,))
    cnx.commit()
    cursor.close()
    cnx.close()
    return "Employee deleted successfully"

from datetime import datetime

@app.route('/flight_data')
def get_flight_data():
    cnx = pool.get_connection()
    cursor = cnx.cursor()
    query = ("SELECT * FROM Flight Order By Flight_Number ASC")
    cursor.execute(query)
    data = cursor.fetchall()
    column_names = [desc[0] for desc in cursor.description]  # Get column names
    cursor.close()
    cnx.close()

    # Convert tuples to list of dictionaries
    data = [dict(zip(column_names, row)) for row in data]

    # Convert timedelta objects to strings
    for flight in data:
        flight["Departure_Time"] = str(flight["Departure_Time"])
        flight["Arrival_Time"] = str(flight["Arrival_Time"])

    return jsonify(data)


@app.route('/delete_flight', methods=['POST'])
def delete_flight():
    flight_number = request.form.get('flight_number')
    date = request.form.get('date')

    cnx = pool.get_connection()
    cursor = cnx.cursor()
    query = "DELETE FROM Flight WHERE Flight_Number = %s AND Date = %s"
    cursor.execute(query, (flight_number, date))
    cnx.commit()
    cursor.close()
    cnx.close()

    return "Flight information deleted successfully"




if __name__ == "__main__":
    app.run(debug=True)
