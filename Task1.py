import pandas as pd
import os
from datetime import datetime

file_path = 'dog_data_2017.csv'


# 1.	Read .csv file
def read_file(file_path):
    """Read a CSV file and return a DataFrame."""
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return None

    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None


# 1. List of unique breeds without duplicates.
def unique_breeds(df):
    # Return a list of unique dog breeds from the DataFrame.
    if 'Breed' not in df.columns:
        print("Column 'Breed' does not exist in the DataFrame.")
        return []

    df['Breed'] = df['Breed'].str.strip().str.lower()
    unique_breeds = df['Breed'].unique().tolist()
    return unique_breeds


# 2. List of number of licenses by LicenseType of each unique breed
def license_counts(df):
    # Group by 'Breed' and 'LicenseType' and count the number of licenses
    l_counts = df.groupby(['Breed', 'LicenseType']).size().reset_index(name='LicenseCount')
    return l_counts


# 3. 3. Top 5 popular name of dogs and create a list of these names along with count of dogs having these names.
def top_dog_names(df):
    top_names = df['DogName'].value_counts().head(5).reset_index()
    top_dog_names.columns = ['DogName', 'Count']
    return top_names


# 4. Method which takes date range as input and return the details of licences issues during that date.
def filter_data(df, start_date, end_date):
    df['ValidDate'] = pd.to_datetime(df['ValidDate'])
    filtered_data = df[(df['ValidDate'] >= start_date) & (df['ValidDate'] <= end_date)]
    return filtered_data
    # result=df.to_sql("Select * from df where ValidDate between 'start_date' and 'end_date'")


df = read_file(file_path)
if df is not None:
    breeds = unique_breeds(df)
    print('List of unique breeds without duplicates : \n', breeds)
    license_count = license_counts(df)
    print('List of number of licenses by LicenseType of each unique breed :\n', license_count)
    topNames = top_dog_names(df)
    print('Top Dog names are : \n', topNames)
    #
    s_date_str = input("Enter the start date (DD-MM-YYYY): ")
    s_date1 = datetime.strptime(s_date_str, '%d-%m-%Y').date()
    s_date=s_date1.strftime('%d-%m-%Y')
    print(s_date)
    e_date_str = input("Enter the end date (YYYY-MM-DD): ")
    e_date1 = datetime.strptime(e_date_str, '%d-%m-%Y').date()
    e_date=e_date1.strftime('%d-%m-%Y')
    print(e_date)
    filtered_data=filter_data(df,s_date,e_date)
    print('Filtered data for the given start & end dates are : \n',filtered_data)
