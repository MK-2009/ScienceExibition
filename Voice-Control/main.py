import speech_recognition as sr
import serial
import time

# Initialize the recognizer
recognizer = sr.Recognizer()

# Create a serial connection to the Arduino (update 'COM4' with your Arduino's port)
arduino = serial.Serial('COM3', 9600, timeout=1)
time.sleep(2)  # Allow time for Arduino to initialize

while True:
    try:
        # Use the laptop's microphone to listen to your voice command
        with sr.Microphone() as source:
            print("Listening for a command...")
            audio = recognizer.listen(source)

        # Recognize the command using Google Web Speech API
        command = recognizer.recognize_google(audio).lower()

        # Print the recognized command
        print("You said: " + command)

        # Send commands to Arduino via serial
        if "turn on LED" or "turn on led" in command:
            arduino.write(b'1')  # Send '1' to turn the LED on
        elif "turn off led" in command:
            arduino.write(b'0')  # Send '0' to turn the LED off
        elif "turn on fan" in command:
            arduino.write(b'2')  # Send '2' to turn the fan (motor) on
        elif "turn off fan" in command:
            arduino.write(b'3')  # Send '3' to turn the fan (motor) off

    except sr.UnknownValueError:
        print("Could not understand the audio")

    except sr.RequestError as e:
        print(f"Could not request results; {e}")

    except KeyboardInterrupt:
        print("Closing the program.")
        arduino.close()
        break
