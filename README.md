# 🧠 Customer Churn Prediction System

This project predicts whether a customer will churn (leave) based on historical service and usage data. The model is deployed as a **live REST API** using Flask and hosted on Render — ready for integration into real-world business systems.

---

## 📌 Project Highlights

- 📊 Real-world business dataset (Telco)
- 🧼 Full data cleaning, preprocessing, and EDA
- 🤖 Trained multiple models (Logistic Regression, Random Forest)
- 📈 Evaluated with precision, recall, F1-score
- 🌐 Built and deployed as a **live API** using Flask + Render

---

## 📂 Dataset Information

**Source**: [Kaggle - Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)  
**Records**: 7,000+ customer records  
**Target**: `Churn` (Yes/No)  
**Features**: 
- Demographics 
- Services subscribed 
- Billing information 
- Account tenure 

---

## ⚙️ Technologies Used

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pandas](https://img.shields.io/badge/Pandas-2.x-green)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.x-orange)
![Flask](https://img.shields.io/badge/Flask-3.x-lightgrey)

- **Data Processing**: Pandas, NumPy
- **Visualization**: Seaborn, Matplotlib
- **ML Framework**: Scikit-learn
- **API Development**: Flask
- **Deployment**: Render
- **Version Control**: Git & GitHub

---

## 🛠️ Project Structure
Customer-Churn-Prediction/
├── app.py # Flask API
├── requirements.txt # Package dependencies
├── model/
│ └── churn_prediction_model.pkl
├── notebooks/
│ ├── EDA_and_Cleaning.ipynb
│ └── Model_Training_and_Evaluation.ipynb
└── README.md


---

## 📈 Model Performance

| Model                | Accuracy | Precision | Recall | F1 Score |
|----------------------|----------|-----------|--------|----------|
| Logistic Regression  | 79.5%    | 74%       | 68%    | 71%      |
| Random Forest        | 83.2%    | 78%       | 75%    | 76.5%    |

*Results obtained from 5-fold cross validation*

---

## 🚀 API Documentation

**Base URL**: [https://customer-churn-api-aa7a.onrender.com](https://customer-churn-api-aa7a.onrender.com)

### `/` - GET
- Health check endpoint
- Returns: `"✅ Customer Churn Prediction API is running!"`

### `/predict` – POST  
**Request Format**:
```json
{
  "features": [0, 1, 0, 2, 1, 45, 1, 0, 2, 0, 1, 0, 0, 1, 0, 3, 0, 1, 60.5, 2435.6]
}
```
Response:
```json
{
  "churn_prediction": 1, "interpretation": "1 = Churn, 0 = No Churn"
} 
```

## ✨ Author

**Manish Saini**  
🎓 B.E. in Computer Science, Chandigarh University  
📍 Alwar, Rajasthan  
🔗 [LinkedIn](https://www.linkedin.com/in/your-linkedin-id)  
🛠️ 6-Star HackerRank | 1200+ DSA Problems Solved

---

## 🧠 Contact Me

Looking for a freelance ML developer or intern?

📧 **Email**: [msaini720415@gmail.com](mailto:msaini720415@gmail.com)
# Customer-Churn
