import requests
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox

def get_weather_data(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def display_weather_data(data):
    if data["cod"] == "404":
        show_error_message("Error", "City not found. Please check the city name.")
    else:
        weather_info = f"Weather in {data['name']}:\n"
        weather_info += f"Description: {data['weather'][0]['description']}\n"
        weather_info += f"Temperature: {data['main']['temp']}°C\n"
        weather_info += f"Humidity: {data['main']['humidity']}%\n"
        weather_info += f"Wind Speed: {data['wind']['speed']} km/h"
        show_info_message("Weather Information", weather_info)

def show_error_message(title, message):
    msg_box = QMessageBox(QMessageBox.Icon.Critical, title, message)
    msg_box.exec()

def show_info_message(title, message):
    msg_box = QMessageBox(QMessageBox.Icon.Information, title, message)
    msg_box.exec()

def fetch_weather():
    api_key = "fe25120146037fa4cf667af23fea530f"  # Replace with your OpenWeatherMap API key
    city = city_entry.text()

    try:
        weather_data = get_weather_data(api_key, city)
        display_weather_data(weather_data)
    except requests.exceptions.RequestException as e:
        show_error_message("Error", "Error fetching weather data. Please check your internet connection.")
    except Exception as e:
        show_error_message("Error", f"An error occurred: {e}")

app = QApplication([])
root = QMainWindow()
root.setWindowTitle("Weather App")

central_widget = QWidget()
root.setCentralWidget(central_widget)

layout = QVBoxLayout()

city_label = QLabel("Enter City Name:")
layout.addWidget(city_label)

city_entry = QLineEdit()
layout.addWidget(city_entry)

get_weather_button = QPushButton("Get Weather")
get_weather_button.clicked.connect(fetch_weather)
layout.addWidget(get_weather_button)

central_widget.setLayout(layout)

root.show()
app.exec()
