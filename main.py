import speech_recognition as sr
import webbrowser
import pyttsx3
import sys
import requests
import time
import os

API_KEY = '905f2fc535322f13ea4629ab678d55b9'

def speak(text):
    engine = pyttsx3.init(driverName='sapi5')
    engine.setProperty('rate', 170)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    try:
        print(f"Jarvis says: {text}")
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print("Speech error:", e)

def processCommand(c):
    c = c.lower().strip()
    print(f"Normalized command: '{c}'")

    if "open google" in c:
        speak("Opening Google")
        webbrowser.open_new_tab("https://www.google.com")

    elif "open youtube" in c:
        speak("Opening YouTube")
        webbrowser.open_new_tab("https://www.youtube.com")

    elif "open spotify" in c:
        speak("Opening Spotify")
        try:
            os.system("start spotify:")
        except Exception as e:
            speak("Sorry, I couldn't open Spotify. Please check if it's installed.")

    elif "open linkedin" in c:
        speak("Opening LinkedIn")
        webbrowser.open_new_tab("https://www.linkedin.com")

    elif "weather" in c:
        speak("Please provide the location details in the console.")
        country = input("Country (2-letter code): ").strip()
        state = input("State (optional): ").strip()
        city = input("City: ").strip()
        speak("Fetching weather information...")
        weather_response = fetch_weather(country, state, city, API_KEY)
        speak(weather_response)
        print("Chatbot:", weather_response)

    elif c in ["exit", "quit", "stop"]:
        speak("Goodbye Sir. Closing the program.")
        sys.exit()

    else:
        speak("Sorry, I didn't understand that command.")

def fetch_weather(country, state, city, api_key):
    location = f"{city},{state},{country}" if state else f"{city},{country}"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        return f"Weather in {city}, {state}, {country}: {weather.capitalize()}, Temp: {temp}°C, Feels like: {feels_like}°C."
    else:
        return f"Sorry, I couldn't retrieve the weather for {city}, {state}, {country}. Please check the city/state/country names."

if __name__ == "__main__":
    speak("Hello Sir, I am Jarvis, your personal assistant.")
    r = sr.Recognizer()

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=3, phrase_time_limit=3)
            word = r.recognize_google(audio)
            print(f"You said: {word}")

            if word.lower() == "jarvis":
                speak("Yes sir")

                while True:
                    try:
                        with sr.Microphone() as source:
                            r.adjust_for_ambient_noise(source, duration=0.5)
                            print("Jarvis Active...")
                            audio = r.listen(source, timeout=5, phrase_time_limit=5)
                            command = r.recognize_google(audio)
                            print(f"Command: {command}")

                            if command.lower().strip() in ["exit", "quit", "stop"]:
                                speak("Goodbye Sir. Closing the program.")
                                sys.exit()

                            speak("Processing your command...")
                            processCommand(command)

                    except sr.WaitTimeoutError:
                        print("No command heard. Exiting active mode.")
                        break
                    except sr.UnknownValueError:
                        print("Couldn’t understand command.")
                        speak("Sorry, I didn't catch that.")
                    except Exception as e:
                        print("Error in command loop:", e)
                        break

        except sr.WaitTimeoutError:
            print("No speech detected. Restarting...")
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
        except Exception as e:
            print("Error:", e)
