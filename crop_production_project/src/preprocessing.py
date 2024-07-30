import pandas as pd

def preprocess_data(df):
    """
    Clean and preprocess the dataset.
    
    Parameters:
    - df (pd.DataFrame): The dataframe to preprocess.
    
    Returns:
    - pd.DataFrame: The preprocessed dataframe.
    """
    # Drop rows with missing values
    df.dropna(inplace=True)
    
    # Convert columns to appropriate data types
    df['Crop_Year'] = df['Crop_Year'].astype(int)
    df['Season'] = df['Season'].str.strip()
    df['Crop'] = df['Crop'].str.strip()
    df['Area'] = df['Area'].astype(float)
    df['Production'] = df['Production'].astype(float)
    
    return df

if __name__ == "__main__":
    # Example usage
    df = pd.read_csv('data/crop_production.csv')
    df = preprocess_data(df)
    print(df.info())
