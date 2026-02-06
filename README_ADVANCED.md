# 🩺 Diabetes Predictor - Advanced Edition

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Django](https://img.shields.io/badge/Django-4.0+-green.svg)
![TailwindCSS](https://img.shields.io/badge/TailwindCSS-3.0-38bdf8.svg)
![Machine Learning](https://img.shields.io/badge/ML-Scikit--Learn-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

*An advanced AI-powered web application for diabetes risk prediction with modern UI*

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Screenshots](#-screenshots)

</div>

---

## 🎯 Overview

The **Diabetes Predictor Advanced Edition** is a cutting-edge web application that leverages machine learning to assess diabetes risk. Built with Django and styled with Tailwind CSS, it offers a modern, responsive interface with comprehensive analytics and health insights.

## ✨ New Features

### 🎨 Modern UI/UX
- **Tailwind CSS Integration** - Beautiful, responsive design
- **Gradient Backgrounds** - Eye-catching color schemes
- **Smooth Animations** - Enhanced user experience
- **Font Awesome Icons** - Professional iconography
- **Mobile Responsive** - Works on all devices

### 📊 Advanced Analytics
- **Interactive Dashboard** - Real-time statistics and metrics
- **Prediction History** - Track all past assessments
- **Visual Charts** - Pie charts and progress bars
- **Health Metrics** - Average glucose and BMI tracking
- **Risk Analysis** - Detailed risk level assessment

### 🔍 Enhanced Predictions
- **Risk Level Classification** - Low, Moderate, High
- **Personalized Recommendations** - Health tips based on results
- **Input Validation** - Real-time form validation
- **Detailed Results** - Comprehensive prediction breakdown
- **Timestamp Tracking** - Date/time for each prediction

### 📈 Data Visualization
- **Distribution Charts** - Visual representation of results
- **Progress Bars** - Health metric indicators
- **Statistics Cards** - Key metrics at a glance
- **Color-Coded Results** - Easy-to-understand visual feedback

## 🛠 Technology Stack

| Component | Technology |
|-----------|------------|
| **Backend** | Django 4.0+ |
| **Frontend** | HTML5, Tailwind CSS 3.0 |
| **Icons** | Font Awesome 6.4 |
| **ML Framework** | Scikit-Learn |
| **Data Processing** | NumPy, Pandas |
| **Model Serialization** | Joblib |
| **Database** | SQLite |

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Virtual environment (recommended)

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/Bhuvanesh3602/Diabetes-Predictor.git
   cd Diabetes-Predictor
   ```

2. **Create and activate virtual environment**
   ```bash
   # Create virtual environment
   python -m venv diabetes_env
   
   # Activate (Windows)
   diabetes_env\Scripts\activate
   
   # Activate (macOS/Linux)
   source diabetes_env/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Start the development server**
   ```bash
   python manage.py runserver
   ```

6. **Access the application**
   ```
   Open browser: http://127.0.0.1:8000/
   ```

## 💻 Usage Guide

### 🏠 Home Page
- Modern landing page with hero section
- Feature highlights and statistics
- Quick access to all functionalities
- "How It Works" guide

### 🔮 Prediction Page
- Beautiful form with 8 medical parameters
- Real-time input validation
- Helpful tooltips and ranges
- Instant risk assessment
- Personalized health recommendations

### 📊 Dashboard
- Total predictions count
- Risk detection statistics
- Average health metrics
- Visual charts and graphs
- Quick action buttons

### 📜 History Page
- Last 10 predictions displayed
- Detailed table view
- Color-coded results
- Export options (Print, CSV, PDF)
- Health tips section

## 📋 Input Parameters

| Parameter | Description | Normal Range | Icon |
|-----------|-------------|--------------|------|
| **Pregnancies** | Number of pregnancies | 0-20 | 👶 |
| **Glucose** | Plasma glucose concentration | 70-140 mg/dL | 🩸 |
| **Blood Pressure** | Diastolic blood pressure | 60-90 mmHg | ❤️ |
| **Skin Thickness** | Triceps skin fold thickness | 10-50 mm | 📏 |
| **Insulin** | 2-Hour serum insulin | 16-166 mu U/ml | 💉 |
| **BMI** | Body mass index | 18.5-24.9 kg/m² | ⚖️ |
| **Diabetes Pedigree** | Genetic predisposition | 0.0-2.5 | 🧬 |
| **Age** | Age in years | 21-100 | 📅 |

## 🎨 UI Components

### Navigation Bar
- Sticky header with smooth scrolling
- Active page highlighting
- Responsive mobile menu
- Brand logo with icon

### Cards & Sections
- Gradient backgrounds
- Shadow effects
- Hover animations
- Rounded corners

### Forms
- Modern input fields
- Focus states
- Validation feedback
- Helper text

### Buttons
- Gradient backgrounds
- Hover effects
- Icon integration
- Multiple variants

## 📁 Project Structure

```
Diabetes-Predictor/
├── 📁 Addition_dj/              # Django project settings
│   ├── settings.py              # Configuration
│   ├── urls.py                  # Main URL routing
│   └── wsgi.py                  # WSGI config
├── 📁 myapp/                    # Main application
│   ├── 📁 migrations/           # Database migrations
│   ├── 📁 templates/            # HTML templates
│   │   ├── base.html            # 🆕 Base template
│   │   ├── index.html           # 🆕 Home page
│   │   ├── predict.html         # 🆕 Prediction form
│   │   ├── dashboard.html       # 🆕 Analytics dashboard
│   │   └── history.html         # 🆕 Prediction history
│   ├── 📁 templatetags/         # 🆕 Custom filters
│   │   ├── __init__.py
│   │   └── custom_filters.py   # Math operations
│   ├── views.py                 # 🔄 Enhanced views
│   ├── urls.py                  # 🔄 Updated routes
│   ├── model.pkl                # ML model
│   ├── scaler.pkl               # Feature scaler
│   └── submissions.csv          # Prediction data
├── requirements.txt             # 🆕 Dependencies
├── manage.py                    # Django CLI
└── README.md                    # Documentation
```

## 🌐 Routes

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Home page |
| `/predict/` | GET | Prediction form |
| `/add/` | POST | Process prediction |
| `/dashboard/` | GET | Analytics dashboard |
| `/history/` | GET | Prediction history |

## 🎯 Key Features Breakdown

### 1. Risk Assessment System
```python
- Low Risk: Healthy parameters
- Moderate Risk: Some elevated values
- High Risk: Multiple risk factors
```

### 2. Recommendation Engine
- Personalized health tips
- Based on input parameters
- Actionable advice
- Professional consultation reminders

### 3. Data Persistence
- CSV storage with timestamps
- Historical data tracking
- Export capabilities
- Data analytics

### 4. Responsive Design
- Mobile-first approach
- Tablet optimization
- Desktop enhancement
- Print-friendly layouts

## 🔧 Configuration

### Tailwind CSS
Loaded via CDN for quick setup:
```html
<script src="https://cdn.tailwindcss.com"></script>
```

### Font Awesome
Icons loaded via CDN:
```html
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
```

### Custom Colors
```javascript
theme: {
  extend: {
    colors: {
      primary: '#6366f1',    // Indigo
      secondary: '#8b5cf6',  // Purple
    }
  }
}
```

## 📊 Analytics Features

### Dashboard Metrics
- ✅ Total predictions count
- ✅ Positive cases (risk detected)
- ✅ Negative cases (low risk)
- ✅ Risk detection rate percentage
- ✅ Average glucose levels
- ✅ Average BMI values

### Visual Elements
- 🎨 Pie charts for distribution
- 📊 Progress bars for metrics
- 📈 Gradient indicators
- 🎯 Color-coded results

## 🚀 Future Enhancements

- [ ] User authentication system
- [ ] PDF report generation
- [ ] Email notifications
- [ ] Multi-language support
- [ ] Dark mode toggle
- [ ] Advanced data visualization (Chart.js)
- [ ] REST API endpoints
- [ ] Mobile app version
- [ ] AI chatbot integration
- [ ] Appointment booking system

## 🐛 Troubleshooting

### Common Issues

**1. Tailwind CSS not loading**
- Check internet connection (CDN required)
- Verify script tag in base.html

**2. Template not found error**
- Ensure all templates are in `myapp/templates/`
- Check template names in views.py

**3. Custom filters not working**
- Verify `{% load custom_filters %}` in template
- Check templatetags directory structure

**4. CSV permission error**
- Ensure write permissions for project directory
- Check submissions.csv file access

## 📱 Browser Support

- ✅ Chrome (recommended)
- ✅ Firefox
- ✅ Safari
- ✅ Edge
- ✅ Opera

## 🎓 Learning Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Tailwind CSS Docs](https://tailwindcss.com/docs)
- [Scikit-Learn Guide](https://scikit-learn.org/stable/)
- [Font Awesome Icons](https://fontawesome.com/icons)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Bhuvanesh**
- GitHub: [@Bhuvanesh3602](https://github.com/Bhuvanesh3602)
- Email: bhuvanesh.s3602@example.com

## 🙏 Acknowledgments

- Dataset: [Pima Indians Diabetes Database](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)
- Django framework for robust backend
- Tailwind CSS for modern styling
- Scikit-learn for ML capabilities
- Font Awesome for beautiful icons

## 📸 Screenshots

### Home Page
Modern landing page with hero section and feature cards

### Prediction Form
Beautiful form with real-time validation and helpful tooltips

### Dashboard
Comprehensive analytics with charts and statistics

### History
Detailed table view of all past predictions

---

<div align="center">

**⭐ Star this repository if you found it helpful!**

**Made with ❤️, 🤖 AI, and 🎨 Tailwind CSS**

</div>
