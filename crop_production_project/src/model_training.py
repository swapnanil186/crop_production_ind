import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def train_model(df):
    """
    Train a linear regression model to predict crop production.
    
    Parameters:
    - df (pd.DataFrame): The dataframe containing crop production data.
    
    Returns:
    - model (LinearRegression): The trained linear regression model.
    - X_test (pd.DataFrame): The test features.
    - y_test (pd.Series): The test target values.
    """
    X = df[['Crop_Year', 'Area']]
    y = df['Production']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    return model, X_test, y_test

def evaluate_model(model, X_test, y_test):
    """
    Evaluate the model using mean squared error.
    
    Parameters:
    - model (LinearRegression): The trained model.
    - X_test (pd.DataFrame): The test features.
    - y_test (pd.Series): The test target values.
    
    Returns:
    - mse (float): The mean squared error of the model.
    """
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    
    return mse

if __name__ == "__main__":
    df = pd.read_csv('data/crop_production.csv')
    df = preprocess_data(df)  # Ensure data is preprocessed
    model, X_test, y_test = train_model(df)
    mse = evaluate_model(model, X_test, y_test)
    print(f'Mean Squared Error: {mse}')
