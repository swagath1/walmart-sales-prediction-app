# walmart-sales-prediction-app

🛒 Walmart Sales Prediction
📌 Project Overview

This project predicts weekly sales for Walmart stores using machine learning.
It helps businesses forecast demand, optimize inventory, and improve decision-making.

🚀 Live App

👉 Try the app here:
🔗 (https://walmart-sales-prediction-app-2awxnflmscxhf4gpvf546c.streamlit.app/)

🎯 Problem Statement

Walmart needs to forecast weekly sales based on various factors like:

Seasonal trends (Month, Week)
Economic conditions (Fuel Price, CPI, Unemployment)
Store characteristics (Type, Size)
External factors (Temperature, Holidays)

The goal is to build a model that accurately predicts sales using these features.

📊 Dataset Features
Store / Dept – Store and department identifiers
Temperature – Weather conditions
Fuel Price – Economic indicator
CPI / Unemployment – Economic factors
MarkDown1–5 – Promotional discounts
IsHoliday – Holiday indicator
Type – Store type (A, B, C)
Size – Store size
Year, Month, Week – Time-based features
⚙️ Data Preprocessing
Converted boolean values (IsHoliday) to numeric
Extracted Month & Week from date
Applied One-Hot Encoding on Store Type
Handled missing values in markdown features
Ensured feature consistency between training and deployment
🤖 Model Used
Gradient Boosting Regressor (or your model name)
Why this model?
Handles non-linear relationships
Performs well on tabular data
Better accuracy compared to linear models
📈 Model Evaluation
Evaluated using regression metrics like:
RMSE (Root Mean Squared Error)
R² Score

👉 The model shows good performance in capturing sales patterns.

🖥️ Streamlit App Features
User-friendly interface
Input fields for:
Temperature
Fuel Price
Month & Week
Holiday
Store Type
Real-time sales prediction
🧠 Key Learning
Importance of feature engineering
Handling categorical variables (get_dummies)
Solving feature mismatch issue during deployment
Building end-to-end ML pipeline
Deploying models using Streamlit Cloud
📂 Project Structure
wall/
│
├── wall.py
├── walmart_sales_model.pkl
├── columns.pkl
├── requirements.txt
└── README.md
⚡ Installation & Run Locally
pip install -r requirements.txt
streamlit run wall.py
📌 Future Improvements
Add more features (store-level trends)
Hyperparameter tuning
Add visualization dashboard
Improve model accuracy
👤 Author

Swagath Reddy

GitHub: (https://github.com/swagath1/walmart-sales-prediction-app)
