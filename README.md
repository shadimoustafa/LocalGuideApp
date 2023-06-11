# The Local Guide App

## Overview
The Local Guide App is a Python desktop application that displays real-time weather and top news headlines for a user-specified city. It uses several APIs to gather information, including the OpenWeatherMap API for weather data, the Photon API for geolocation, the NewsAPI for news data, and the TimezoneFinder library for timezone data. The app is built using the Tkinter library for the GUI.

![image](https://github.com/shadimoustafa/LocalGuideApp/assets/35777080/d06e4d11-1d01-4fcb-ab5e-a4e909b98e1b)

## Features
* Real-time weather data for any city around the world.
* Top news headlines relevant to the specified city.
* Current local time of the specified city.

## Getting Started
### Prerequisites
Before you start, you should have Python 3 installed on your system. You will also need pip, which is usually included in most Python installations.

### Installation
1. Clone the repo:
git clone [https://github.com/your_username_/Project-Name.git](https://github.com/shadimoustafa/LocalGuideApp.git)

markdown
Copy code
2. Install required Python libraries:
pip install tkinter geopy timezonefinder datetime requests pytz newsapi-python

markdown
Copy code
3. Obtain your API keys for [OpenWeatherMap](https://home.openweathermap.org/users/sign_up) and [NewsAPI](https://newsapi.org/register).

4. Replace the placeholders in the `app.py` file with your API keys.

### Usage
Run `WeatherApp.py` to start the application. Enter a city name in the input field and hit the search icon to display the weather, current time, and top news headlines for that city.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
