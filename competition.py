import requests
import pandas as pd
import json

# Fetch the data
url = "https://api.sportradar.com/tennis/trial/v3/en/competitions.json?api_key=2mGwDCeJDgBxY7VjgT41wTQu62PDiJ4MQNLF84N5"
headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    # Parse JSON response
    data = response.json()
    
    # Example: Flatten the "competitions" data if it's nested
    if "competitions" in data:
        competitions = data["competitions"]
        
        # Flatten the JSON structure
        df = pd.json_normalize(competitions)
        
        # Display the DataFrame
        print(df.head())
        
        # Save to CSV for further analysis
        df.to_csv("competitions_flat.csv", index=False)
        print("Flattened JSON saved to competitions_flat.csv")
    else:
        print("No 'competitions' key found in the response.")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
