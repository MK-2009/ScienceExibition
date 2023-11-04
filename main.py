import speech_recognition as sr
import pyttsx3
import openai
import json

# Initialize the recognizer and the text to speech engine
r = sr.Recognizer()
engine = pyttsx3.init()

# Get the list of voices
voices = engine.getProperty('voices')

# Set the voice you want to use by its ID
desired_voice_id = voices[2].id  # Replace 0 with the index of the voice you want to use
engine.setProperty('voice', desired_voice_id)


# Function to convert text to speech
def speak(text):
    print(text)  # Print the text to the console
    engine.say(text)
    engine.runAndWait()


# Function to listen to the microphone
def listen():
    with sr.Microphone() as source:
        speak("Listening...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except:
            speak("Sorry, I didn't get that")
            return listen()


# Set your OpenAI API key here
openai.api_key = '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'

# Load the conversation history from a file
try:
    with open('history.json', 'r') as f:
        messages = json.load(f)
except FileNotFoundError:
    # If the file doesn't exist, initialize the list of messages with the system message
    messages = [{"role": "system", "content": "You're name's Sofiya.You are a kinda bot, created by MK.You have the ability to remember personal details.You are created in Bagya Matriculation School.Your Developer Name is MK.He is an indie-Developer Who creates amazing games, applications, Animations, Websites, and some programmings.You're Created in Sri Bagya Matriculation School by MK.You must thankful for the teachers who supported in creating you.You're owner's name is MK.As an AI you have a name but not age or anything else.You are created esspeciealy for a Science Exhibition as his project.If you cant answer the question you just simply say, Ask MK.As well as you can speak throuh spoken words you only support english"}]

while True:
    # Listen to the user's question
    question = listen()

    # Add the user's question to the list of messages
    messages.append({"role": "user", "content": question})

    if question.lower() == "stop":
        break

    # Get the answer from ChatGPT
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages  # Use the list of messages here
    )

    # Speak out and print the answer
    answer = response['choices'][0]['message']['content']
    speak(answer)

    # Add the assistant's answer to the list of messages
    messages.append({"role": "assistant", "content": answer})

    # Saving the conversation history to a file
    with open('history.json', 'w') as f:
        json.dump(messages, f)
