import pandas as pd

def load_data(file_path):
    """
    Load the dataset from a CSV file.
    
    Parameters:
    - file_path (str): The path to the CSV file.
    
    Returns:
    - pd.DataFrame: The loaded dataframe.
    """
    return pd.read_csv(file_path)

if __name__ == "__main__":
    # Example usage
    df = load_data('data/crop_production.csv')
    print(df.head())
