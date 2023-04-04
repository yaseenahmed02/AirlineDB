from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

@app.route("/")
def home():
    # Connect to MySQL database
    mydb = mysql.connector.connect(
        host="sql9.freemysqlhosting.net",
        user="sql9610598",
        password="1Fpa25RFZ1",
        database="sql9610598"
    )

    # Check if connection was successful
    if mydb.is_connected():
        # Get the customer data
        cursor = mydb.cursor()
        cursor.execute("SHOW TABLES")
        tables = [table[0] for table in cursor.fetchall()]
        
        # Render the template with the tables data
        return render_template("index.html", tables=tables)
    else:
        return render_template("index.html", message="Failed to Connect to Database")

@app.route("/<selected_table>")
def display_table(selected_table):
    return render_template(f"{selected_table}.html")

if __name__ == "__main__":
    app.run(debug=True)
