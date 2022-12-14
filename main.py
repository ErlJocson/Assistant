import speech_recognition as sr
from speak import speak
from command import get_command

listener = sr.Recognizer()


def main():
    speak("Welcome back sir.")
    speak("Tell me what to do!")
    try:
        with sr.Microphone() as source:
            voice = listener.listen(source)
        command = listener.recognize_google(voice).lower()
        get_command(command)
    except sr.RequestError:
        speak("API unavailable")

    except sr.UnknownValueError:
        speak("Sorry i did not understand that")
    main()


if __name__ == "__main__":
    main()
