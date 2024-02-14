# Import necessary modules and libraries
import pytz 
import json
import ipdata
import requests
from datetime import datetime

# API keys and constants
IP_API_KEY = 'c620dfd0f0f494e8fc73c56baee299eafc18d349bbf212304f2a5bcc'
WEATHER_API_KEY = 'e96cfa3532dadb821370a79d4ab262ff'
LOG_BASE_LOCATION = 'static/log/logs.json'
IST = pytz.timezone('Asia/Kolkata')
LOGDATA = []

# Class for handling time-related operations
class Time:
    @staticmethod
    def getTime():
        # Get the current time in the Indian Standard Time (IST) timezone
        return str(datetime.now(IST))[:-13]
    
# Class for logging user activities
class Logger:
    
    def __init__(self) -> None:
        pass

    def __writeLog(self, data: dict) -> None:
        # Write log data to the logs.json file
        with open(LOG_BASE_LOCATION, 'w') as logfile:
            logfile.write(data)

    def readLog(self, ip_address: str, location: str, page: str) -> None:
        # Read log data from the logs.json file
        with open(LOG_BASE_LOCATION, 'r') as logfile:
            data = json.load(logfile)
            # Update log data with user's IP address, accessed page, and visit information
            if ip_address not in data:
                data.update(
                    {
                        ip_address:{
                            page:{
                                'Location': [location], 
                                'Access Time': [
                                    Time.getTime()
                                ],
                                'Visits': 1
                            }
                        }
                    }
                )
            else:
                if page not in data[ip_address]:
                    data[ip_address].update(
                        {
                            page:{
                                'Location': [location], 
                                'Access Time': [
                                    Time.getTime()
                                ],
                                'Visits': 1
                            }
                        }
                    )
                else:
                    data[ip_address][page]['Location'].append(location)
                    data[ip_address][page]['Access Time'].append(Time.getTime())
                    data[ip_address][page]['Visits'] += 1
        data = json.dumps(data, indent=4)
        return self.__writeLog(data)

# Class for handling newsletter subscriptions
class NewsLetter:
    @staticmethod
    def subscribeToNewsLetter(email: str):
        # Append the email to the newsletter.txt file
        with open("static/forms/newsletter.txt", "a") as file:
            if email:
                file.write(email + "\n")
            file.flush()

# Class for getting coordinates based on IP address
class Coordinates:
    @staticmethod
    def getCoordinates(ip) -> list:
        # Fetch latitude and longitude using IP address
        ipdata.api_key = f'{IP_API_KEY}'
        response = ipdata.lookup(ip)
        # Return weather data based on latitude and longitude
        return Weather.getCurrentWeather(str(response['latitude']), str(response['longitude']))

# Class for fetching current weather data
class Weather:
    @staticmethod
    def getCurrentWeather(latitude: str, longitude: str) -> list:
        # Fetch current weather data using latitude and longitude
        response = dict(requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&units=metric&appid={WEATHER_API_KEY}'
        ).json())
        # Extract and return temperature and city name
        return [int(response['main']['temp']), response['name']]

# class to read & write query of contact field
class Contacts:
    @staticmethod
    def addQuery(name: str, email: str, comment: str) -> None:
        with open('static/forms/feedback.txt', 'a') as querylog:
            querylog.write(name + '\n')
            querylog.write('\t' + email + '\n')
            querylog.write('\t' + comment + '\n')
            querylog.flush()