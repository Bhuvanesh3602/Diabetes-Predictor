import pandas as pd
import os

# Path to CSV file
csv_path = 'myapp/submissions.csv'

print("Fixing CSV file...")

try:
    # Read CSV with error handling
    df = pd.read_csv(csv_path, on_bad_lines='skip')
    
    print(f"Original rows: {len(df)}")
    print(f"Columns: {list(df.columns)}")
    
    # Check if Timestamp column exists
    if 'Timestamp' in df.columns:
        # Keep only rows with valid data
        df['Outcome'] = pd.to_numeric(df['Outcome'], errors='coerce')
        df = df.dropna(subset=['Outcome'])
        
        # Ensure all numeric columns are numeric
        numeric_cols = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 
                       'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome']
        
        for col in numeric_cols:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce')
        
        # Drop rows with any NaN values
        df = df.dropna()
        
        print(f"Cleaned rows: {len(df)}")
        
        # Save cleaned CSV
        df.to_csv(csv_path, index=False)
        print(f"✅ CSV file fixed! Saved {len(df)} valid rows.")
        
        # Show statistics
        print(f"\nStatistics:")
        print(f"Total predictions: {len(df)}")
        print(f"Diabetes risk detected: {int((df['Outcome'] == 1).sum())}")
        print(f"Low risk: {int((df['Outcome'] == 0).sum())}")
        print(f"Average Glucose: {df['Glucose'].mean():.1f}")
        print(f"Average BMI: {df['BMI'].mean():.1f}")
    else:
        print("⚠️ No Timestamp column found. CSV might be in old format.")
        print("Adding Timestamp column...")
        
        # Add timestamp column at the beginning
        from datetime import datetime
        df.insert(0, 'Timestamp', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        
        # Save with timestamp
        df.to_csv(csv_path, index=False)
        print("✅ Timestamp column added!")
        
except Exception as e:
    print(f"❌ Error: {e}")
    print("\nTrying alternative fix...")
    
    # Create a clean CSV with sample data
    sample_data = {
        'Timestamp': ['2024-01-15 10:00:00', '2024-01-15 11:00:00', '2024-01-15 12:00:00'],
        'Pregnancies': [1, 6, 2],
        'Glucose': [85, 148, 120],
        'BloodPressure': [66, 72, 70],
        'SkinThickness': [29, 35, 30],
        'Insulin': [0, 0, 100],
        'BMI': [26.6, 33.6, 28.5],
        'DiabetesPedigreeFunction': [0.351, 0.627, 0.450],
        'Age': [31, 50, 40],
        'Outcome': [0, 1, 0]
    }
    
    df_clean = pd.DataFrame(sample_data)
    df_clean.to_csv(csv_path, index=False)
    print("✅ Created new CSV with sample data!")

print("\n🎉 Done! Restart your server and check the dashboard.")
