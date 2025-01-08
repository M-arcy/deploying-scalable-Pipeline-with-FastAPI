import pickle
from sklearn.metrics import fbeta_score, precision_score, recall_score
from ml.data import process_data
# TODO: add necessary import
from sklearn.ensemble  import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score  

# Optional: implement hyperparameter tuning.
def train_model(X_train, y_train):
    """
    Trains a machine learning model and returns it.

    Inputs
    ------
    X_train : np.array
        Training data.
    y_train : np.array
        Labels.
    Returns
    -------
    model
        Trained machine learning model.
    """
    # TODO: implement the function
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    return model
    


def compute_model_metrics(y, preds):
    """
    Validates the trained machine learning model using precision, recall, and F1.

    Inputs
    ------
    y : np.array
        Known labels, binarized.
    preds : np.array
        Predicted labels, binarized.
    Returns
    -------
    precision : float
    recall : float
    fbeta : float
    """
    fbeta = fbeta_score(y, preds, beta=1, zero_division=1)
    precision = precision_score(y, preds, zero_division=1)
    recall = recall_score(y, preds, zero_division=1)
    return precision, recall, fbeta


def inference(model, X_test):
    """ Run model inferences and return the predictions.

    Inputs
    ------
    model : model (RandomForestClassifier)
        Trained machine learning model.
    X_test : np.array
        Data used for prediction.
    Returns
    -------
    preds : np.array
        Predictions from the model.
    """
    # TODO: implement the function
    preds = model.predict(X_test)

    return preds



def save_model(model, path):
    """ Serializes model to a file.

    Inputs
    ------
    model
        Trained machine learning model or OneHotEncoder.
    path : str
        Path to save pickle file.
    """
    # TODO: implement the function
    try:
        with open(path, 'wb') as f:  # Write in binary mode
            pickle.dump(model, f)
    except Exception as e:
        print(f"Model not saved. Error: {e}")

def load_model(path):
    """ Loads pickle file from `path` and returns it."""
    # TODO: implement the function
    try:
        with open(path, 'rb') as f:  # Read in binary mode
            model = pickle.load(f)
        return model
    except Exception as e:
        print(f"Model not loaded. Error: {e}")


#function to compute performance on a categorical slice of data 
def performance_on_categorical_slice(
    data, column_name, slice_value, categorical_features, label, encoder, lb, model
):
    """ Computes the model metrics on a slice of the data specified by a column name and

    Processes the data using one hot encoding for the categorical features and a
    label binarizer for the labels. This can be used in either training or
    inference/validation.
    
    performance_on_categorical_slice is a function that computes the performance metrics when the value of a given feature is held fixed. E.g., for education, it would print out the model metrics for data with a particular value for education.

    Inputs
    ------
    data : pd.DataFrame
        Dataframe containing the features and label. Columns in `categorical_features`
    column_name : str
        Column containing the sliced feature.
    slice_value : str, int, float
        Value of the slice feature.
    categorical_features: list
        List containing the names of the categorical features (default=[])
    label : str
        Name of the label column in `X`. If None, then an empty array will be returned
        for y (default=None)
    encoder : sklearn.preprocessing._encoders.OneHotEncoder
        Trained sklearn OneHotEncoder, only used if training=False.
    lb : sklearn.preprocessing._label.LabelBinarizer
        Trained sklearn LabelBinarizer, only used if training=False.
    model : model(RandomForestClassifier)
        Model used for the task.

    Returns
    -------
    precision : float
    recall : float
    fbeta : float

    """
    # TODO: implement the function
    input_data = data[data[column_name] == slice_value]
    if input_data.empty:
        return 0, 0, 0  # Handle empty slice case
    X_slice, y_slice, _, _ = process_data(
        X=input_data,
        categorical_features=categorical_features,
        label=label,
        training=False,
        encoder=encoder,
        lb=lb,
        # your code here
        # for input data, use data in column given as "column_name", with the slice_value 
        # use training = False
    )
    preds = inference(model, X_slice) # your code here to get prediction on X_slice using the inference function
    precision, recall, fbeta = compute_model_metrics(y_slice, preds)
    return precision, recall, fbeta
