

# Calories Calculation App

## About the Project

This project is a **calories calculation app** developed as part of a college project. It is designed to assist users in managing their calorie intake and achieving their fitness goals by calculating BMI, BMR, and target calorie requirements based on user input. The app includes user registration, login, and calorie-tracking functionalities.

The project is implemented using **Flask** for the backend and a trained Convolutional Neural Network (CNN) model to identify food items. The final version of the app will include an integrated frontend and backend for a complete user experience.

---

## Features Implemented So Far

### Backend:
1. **User Registration:**
   - Users can register by providing their name, email, and password.
   - A unique business ID is generated for each user.
   - User details are stored in a MySQL database.

2. **User Login & Logout:**
   - Users can log in using their email and password.
   - Basic authentication implemented to validate credentials.

3. **BMI Calculation:**
   - Calculates Basal Metabolic Rate (BMR) and target calorie requirements based on user inputs like height, weight, age, gender, activity level, and purpose (e.g., weight gain or maintenance).
   - Stores BMI data in the database.

4. **Endpoints with JSON Responses:**
   - `/authAdapter`: User registration.
   - `/BMI`: BMI and calorie calculations.
   - `/login`: User authentication.
   - `/logout`: Logout simulation.

5. **Database Integration:**
   - MySQL database for storing user and BMI data.

### Model Training:
- Trained a **CNN model** (see `cnn_model.ipynb`) to identify food items based on images. This model will be integrated to provide calorie details for detected food items.

---

## Current Progress

### Completed:
- Backend development for core functionalities.
- User authentication and BMI calculation logic.
- Database integration with user and BMI data storage.
- Model training for food item recognition.

### Pending Tasks:
1. **Model Integration:**
   - Integrate the CNN model into the backend to enable food item recognition.
   - Implement endpoints to receive food images and return detected items along with calorie details.

2. **Frontend Development:**
   - Design and implement a user-friendly frontend interface.
   - Ensure smooth interaction between the frontend and backend.

3. **Final Integration:**
   - Connect the backend, frontend, and trained model to create a cohesive app.

4. **Testing & Deployment:**
   - Conduct thorough testing of the complete app.
   - Deploy the app for use.

---

## Installation and Setup Instructions

1. Clone the repository.
2. Set up the MySQL database:
   - Create a database named `ml`.
   - Import the required database schema (provided separately).
3. Install the dependencies:
   ```bash
   pip install flask flask-cors mysql-connector-python
   ```
4. Run the Flask app:
   ```bash
   python app.py
   ```
5. Open the CNN model notebook (`cnn_model.ipynb`) for food item detection and train if required.

---


