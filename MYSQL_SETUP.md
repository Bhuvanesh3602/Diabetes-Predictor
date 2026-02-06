# 🗄️ MySQL Database Setup Guide

## 📋 Prerequisites

1. **MySQL Server** installed on your system
2. **MySQL Workbench** (optional, for GUI management)
3. **Python mysqlclient** package

---

## 🚀 Quick Setup

### Step 1: Install MySQL Server

#### Windows:
1. Download MySQL Installer from [mysql.com](https://dev.mysql.com/downloads/installer/)
2. Run installer and select "MySQL Server"
3. Set root password during installation
4. Remember your password!

#### Verify Installation:
```bash
mysql --version
```

---

### Step 2: Install MySQL Python Client

```bash
# Activate virtual environment first
diabetes_env\Scripts\activate

# Install mysqlclient
pip install mysqlclient
```

**If installation fails on Windows:**
```bash
# Alternative: Use PyMySQL
pip install pymysql
```

---

### Step 3: Create Database

#### Option A: Using MySQL Command Line
```bash
# Login to MySQL
mysql -u root -p

# Enter your password, then run:
CREATE DATABASE diabetes_db;
SHOW DATABASES;
EXIT;
```

#### Option B: Using MySQL Workbench
1. Open MySQL Workbench
2. Connect to local instance
3. Click "Create Schema" icon
4. Name: `diabetes_db`
5. Click "Apply"

---

### Step 4: Configure Django Settings

Open `Addition_dj/settings.py` and update:

```python
# Comment out SQLite configuration
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# Uncomment and configure MySQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'diabetes_db',
        'USER': 'root',
        'PASSWORD': 'your_mysql_password',  # Change this!
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}
```

**If using PyMySQL instead of mysqlclient:**

Add this to `Addition_dj/__init__.py`:
```python
import pymysql
pymysql.install_as_MySQLdb()
```

---

### Step 5: Run Migrations

```bash
# Make sure virtual environment is activated
python manage.py makemigrations
python manage.py migrate
```

You should see:
```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  ...
```

---

### Step 6: Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

Enter:
- Username: admin
- Email: your@email.com
- Password: (your choice)

---

### Step 7: Test Connection

```bash
python manage.py dbshell
```

If successful, you'll see MySQL prompt:
```
mysql>
```

Type `exit` to quit.

---

## 🔧 Configuration Examples

### Local Development (Default)
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'diabetes_db',
        'USER': 'root',
        'PASSWORD': 'root123',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### Remote MySQL Server
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'diabetes_db',
        'USER': 'diabetes_user',
        'PASSWORD': 'secure_password',
        'HOST': '192.168.1.100',  # Remote IP
        'PORT': '3306',
    }
}
```

### Using Environment Variables (Recommended for Production)
```python
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DB_NAME', 'diabetes_db'),
        'USER': os.environ.get('DB_USER', 'root'),
        'PASSWORD': os.environ.get('DB_PASSWORD', ''),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', '3306'),
    }
}
```

---

## 🐛 Troubleshooting

### Error: "No module named 'MySQLdb'"

**Solution 1:** Install mysqlclient
```bash
pip install mysqlclient
```

**Solution 2:** Use PyMySQL
```bash
pip install pymysql
```

Add to `Addition_dj/__init__.py`:
```python
import pymysql
pymysql.install_as_MySQLdb()
```

---

### Error: "Access denied for user 'root'@'localhost'"

**Solution:** Check your password
```bash
# Reset MySQL root password
mysql -u root -p
ALTER USER 'root'@'localhost' IDENTIFIED BY 'new_password';
FLUSH PRIVILEGES;
```

---

### Error: "Can't connect to MySQL server"

**Solutions:**
1. Check if MySQL is running:
   ```bash
   # Windows
   net start MySQL80
   
   # Check status
   sc query MySQL80
   ```

2. Verify port 3306 is open:
   ```bash
   netstat -an | findstr 3306
   ```

3. Check firewall settings

---

### Error: "Unknown database 'diabetes_db'"

**Solution:** Create the database
```sql
mysql -u root -p
CREATE DATABASE diabetes_db;
```

---

### Error: "mysqlclient installation failed"

**Windows Solution:**
1. Install Visual C++ Build Tools
2. Or use pre-built wheel:
   ```bash
   pip install mysqlclient-1.4.6-cp311-cp311-win_amd64.whl
   ```
3. Or use PyMySQL (easier):
   ```bash
   pip install pymysql
   ```

---

## 📊 Database Management

### View Tables
```sql
mysql -u root -p
USE diabetes_db;
SHOW TABLES;
```

### View Data
```sql
SELECT * FROM auth_user;
SELECT * FROM django_migrations;
```

### Backup Database
```bash
mysqldump -u root -p diabetes_db > backup.sql
```

### Restore Database
```bash
mysql -u root -p diabetes_db < backup.sql
```

---

## 🔄 Switching Between SQLite and MySQL

### To SQLite:
1. Comment MySQL config in `settings.py`
2. Uncomment SQLite config
3. Run: `python manage.py migrate`

### To MySQL:
1. Comment SQLite config in `settings.py`
2. Uncomment MySQL config
3. Run: `python manage.py migrate`

---

## 🎯 Testing MySQL Connection

Create `test_mysql.py` in project root:

```python
import mysql.connector

try:
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='your_password',
        database='diabetes_db'
    )
    
    if connection.is_connected():
        print("✅ Successfully connected to MySQL!")
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE();")
        record = cursor.fetchone()
        print(f"Connected to database: {record}")
        
except Exception as e:
    print(f"❌ Error: {e}")
    
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection closed")
```

Run:
```bash
python test_mysql.py
```

---

## 📝 Complete Setup Checklist

- [ ] MySQL Server installed
- [ ] MySQL service running
- [ ] Database `diabetes_db` created
- [ ] mysqlclient or pymysql installed
- [ ] settings.py configured with MySQL credentials
- [ ] Migrations run successfully
- [ ] Test connection successful
- [ ] Application runs without errors

---

## 🚀 Final Steps

```bash
# 1. Activate environment
diabetes_env\Scripts\activate

# 2. Install MySQL client
pip install mysqlclient

# 3. Run migrations
python manage.py migrate

# 4. Start server
python manage.py runserver

# 5. Test at http://127.0.0.1:8000/
```

---

## 💡 Pro Tips

1. **Use environment variables** for sensitive data
2. **Regular backups** of your database
3. **Different databases** for development/production
4. **Connection pooling** for better performance
5. **Monitor slow queries** for optimization

---

## 📚 Additional Resources

- [Django MySQL Documentation](https://docs.djangoproject.com/en/4.0/ref/databases/#mysql-notes)
- [MySQL Documentation](https://dev.mysql.com/doc/)
- [mysqlclient GitHub](https://github.com/PyMySQL/mysqlclient)

---

## ✅ Success!

Once configured, your Django app will use MySQL instead of SQLite. All data will be stored in MySQL database tables.

**Benefits:**
- ✅ Better performance for large datasets
- ✅ Multi-user support
- ✅ Advanced querying capabilities
- ✅ Production-ready database
- ✅ Better data integrity

---

**Need Help?** Check the troubleshooting section or create an issue on GitHub!
