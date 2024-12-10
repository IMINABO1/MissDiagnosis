from openai import OpenAI
from datetime import datetime
from model import make_prediction

# Initialize OpenAI client
client = OpenAI(api_key="")

# Example outbreak data
outbreak_data = {
    'outbreak_1': {'date': '13 November 2024', 'title': 'Marburg virus disease in Rwanda'},
    'outbreak_2': {'date': '1 November 2024', 'title': 'Marburg virus disease in Rwanda'},
    'outbreak_3': {'date': '31 October 2024', 'title': 'Malaria in Ethiopia'},
    'outbreak_4': {'date': '25 October 2024', 'title': 'Marburg virus disease in Rwanda'},
    'outbreak_10': {'date': '20 September 2024', 'title': 'Avian Influenza A(H9N2) in Ghana'},
    'outbreak_19': {'date': '9 July 2024', 'title': 'Mpox in South Africa'},
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

def analyze_with_outbreaks(symptoms, patient_history, malaria_status, outbreaks):
    """
    Analyze symptoms and patient history with recent outbreak data and malaria status.
    """
    rwanda_outbreaks = {k: v for k, v in outbreaks.items() if 'Rwanda' in v['title']}
    malaria_info = f"The patient is {malaria_status.lower()} for malaria."
    prompt = (
        f"Given a Rwandan patient with symptoms: {symptoms}, history: {patient_history}, "
        f"is {malaria_info} with malaria, and recent outbreaks in Rwanda: {[v['title'] for v in rwanda_outbreaks.values()]}, "
        "provide a 5-line analysis focused ONLY on Rwanda epidemiology."
    )
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a doctor in Rwanda. Respond in max 5 lines."},
            {"role": "user", "content": prompt},
        ]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    # Example patient data
    patient_symptoms = "Fever, headache, muscle pain, and vomiting"
    patient_history = "Lives in Rwanda"
    malaria_status = make_prediction()  # Use "infected" or "uninfected"

    # Get relevant outbreaks (e.g., last 90 days)
    recent_outbreaks = get_recent_outbreaks(outbreak_data, threshold_days=90)

    # Analyze symptoms with outbreak data and malaria status
    analysis = analyze_with_outbreaks(patient_symptoms, patient_history, malaria_status, recent_outbreaks)

    # Display results
    print(analysis)
