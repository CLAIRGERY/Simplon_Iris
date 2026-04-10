import joblib
import os
import pandas as pd

def test_model_loading():
    path = "../model/model.pkl" 
    assert os.path.exists(path)
    model = joblib.load(path)
    assert model is not None

def test_model_prediction_logic():
    path = "../model/model.pkl" 
    model = joblib.load(path)
    
    # Au lieu d'une liste, on crée un petit DataFrame avec les bons noms de colonnes
    feature_names = ["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]
    sample = pd.DataFrame([[5.1, 3.5, 1.4, 0.2]], columns=feature_names)
    
    prediction = model.predict(sample)
    assert prediction[0] in ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']