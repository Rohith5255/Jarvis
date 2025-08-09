# Jarvis Voice Assistant 🎙️💻

This is my personal Python-based voice assistant, **Jarvis**, that can listen to my commands, talk back to me, and perform some basic tasks like:

- Opening websites (Google, YouTube, LinkedIn)
- Opening the Spotify desktop app
- Fetching live weather updates (via OpenWeatherMap API)
- Responding to simple voice prompts
- Exiting gracefully on voice command

It’s built using Python and a few awesome libraries for speech recognition and text-to-speech.

---

## Features

- **Wake word**: Say `"Jarvis"` to activate it.
- **Commands available**:
  - `"Open Google"`
  - `"Open YouTube"`
  - `"Open LinkedIn"`
  - `"Open Spotify"`
  - `"Weather"` → asks for location and fetches weather data.
  - `"Exit" / "Quit" / "Stop"` → ends the program.
- Talks back using `pyttsx3` and recognizes speech using Google’s speech recognition API.


## Requirements

Make sure you have Python 3 installed, then install these:
`"pip install speechrecognition pyttsx3 requestsp"`

On Windows, you’ll also need PyAudio for microphone input:
`"pip install pipwin"`
`"pipwin install pyaudio"`

Weather API Setup
For the weather command to work, you need an OpenWeatherMap API key.
- Sign up at `"https://openweathermap.org/api"`
- Create a free API key.
- Replace the API_KEY variable in the script with your key.
