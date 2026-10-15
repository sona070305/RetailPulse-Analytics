import pandas as pd
import numpy as np
import pickle
from pathlib import Path
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score

BASE_DIR = Path(__file__).resolve().parent.parent
RFM_PATH = BASE_DIR / "processed" / "Customer_RFM_Segments.csv"
MODEL_DIR = BASE_DIR / "backend" / "app" / "models"

# Ensure directory exists cleanly
MODEL_DIR.mkdir(parents=True, exist_ok=True)

def train_churn_model():
    if not RFM_PATH.exists():
        raise FileNotFoundError(f"Missing processed file: {RFM_PATH}")
        
    df_rfm = pd.read_csv(RFM_PATH)
    df_rfm['Is_Churned'] = (df_rfm['Churn_Probability'] >= 0.70).astype(int)
    
    X = df_rfm[['Recency', 'Frequency', 'Monetary']]
    y = df_rfm['Is_Churned']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    y_preds = model.predict_proba(X_test)[:, 1]
    auc_score = roc_auc_score(y_test, y_preds)
    print(f"✅ Churn Model Trained Successfully! AUC-ROC Score: {auc_score:.4f}")
    
    output_model_path = MODEL_DIR / "churn_model.pkl"
    with open(output_model_path, "wb") as f:
        pickle.dump(model, f)
        
    print(f"📦 Model artifact saved to: {output_model_path}")

if __name__ == "__main__":
    train_churn_model()