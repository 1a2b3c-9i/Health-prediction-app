from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import pickle

app = Flask(__name__)

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///patients.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Load ML Model
model = pickle.load(open('model.pkl', 'rb'))

# Database Model
class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100))
    dob = db.Column(db.String(20))
    email = db.Column(db.String(100))
    glucose = db.Column(db.Float)
    haemoglobin = db.Column(db.Float)
    cholesterol = db.Column(db.Float)
    remarks = db.Column(db.String(200))

# Create Database
with app.app_context():
    db.create_all()

# Home Page - Read Records
@app.route('/')
def index():
    patients = Patient.query.all()
    return render_template('index.html', patients=patients)

# Add Patient - Create Record
@app.route('/add', methods=['GET', 'POST'])
def add():

    if request.method == 'POST':

        name = request.form['name']
        dob = request.form['dob']
        email = request.form['email']

        glucose = float(request.form['glucose'])
        haemoglobin = float(request.form['haemoglobin'])
        cholesterol = float(request.form['cholesterol'])

        prediction = model.predict(
            [[glucose, haemoglobin, cholesterol]]
        )[0]

        patient = Patient(
            full_name=name,
            dob=dob,
            email=email,
            glucose=glucose,
            haemoglobin=haemoglobin,
            cholesterol=cholesterol,
            remarks=prediction
        )

        db.session.add(patient)
        db.session.commit()

        return redirect('/')

    return render_template('add.html')

# Edit Patient - Update Record
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):

    patient = Patient.query.get_or_404(id)

    if request.method == 'POST':

        patient.full_name = request.form['name']
        patient.dob = request.form['dob']
        patient.email = request.form['email']

        patient.glucose = float(request.form['glucose'])
        patient.haemoglobin = float(request.form['haemoglobin'])
        patient.cholesterol = float(request.form['cholesterol'])

        patient.remarks = model.predict(
            [[
                patient.glucose,
                patient.haemoglobin,
                patient.cholesterol
            ]]
        )[0]

        db.session.commit()

        return redirect('/')

    return render_template('edit.html', patient=patient)

# Delete Patient - Delete Record
@app.route('/delete/<int:id>')
def delete(id):

    patient = Patient.query.get_or_404(id)

    db.session.delete(patient)
    db.session.commit()

    return redirect('/')

# Run Application
if __name__ == "__main__":
    app.run(debug=True)