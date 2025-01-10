import pandas as pd
import mysql.connector
from mysql.connector import Error

# Database connection details
host = 'localhost'
user = 'root'  # Replace with your MySQL username
password = 'Bb$alws90m!'  # Replace with your MySQL password
database = 'Tennis'  # Replace with your database name

# Read the CSV file
csv_file = 'competitions_flat.csv'  # Path to your CSV file
df = pd.read_csv(csv_file)

# Debug: Print the column names to check for any issues
print("Columns in CSV:", df.columns)

# Clean column names by stripping any extra spaces
df.columns = df.columns.str.strip()

# Check again after cleaning
print("Cleaned Columns in CSV:", df.columns)

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

# Insert data into Categories table
def insert_categories(cursor, df):
    categories = df['category_id'].unique()  # Get unique category IDs from the CSV

    for category_id in categories:
        category_name = df[df['category_id'] == category_id]['category_name'].iloc[0]
        
        try:
            cursor.execute("""
                INSERT IGNORE INTO Categories (category_id, category_name)
                VALUES (%s, %s)
            """, (category_id, category_name))
        except Error as e:
            print(f"Error inserting into Categories: {e}")

# Insert data into Competitions table
def insert_competitions(cursor, df):
    for index, row in df.iterrows():
        try:
            cursor.execute("""
                INSERT INTO Competitions (competition_id, competition_name, parent_id, type, gender, category_id)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (
                row['competition_id'], 
                row['competition_name'], 
                row['parent_id'] if pd.notna(row['parent_id']) else None, 
                row['type'], 
                row['gender'], 
                row['category_id']
            ))
        except Error as e:
            print(f"Error inserting into Competitions: {e}")

# Main function to process the data
def main():
    connection = create_connection()
    if connection:
        cursor = connection.cursor()

        # Insert data into Categories and Competitions tables
        insert_categories(cursor, df)
        insert_competitions(cursor, df)

        # Commit the transaction
        connection.commit()

        print("Data successfully inserted into Categories and Competitions tables!")

        # Close the cursor and connection
        cursor.close()
        connection.close()

# Run the main function
if __name__ == '__main__':
    main()
