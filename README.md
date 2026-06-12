# House-Price-Prediction
🏠 An end-to-end Machine Learning project that predicts residential property prices using housing characteristics from the Ames Housing Dataset. The project covers the complete ML lifecycle including data preprocessing, feature engineering, model comparison, feature selection, deployment, and cloud hosting.

---

# 🚀 Live Demo

# Streamlit Application

https://house-price-prediction-apgdwjenrthvq8rscxtxr8.streamlit.app/

---

# 📖 Project Overview

Accurate house price estimation is important for buyers, sellers, investors, and real estate professionals. Property prices are influenced by multiple factors such as location, lot size, construction quality, neighborhood, and available amenities.

The objective of this project was to build a machine learning solution capable of predicting house prices while maintaining a simple and user-friendly interface.

Instead of requiring a large number of user inputs, the final deployed model uses a compact set of high-impact features, providing strong predictive performance with improved usability.

---

# 🎯 Problem Statement

Develop a regression model that can accurately predict residential property prices based on housing characteristics and deploy it as an interactive web application accessible to end users.

---

# 📊 Dataset

The project uses the Ames Housing Dataset, a widely used dataset for regression problems containing detailed information about residential properties.

# Target Variable
SalePrice

---

# 🔧 Data Preprocessing

The following preprocessing techniques were applied:

## Missing Value Treatment
Identified missing values

Handled null values using appropriate strategies

## Categorical Feature Encoding

Implemented One-Hot Encoding for categorical variables including:

HouseStyle
Neighborhood

## Data Transformation

Used:

ColumnTransformer

Pipeline

Train-Test Split

Feature Selection

These preprocessing steps ensured consistency between model training and deployment.

---

# 🤖 Models Evaluated

Multiple regression algorithms were trained and compared.

Model |	R² Score |

Linear Regression | 87.24% |

Random Forest Regressor | 88.61% |

XGBoost Regressor | 90.51% |

Gradient Boosting Regressor | 90.83% |

The experiments demonstrated that ensemble-based boosting techniques outperformed traditional linear models for this problem.

---

# 🔍 Feature Importance Analysis

Feature importance analysis was performed using Gradient Boosting Regressor to identify the most influential variables affecting house prices.

Several experiments were conducted using different feature subsets:

Features Used |	R² Score |

Top 5 Features | ~67% |

Top 10 Features	| ~70% |

Top 15 Features | ~78% |

Although larger feature sets improved performance, they increased the amount of information required from users.

To improve usability, a smaller feature set was selected for deployment.

---

# ✅ Final Features Used in Deployment

The deployed application uses the following seven features:

LotArea

HouseStyle

Neighborhood

YearBuilt

OverallQual

TotalBsmtSF

GarageCars

These features provide a balance between prediction accuracy and user convenience.

---

# 🚀 Deployed Model

The production application uses a Gradient Boosting Regressor trained on the selected feature set.

Performance

Approximate R² Score: 88%

Optimized for real-world usability

Reduced user input requirements

Faster prediction workflow

This approach sacrifices a small amount of accuracy in exchange for a significantly better user experience.

---

# 🖥️ Web Application Features

Users can:

Enter property information

Select house style

Select neighborhood

Provide construction details

Submit information through an intuitive interface

Instantly receive a predicted house price

---

# 🛠️ Technologies Used

# Programming

Python

# Data Analysis

Pandas

NumPy

# Machine Learning

Scikit-Learn

Gradient Boosting Regressor

Random Forest Regressor

XGBoost Regressor

Linear Regression

# Deployment

Streamlit

# Version Control

Git

GitHub

---

# 📂 Project Structure

House-Price-Prediction/

│

├── app.py

├── gb_model.pkl

├── requirements.txt

├── README.md

├── LICENSE

├── images/
│   └── app_preview.png

└── House Price Prediction using Machine Learning.ipynb

---

# 📈 Machine Learning Workflow
Data Collection
        ↓
        
Data Cleaning
        ↓
        
Missing Value Handling
        ↓
        
Feature Engineering
        ↓
        
Categorical Encoding
        ↓
        
Feature Selection
        ↓ 
        
Model Training
        ↓ 
        
Model Evaluation
        ↓ 
        
Model Serialization
        ↓ 
        
Streamlit Application
        ↓ 
        
Cloud Deployment

---

# ▶️ Run Locally

# Clone the repository:

git clone https://github.com/su1sh2il/House-Price-Prediction.git

Navigate to the project directory:

cd House-Price-Prediction

Install dependencies:

pip install -r requirements.txt

Run the application:

streamlit run app.py

---

# 🎓 Key Skills Demonstrated

Data Preprocessing

Missing Value Handling

Feature Engineering

Feature Selection

One-Hot Encoding

ColumnTransformer

Scikit-Learn Pipelines

Regression Modeling

Model Evaluation

Cross Validation

Streamlit Development

Git & GitHub

Cloud Deployment

---

# 🔮 Future Improvements

Hyperparameter optimization

Interactive feature importance dashboard

Batch prediction using CSV upload

Advanced visualization components

Automated model comparison interface

---

# 👨‍💻 Author

# Sushil Kumar

Machine Learning | Data Science | AI

GitHub: https://github.com/su1sh2il

---

⭐ If you found this project useful, consider giving the repository a star.

