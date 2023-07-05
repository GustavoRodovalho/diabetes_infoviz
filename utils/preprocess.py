import missingno as msno
import pandas as pd
import numpy as np

def load(path:str):
    df = pd.read_csv("data/diabetes.csv")
    df[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']] = df[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']].replace(0, np.NaN)
    df["Glucose"].fillna(df["Glucose"].mean(), inplace = True)
    df["BloodPressure"].fillna(df["BloodPressure"].mean(), inplace = True)
    df["SkinThickness"].fillna(df["SkinThickness"].mean(), inplace = True)
    df["Insulin"].fillna(df["Insulin"].mean(), inplace = True)
    df["BMI"].fillna(df["BMI"].mean(), inplace = True)
    
    return df