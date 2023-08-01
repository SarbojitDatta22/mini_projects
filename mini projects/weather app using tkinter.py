import requests
import tkinter as tk
from tkinter import messagebox

def get_weather_data(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def display_weather_data(data):
    if data["cod"] == "404":
        messagebox.showerror("Error", "City not found. Please check the city name.")
    else:
        weather_info = f"Weather in {data['name']}:\n"
        weather_info += f"Description: {data['weather'][0]['description']}\n"
        weather_info += f"Temperature: {data['main']['temp']}°C\n"
        weather_info += f"Humidity: {data['main']['humidity']}%\n"
        weather_info += f"Wind Speed: {data['wind']['speed']} km/h"
        messagebox.showinfo("Weather Information", weather_info)

def fetch_weather():
    api_key = "fe25120146037fa4cf667af23fea530f"  # Replace with your OpenWeatherMap API key
    city = city_entry.get()

    try:
        weather_data = get_weather_data(api_key, city)
        display_weather_data(weather_data)
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", "Error fetching weather data. Please check your internet connection.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main window
root = tk.Tk()
root.title("Weather App")

# Create widgets
city_label = tk.Label(root, text="Enter City Name:")
city_label.pack(pady=10)

city_entry = tk.Entry(root)
city_entry.pack(pady=5)

get_weather_button = tk.Button(root, text="Get Weather", command=fetch_weather)
get_weather_button.pack(pady=10)

# Start the tkinter main loop
root.mainloop()
