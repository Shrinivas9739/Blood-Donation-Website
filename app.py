from flask import Flask, render_template, request, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Database connection
def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='2444666668888888@',
            database='blood_group'
        )
        return connection
    except Error as e:
        print(f"Error connecting to the database: {e}")
        return None


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    try:
        # Collect data from the form
        name = request.form['name']
        department = request.form['department']
        usn = request.form['usn']
        year = request.form['year']
        blood_group = request.form['bloodGroup']
        contact = request.form['contact']
        email = request.form['email']
        age = request.form['age']

        # Connect to the database
        connection = get_db_connection()
        if connection is None:
            return jsonify({"message": "Database connection failed!"}), 500

        cursor = connection.cursor()

        # SQL query to insert data
        query = """
            INSERT INTO donors (Name, Department, USN, Year, BloodGroup, Contact, Email, Age)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (name, department, usn, year, blood_group, contact, email, age))

        # Commit the transaction
        connection.commit()

        # Close the cursor and connection
        cursor.close()
        connection.close()

        return jsonify({"message": "Thank you for donating blood."}), 200

    except Error as e:
        print(f"Error: {e}")
        return jsonify({"message": "An error occurred while processing your request! Check USN(Duplicate USN not allowed)."}), 500

    except Exception as e:
        print(f"Unexpected error: {e}")
        return jsonify({"message": "An unexpected error occurred!"}), 500


if __name__ == '__main__':
    app.run(debug=True)
