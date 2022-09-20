import webbrowser
from speak import speak

class AssistantBehavior:
    def __init__(self, command):
        self.command = command

    def get_definition(self):
        self.command = self.command.replace("define ", "")
        webbrowser.open(f'https://www.google.com/search?q={self.command}')
        speak(f"Searching {self.command} in google")

    def search_in_youtube(self):
        self.command = self.command.replace("youtube ", "")
        webbrowser.open(f'https://www.youtube.com/results?search_query={self.command}')
        speak(f"Searching {self.command} in youtube")

    def open_tabs(self):
        self.command = self.command.replace("open ", "")
        webbrowser.open(f"https://{self.command}")
        speak(f"Opening {self.command}")
