from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
import numpy as np
import joblib
import os
import csv
import pandas as pd
from datetime import datetime
from .models import Prediction

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

            # Save to database
            Prediction.objects.create(
                pregnancies=inputs[0],
                glucose=inputs[1],
                blood_pressure=inputs[2],
                skin_thickness=inputs[3],
                insulin=inputs[4],
                bmi=inputs[5],
                diabetes_pedigree_function=inputs[6],
                age=inputs[7],
                outcome=result,
                risk_level=risk_level
            )

            # Also save to CSV for backup
            file_path = os.path.join(settings.BASE_DIR, 'myapp', 'submissions.csv')
            file_empty = not os.path.exists(file_path) or os.stat(file_path).st_size == 0

            with open(file_path, mode='a', newline='') as file:
                writer = csv.writer(file)
                if file_empty:
                    writer.writerow(['Timestamp'] + labels + ['Outcome'])
                writer.writerow([datetime.now().strftime('%Y-%m-%d %H:%M:%S')] + inputs + [result])

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
    # Get data from database
    predictions = Prediction.objects.all()[:10]
    history_data = []
    
    for pred in predictions:
        history_data.append({
            'Timestamp': pred.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            'Pregnancies': pred.pregnancies,
            'Glucose': pred.glucose,
            'BloodPressure': pred.blood_pressure,
            'SkinThickness': pred.skin_thickness,
            'Insulin': pred.insulin,
            'BMI': pred.bmi,
            'DiabetesPedigreeFunction': pred.diabetes_pedigree_function,
            'Age': pred.age,
            'Outcome': pred.outcome
        })
    
    # Calculate stats
    total = Prediction.objects.count()
    positive = Prediction.objects.filter(outcome=1).count()
    negative = Prediction.objects.filter(outcome=0).count()
    
    stats = {
        'total': total,
        'positive': positive,
        'negative': negative
    }

    return render(request, 'history.html', {'history': history_data, 'stats': stats})

def dashboard(request):
    # Get stats from database
    from django.db.models import Avg
    
    total = Prediction.objects.count()
    positive = Prediction.objects.filter(outcome=1).count()
    negative = Prediction.objects.filter(outcome=0).count()
    
    avg_glucose = Prediction.objects.aggregate(Avg('glucose'))['glucose__avg'] or 0
    avg_bmi = Prediction.objects.aggregate(Avg('bmi'))['bmi__avg'] or 0
    
    stats = {
        'total': total,
        'positive': positive,
        'negative': negative,
        'avg_glucose': round(avg_glucose, 1),
        'avg_bmi': round(avg_bmi, 1)
    }

    return render(request, 'dashboard.html', {'stats': stats})
