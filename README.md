# 🏦 Credit Score Classification Dashboard

## 📌 Project Overview
This project showcases an end to end ML pipeline of customers' credit score predictions comprising "Dataset Preparation & Exploratory Analysis", "Model Development & Performance Validation", "Model Deployment & Inference", and "Dashboard & Visualization". 
The datasets ("train.csv" and "test.csv") are obtained from a Kaggle dataset page: https://www.kaggle.com/datasets/parisrohan/credit-score-classification

please download these datasets from the Kaggle page and put them in a "Dataset/" folder

The **Credit Score** categories comprising three classes (`Good`, `Standard`, `Poor`).


The workflow is split into four parts:
1. **Dataset Preparation & Exploratory Analysis** => load "Dataset/train.csv" and "Dataset/test.csv", select categorical and numerical feature columns, analyze data imperfections (NaNs, invalid strings, etc), conduct feature engineering (manual mapping, label encoding, one-hot encoding, interpolation & standardization), select usable features based on Pearson's correlation matrix and Gini Feature Importance

repository file: "Dataset Preparation.ipynb"

outputs:
- pre-processed datasets: "Dataset/preprocessed_train dataset.csv" & "Dataset/preprocessed_test dataset.csv"
- artifacts: "Label_Encoded_columns.pkl", "OneHot_Encoded_columns.pkl", "label_encoders.pkl"

2. **Model Development & Performance Validation** => Compare ML classification model performance with 0.2 validation size (from train dataset): 
- Random Forest Classifier (RFC) ==> scikit-learn
- K-Nearest Neighbor (KNN) Classifier ==> scikit-learn
- XGBoost (XGB) Classifier ==> xgboost
- LightGBM (LGBM) Classifier ==> lgbm
- Deep Neural Network ==> keras

repository file: "Model Development.ipynb"

Each non-neural network model undergone GridSearchCV-based hyperparameter tuning to ensure the best performing parameter set. Random Forest Classifier (RFC) was proven to be the most performing model based on the accuracy, precision, recall, and F1-score that span between 76-78%. 

outputs:
- Models: "Saved Models/"
- artifact: "standard_scaler.pkl"

3. **Model & Inference** => Run ML model (Random Forest Classifier) to predict "Dataset/preprocessed_test dataset.csv"

repository file: "Model Deployment and Inference.py"
output: prediction result ==> "Dataset/predicted_test.csv"

how to run:
   ```bash
   python "Model Deployment and Inference.py"
   ```

4. **Dashboard & Visualization** => load prediction result "Dataset/preprocessed_test dataset.csv", create a streamlit dashboard and data visualization

![Predictions Table](Dashboard_Predictions%20Table.png)

A. "Credit Score distribution": overall distribution of predicted credit score

![Credit Score distribution](Dashboard_CS%20Distribution.png)


B. "Customer Drill-Down": a customer name selection to showcase monthly trends of balance, total EMI, and total investment

![Monthly Balance](Dashboard_Monthly%20Balance.png)

![Monthly Total EMI](Dashboard_Total%20EMI.png)

![Monthly Total Investment](Dashboard_Total%20Investment.png)


repository file: "Streamlit Dashboard.py"

how to run:
   ```bash
   streamlit run "Streamlit Dashboard.py"
   ```

## ⚙️ Dependencies
- **Python 3.10 or above** 
- **Libraries and Packages**: "requirements.txt"
```bash
   pip install -r "requirements.txt"
   ```
---

## 📂 Project Structure
```
project-root/
│
├── Dataset/
│   ├── train.csv
│   ├── test.csv
│   ├── preprocessed_train dataset.csv
│   ├── preprocessed_test dataset.csv
│   └── predicted_test.csv
│
├── Saved Models/
│    ├── model_RFC.pkl
│    ├── model_KNN.pkl
│    ├── model_XGB.pkl
│    ├── model_LGBM.pkl
│    ├── model_DNN.keras
│
├── Dataset Preparation.ipynb
├── Model Development.ipynb
├── Model Deployment and Inference.py
├── Streamlit Dashboard.py
│
├── label_encoders.pkl
├── Label_Encoded_columns.pkl
├── OneHot_Encoded_columns.pkl
├── standard_scaler.pkl
│
├── Dashboard_CS Distribution.png
├── Dashboard_Predictions Table.png
├── Dashboard_Monthly Balance.png
├── Dashboard_Total EMI.png
├── Dashboard_Total Investment.png
│
├── requirements.txt
└── README.md
```
