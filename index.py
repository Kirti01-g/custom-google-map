import pyttsx3

def init_speaker():
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)  # Speech speed
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # Change index for different voices
    return engine

def speak(engine, text):
    engine.say(text)
    engine.runAndWait()

def main():
    engine = init_speaker()
    print("🤖 RoboSpeaker is running...")
    print("Type 'exit' to stop.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            speak(engine, "Goodbye. Have a nice day.")
            break
        speak(engine, user_input)

if __name__ == "__main__":
    main()
