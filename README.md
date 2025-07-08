# 🏠 House Price Prediction App

This project is a simple machine learning web app to predict house prices using user input features such as location, area, number of bedrooms, etc. The model is trained using Linear Regression.

## 🚀 Demo

Gradio app opens in your browser and allows you to input features to get the predicted house price instantly.

## 📂 Project Structure

house-price-prediction/
├── data/
│ └── House Price Prediction Dataset.csv
├── app.py
├── House_price_prediction.ipynb
├── requirements.txt
└── README.md


## 🧠 Model Info

- **Algorithm:** Linear Regression
- **Libraries Used:** pandas, scikit-learn, gradio

## 🔧 Setup Instructions

1. Clone the repo:

```bash
git clone https://github.com/Akhilesh-yadav680/house-price-prediction.git
cd house-price-prediction
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the app:

bash
Copy
Edit
python app.py
A local web interface will open where you can input house details to get price predictions.

📊 Sample Features Used
Location

Area (sq ft)

Bedrooms

Bathrooms

Furnishing Status

... (based on dataset columns)

✅ Output
Predicted House Price (in ₹)

📝 License
This project is licensed under the MIT License.

Made  using Python & Gradio



---

### 📄 `requirements.txt`

```txt
pandas
scikit-learn
gradio
📄 .gitignore
gitignore
Copy
Edit
__pycache__/
*.pyc
*.pkl
*.ipynb_checkpoints/
.env
🧠 Optional: Export Trained Model
In your notebook, you can export the model like this:

import joblib
joblib.dump(model, 'model.pkl')
Then you can load it in app.py instead of retraining every time.













