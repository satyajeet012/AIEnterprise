from flask import Flask, request, jsonify, render_template
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib  

app = Flask(__name__, template_folder='.')

# Load the dataset
data = pd.read_csv('fish.csv')

# Encode categorical labels
label_encoder = LabelEncoder()
data['Species'] = label_encoder.fit_transform(data['Species'])

# Split features and labels
X = data.drop(columns=['Species'])
y = data['Species']

# Train the Random Forest classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

@app.route('/')
def home():
    print("Rendering the home page...")
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    print("Received prediction request...")
    # Get input values
    weight = float(request.json['weight'])
    length1 = float(request.json['length1'])
    length2 = float(request.json['length2'])
    length3 = float(request.json['length3'])
    height = float(request.json['height'])
    width = float(request.json['width'])

    # Make prediction
    prediction = model.predict([[weight, length1, length2, length3, height, width]])
    predicted_species = label_encoder.inverse_transform(prediction)[0]
    print("Predicted species:", predicted_species)

    return jsonify({'species': predicted_species})

if __name__ == '__main__':
    app.run(debug=True)
