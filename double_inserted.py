import pandas as pd
import mysql.connector
from mysql.connector import Error

# Database connection details
host = 'localhost'
user = 'root'  # Replace with your MySQL username
password = 'Bb$alws90m!'  # Replace with your MySQL password
database = 'Tennis'  # Replace with your database name

# Read the CSV file (path where your flattened data is stored)
csv_file = 'competitor_rankings.csv'  # Path to your CSV file
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

# Insert data into Competitors table
def insert_competitors(cursor, df):
    for index, row in df.iterrows():
        competitor_id = row['competitor_id']
        name = row['competitor_name']
        country = row['competitor_country']
        abbreviation = row['competitor_abbreviation']
        
        try:
            cursor.execute("""
                INSERT IGNORE INTO Competitors (competitor_id, name, country, country_code, abbreviation)
                VALUES (%s, %s, %s, %s, %s)
            """, (competitor_id, name, country, abbreviation))
        except Error as e:
            print(f"Error inserting into Competitors: {e}")

# Insert data into Competitor_Rankings table
def insert_competitor_rankings(cursor, df):
    for index, row in df.iterrows():
        rank = row['rank']
        movement = row['movement']
        points = row['points']
        competitions_played = row['competitions_played']
        competitor_id = row['competitor_id']
        
        try:
            cursor.execute("""
                INSERT INTO Competitor_Rankings (`rank`, movement, points, competitions_played, competitor_id)
                VALUES (%s, %s, %s, %s, %s)
            """, (rank, movement, points, competitions_played, competitor_id))
        except Error as e:
            print(f"Error inserting into Competitor_Rankings: {e}")

# Main function to process the data
def main():
    connection = create_connection()
    if connection:
        cursor = connection.cursor()

        # Insert data into Competitors and Competitor_Rankings tables
        insert_competitors(cursor, df)
        insert_competitor_rankings(cursor, df)

        # Commit the transaction
        connection.commit()

        print("Data successfully inserted into Competitors and Competitor_Rankings tables!")

        # Close the cursor and connection
        cursor.close()
        connection.close()

# Run the main function
if __name__ == '__main__':
    main()
