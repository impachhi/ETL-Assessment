import pandas as pd
import sqlite3


# Step 1: Extract data from the flat file
def extract_data(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error reading the file: {e}")
        return None


# Step 2: Transform data
def transform_data(df):
    # Trim spaces and convert data types
    df['name'] = df['name'].str.strip()
    df['date_of_birth'] = pd.to_datetime(df['date_of_birth'], errors='coerce')
    df['salary'] = pd.to_numeric(df['salary'], errors='coerce')
    df['department_id'] = df['department_id'].astype(int)
    return df


# Step 3: Load data into employees table
def load_employees(df, connection):
    df.to_sql('employees', connection, if_exists='replace', index=False)


# Step 4: Populate departments table with unique department IDs and names
def load_departments(df, connection):
    unique_departments = df[['department_id', 'name']].drop_duplicates(subset='department_id')
    unique_departments = unique_departments.rename(columns={'name': 'department_name'})
    unique_departments.to_sql('departments', connection, if_exists='replace', index=False)


def main():
    # Database connection
    conn = sqlite3.connect('company.db')

    # Extract data
    df = extract_data('employees.txt')

    if df is not None:
        # Transform data
        df = transform_data(df)

        # Load employees data
        load_employees(df, conn)
        print("Employees table loaded successfully.")

        # Load departments data
        load_departments(df, conn)
        print("Departments table loaded successfully.")

    # Close the connection
    conn.close()


if __name__ == "__main__":
    main()
