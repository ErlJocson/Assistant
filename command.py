from behavior import AssistantBehavior
from speak import speak


def get_command(command):
    assistant = AssistantBehavior(command)

    if "define" in command:
        assistant.get_definition()

    elif "youtube" in command:
        assistant.search_in_youtube()

    elif "open" in command:
        assistant.open_tabs()

    elif "stop the program" or "end the program" or "stop program" or "end program" in command:
        speak("Stopping the program!")
        exit()
