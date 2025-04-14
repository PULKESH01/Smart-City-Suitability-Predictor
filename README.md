# 🌍 Smart City Suitability Predictor

A data-driven, machine learning-powered application that predicts **whether it's good to stay in a city** based on **real-time weather** and **air quality index (AQI)** data fetched from OpenWeatherMap APIs. It also provides a **5-day weather forecast with a visualization**, combining environmental science with practical AI insights.

---

## 🚀 Features

- 🔍 **Real-Time Data**: Fetches live weather and AQI data from OpenWeatherMap API.
- 🧠 **Machine Learning Prediction**: Predicts if the current conditions are suitable to live using a trained Random Forest model.
- 📈 **5-Day Forecast Visualization**: Beautiful temperature trendline using Seaborn and Matplotlib.
- 🛠️ **Custom Trained Classifier**: Uses synthetic data to train a model that evaluates temperature, humidity, wind speed, and AQI levels.
- 🌐 **Interactive CLI Input**: Asks users to input any city and country code.

---

## 🧪 Technologies Used

| Component         | Tech Stack                                    |
|------------------|-----------------------------------------------|
| Language         | Python 3.x                                     |
| Data Source      | OpenWeatherMap API (Weather + Air Pollution)  |
| Machine Learning | Scikit-learn (Random Forest Classifier)        |
| Data Viz         | Matplotlib, Seaborn                            |
| Scaling          | StandardScaler from Scikit-learn              |

---

## 📦 Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/PULKESH01/smart-city-suitability-predictor.git
   cd smart-city-suitability-predictor
   ```

2. Install dependencies (or use Colab):
   ```bash
   pip install -r requirements.txt
   ```

3. Add your OpenWeatherMap API key:
   ```python
   API_KEY = "5acc79a4dd0593bf86e79fe226f2db09"
   ```

4. Run the script:
   ```bash
   python main.py
   ```

---

## 📝 How It Works

1. **User Input**: User enters the city and country code.
2. **API Fetching**: Weather and AQI data are pulled using latitude & longitude.
3. **Model Evaluation**:
   - Temperature, Humidity, Wind Speed, and AQI are input into a classifier.
   - A Random Forest Classifier (trained on 200 synthetic environmental samples) determines whether conditions are suitable to stay.
4. **Forecast Plot**: The script pulls and displays the 5-day temperature forecast using line charts.

---

## 📈 Example Output

```text
Enter city name: Delhi
Enter country code (e.g., IN): IN

📍 City: Delhi, IN
🌡️ Temperature: 33.1°C
💧 Humidity: 30%
🍃 Wind Speed: 2.5 m/s
💨 AQI Level: 4 (1=Good, 5=Very Poor)

🏠 Stay Suitability: ⚠️ Not ideal to stay
```

_Followed by a 5-day temperature line chart._

---

## 🔐 API Access

You need a free API key from [OpenWeatherMap](https://openweathermap.org/api). Enable:

- Geocoding API
- Current Weather Data API
- Air Pollution API
- 5-Day / 3-Hour Forecast API

---

## 🧠 Future Improvements

- ✅ Add support for storing historic city performance
- 📈 Track AQI trends across weeks/months
- 🌱 Recommend health precautions based on air quality
- ☁️ Deploy as a web dashboard using Streamlit or Flask

---

## 📌 License

This project is licensed under the MIT License.

