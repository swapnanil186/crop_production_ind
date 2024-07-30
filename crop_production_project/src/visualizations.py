import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_crop_production_over_time(df):
    """
    Plot crop production over time.
    
    Parameters:
    - df (pd.DataFrame): The dataframe containing crop production data.
    """
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df, x='Crop_Year', y='Production', hue='Crop')
    plt.title('Crop Production Over Time')
    plt.xlabel('Year')
    plt.ylabel('Production')
    plt.legend(loc='upper right')
    plt.show()

def plot_production_by_state(df):
    """
    Plot production by state.
    
    Parameters:
    - df (pd.DataFrame): The dataframe containing crop production data.
    """
    plt.figure(figsize=(12, 6))
    sns.barplot(data=df, x='State_Name', y='Production', ci=None)
    plt.title('Production by State')
    plt.xlabel('State')
    plt.ylabel('Production')
    plt.xticks(rotation=90)
    plt.show()

def plot_top_10_states_by_production(df):
    """
    Plot the top 10 states by production counts.
    
    Parameters:
    - df (pd.DataFrame): The dataframe containing crop production data.
    """
    top_10_states = df['State_Name'].value_counts()[:10]
    top_10_states.plot(kind='bar', figsize=(12, 6))
    plt.xlabel('State Name')
    plt.ylabel('Counts')
    plt.title('Top 10 States by Production Counts')
    plt.show()

def plot_top_10_districts_by_production(df):
    """
    Plot the top 10 districts by production counts.
    
    Parameters:
    - df (pd.DataFrame): The dataframe containing crop production data.
    """
    top_10_districts = df['District_Name'].value_counts()[:10]
    top_10_districts.plot(kind='bar', figsize=(12, 6))
    plt.xlabel('District')
    plt.ylabel('Counts')
    plt.title('Top 10 Districts by Production Counts')
    plt.show()

def plot_production_pie_chart(df):
    """
    Plot a pie chart of production by crop.
    
    Parameters:
    - df (pd.DataFrame): The dataframe containing crop production data.
    """
    crop_production = df.groupby('Crop')['Production'].sum().sort_values(ascending=False)
    plt.figure(figsize=(10, 8))
    crop_production.plot(kind='pie', autopct='%1.1f%%')
    plt.title('Crop Production Distribution')
    plt.ylabel('')
    plt.show()

if __name__ == "__main__":
    # Example usage
    df = pd.read_csv('data/crop_production.csv')
    df = preprocess_data(df)  # Ensure data is preprocessed
    plot_crop_production_over_time(df)
    plot_production_by_state(df)
    plot_top_10_states_by_production(df)
    plot_top_10_districts_by_production(df)
    plot_production_pie_chart(df)
