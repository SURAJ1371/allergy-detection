from flask import Flask, render_template, request
from model.allergy_model import predict_allergy

app = Flask(__name__)

# Route to render homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submissions
@app.route('/predict', methods=['POST'])
def predict():
    symptoms = request.form['symptoms']
    result = predict_allergy(symptoms)
    return render_template('index.html', prediction=result)

if __name__ == "__main__":
    app.run(debug=True)
