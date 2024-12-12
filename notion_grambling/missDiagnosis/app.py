from flask import Flask, request, render_template, jsonify
from main import the_main

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/submit_record', methods=['POST'])
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

    the_response = the_main(patient_symptoms= symptoms, malaria_status="infected")
    print(the_response)
    return jsonify({'alert_message': the_response})

    # return render_template('dashboard.html', alert_message=the_response)
    print("------------------------\n")
    print(the_response)


    # Print the collected data in the terminal
    # print("\n--- New Medical Record ---")
    # print(f"Patient Name: {patient_name}")
    # print(f"Date of Birth: {dob}")
    # print(f"Symptoms: {symptoms}")
    # print(f"Diagnosis: {diagnosis}")
    # print("Prescription Details:")
    # print(f"  Medicine: {medicine}")
    # print(f"  Dosage: {dosage}")
    # print(f"  Frequency: {frequency}")
    # print(f"  Duration: {duration}")
    # print(f"Medical History: {medical_history}")
    # print(f"Allergies: {allergies}")
    # print(f"Tests Required: {tests_required}")
    print("------------------------\n")

    return 

    # Return a simple confirmation message


if __name__ == '__main__':
    app.run(debug=True)