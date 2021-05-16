import subprocess

class Voiceroid:
    def __init__(self, path):
        self.vrx_path = path

    def talk(self, text):
        print("> " + text)
        subprocess.run([self.vrx_path, text])