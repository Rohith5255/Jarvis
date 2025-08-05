import speech_recognition as sr
import webbrowser
import pyttsx3
import time

import pyttsx3
engine = pyttsx3.init()


def speak(text):
    print(f"Jarvis says: {text}")  # Debug
    time.sleep(0.5)  # Short delay before speaking
    engine.say(text)
    engine.runAndWait()


def processCommand(c):
    c = c.lower().strip()  # Normalize input
    print(f"Normalized command: '{c}'")  # Debugging
    
    if "open google" in c:
        speak("Opening Google")
        webbrowser.open_new_tab("https://www.google.com")

    elif "open youtube" in c:
        speak("Opening YouTube")
        try:
            chrome = webbrowser.get(using='windows-default')  # optional
            chrome.open_new_tab("https://www.youtube.com")
        except Exception as e:
            speak("Sorry, I couldn't open YouTube.")
            print("Error opening YouTube:", e)

    elif "open linkedin" in c:
        speak("Opening LinkedIn")
        webbrowser.open_new_tab("https://www.linkedin.com")

    else:
        speak("Sorry, I didn't understand that command. Please try again.")
        print(f"Unrecognized command: {c}")


if __name__ == "__main__":
    time.sleep(2)  # Initial delay for better performance
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
                            print("Jarvis Active...")
                            audio = r.listen(source, timeout=5, phrase_time_limit=5)
                            command = r.recognize_google(audio)
                            print(f"Command: {command}")
                            speak("Processing your command...")
                            processCommand(command)

                    except sr.WaitTimeoutError:
                        print("No command heard. Exiting active mode.")
                        break
                    except sr.UnknownValueError:
                        print("Couldn’t understand command.")
                    except Exception as e:
                        print("Error in command loop:", e)
                        break

        except sr.WaitTimeoutError:
            print("No speech detected. Restarting...")
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")            
        except Exception as e:
            print("Error:", e)
