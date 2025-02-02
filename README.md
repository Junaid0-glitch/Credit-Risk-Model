# RiskGuard AI: Credit Risk Modelling 🚀

## 📌 Overview  
**RiskGuard AI** is a machine learning-based credit risk modeling system designed to help Risk Units assess customer creditworthiness. It predicts the likelihood of loan default using historical loan and bureau data.

## 🎯 Objective  
To build a reliable credit risk model with high interpretability and strong performance in real-world scenarios.

## 📊 Dataset  
- **Size:** 50,000 records  
- **Features:** Customer loan and bureau data  
- **Target Variable:** Default (Binary: 1 = Default, 0 = No Default)  

## 🛠️ Tech Stack  
- **Programming:** Python  
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn  
- **Modeling:** XGBoost, Logistic Regression, Random Forest  
- **Optimization:** Optuna, RandomizedSearchCV  
- **Deployment:** Streamlit App, MLOps & Cloud Tools  

## 🔄 Data Preprocessing  
- Replaced invalid loan purpose values with mode  
- Feature selection using **Information Value (IV), Variance Inflation Factor (VIF), and domain knowledge**  
- Min-Max scaling for numerical features  

## 🏆 Model Performance Metrics  
| Metric | Target | Achieved |
|--------|--------|----------|
| **AUC (Area Under Curve)** | > 85% | ✅ Achieved |
| **Gini Coefficient** | > 85 | ✅ Achieved |
| **KS Statistic** | > 40 | ✅ Achieved (Max KS in first 3 deciles) |

## 📊 Model Evaluation  
- **AUC, KS, Gini Coefficients**  
- **Classification Report**  
- **Decile-wise Performance Analysis**  

## 🚀 Deployment  
- **Streamlit App** for user-friendly risk assessment  
- **MLOps & Cloud Integration** for scalability  
