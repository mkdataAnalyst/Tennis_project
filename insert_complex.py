import pandas as pd
import json
import mysql.connector
from mysql.connector import Error

# Database connection details
host = 'localhost'
user = 'root'  # Replace with your MySQL username
password = 'Bb$alws90m!'  # Replace with your MySQL password
database = 'Tennis'  # Replace with your database name

# Read the CSV file
csv_file = 'complexes_flat.csv'  # Path to your CSV file
df = pd.read_csv(csv_file)

# Debug: Print the first few rows of the DataFrame
print("CSV Data Preview:\n", df.head())

# Establish MySQL connection
def create_connection():
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        if connection.is_connected():
            print('Successfully connected to the database')
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

# Insert data into Complexes table
def insert_complexes(cursor, df):
    for _, row in df.iterrows():
        try:
            cursor.execute("""
                INSERT IGNORE INTO Complexes (complex_id, complex_name)
                VALUES (%s, %s)
            """, (row['complex_id'], row['complex_name']))
        except Error as e:
            print(f"Error inserting into Complexes: {e}")

# Insert data into Venues table
def insert_venues(cursor, df):
    for _, row in df.iterrows():
        try:
            # Check if 'venues' is not NaN and is a valid string
            if pd.notna(row['venues']) and isinstance(row['venues'], str):
                # Parse the venues JSON-like string
                venues = json.loads(row['venues'].replace("'", "\""))  # Replace single quotes with double quotes for valid JSON

                # Iterate over each venue and insert into the Venues table
                for venue in venues:
                    cursor.execute("""
                        INSERT INTO Venues (id, name, city_name, country_name, country_code, timezone, complex_id)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """, (
                        venue['id'], venue['name'], venue['city_name'],
                        venue['country_name'], venue['country_code'],
                        venue['timezone'], row['complex_id']
                    ))
            else:
                print(f"Skipping row with invalid 'venues': {row['venues']}")
        except json.JSONDecodeError as e:
            print(f"JSON decode error for complex_id={row['complex_id']}: {e}")
        except Error as e:
            print(f"Database error for complex_id={row['complex_id']}: {e}")

# Main function to process the data
def main():
    connection = create_connection()
    if connection:
        cursor = connection.cursor()

        # Insert data into Complexes and Venues tables
        insert_complexes(cursor, df)
        insert_venues(cursor, df)

        # Commit the transaction
        connection.commit()

        print("Data successfully inserted into Complexes and Venues tables!")

        # Close the cursor and connection
        cursor.close()
        connection.close()

# Run the main function
if __name__ == '__main__':
    main()
