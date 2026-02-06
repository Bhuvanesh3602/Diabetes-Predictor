# 🗄️ MySQL Database Setup - Complete Guide

## ✅ What Changed

Now all predictions are saved to **MySQL database** instead of CSV files!

### Benefits:
- ✅ Better performance
- ✅ Data integrity
- ✅ Easy querying
- ✅ Scalable
- ✅ Admin panel access

---

## 🚀 Quick Setup (SQLite - Default)

If you want to use SQLite (easier, no MySQL needed):

```bash
# 1. Activate environment
& D:\Project\Diabetes-Predictor\diabetes_env\Scripts\Activate.ps1

# 2. Create database tables
python manage.py makemigrations
python manage.py migrate

# 3. Create admin user (optional)
python manage.py createsuperuser

# 4. Run server
python manage.py runserver
```

**Done! Visit http://127.0.0.1:8000/**

---

## 🗄️ MySQL Setup (Advanced)

### Step 1: Install MySQL

Download and install MySQL from: https://dev.mysql.com/downloads/installer/

During installation:
- Set root password (remember it!)
- Start MySQL service

### Step 2: Create Database

```bash
# Open MySQL command line
mysql -u root -p

# Enter password, then:
CREATE DATABASE diabetes_db;
SHOW DATABASES;
EXIT;
```

### Step 3: Install MySQL Client

```bash
# Activate environment
& D:\Project\Diabetes-Predictor\diabetes_env\Scripts\Activate.ps1

# Install MySQL client
pip install mysqlclient

# If fails, use PyMySQL:
pip install pymysql
```

### Step 4: Configure Django

Edit `Addition_dj/settings.py`:

**Comment out SQLite:**
```python
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
```

**Uncomment MySQL:**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'diabetes_db',
        'USER': 'root',
        'PASSWORD': 'your_password_here',  # Change this!
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

**If using PyMySQL**, add to `Addition_dj/__init__.py`:
```python
import pymysql
pymysql.install_as_MySQLdb()
```

### Step 5: Create Tables

```bash
python manage.py makemigrations
python manage.py migrate
```

You should see:
```
Running migrations:
  Applying myapp.0001_initial... OK
```

### Step 6: Create Admin User

```bash
python manage.py createsuperuser
```

Enter:
- Username: admin
- Email: admin@example.com
- Password: (your choice)

### Step 7: Run Server

```bash
python manage.py runserver
```

---

## 📊 Database Structure

### Table: `diabetes_predictions`

| Column | Type | Description |
|--------|------|-------------|
| id | Integer | Auto-increment primary key |
| timestamp | DateTime | When prediction was made |
| pregnancies | Float | Number of pregnancies |
| glucose | Float | Glucose level |
| blood_pressure | Float | Blood pressure |
| skin_thickness | Float | Skin thickness |
| insulin | Float | Insulin level |
| bmi | Float | Body Mass Index |
| diabetes_pedigree_function | Float | Genetic factor |
| age | Float | Age in years |
| outcome | Integer | 0=No diabetes, 1=Diabetes |
| risk_level | String | Low/Moderate/High |

---

## 🎯 How It Works

### Before (CSV):
```
User submits form → Save to CSV file → Read CSV for dashboard
```

### Now (Database):
```
User submits form → Save to MySQL table → Query database for dashboard
```

---

## 🔍 View Your Data

### Option 1: Django Admin Panel

1. Visit: http://127.0.0.1:8000/admin/
2. Login with superuser credentials
3. Click "Predictions"
4. View/Edit/Delete records

### Option 2: MySQL Command Line

```bash
mysql -u root -p
USE diabetes_db;

# View all predictions
SELECT * FROM diabetes_predictions;

# Count by outcome
SELECT outcome, COUNT(*) FROM diabetes_predictions GROUP BY outcome;

# Average glucose
SELECT AVG(glucose) FROM diabetes_predictions;
```

### Option 3: MySQL Workbench

1. Open MySQL Workbench
2. Connect to localhost
3. Select `diabetes_db`
4. Browse `diabetes_predictions` table

---

## 📈 Dashboard Now Uses Database

### Old Code (CSV):
```python
df = pd.read_csv('submissions.csv')
stats = df.describe()
```

### New Code (Database):
```python
total = Prediction.objects.count()
positive = Prediction.objects.filter(outcome=1).count()
avg_glucose = Prediction.objects.aggregate(Avg('glucose'))
```

**Much faster and more reliable!**

---

## 🔄 Migrate Existing CSV Data

If you have old CSV data, import it:

```python
# Run in Django shell: python manage.py shell

import pandas as pd
from myapp.models import Prediction
from datetime import datetime

# Read CSV
df = pd.read_csv('myapp/submissions.csv')

# Import each row
for _, row in df.iterrows():
    Prediction.objects.create(
        pregnancies=row['Pregnancies'],
        glucose=row['Glucose'],
        blood_pressure=row['BloodPressure'],
        skin_thickness=row['SkinThickness'],
        insulin=row['Insulin'],
        bmi=row['BMI'],
        diabetes_pedigree_function=row['DiabetesPedigreeFunction'],
        age=row['Age'],
        outcome=row['Outcome']
    )

print(f"Imported {Prediction.objects.count()} records!")
```

---

## ✅ Verification

### Test Everything Works:

1. **Make a prediction:**
   - Go to http://127.0.0.1:8000/predict/
   - Fill form and submit

2. **Check database:**
   ```bash
   python manage.py shell
   >>> from myapp.models import Prediction
   >>> Prediction.objects.count()
   1
   >>> Prediction.objects.first().glucose
   148.0
   ```

3. **Check dashboard:**
   - Visit http://127.0.0.1:8000/dashboard/
   - Should show statistics

4. **Check admin:**
   - Visit http://127.0.0.1:8000/admin/
   - Login and view predictions

---

## 🐛 Troubleshooting

### Error: "No such table: diabetes_predictions"

**Fix:**
```bash
python manage.py makemigrations
python manage.py migrate
```

### Error: "Access denied for user 'root'"

**Fix:** Check MySQL password in settings.py

### Error: "Can't connect to MySQL server"

**Fix:**
```bash
# Start MySQL service
net start MySQL80
```

### Dashboard shows zero

**Fix:** Make a new prediction first!

---

## 📝 Commands Cheat Sheet

```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Open Django shell
python manage.py shell

# Check database
python manage.py dbshell

# Run server
python manage.py runserver
```

---

## 🎉 Success!

Your Diabetes Predictor now uses:
- ✅ MySQL/SQLite database
- ✅ Django ORM for queries
- ✅ Admin panel for management
- ✅ Better performance
- ✅ Data integrity

**Dashboard and History now pull data from database, not CSV!**

---

## 💡 Next Steps

1. Make some predictions
2. Check dashboard for statistics
3. View history page
4. Access admin panel
5. Query database directly

**Enjoy your database-powered application! 🚀**
