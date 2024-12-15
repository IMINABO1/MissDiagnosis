from flask import Flask, request, render_template, jsonify
from main import the_main
# from time import sleep

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/submit_response', methods=['POST'])
def submit_record():
    # Collect data from the form
    print("collecting")
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
    print(jsonify({'alert_message': the_response}), 200, {'Content-Type': 'application/json'})
    return jsonify({'alert_message': the_response}), 200, {'Content-Type': 'application/json'}
    # print(jsonify({'alert_message': "Heyoooo"}), 200, {'Content-Type': 'application/json'})
    # return jsonify({'alert_message': "Heyoooo"}), 200, {'Content-Type': 'application/json'}

    # return jsonify({'alert_message': the_response})

# if __name__ == '__main__':
#     app.run(debug=True)

if __name__ == '__main__':
    # port = int(os.environ.get("PORT", 8000))  # Use the PORT environment variable or default to 8000
    app.run(host="0.0.0.0", port=1000, debug=True)