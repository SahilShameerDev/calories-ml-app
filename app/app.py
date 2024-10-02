# Importing required modules from Flask, for handling web requests and enabling CORS
from flask import Flask, request, jsonify
from flask_cors import CORS
# Importing json module for handling JSON data and mysql.connector for MySQL database connections
import json
import mysql.connector
# Importing random and string modules for generating random business IDs
import random
import string

# Creating a Flask application instance
app = Flask(__name__)
# Enabling CORS for the Flask application
CORS(app)

# Database configuration dictionary
db_config = {
    'host' : 'localhost',
    'user':'root',
    'password' : '',
    'database' : 'ml'
}

# Function to get a connection to the MySQL database
def get_db_connection():
    return mysql.connector.connect(**db_config)

# Function to generate a business ID based on the user's email
def generate_buisness_id(email):
    email_prefix = email.split('@')[0]  # Get the part of the email before the '@'
    random_num = ''.join(random.choices(string.digits, k=5))  # Generate a random 5-digit number
    return f"{email_prefix}_{random_num}"  # Combine the email prefix and random number to create a business ID

# Route for the root endpoint
@app.route('/root', methods=['GET'])
def root():
    return jsonify({
        'statusCode': 'SC0000',
        "statusDescription": "Success",
        'message': 'Hello World'
    })

# Route for user registration
@app.route('/authAdapter', methods=['POST'])
def authAdapter():
    try:
        # Get JSON data from the request
        data = request.get_json()
        fullName = data.get('full_name')
        email = data.get('email')
        password = data.get('password')

        # Check if all required fields are provided and not empty
        if(fullName and email and password and fullName != "" and email != "" and password != "" and fullName != "NA" and email != "NA" and password != "NA"):
            # Check if the user already exists in the database
            connection = get_db_connection()
            cursor = connection.cursor()
            cursor.execute("SELECT COUNT(*) FROM user WHERE Email = %s",(email,))
            row = cursor.fetchone()
            connection.close()
            if row and row[0] > 0:
                # If user exists, return an error response
                return jsonify({
                    "statusDesc": "Failure",
                    "statusCode": {
                        "code": "F005"
                    },
                    "message": "User already exist"
                }), 400
            else:
                # If user does not exist, create a new user
                buisness_id = generate_buisness_id(email)  # Generate a business ID
                status = 1
                
                connection = get_db_connection()
                cursor = connection.cursor()
                cursor.execute("INSERT INTO user (Full_Name , Email , Password , Status , Business_ID) VALUES (%s, %s, %s, %s, %s)", [fullName, email, password, status, buisness_id])
                connection.commit()
                connection.close()
                
                # Return a success response
                return jsonify({
                    "statusDesc": "Success",
                    "statusCode": {
                        "code": "SC000"
                    },
                    "message": "User created successfully",
                    "param": {
                        "userEmail" : email,
                        "businessId" : buisness_id,
                        "status" : status
                    }
                })
        else:
            # If mandatory fields are missing, return an error response
            return jsonify({
                "statusDesc": "Failure",
                "statusCode": {
                    "code": "F005"
                },
                "message": "Some mandatory fields are missing"
            }), 400
    except Exception as e:
        # Return an error response if an exception occurs
        return jsonify({
            'error': str(e)
        }), 500

# Route for calculating BMI
@app.route('/BMI', methods=['POST'])
def BMI():
    try:
        # Get JSON data from the request
        data = request.get_json()
        height = data.get('height')
        gender = data.get('gender')
        actual_weight = data.get('actual_weight')
        desired_weight = data.get('desired_weight')
        purpose = data.get('purpose')
        age = data.get('age')
        activity = data.get('activity')
        buisness_id = data.get('buisness_id')
        
        # Check if all required fields are provided and not empty
        if(activity and height and gender and actual_weight and desired_weight and purpose and age and buisness_id and activity != "" and height != "" and gender != "" and actual_weight != "" and desired_weight != "" and purpose != "" and age != "" and buisness_id != "" and  activity != "NA" and height != "NA" and gender != "NA" and actual_weight != "NA" and desired_weight != "NA" and purpose != "NA" and age != "NA" and buisness_id != "NA"):
            if gender == "male":
                # Calculate BMR for males
                BMR = 10 * actual_weight + 6.25 * height - 5 * age + 5
                Calories = BMR * float(activity)
                if purpose == '0':
                    # Calculate target calories for purpose 0
                    ten_percent = Calories * 0.1
                    targetCalories = Calories + ten_percent
                    connection = get_db_connection()
                    cursor = connection.cursor()
                    cursor.execute("INSERT INTO bmr (BMR, targetCalories, buisness_ID) VALUES (%s, %s, %s)",[BMR,targetCalories, buisness_id])
                    connection.commit()
                    connection.close()
                    # Return a success response
                    return jsonify({
                        "statusDesc": "Success",
                        "statusCode": {
                            "code": "SC000"
                        },
                        "message": "BMI calculated successfully",
                        "param": {
                            "BMR" : BMR,
                            "targetCalories" : targetCalories
                        }
                    })
                elif purpose == '1':
                    # Calculate target calories for purpose 1
                    seventy_percent = Calories * 0.7
                    targetCalories = Calories + seventy_percent
                    connection = get_db_connection()
                    cursor = connection.cursor()
                    cursor.execute("INSERT INTO bmr (BMR, targetCalories, buisness_ID) VALUES (%s, %s, %s)",[BMR,targetCalories, buisness_id])
                    connection.commit()
                    connection.close()
                    # Return a success response
                    return jsonify({
                        "statusDesc": "Success",
                        "statusCode": {
                            "code": "SC000"
                        },
                        "message": "BMI calculated successfully",
                        "param": {
                            "BMR" : BMR,
                            "targetCalories" : targetCalories
                        }
                    })
                    
            elif gender == "female":
                # Calculate BMR for females
                BMR = 10 * actual_weight + 6.25 * height - 5 * age - 161
                Calories = BMR * float(activity)
                if purpose == '0':
                    # Calculate target calories for purpose 0 (maintenance or slight weight gain)
                    ten_percent = Calories * 0.1
                    targetCalories = Calories + ten_percent
                elif purpose == '1':
                    # Calculate target calories for purpose 1 (weight gain)
                    seventy_percent = Calories * 0.7
                    targetCalories = Calories + seventy_percent
                
                # Insert the calculated BMR and targetCalories into the database
                connection = get_db_connection()
                cursor = connection.cursor()
                cursor.execute("INSERT INTO bmr (BMR, targetCalories, buisness_ID) VALUES (%s, %s, %s)", [BMR, targetCalories, buisness_id])
                connection.commit()
                connection.close()     
                
                # Return a success response
                return jsonify({
                    "statusDesc": "Success",
                    "statusCode": {
                        "code": "SC000"
                    },
                    "message": "BMI calculated successfully",
                    "param": {
                        "BMR": BMR,
                        "targetCalories": targetCalories
                    }
                })

        else:
                # If mandatory fields are missing, return an error response
                return jsonify({
                    "statusDesc": "Failure",
                    "statusCode": {
                        "code": "F005"
                    },
                    "message": "Some mandatory fields are missing"
                }), 400
        
    except Exception as e:
        # Return an error response if an exception occurs
        return jsonify({
            'error': str(e)
        }), 500

# Run the Flask application on host 0.0.0.0 and port 3000 in debug mode
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
