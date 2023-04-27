import email
import hashlib
import os
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
    password = request.form['Password']
    salt = os.urandom(16).hex()
    password_hash = hash_password(password, salt)

    # Get a connection from the pool
    cnx = pool.get_connection()

    # Insert the customer data into the database
    cursor = cnx.cursor()
    query = "INSERT INTO Customer (First, Middle, Last, DOB, Gender, Passport_Number, Phone_Number, Email_Address, Password, Salt) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (first, middle, last, dob, gender, passport_number, phone_number, email_address, password_hash, salt)
    print(f"Received data: {first}, {middle}, {last}, {dob}, {gender}, {passport_number}, {phone_number}, {email_address}, {password_hash}")
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
    password = request.json.get("password")
    print("LOGIN FUNCTION CALLED")

    
    try:
        cnx = pool.get_connection()

        cursor = cnx.cursor()
        query = f"SELECT * FROM Customer WHERE Email_Address='{email}'"
        cursor.execute(query)
        customer = cursor.fetchone()

        print(customer[10]) #salt
        print(customer[9]) #password

        if customer and hash_password(password, customer[10]) == customer[9]:
            return jsonify({"success": True})
        else:
            return jsonify({"success": False, "message": "Incorrect credentials"})
    except Error as e:
        print("Error while connecting to MySQL using Connection pool ", e)
    finally:
        # Release the connection back to the pool
        cnx.close()

# Hashes the password using the specified salt
def hash_password(password, salt):
    return hashlib.sha256(password.encode('utf-8') + salt.encode('utf-8')).hexdigest()


# Hashes the password using the specified salt
def hash_password(password, salt):
    return hashlib.sha256(password.encode('utf-8') + salt.encode('utf-8')).hexdigest()




@app.route('/admin_login', methods=["POST"])
def admin_login():
    email_or_username = request.json.get("email_or_username")
    password = request.json.get("password")
    print("ADMIN LOGIN FUNCTION CALLED")
    try:
        cnx = pool.get_connection()
        cursor = cnx.cursor()

        if email_or_username == "admin" and password == "pass":
            return jsonify({"success": True})

        if not email_or_username.endswith("@airlineadmin.com"):
            return jsonify({"success": False, "message": "Incorrect credentials"})

        query = f"SELECT * FROM Employee WHERE Email_Address='{email_or_username}' AND Role='Admin'"
        cursor.execute(query)
        employee = cursor.fetchone()

        if employee and hash_password(password, employee[13]) == employee[12]:
            return jsonify({"success": True})
        else:
            return jsonify({"success": False, "message": "Incorrect credentials"})
    except Error as e:
        print("Error while connecting to MySQL using Connection pool ", e)
    finally:
        # Release the connection back to the pool
        cnx.close()



if __name__ == '__main__':
    app.run(debug=True)

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
    airport_code = request.form['Airport_Code']
    password = request.form['Password']
    salt = os.urandom(16).hex()
    password_hash = hash_password(password, salt)
    

    # Get a connection from the pool
    cnx = pool.get_connection()

    # Insert the customer data into the database
    cursor = cnx.cursor()
    query = "INSERT INTO Employee (First, Middle, Last, DOB, Gender, Role, Wage, Hire_Date, Email_Address, Airport_Code, Password, Salt) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (first, middle, last, dob, gender, role, wage, hire_date, email_address, airport_code, password_hash, salt)
    print(f"Received data: {first}, {middle}, {last}, {dob}, {gender}, {role}, {wage}, {hire_date}, {email_address}, {airport_code}, {password}")
    cursor.execute(query, values)

    cnx.commit()

    # Release the connection back to the pool
    cursor.close()
    cnx.close()

    # Return a success message
    return jsonify({'status': 'success'})

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

@app.route("/customer_change_password", methods=["POST"])
def customer_change_password():
    email = request.json.get("email")
    password = request.json.get("password")
    newPassword = request.json.get("newpassword")
    print("CHANGE PASSWORD FUNCTION CALLED")

    
    try:
        cnx = pool.get_connection()

        cursor = cnx.cursor()
        query = f"SELECT * FROM Customer WHERE Email_Address='{email}'"
        cursor.execute(query)
        customer = cursor.fetchone()

        print(customer[10]) #salt
        print(customer[9]) #password

        if customer and hash_password(password, customer[10]) == customer[9]:
            query = f"UPDATE Customer SET Password = '{hash_password(newPassword, customer[10])}' WHERE Email_Address='{email}'"
            cursor.execute(query)
            return jsonify({"success": True})
        else:
            return jsonify({"success": False, "message": "Incorrect credentials"})
    except Error as e:
        print("Error while connecting to MySQL using Connection pool ", e)
    finally:
        # Release the connection back to the pool
        cnx.close()

@app.route("/employee_change_password", methods=["POST"])
def employee_change_password():
    email = request.json.get("email")
    password = request.json.get("password")
    newPassword = request.json.get("newpassword")
    print("CHANGE PASSWORD FUNCTION CALLED")
    
    try:
        cnx = pool.get_connection()

        cursor = cnx.cursor()
        query = f"SELECT * FROM Employee WHERE Email_Address='{email}'"
        cursor.execute(query)
        employee = cursor.fetchone()

        print(employee[10]) #salt
        print(employee[9]) #password

        if employee and hash_password(password, employee[10]) == employee[9]:
            query = f"UPDATE Employee SET Password = '{hash_password(newPassword, employee[10])}' WHERE Email_Address='{email}'"
            cursor.execute(query)
            return jsonify({"success": True})
        else:
            return jsonify({"success": False, "message": "Incorrect credentials"})
    except Error as e:
        print("Error while connecting to MySQL using Connection pool ", e)
    finally:
        # Release the connection back to the pool
        cnx.close()

@app.route("/employee_login", methods=["POST"])
def customer_login():
    email = request.json.get("email")
    password = request.json.get("password")
    print("LOGIN FUNCTION CALLED")

    
    try:
        cnx = pool.get_connection()

        cursor = cnx.cursor()
        query = f"SELECT * FROM Employee WHERE Email_Address='{email}'"
        cursor.execute(query)
        employee = cursor.fetchone()

        print(employee[10]) #salt
        print(employee[9]) #password

        if employee and hash_password(password, employee[10]) == employee[9]:
            return jsonify({"success": True})
        else:
            return jsonify({"success": False, "message": "Incorrect credentials"})
    except Error as e:
        print("Error while connecting to MySQL using Connection pool ", e)
    finally:
        # Release the connection back to the pool
        cnx.close()

if __name__ == "__main__":
    app.run(debug=True)
