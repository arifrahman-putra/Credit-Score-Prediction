import pandas as pd
import numpy as np
import joblib



# pick the best performed model
model_RFC = joblib.load("Saved Models/model_RFC.pkl")

# load the artifacts
scaler = joblib.load("standard_scaler.pkl")
encoders = joblib.load("label_encoders.pkl")
target_encoder = encoders["Credit_Score"]
Label_Encoded_columns = joblib.load("Label_Encoded_columns.pkl")
OneHot_Encoded_columns = joblib.load("OneHot_Encoded_columns.pkl")

# load and scale test dataset features
X_test = pd.read_csv("Dataset/preprocessed_test dataset.csv")
numerical_cols = [col for col in X_test.columns if col not in OneHot_Encoded_columns + Label_Encoded_columns]

# scale only the numerical columns
X_test_scaled = X_test.copy()
X_test_scaled.loc[:, numerical_cols] = scaler.transform(X_test[numerical_cols])


y_pred = model_RFC.predict(X_test_scaled)
y_pred = target_encoder.inverse_transform(y_pred)


# load original test dataset
df_test_original = pd.read_csv("Dataset/test.csv")
df_test_original["Credit_Score"] = y_pred

df_test_original.to_csv("Dataset/predicted_test.csv", index=False)