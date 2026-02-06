# 🔧 Dashboard & History Fix Guide

## ❌ Common Issues & Solutions

### Issue 1: Dashboard/History Pages Not Loading

#### Symptoms:
- Blank page
- 404 Error
- Template not found error

#### Solutions:

**Step 1: Verify Templates Exist**
```bash
# Check if templates are in correct location
dir myapp\templates
```

You should see:
- base.html
- index.html
- predict.html
- dashboard.html
- history.html

**Step 2: Check URL Configuration**
```bash
# Verify URLs are registered
python manage.py show_urls
```

Should show:
- / → index
- /predict/ → predict
- /dashboard/ → dashboard
- /history/ → history

**Step 3: Restart Server**
```bash
# Stop server (Ctrl+C)
# Start again
python manage.py runserver
```

---

### Issue 2: Template Syntax Error

#### Error Message:
```
TemplateSyntaxError: Invalid block tag on line X
```

#### Solution:
Add `{% load custom_filters %}` at top of dashboard.html:

```django
{% extends 'base.html' %}
{% load custom_filters %}

{% block title %}Dashboard{% endblock %}
```

---

### Issue 3: No Data Showing

#### Symptoms:
- Dashboard shows all zeros
- History table is empty

#### Solutions:

**Check CSV File:**
```bash
# View submissions.csv
type myapp\submissions.csv
```

**If file is empty or missing:**
1. Go to `/predict/` page
2. Fill in the form
3. Submit a prediction
4. Check dashboard again

**Manually create test data:**
```csv
Timestamp,Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age,Outcome
2024-01-15 10:30:00,1,85,66,29,0,26.6,0.351,31,0
2024-01-15 11:45:00,6,148,72,35,0,33.6,0.627,50,1
```

Save as `myapp\submissions.csv`

---

### Issue 4: Custom Filters Not Working

#### Error Message:
```
TemplateSyntaxError: 'custom_filters' is not a registered tag library
```

#### Solution:

**Step 1: Verify templatetags directory structure**
```
myapp/
├── templatetags/
│   ├── __init__.py
│   └── custom_filters.py
```

**Step 2: Check __init__.py exists**
```bash
# Create if missing
echo # Template tags package > myapp\templatetags\__init__.py
```

**Step 3: Restart Django server**
```bash
# Stop (Ctrl+C) and restart
python manage.py runserver
```

---

### Issue 5: Pandas/NumPy Errors

#### Error Message:
```
ModuleNotFoundError: No module named 'pandas'
```

#### Solution:
```bash
# Activate environment
diabetes_env\Scripts\activate

# Install dependencies
pip install pandas numpy
```

---

### Issue 6: CSV Permission Error

#### Error Message:
```
PermissionError: [Errno 13] Permission denied: 'submissions.csv'
```

#### Solutions:

**Option 1: Close Excel/CSV viewers**
- Close any program viewing submissions.csv
- Try again

**Option 2: Check file permissions**
```bash
# Windows: Right-click submissions.csv
# Properties → Security → Edit → Allow Full Control
```

**Option 3: Delete and recreate**
```bash
del myapp\submissions.csv
# Make a new prediction to recreate
```

---

## 🔍 Debugging Steps

### Step 1: Check Django Logs

Look at terminal output when accessing pages:
```
[15/Jan/2024 10:30:00] "GET /dashboard/ HTTP/1.1" 200 5234
```

- **200** = Success ✅
- **404** = Page not found ❌
- **500** = Server error ❌

### Step 2: Enable Debug Mode

In `settings.py`:
```python
DEBUG = True
```

This shows detailed error messages.

### Step 3: Test Each View

**Test Dashboard:**
```bash
# Open browser
http://127.0.0.1:8000/dashboard/
```

**Test History:**
```bash
http://127.0.0.1:8000/history/
```

### Step 4: Check Python Console

Add debug prints to `views.py`:

```python
def dashboard(request):
    print("Dashboard view called")
    file_path = os.path.join(settings.BASE_DIR, 'myapp', 'submissions.csv')
    print(f"Looking for file: {file_path}")
    print(f"File exists: {os.path.exists(file_path)}")
    # ... rest of code
```

---

## 🧪 Test Script

Create `test_views.py`:

```python
import os
import pandas as pd
from django.conf import settings

# Test file path
file_path = os.path.join(settings.BASE_DIR, 'myapp', 'submissions.csv')
print(f"File path: {file_path}")
print(f"File exists: {os.path.exists(file_path)}")

if os.path.exists(file_path):
    print(f"File size: {os.path.getsize(file_path)} bytes")
    
    # Try reading CSV
    try:
        df = pd.read_csv(file_path)
        print(f"Rows: {len(df)}")
        print(f"Columns: {list(df.columns)}")
        print("\nFirst row:")
        print(df.head(1))
    except Exception as e:
        print(f"Error reading CSV: {e}")
else:
    print("❌ File not found!")
```

Run:
```bash
python manage.py shell < test_views.py
```

---

## ✅ Quick Fix Checklist

Run these commands in order:

```bash
# 1. Activate environment
diabetes_env\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Check for errors
python manage.py check

# 4. Collect static files (if needed)
python manage.py collectstatic --noinput

# 5. Clear cache
python manage.py clearsessions

# 6. Restart server
python manage.py runserver
```

---

## 🎯 Verify Everything Works

### Test Checklist:

1. **Home Page** (`/`)
   - [ ] Loads without errors
   - [ ] Navigation links work
   - [ ] Tailwind CSS styles applied

2. **Predict Page** (`/predict/`)
   - [ ] Form displays correctly
   - [ ] Can submit prediction
   - [ ] Results show properly

3. **Dashboard** (`/dashboard/`)
   - [ ] Statistics display
   - [ ] Charts render
   - [ ] No errors in console

4. **History** (`/history/`)
   - [ ] Table shows data
   - [ ] Stats are correct
   - [ ] Export buttons work

---

## 🔄 Reset Everything

If nothing works, start fresh:

```bash
# 1. Backup your data
copy myapp\submissions.csv submissions_backup.csv

# 2. Delete database
del db.sqlite3

# 3. Delete migrations (except __init__.py)
del myapp\migrations\*.py
# Keep __init__.py

# 4. Recreate migrations
python manage.py makemigrations
python manage.py migrate

# 5. Restore data
copy submissions_backup.csv myapp\submissions.csv

# 6. Restart server
python manage.py runserver
```

---

## 📞 Still Having Issues?

### Check These:

1. **Python Version**
   ```bash
   python --version
   # Should be 3.8+
   ```

2. **Django Version**
   ```bash
   python -m django --version
   # Should be 4.0+
   ```

3. **Virtual Environment Active**
   ```bash
   # Should see (diabetes_env) in prompt
   ```

4. **All Dependencies Installed**
   ```bash
   pip list
   # Check for: django, pandas, numpy, scikit-learn
   ```

---

## 💡 Pro Tips

1. **Always check terminal output** for error messages
2. **Use browser DevTools** (F12) to check for JavaScript errors
3. **Clear browser cache** if styles don't update
4. **Check file paths** are correct for your OS
5. **Make test predictions** to generate data

---

## 🎉 Success Indicators

When everything works:
- ✅ All pages load without errors
- ✅ Dashboard shows statistics
- ✅ History displays predictions
- ✅ Charts and graphs render
- ✅ No console errors
- ✅ Styles look correct

---

**If you've followed all steps and still have issues, check the error message carefully and search for it online or ask for help!**
