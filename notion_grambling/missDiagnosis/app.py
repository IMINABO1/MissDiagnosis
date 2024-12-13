from flask import Flask, request, render_template, jsonify
from main import the_main

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/dashboard', methods=['POST'])
def submit_record():
    # Collect data from the form
    patient_name = request.form.get('patient_name', '')
    dob = request.form.get('dob', '')
    symptoms = request.form.get('symptoms', '')
    diagnosis = request.form.get('diagnosis', '')
    medicine = request.form.get('medicine', '')
    dosage = request.form.get('dosage', '')
    frequency = request.form.get('frequency', '')
    duration = request.form.get('duration', '')
    medical_history = request.form.get('medical_history', '')
    allergies = request.form.get('allergies', '')
    tests_required = request.form.get('tests_required', '')

    the_response = the_main(patient_symptoms=symptoms, malaria_status="infected")
    print(the_response)
    return jsonify({'alert_message': the_response})

if __name__ == '__main__':
    app.run(debug=True)