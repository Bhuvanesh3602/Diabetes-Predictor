# 🍃 MongoDB Setup - Simple Guide

## ⚡ Quick Setup

### Step 1: Install MongoDB
Download: https://www.mongodb.com/try/download/community
- Run installer
- Install as Windows Service
- Install MongoDB Compass (optional GUI)

### Step 2: Start MongoDB
```bash
net start MongoDB
```

### Step 3: Install PyMongo
```bash
& D:\Project\Diabetes-Predictor\diabetes_env\Scripts\Activate.ps1
pip install pymongo
```

### Step 4: Run Server
```bash
python manage.py runserver
```

## ✅ That's It!

No migrations needed! PyMongo works directly with MongoDB.

## 🎯 Test

1. Visit: http://127.0.0.1:8000/predict/
2. Make a prediction
3. Check: http://127.0.0.1:8000/dashboard/

## 📊 View Data

### MongoDB Compass:
- Connect to: mongodb://127.0.0.1:27017
- Database: Diabetes
- Collection: predictions

### Command Line:
```bash
mongo
> use Diabetes
> db.predictions.find().pretty()
> db.predictions.count()
```

## 🎉 Done!
All data saved to MongoDB at: mongodb://127.0.0.1:27017/Diabetes
No CSV files used!
