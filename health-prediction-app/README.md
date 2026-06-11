# Health Prediction Application

## Project Overview

The Health Prediction Application is a Flask-based web application designed to manage patient health records and generate health risk predictions using a Machine Learning model. The system allows users to perform complete CRUD (Create, Read, Update, Delete) operations on patient data and automatically predicts potential health risks based on blood test parameters.

---

## Features

* Create Patient Records
* View Patient Records
* Update Existing Records
* Delete Patient Records
* Machine Learning-Based Health Prediction
* SQLite Database Integration
* Responsive Bootstrap User Interface
* Automatic Prediction Generation in Remarks Field

---

## Technology Stack

### Backend

* Python
* Flask
* SQLAlchemy

### Database

* SQLite

### Machine Learning

* Scikit-Learn
* Random Forest Classifier

### Frontend

* HTML
* Bootstrap 5

---

## Input Parameters

The application collects the following patient information:

* Full Name
* Date of Birth
* Email Address
* Glucose Level
* Haemoglobin Level
* Cholesterol Level

Based on the entered values, the Machine Learning model predicts a possible health condition and stores the result in the Remarks field.

---

## Project Structure

health-prediction-app/

├── app.py

├── train_model.py

├── model.pkl

├── patient_data.csv

├── requirements.txt

├── templates/

│   ├── index.html

│   ├── add.html

│   └── edit.html

├── screenshots/

│   ├── dashboard.png

│   ├── add_patient.png

│   └── prediction_result.png

└── README.md

---

## Installation and Setup

### Step 1: Clone Repository

git clone <repository-url>

### Step 2: Install Dependencies

pip install -r requirements.txt

### Step 3: Train Model

python train_model.py

### Step 4: Run Application

python app.py

### Step 5: Open Browser

http://127.0.0.1:5000

---

## Screenshots


* Dashboard Page
* Add Patient Form
* Edit Patient Form
* Prediction Result

---

## Future Enhancements

* AI-generated detailed medical remarks
* Advanced health analytics dashboard
* External Health API Integration
* User Authentication and Authorization
* Cloud Deployment

---

## Author

Niveditha J


