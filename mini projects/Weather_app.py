import requests
import argparse

def get_weather_data(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def print_weather_info(api_key, city):
    try:
        weather_data = get_weather_data(api_key, city)
        if weather_data["cod"] == "404":
            print("City not found. Please check the city name.")
        else:
            print(f"Weather in {weather_data['name']}:")
            print(f"Description: {weather_data['weather'][0]['description']}")
            print(f"Temperature: {weather_data['main']['temp']}°C")
            print(f"Humidity: {weather_data['main']['humidity']}%")
            print(f"Wind Speed: {weather_data['wind']['speed']} km/h")
    except requests.exceptions.RequestException as e:
        print("Error fetching weather data. Please check your internet connection.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Weather App")
    parser.add_argument("--api-key", required=True, help="OpenWeatherMap API key")
    parser.add_argument("--city", required=True, help="City name")
    args = parser.parse_args()

    print_weather_info(args.api_key, args.city)
