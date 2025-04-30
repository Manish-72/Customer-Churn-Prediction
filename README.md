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


## 📈 Model Performance

| Model               | Accuracy | Precision | Recall | Specificity | F1 Score | ROC AUC | Confusion Matrix       |
|---------------------|----------|-----------|--------|-------------|----------|---------|------------------------|
| Gradient Boosting   | 81.94%   | 69.03%    | 57.95% | 90.61%      | 62.99%   | 87.58%  | [[938, 97], [157, 217]] |
| XGBoost             | 80.05%   | 64.08%    | 56.50% | 88.56%      | 60.04%   | 85.43%  | [[916, 118], [163, 211]] |
| Random Forest       | 80.49%   | 66.11%    | 54.31% | 89.95%      | 59.59%   | 85.26%  | [[931, 104], [171, 203]] |
| Decision Tree       | 75.32%   | 53.42%    | 55.16% | 82.61%      | 54.25%   | 68.95%  | [[855, 180], [168, 206]] |

*Metrics obtained from cross-validation testing*

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
  "features": [1, 0, 2, 1, 45, 1, 0, 2, 0, 1, 0, 0, 1, 0, 3, 0, 1, 60.5, 2435.6]
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
🔗 [LinkedIn](https://www.linkedin.com/in/manish-saini-274a371b4/)  
🛠️ 6-Star HackerRank | 1200+ DSA Problems Solved

---

## 🧠 Contact Me

Looking for a Data Scientist, freelance ML developer or intern?

📧 **Email**: [msaini720415@gmail.com](mailto:msaini720415@gmail.com)
