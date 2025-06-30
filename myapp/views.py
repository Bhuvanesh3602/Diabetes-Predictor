from django.shortcuts import render
from django.conf import settings
import numpy as np
import joblib
import os
import csv

def index(request):
    return render(request, 'add.html')

def add_numbers(request):
    result = None
    report = None

    try:
        if request.method == 'POST':
            # Load model and scaler
            scaler = joblib.load(os.path.join(settings.BASE_DIR, 'myapp', 'scaler.pkl'))
            model = joblib.load(os.path.join(settings.BASE_DIR, 'myapp', 'model.pkl'))

            # Collect inputs from form
            inputs = [float(request.POST.get(f'num{i}')) for i in range(1, 9)]

            # Scale and predict
            new_data = np.array([inputs])
            scaled_data = scaler.transform(new_data)
            prediction = model.predict(scaled_data)
            result = int(prediction[0])

            # ✅ Save to CSV
            file_path = os.path.join(settings.BASE_DIR, 'myapp', 'submissions.csv')
            file_empty = not os.path.exists(file_path) or os.stat(file_path).st_size == 0

            with open(file_path, mode='a', newline='') as file:
                writer = csv.writer(file)

                # ✅ Write header only if file is empty
                if file_empty:
                    writer.writerow([
                        'Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
                        'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome'
                    ])

                # ✅ Write user input + prediction result
                writer.writerow(inputs + [result])

    except Exception as e:
        report = f"Error: {e}"

    return render(request, 'add.html', {'result': result, 'report': report})
