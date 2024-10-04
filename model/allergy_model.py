import re
import spacy

# Load NLP model
nlp = spacy.load("en_core_web_sm")

# Sample data for allergies and symptoms
allergy_data = {
    "dust allergy": ["sneezing", "coughing", "watery eyes"],
    "food allergy": ["stomach pain", "vomiting", "hives", "rash"],
    "pollen allergy": ["sneezing", "runny nose", "itchy eyes"]
}

def predict_allergy(symptoms):
    # Clean input
    symptoms = symptoms.lower()
    doc = nlp(symptoms)

    # Simple keyword matching for demo purposes
    for allergy, symptoms_list in allergy_data.items():
        if any(re.search(r"\b" + re.escape(symptom) + r"\b", symptoms) for symptom in symptoms_list):
            return f"You may have {allergy}. Please consult a doctor."

    return "Unable to determine allergy from symptoms. Consult a specialist."
