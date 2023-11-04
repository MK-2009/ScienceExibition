import pyttsx3
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import speech_recognition as sr

# Initialize recognizer
r = sr.Recognizer()

# Function to get audio command from user
def get_command():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio)
            print(f"You said: {command}")
        except Exception as e:
            print("Sorry, I didn't catch that.")
            return ""
    return command.lower()

# Initializing the Edge driver
driver = webdriver.Edge(service=Service(r'C:\\Users\\Admin\\Downloads\\edgedriver_win64\\msedgedriver.exe'))

# Function to play song on YouTube using Selenium
def play_song_on_youtube(song_name):
    # Navigate to the YouTube search page with the song name
    driver.get(f"https://www.youtube.com/results?search_query={song_name}")

    # Wait for the page to load
    time.sleep(2)

    # Find the first video and click it to play
    video = driver.find_element(By.ID, "video-title")
    video.click()

    # Call the function to skip ad
    skip_ad()

# Function to skip ad on YouTube using Selenium
def skip_ad():
    time.sleep(5)  # Wait for the ad to load
    try:
        # Find the "Skip Ads" button and click it
        skip_button = driver.find_element(By.CLASS_NAME, "ytp-ad-skip-button")
        skip_button.click()
        print("Ad skipped")
    except Exception as e:
        print("No skippable ad")

# Main function to process commands
def main():
    while True:
        command = get_command()
        if "play" in command:
            song_name = command.split(" ", 1)[1]  # Get the song name from the command
            try:
                play_song_on_youtube(song_name)  # Open the search results for the specified song in the default web browser
                print(f"Playing {song_name} on YouTube")
            except Exception as e:
                print(f"Sorry, I couldn't play {song_name}")

if __name__ == "__main__":
    main()
