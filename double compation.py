import requests
import pandas as pd

# API URL and headers
url = "https://api.sportradar.com/tennis/trial/v3/en/double_competitors_rankings.json?api_key=2mGwDCeJDgBxY7VjgT41wTQu62PDiJ4MQNLF84N5"
headers = {"accept": "application/json"}

# Send GET request to fetch the data
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
else:
    print(f"Error fetching data: {response.status_code}")
    data = None

# Extract the rankings if the data exists
if data:
    rankings = data.get("rankings", [])

    # Prepare a list to hold the flattened data
    flat_data = []

    # Iterate over each ranking entry
    for ranking_entry in rankings:
        type_id = ranking_entry['type_id']
        name = ranking_entry['name']
        year = ranking_entry['year']
        week = ranking_entry['week']
        gender = ranking_entry['gender']

        # Extract competitor rankings
        for ranking in ranking_entry['competitor_rankings']:
            competitor = ranking['competitor']
            flat_data.append({
                'type_id': type_id,
                'name': name,
                'year': year,
                'week': week,
                'gender': gender,
                'rank': ranking['rank'],
                'movement': ranking['movement'],
                'points': ranking['points'],
                'competitions_played': ranking['competitions_played'],
                'competitor_id': competitor['id'],
                'competitor_name': competitor['name'],
                'competitor_country': competitor['country'],
                'competitor_abbreviation': competitor['abbreviation']
            })

    # Create a DataFrame from the extracted data
    df = pd.DataFrame(flat_data)

    # Save the data to a CSV file
    df.to_csv('competitor_rankings.csv', index=False)
    print("Data successfully saved to competitor_rankings.csv")

