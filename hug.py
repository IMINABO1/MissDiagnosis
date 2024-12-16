from openai import OpenAI
from datetime import datetime
from model import make_prediction
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize OpenAI client
openai_api_key = os.environ.get("OPENAI_KEY")
client = OpenAI(api_key=openai_api_key)

# Example outbreak data
outbreak_data = {   'outbreak_1': {   'date': '8 December 2024 ',
                      'title': 'Undiagnosed disease in Democratic Republic of the Congo'},
    'outbreak_10': {   'date': '2 October 2024 ',
                       'title': 'Middle East respiratory syndrome coronavirus in Kingdom of Saudi Arabia'},
    'outbreak_11': {   'date': '30 September 2024 ',
                       'title': 'Marburg virus disease in Rwanda'},
    'outbreak_12': {   'date': '20 September 2024 ',
                       'title': 'Avian Influenza A(H9N2) in Ghana'},
    'outbreak_13': {   'date': '4 September 2024 ',
                       'title': 'Influenza A(H1N1) variant virus in Viet Nam'},
    'outbreak_14': {   'date': '2 September 2024 ',
                       'title': 'Avian Influenza A(H5N1) in Cambodia'},
    'outbreak_15': {'date': '30 August 2024 ', 'title': 'Mpox in Sweden'},
    'outbreak_16': {   'date': '23 August 2024 ',
                       'title': 'Oropouche virus disease in Region of the Americas'},
    'outbreak_17': {   'date': '23 August 2024 ',
                       'title': 'Acute encephalitis syndrome due to Chandipura virus in India'},
    'outbreak_18': {   'date': '22 August 2024 ',
                       'title': 'Mpox – African Region'},
    'outbreak_19': {   'date': '31 July 2024 ',
                       'title': 'Antimicrobial Resistance Hypervirulent Klebsiella pneumoniae in Global situation'},
    'outbreak_2': {   'date': '5 December 2024 ',
                      'title': 'Oropouche virus disease in Region of the Americas'},
    'outbreak_20': {   'date': '22 July 2024 ',
                       'title': 'Dengue in Iran (Islamic Republic of)'},
    'outbreak_21': {'date': '9 July 2024 ', 
                    'title': 'Mpox in South Africa'},
    'outbreak_22': {   'date': '14 June 2024 ',
                       'title': 'Avian Influenza A(H5N2) in Mexico'},
    'outbreak_23': {   'date': '14 June 2024 ',
                       'title': 'Mpox in Democratic Republic of the Congo'},
    'outbreak_24': {   'date': '11 June 2024 ',
                       'title': 'Avian Influenza A (H9N2) in India'},
    'outbreak_25': {   'date': '11 June 2024 ',
                       'title': 'Oropouche virus disease in Cuba'},
    'outbreak_26': {   'date': '7 June 2024 ',
                       'title': 'Avian Influenza A (H5N1) in Australia'},
    'outbreak_27': {   'date': '5 June 2024 ',
                       'title': 'Avian Influenza A(H5N2) in Mexico'},
    'outbreak_28': {   'date': '30 May 2024 ',
                       'title': 'Dengue in Global situation'},
    'outbreak_3': {   'date': '13 November 2024 ',
                      'title': 'Marburg virus disease in Rwanda'},
    'outbreak_4': {   'date': '1 November 2024 ',
                      'title': 'Marburg virus disease in Rwanda'},
    'outbreak_5': {'date': '31 October 2024 ', 
                   'title': 'Malaria in Ethiopia'},
    'outbreak_6': {   'date': '25 October 2024 ',
                      'title': 'Marburg virus disease in Rwanda'},
    'outbreak_7': {   'date': '18 October 2024 ',
                      'title': 'Marburg virus disease in Rwanda'},
    'outbreak_8': {   'date': '11 October 2024 ',
                      'title': 'Marburg virus disease in Rwanda'},
    'outbreak_9': {   'date': '3 October 2024 ',
                      'title': 'West Nile virus in Barbados'}
}

def get_recent_outbreaks(outbreak_data, threshold_days=90):
    """
    Filter outbreaks that occurred within the last `threshold_days`.
    """
    recent_outbreaks = {}
    today = datetime.now()

    for key, outbreak in outbreak_data.items():
        # Strip whitespace from the date string
        outbreak_date_str = outbreak['date'].strip()
        try:
            outbreak_date = datetime.strptime(outbreak_date_str, '%d %B %Y')
            days_difference = (today - outbreak_date).days

            if days_difference <= threshold_days:
                recent_outbreaks[key] = outbreak
        except ValueError as e:
            print(f"Error processing date for outbreak {key}: {e}")
            continue

    return recent_outbreaks

def analyze_with_outbreaks(symptoms, patient_history, malaria_status, diagnosis, medicine, tests="0", outbreaks=get_recent_outbreaks(outbreak_data, threshold_days=90)):
    """
    Analyze symptoms and patient history with recent outbreak data and malaria status.
    """
    country_outbreaks = {k: v for k, v in outbreaks.items() if 'Americas' in v['title']}
    malaria_info = f"The patient is {malaria_status.lower()} for malaria."
    prompt = (
        f"Given a patient from the Americas region with symptoms: {symptoms}, medical history: {patient_history}, "
        f"{malaria_info}, and recent outbreaks in Americas region: {[v['title'] for v in country_outbreaks.values()]}, "
        f"these are some of my diagnosis as a Doctor: {diagnosis} and i suggested these medicines: {medicine}"
        f"I am suggesting this test: {tests}"
        "provide a 5-line analysis focused ONLY on the epidemiology."
    )
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a doctor's assistant in Brazil. Your sole job is to tell the doctor if his input in the emr is correct or if there might be a mistake and explain you reason for saying he might be mistaken and correct him Respond in max 5 lines. You must talk only in English. When you are responding dont say the doctor input but say your input like you are speaking directly to the doctor"},
            {"role": "user", "content": prompt},
        ]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    # Example patient data
    
    patient_symptoms = "Fever, headache, muscle pain, rash, and vomiting"
    patient_history = "No significant past medical history."
    my_diagnosis = "Might be malaria or the recent epidemic disease I can't remember"
    malaria_status = make_prediction()  # Use "infected" or "uninfected"
    medicine = "paracetamol Ibuprofen"
    further_test = "CBC (Complete Blood Count), Dengue NS1 Antigen Test"
    # Get relevant outbreaks (e.g., last 90 days)
    recent_outbreaks = get_recent_outbreaks(outbreak_data, threshold_days=90)

    # Analyze symptoms with outbreak data and malaria status
    analysis = analyze_with_outbreaks(patient_symptoms, patient_history, malaria_status, my_diagnosis, medicine, tests=further_test)

    # Display results
    print(analysis)
