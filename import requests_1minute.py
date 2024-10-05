import requests
import csv
from datetime import datetime, timedelta

# Your HDFC API authorization key
api_key = 'your_hdfc_authorization_key'

# Function to fetch historical data in chunks
def fetch_historical_data(symbol, interval, start_date, end_date):
    url = f'https://api.hdfcsec.com/historical-data/{symbol}?interval={interval}&start_date={start_date}&end_date={end_date}'
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Unable to fetch data, Status Code: {response.status_code}")
        return None

# Save the data to CSV
def save_to_csv(data, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Datetime', 'Open', 'High', 'Low', 'Close', 'Volume'])

        for row in data:
            writer.writerow([row['datetime'], row['open'], row['high'], row['low'], row['close'], row['volume']])

# Set stock symbol, interval, and date range (past 10 years)
symbol = 'NSE:NHPC'
interval = '1min'
start_date = '2013-10-01'
end_date = '2023-10-01'

# Fetch and save the data
historical_data = fetch_historical_data(symbol, interval, start_date, end_date)

if historical_data:
    save_to_csv(historical_data, 'nhpc_historical_1min.csv')
    print(f"Data saved to nhpc_historical_1min.csv")
