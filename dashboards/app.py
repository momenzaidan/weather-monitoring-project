.# dashboards/app.py
import streamlit as st
import pandas as pd
import os

# --- Configuration ---
# The file path is relative to where the script is run from (the main project folder)
DATA_FILE_PATH = os.path.join('data', 'raw_weather_data.csv')

st.set_page_config(layout="wide")
st.title("☀️ OpenWeatherMap Live Monitoring Dashboard")

@st.cache_data(ttl=3600) # Caches the data for 1 hour so it doesn't read the file every time
def load_data():
    """Loads and prepares the weather data from the CSV file."""
    if not os.path.exists(DATA_FILE_PATH):
        return pd.DataFrame()

    df = pd.read_csv(DATA_FILE_PATH)
    # Convert timestamp to a proper datetime format
    df['datetime_utc'] = pd.to_datetime(df['timestamp_utc'], unit='s')
    df.set_index('datetime_utc', inplace=True)
    return df

# Load the data
df = load_data()

if df.empty:
    st.warning("No data collected yet. Please run the collection script.")
else:
    # --- 1. Key Metrics Section ---
    st.header(f"Current Conditions for {df['city'].iloc[-1]}")

    # Get the latest data point
    latest = df.iloc[-1]

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Temperature", f"{latest['temperature_c']:.1f}°C")
    col2.metric("Humidity", f"{latest['humidity_percent']}%")
    col3.metric("Wind Speed", f"{latest['wind_speed_m_s']:.1f} m/s")
    col4.metric("Description", latest['weather_description'].title())

    st.divider()

    # --- 2. Time-Series Visualization ---
    st.header("Historical Temperature Trend")

    # Select columns for the chart
    chart_data = df[['temperature_c', 'feels_like_c']]

    # Streamlit automatically generates an interactive line chart
    st.line_chart(chart_data, use_container_width=True)

    st.caption(f"Data collected from {df.index.min().strftime('%Y-%m-%d %H:%M')} to {df.index.max().strftime('%Y-%m-%d %H:%M')} UTC")