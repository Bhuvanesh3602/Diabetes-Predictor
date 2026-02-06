from django.shortcuts import render
from django.conf import settings
import numpy as np
import joblib
import os
from datetime import datetime
from pymongo import MongoClient

# MongoDB connection
def get_mongo_db():
    client = MongoClient('mongodb://127.0.0.1:27017/')
    return client['Diabetes']

def index(request):
    return render(request, 'index.html')

def predict(request):
    return render(request, 'predict.html')

def add_numbers(request):
    result = None
    report = None
    risk_level = None
    recommendations = []
    input_data = {}

    try:
        if request.method == 'POST':
            scaler = joblib.load(os.path.join(settings.BASE_DIR, 'myapp', 'scaler.pkl'))
            model = joblib.load(os.path.join(settings.BASE_DIR, 'myapp', 'model.pkl'))

            inputs = [float(request.POST.get(f'num{i}')) for i in range(1, 9)]
            labels = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
            input_data = dict(zip(labels, inputs))

            new_data = np.array([inputs])
            scaled_data = scaler.transform(new_data)
            prediction = model.predict(scaled_data)
            result = int(prediction[0])

            # Risk assessment
            if result == 1:
                if inputs[1] > 140 or inputs[5] > 30:
                    risk_level = 'High'
                else:
                    risk_level = 'Moderate'
            else:
                risk_level = 'Low'

            # Generate recommendations
            recommendations = generate_recommendations(input_data, result)

            # Save to MongoDB
            db = get_mongo_db()
            prediction_doc = {
                'timestamp': datetime.now(),
                'pregnancies': inputs[0],
                'glucose': inputs[1],
                'blood_pressure': inputs[2],
                'skin_thickness': inputs[3],
                'insulin': inputs[4],
                'bmi': inputs[5],
                'diabetes_pedigree_function': inputs[6],
                'age': inputs[7],
                'outcome': result,
                'risk_level': risk_level
            }
            db.predictions.insert_one(prediction_doc)

    except Exception as e:
        report = f"Error: {e}"

    return render(request, 'predict.html', {
        'result': result,
        'report': report,
        'risk_level': risk_level,
        'recommendations': recommendations,
        'input_data': input_data
    })

def generate_recommendations(data, result):
    recs = []
    if result == 1:
        recs.append('Consult a healthcare professional immediately')
    if data['Glucose'] > 140:
        recs.append('Monitor blood glucose levels regularly')
    if data['BMI'] > 30:
        recs.append('Consider a weight management program')
    if data['BloodPressure'] > 90:
        recs.append('Monitor blood pressure regularly')
    if data['Age'] > 45:
        recs.append('Schedule regular health checkups')
    if not recs:
        recs.append('Maintain a healthy lifestyle with regular exercise')
        recs.append('Follow a balanced diet')
    return recs

def history(request):
    history_data = []
    stats = {'total': 0, 'positive': 0, 'negative': 0}

    try:
        db = get_mongo_db()
        predictions = list(db.predictions.find().sort('timestamp', -1).limit(10))
        
        for pred in predictions:
            history_data.append({
                'Timestamp': pred['timestamp'].strftime('%Y-%m-%d %H:%M:%S'),
                'Glucose': pred['glucose'],
                'BMI': pred['bmi'],
                'BloodPressure': pred['blood_pressure'],
                'Age': pred['age'],
                'Outcome': pred['outcome']
            })
        
        stats['total'] = db.predictions.count_documents({})
        stats['positive'] = db.predictions.count_documents({'outcome': 1})
        stats['negative'] = db.predictions.count_documents({'outcome': 0})
    except Exception as e:
        print(f"Error: {e}")

    return render(request, 'history.html', {'history': history_data, 'stats': stats})

def dashboard(request):
    stats = {'total': 0, 'positive': 0, 'negative': 0, 'avg_glucose': 0, 'avg_bmi': 0}

    try:
        db = get_mongo_db()
        
        stats['total'] = db.predictions.count_documents({})
        stats['positive'] = db.predictions.count_documents({'outcome': 1})
        stats['negative'] = db.predictions.count_documents({'outcome': 0})
        
        # Calculate averages
        pipeline = [
            {
                '$group': {
                    '_id': None,
                    'avg_glucose': {'$avg': '$glucose'},
                    'avg_bmi': {'$avg': '$bmi'}
                }
            }
        ]
        result = list(db.predictions.aggregate(pipeline))
        if result:
            stats['avg_glucose'] = round(result[0]['avg_glucose'], 1)
            stats['avg_bmi'] = round(result[0]['avg_bmi'], 1)
    except Exception as e:
        print(f"Error: {e}")

    return render(request, 'dashboard.html', {'stats': stats})
