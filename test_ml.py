import pytest
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from ml.data import process_data
from ml.model import train_model, compute_model_metrics

# TODO: implement the first test. Change the function name and input as needed
def test_one():
    """
    # Test that process_data outputs arrays of the expected shape.
    """
    data = pd.read_csv("data/census.csv")
    categorical_features = ["workclass", "education", "marital-status", "occupation", "relationship", "race", "sex", "native-country"]
    
    # Process the data
    X, y, _, _ = process_data(data, categorical_features=categorical_features, label="salary", training=True)
    
    # Check that the processed data is not empty
    assert X.shape[0] > 0, "Processed data should not be empty"
    assert y.shape[0] > 0, "Labels should not be empty"
    # Check that X and y have the same number of rows
    assert X.shape[0] == y.shape[0], "X and y should have the same length"

# TODO: implement the second test. Change the function name and input as needed
def test_two():
    """
    # Test that train_model returns a RandomForestClassifier instance.
    """
    # Dummy data to avoid training on the full dataset during testing
    X_train = np.random.rand(100, 5)
    y_train = np.random.randint(0, 2, 100)
    
    model = train_model(X_train, y_train)
    
    # Check that the model is an instance of RandomForestClassifier
    assert isinstance(model, RandomForestClassifier), "The model should be a RandomForestClassifier"

# TODO: implement the third test. Change the function name and input as needed
def test_three():
    """
    # Test that compute_model_metrics returns values between 0 and 1.
    """
    y_true = [0, 1, 1, 0, 1]
    y_pred = [0, 1, 1, 0, 0]

    precision, recall, f1 = compute_model_metrics(y_true, y_pred)
    
    # Check that precision, recall, and F1-score are between 0 and 1
    assert 0 <= precision <= 1, "Precision should be between 0 and 1"
    assert 0 <= recall <= 1, "Recall should be between 0 and 1"
    assert 0 <= f1 <= 1, "F1 score should be between 0 and 1"
