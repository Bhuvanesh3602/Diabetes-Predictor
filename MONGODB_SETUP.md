# 🍃 MongoDB Setup Guide

## ✅ Quick Setup

### Step 1: Install MongoDB

Download MongoDB Community Server:
https://www.mongodb.com/try/download/community

**Windows Installation:**
1. Run installer
2. Choose "Complete" installation
3. Install as Windows Service
4. Install MongoDB Compass (GUI tool)

### Step 2: Start MongoDB

```bash
# Check if MongoDB is running
net start MongoDB

# If not started, start it
net start MongoDB
```

### Step 3: Install Python Dependencies

```bash
# Activate environment
& D:\Project\Diabetes-Predictor\diabetes_env\Scripts\Activate.ps1

# Install MongoDB packages
pip install pymongo djongo sqlparse
```

### Step 4: Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Run Server

```bash
python manage.py runserver
```

### Step 6: Test

Visit: http://127.0.0.1:8000/predict/
Make a prediction and check dashboard!

---

## 🔍 Verify MongoDB Connection

### Check MongoDB is Running:
```bash
mongo --version
```

### Connect to MongoDB:
```bash
mongo
> show dbs
> use Diabetes
> show collections
> db.myapp_prediction.find()
```

---

## 📊 View Data in MongoDB

### Option 1: MongoDB Compass (GUI)
1. Open MongoDB Compass
2. Connect to: mongodb://127.0.0.1:27017
3. Select database: Diabetes
4. View collection: myapp_prediction

### Option 2: Command Line
```bash
mongo
> use Diabetes
> db.myapp_prediction.find().pretty()
> db.myapp_prediction.count()
```

### Option 3: Python Shell
```bash
python manage.py shell
>>> from myapp.models import Prediction
>>> Prediction.objects.all()
>>> Prediction.objects.count()
```

---

## 🎯 What Changed

### Before (CSV):
- Data saved to submissions.csv
- Slow file reading
- No data validation

### Now (MongoDB):
- Data saved to MongoDB
- Fast queries
- NoSQL flexibility
- No CSV files needed

---

## 🐛 Troubleshooting

### Error: "No module named 'djongo'"
```bash
pip install djongo pymongo sqlparse
```

### Error: "Can't connect to MongoDB"
```bash
# Start MongoDB service
net start MongoDB

# Check status
sc query MongoDB
```

### Error: "ServerSelectionTimeoutError"
- MongoDB is not running
- Check: `net start MongoDB`

### Error: "No migrations to apply"
```bash
python manage.py makemigrations myapp
python manage.py migrate
```

---

## ✅ Success Checklist

- [ ] MongoDB installed
- [ ] MongoDB service running
- [ ] pymongo and djongo installed
- [ ] Migrations completed
- [ ] Server running
- [ ] Can make predictions
- [ ] Dashboard shows data
- [ ] History shows data

---

## 🎉 Done!

Your app now uses MongoDB at:
**mongodb://127.0.0.1:27017/Diabetes**

All predictions stored in MongoDB collection!
No CSV files needed!
