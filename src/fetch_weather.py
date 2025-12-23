# src/fetch_weather.py

import requests
import json
import time
import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv(dotenv_path='/home/ubuntu/weather-monitoring-project/.env')

# --- Configuration ---
# Retrieve the sensitive key and city from the environment (safe)
API_KEY = os.getenv("OPENWEATHER_API_KEY")
CITY_NAME = os.getenv("CITY_NAME")

# Check if the key was loaded successfully
if not API_KEY or not CITY_NAME:
    print("ERROR: API Key or City Name not found. Check your .env file.")
    exit()

BASE_URL = "http://api.openweathermap.org/data/2.5/weather" 
UNIT = "metric" # for Celsius and meters/sec

def fetch_weather_data():
    """Fetches current weather data for the specified city and returns a cleaned dictionary."""

    # 1. Construct the API URL
    url = f"{BASE_URL}?q={CITY_NAME}&appid={API_KEY}&units={UNIT}"

    print(f"Fetching data for: {CITY_NAME}...")

    try:
        # 2. Make the request to OpenWeatherMap
        response = requests.get(url)
        response.raise_for_status() # Raise an exception for bad status codes (4xx or 5xx)
        data = response.json()

        # 3. Extract and clean the relevant data points
        weather_data = {
            'timestamp_utc': data['dt'], # Time of data calculation, UTC
            'city': data.get('name', CITY_NAME),
            'temperature_c': data['main']['temp'],
            'feels_like_c': data['main']['feels_like'],
            'humidity_percent': data['main']['humidity'],
            'pressure_hpa': data['main']['pressure'],
            'wind_speed_m_s': data['wind']['speed'],
            'weather_main': data['weather'][0]['main'],
            'weather_description': data['weather'][0]['description']
        }

        return weather_data

    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the API call: {e}")
        return None
    except KeyError as e:
        print(f"Error parsing JSON data: Missing key {e}")
        return None


def save_data(data_record):
    """Appends the fetched weather data to a CSV file in the data/raw folder."""

    file_path = os.path.join('data', 'raw_weather_data.csv')

    # Convert the single record dictionary to a DataFrame
    df = pd.DataFrame([data_record])

    # Check if file exists to determine if we need to write the header
    if os.path.exists(file_path):
        # Append without writing the header
        df.to_csv(file_path, mode='a', header=False, index=False)
        print(f"Data appended to {file_path}")
    else:
        # Write with header for the first time
        df.to_csv(file_path, mode='w', header=True, index=False)
        print(f"New data file created at {file_path}")


if __name__ == "__main__":
    # Ensure the data folder exists before trying to save
    os.makedirs('data', exist_ok=True)

    # Call the functions
    record = fetch_weather_data()

    if record:
        save_data(record)
    else:
        print("Failed to save data due to an error.")
