import email
import hashlib
import os
from flask import Flask, render_template, request, jsonify
import mysql.connector
from mysql.connector import pooling, Error

app = Flask(__name__, static_folder='static')

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
    cnx.close()

    # Return a success message
    return jsonify({'status': 'success'})




# # Hashes the password using the specified salt
# def hash_password(password, salt):
#     return hashlib.sha256(password.encode('utf-8') + salt.encode('utf-8')).hexdigest()


# @app.route('/admin_login', methods=["POST"])
# def admin_login():
#     email_or_username = request.json.get("email_or_username")
#     password = request.json.get("password")
#     print("ADMIN LOGIN FUNCTION CALLED")
#     try:
#         cnx = pool.get_connection()
#         cursor = cnx.cursor()

#         if email_or_username == "admin" and password == "pass":
#             return jsonify({"success": True})

#         if not email_or_username.endswith("@airlineadmin.com"):
#             return jsonify({"success": False, "message": "Incorrect credentials"})

#         query = f"SELECT * FROM Employee WHERE Email_Address='{email_or_username}' AND Role='Admin'"
#         cursor.execute(query)
#         employee = cursor.fetchone()

#         if employee and hash_password(password, employee[13]) == employee[12]:
#             return jsonify({"success": True})
#         else:
#             return jsonify({"success": False, "message": "Incorrect credentials"})
#     except Error as e:
#         print("Error while connecting to MySQL using Connection pool ", e)
#     finally:
#         # Release the connection back to the pool
#         cnx.close()



@app.route('/customer_login', methods=['POST'])
def customer_login():
    email = request.json.get("email")
    password = request.json.get("password")
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

@app.route('/add_flight_data', methods=['POST'])
def add_flight_data():
    print(request.form)
    # Extract the data from the request
    flight_number = request.form['Flight_Number']
    date = request.form['Date']
    num_passengers = request.form['Num_Passengers']
    num_crew = request.form['Num_Crew']
    departure_time = request.form['Departure_Time']
    arrival_time = request.form['Arrival_Time']
    status = request.form['Status']
    tail_num = request.form['Tail_Num']

    # Get a connection from the pool
    cnx = pool.get_connection()

    # Insert the customer data into the database
    cursor = cnx.cursor()
    query = "INSERT INTO Flight (Flight_Number, Date, Num_Passengers, Num_Crew, Departure_Time, Arrival_Time, Status, Tail_Num) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    values = (flight_number, date, num_passengers, num_crew, departure_time, arrival_time, status, tail_num)
    print(f"Received data: {flight_number}, {date}, {num_passengers}, {num_crew}, {departure_time}, {arrival_time}, {status}, {tail_num}")
    cursor.execute(query, values)

    cnx.commit()

    # Release the connection back to the pool
    cursor.close()
    cnx.close()

    # Return a success message
    return jsonify({'status': 'success'})

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
#    date = request.form.get('date')

    cnx = pool.get_connection()
    cursor = cnx.cursor()
    query = "DELETE FROM Flight WHERE Flight_Number = %s"
    cursor.execute(query, (flight_number,))
    cnx.commit()
    cursor.close()
    cnx.close()

    return "Flight information deleted successfully"


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


@app.route('/ticket_data')
def get_ticket_data():
    cnx = pool.get_connection()
    cursor = cnx.cursor()
    query = ("SELECT * FROM Ticket")
    cursor.execute(query)
    data = cursor.fetchall()
    column_names = [desc[0] for desc in cursor.description]  # Get column names
    cursor.close()
    cnx.close()

    # Convert tuples to list of dictionaries
    data = [dict(zip(column_names, row)) for row in data]

    return jsonify(data)


@app.route('/luggage_data')
def get_luggage_data():
    cnx = pool.get_connection()
    cursor = cnx.cursor()
    query = ("SELECT * FROM Baggage")
    cursor.execute(query)
    data = cursor.fetchall()
    column_names = [desc[0] for desc in cursor.description]  # Get column names
    cursor.close()
    cnx.close()

    # Convert tuples to list of dictionaries
    data = [dict(zip(column_names, row)) for row in data]

    return jsonify(data)


@app.route('/add_employee_data', methods=['POST'])
def add_employee_data():
    print(request.form)
    cursor.execute("")
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

    query = "SELECT MAX(ID) FROM Employee"
    cursor.execute(query)
    Id = cursor.fetchone()[0] + 1
    # salt = os.urandom(16).hex()
    # password_hash = hash_password(password, salt)
    

    # Get a connection from the pool
    cnx = pool.get_connection()

    # Insert the customer data into the database
    cursor = cnx.cursor()
    query = "INSERT INTO Employee (ID, First, Middle, Last, DOB, Gender, Role, Wage, Hire_Date, Email_Address, Airport_Code, Password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (Id, first, middle, last, dob, gender, role, wage, hire_date, email_address, airport_code, password)
    print(f"Received data: {first}, {middle}, {last}, {dob}, {gender}, {role}, {wage}, {hire_date}, {email_address}, {airport_code}")
    cursor.execute(query, values)

    cnx.commit()

    # Release the connection back to the pool
    cursor.close()
    cnx.close()

    # Return a success message
    return jsonify({'status': 'success'})


# @app.route("/customer_change_password", methods=["POST"])
# def customer_change_password():
#     email = request.json.get("email")
#     password = request.json.get("password")
#     newPassword = request.json.get("newpassword")
#     print("CHANGE PASSWORD FUNCTION CALLED")

    
#     try:
#         cnx = pool.get_connection()

#         cursor = cnx.cursor()
#         query = f"SELECT * FROM Customer WHERE Email_Address='{email}'"
#         cursor.execute(query)
#         customer = cursor.fetchone()


#         if customer and hash_password(password, customer[10]) == customer[9]:
#             query = f"UPDATE Customer SET Password = '{hash_password(newPassword, customer[10])}' WHERE Email_Address='{email}'"
#             cursor.execute(query)
#             return jsonify({"success": True})
#         else:
#             return jsonify({"success": False, "message": "Incorrect credentials"})
#     except Error as e:
#         print("Error while connecting to MySQL using Connection pool ", e)
#     finally:
#         # Release the connection back to the pool
#         cnx.close()

# @app.route("/admin_change_password", methods=["POST"])
# def admin_change_password():
#     email = request.json.get("email")
#     password = request.json.get("password")
#     newPassword = request.json.get("newpassword")
#     print("CHANGE PASSWORD FUNCTION CALLED")

    
#     try:
#         cnx = pool.get_connection()

#         cursor = cnx.cursor()
#         query = f"SELECT * FROM Employee WHERE Email_Address='{email}'"
#         cursor.execute(query)
#         customer = cursor.fetchone()


#         if customer and hash_password(password, customer[10]) == customer[9]:
#             query = f"UPDATE Customer SET Password = '{hash_password(newPassword, customer[10])}' WHERE Email_Address='{email}'"
#             cursor.execute(query)
#             return jsonify({"success": True})
#         else:
#             return jsonify({"success": False, "message": "Incorrect credentials"})
#     except Error as e:
#         print("Error while connecting to MySQL using Connection pool ", e)
#     finally:
#         # Release the connection back to the pool
#         cnx.close()


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



if __name__ == "__main__":
    app.run(debug=True)
