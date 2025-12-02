import pickle
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
from pathlib import Path

class MLService:
    def __init__(self):
        self.model = GaussianNB()
        self.label_encoders = {}
        self.feature_columns = [
            'academic_pressure', 'work_pressure', 'cgpa',
            'study_satisfaction', 'job_satisfaction', 'work_study_hours',
            'financial_stress', 'age'
        ]
        self.categorical_columns = ['gender', 'sleep_duration', 'dietary_habits', 
                                    'suicidal_thoughts', 'family_history']
    
    def prepare_features(self, df: pd.DataFrame, fit_encoders=False):
        """Prepare features for training/prediction"""
        X = df.copy()
        
        # Encode categorical variables
        for col in self.categorical_columns:
            if col in X.columns:
                if fit_encoders:
                    self.label_encoders[col] = LabelEncoder()
                    X[col] = self.label_encoders[col].fit_transform(X[col].fillna('Unknown'))
                else:
                    if col in self.label_encoders:
                        X[col] = self.label_encoders[col].transform(X[col].fillna('Unknown'))
        
        # Select numerical features
        feature_cols = [col for col in self.feature_columns if col in X.columns]
        feature_cols += [col for col in self.categorical_columns if col in X.columns]
        
        return X[feature_cols].fillna(0)
    
    def train(self, df: pd.DataFrame):
        """Train Naive Bayes model"""
        X = self.prepare_features(df, fit_encoders=True)
        y = df['depression']
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        # Train model
        self.model.fit(X_train, y_train)
        
        # Evaluate
        y_pred = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred, output_dict=True)
        
        return {
            "accuracy": accuracy,
            "report": report,
            "train_size": len(X_train),
            "test_size": len(X_test)
        }
    
    def predict(self, student_data: dict):
        """Predict depression for a single student"""
        df = pd.DataFrame([student_data])
        X = self.prepare_features(df, fit_encoders=False)
        
        prediction = self.model.predict(X)[0]
        probability = self.model.predict_proba(X)[0]
        
        return {
            "prediction": int(prediction),
            "probability": {
                "no_depression": float(probability[0]),
                "depression": float(probability[1])
            }
        }
    
    def save_model(self, path: str):
        """Save model to disk"""
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        with open(path, 'wb') as f:
            pickle.dump({
                'model': self.model,
                'label_encoders': self.label_encoders
            }, f)
    
    def load_model(self, path: str):
        """Load model from disk"""
        with open(path, 'rb') as f:
            data = pickle.load(f)
            self.model = data['model']
            self.label_encoders = data['label_encoders']