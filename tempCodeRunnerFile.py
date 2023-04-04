 if mydb.is_connected():
        # Get the customer data
        cursor = mydb.cursor()
        cursor.execute("SHOW TABLES")