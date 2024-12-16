from scrape import scrape_to_html
from scrape2 import parse_disease_outbreaks_as_dict
from hug import get_recent_outbreaks, analyze_with_outbreaks
import pprint


def the_main(patient_symptoms, patient_history, malaria_status, my_diagnosis, medicine, tests):
    # scrape_to_html() #uncomment this later

    with open("res.html", "r", encoding="utf-8") as f:
        html_content = f.read()

        # Parse the outbreaks into a dictionary of dictionaries
        outbreaks = parse_disease_outbreaks_as_dict(html_content)
        # pprint.pprint(outbreaks, indent=4)

    # Example patient data
    #patient_symptoms = "Fever, headache, muscle pain, and vomiting"
    # Get relevant outbreaks (e.g., last 90 days)
    # recent_outbreaks = get_recent_outbreaks(outbreak_data, threshold_days=90)
    # Analyze symptoms with outbreak data and malaria status
    analysis = analyze_with_outbreaks(patient_symptoms, patient_history, malaria_status, my_diagnosis, medicine, tests)
    
    # Display results
    return analysis

# patient_symptoms = "Fever, headache, muscle pain, rash, and vomiting"
# patient_history = "No significant past medical history."
# my_diagnosis = "Might be malaria or the recent epidemic disease I can't remember"
# malaria_status = "infected"  # Use "infected" or "uninfected"
# medicine = "paracetamol Ibuprofen"
# further_test = "CBC (Complete Blood Count), Dengue NS1 Antigen Test"

# print(the_main(patient_symptoms, patient_history, malaria_status, my_diagnosis, medicine, further_test))