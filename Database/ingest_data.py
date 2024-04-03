import os
import pandas as pd
from sqlalchemy import create_engine, VARCHAR, INTEGER, DATE,DECIMAL

# Database connection parameters
DB_USER = 'postgres'
DB_PASSWORD = '41433448'
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'Group_one'

# Database URL
DB_URL = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'


def create_table(engine, table_name, df):
    # Define the data types mapping
    data_types_mapping = {
        'object': VARCHAR,
        'int64': INTEGER,
        'float64': DECIMAL,  
        'datetime64': DATE   
    }
    
    
    column_types = {col: data_types_mapping[str(df[col].dtype)] for col in df.columns}
    
    # Create the table
    df.to_sql(table_name, engine, if_exists='replace', index=False, dtype=column_types)


def ingest_data():
    # Connect to the database
    engine = create_engine(DB_URL)
    
    # Define the directory containing CSV files
    data_dir = '../Data_generation/generated_data'
    
    # Get list of CSV files in the generated_data directory
    csv_files = [f for f in os.listdir(data_dir) if f.endswith('.csv')]
    
    # Iterate through each CSV file
    for file in csv_files:
        # Read the CSV file using pandas
        df = pd.read_csv(os.path.join(data_dir, file))
        
        # Determine the table name from the filename
        table_name = os.path.splitext(file)[0].lower().replace(' ', '_')
        
        # Create table and insert data
        create_table(engine, table_name, df)
        print(f'Table {table_name} created and data from {file} ingested')

if __name__ == "__main__":
    ingest_data()
