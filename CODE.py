import requests
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import joblib

# Set your OpenWeatherMap API Key
API_KEY = "5acc79a4dd0593bf86e79fe226f2db09"

# ---------------------- API Functions ----------------------

def get_coordinates(city, country, api_key):
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city},{country}&limit=1&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    if data:
        return data[0]["lat"], data[0]["lon"]
    else:
        print("⚠️ Could not fetch coordinates.")
        return None, None

def get_weather(city, country, api_key):
    lat, lon = get_coordinates(city, country, api_key)
    if lat is None or lon is None:
        return None, None, None

    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data, lat, lon

def get_aqi(lat, lon, api_key):
    url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    try:
        return data["list"][0]["main"]["aqi"]
    except:
        print("⚠️ Could not fetch AQI.")
        return None

def get_5_day_forecast(lat, lon, api_key):
    url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

# ---------------------- Model & Prediction ----------------------

def create_dummy_data():
    np.random.seed(42)
    data = []
    for _ in range(200):
        temp = np.random.uniform(5, 40)
        humidity = np.random.uniform(10, 90)
        wind = np.random.uniform(0.5, 15)
        aqi = np.random.randint(1, 6)
        label = 1 if (aqi <= 2 and humidity < 70 and temp >= 15 and temp <= 35) else 0
        data.append([temp, humidity, wind, aqi, label])
    return np.array(data)

def train_model(data):
    X = data[:, :-1]
    y = data[:, -1]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    model = RandomForestClassifier(n_estimators=150, max_depth=10, random_state=42)
    model.fit(X_scaled, y)
    return model, scaler

def predict_stay(model, scaler, weather_data, aqi):
    temperature = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']

    features = np.array([[temperature, humidity, wind_speed, aqi]])
    features_scaled = scaler.transform(features)
    prediction = model.predict(features_scaled)[0]
    return "✅ Good to stay" if prediction == 1 else "⚠️ Not ideal to stay"

# ---------------------- Visualization ----------------------

def plot_forecast(forecast_data):
    temps = []
    timestamps = []
    for item in forecast_data["list"]:
        temps.append(item["main"]["temp"])
        timestamps.append(item["dt_txt"])

    plt.figure(figsize=(12, 5))
    sns.lineplot(x=timestamps, y=temps, marker="o", color="dodgerblue")
    plt.xticks(rotation=45, ha="right")
    plt.title("🌤️ 5-Day Temperature Forecast")
    plt.xlabel("Date & Time")
    plt.ylabel("Temperature (°C)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# ---------------------- Main Script ----------------------

def main():
    city = input("Enter city name: ")
    country = input("Enter country code (e.g., IN for India): ")

    weather_data, lat, lon = get_weather(city, country, API_KEY)
    if weather_data is None:
        return

    aqi = get_aqi(lat, lon, API_KEY)
    if aqi is None:
        return

    print(f"\n📍 City: {city}, {country}")
    print(f"🌡️ Temperature: {weather_data['main']['temp']}°C")
    print(f"💧 Humidity: {weather_data['main']['humidity']}%")
    print(f"🍃 Wind Speed: {weather_data['wind']['speed']} m/s")
    print(f"💨 AQI Level: {aqi} (1=Good, 5=Very Poor)\n")

    # Train model
    data = create_dummy_data()
    model, scaler = train_model(data)

    # Predict stay suitability
    status = predict_stay(model, scaler, weather_data, aqi)
    print(f"🏠 Stay Suitability: {status}")

    # Forecast visualization
    forecast_data = get_5_day_forecast(lat, lon, API_KEY)
    print("\n📊 5-Day Temperature Forecast:")
    plot_forecast(forecast_data)

# Run it
if __name__ == "__main__":
    main()
