@app.route("/customer_login", methods=["POST"])
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