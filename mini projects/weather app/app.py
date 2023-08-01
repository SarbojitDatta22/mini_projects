import requests
from flask import Flask, render_template, request, flash

def create_app():
    app = Flask(__name__)
    app.secret_key = 'your_secret_key'  # Replace with your secret key

    def get_weather_data(api_key, city):
         url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
         response = requests.get(url)
         data = response.json()
         return data

    @app.route('/', methods=['GET', 'POST'])
    def weather_app():
        if request.method == 'POST':
            api_key = "fe25120146037fa4cf667af23fea530f"  # Replace with your OpenWeatherMap API key
            city = request.form['city']

            try:
                weather_data = get_weather_data(api_key, city)
                if weather_data["cod"] == "404":
                    flash("City not found. Please check the city name.", "error")
                else:
                    weather_info = f"Weather in {weather_data['name']}:\n"
                    weather_info += f"Description: {weather_data['weather'][0]['description']}\n"
                    weather_info += f"Temperature: {weather_data['main']['temp']}°C\n"
                    weather_info += f"Humidity: {weather_data['main']['humidity']}%\n"
                    weather_info += f"Wind Speed: {weather_data['wind']['speed']} km/h"
                    flash(weather_info, "info")
            except requests.exceptions.RequestException as e:
                flash("Error fetching weather data. Please check your internet connection.", "error")
            except Exception as e:
                flash(f"An error occurred: {e}", "error")

        return render_template('weather_app.html')
    
    return app

if __name__ == "__main__":
    app=create_app()
    app.run(debug=True, port=8000)
