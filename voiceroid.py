import os
import subprocess

class Voiceroid:
    def __init__(self, path = None):
        if not path == None:
            self.set_path(path)

    def talk(self, text):
        print("> " + text)
        try:
            subprocess.run([self.__vrx_path, text])
        except Exception as e:
            print(e)

    def set_path(self, path):
        if not os.path.exists(path):
            raise PathSetError("vrx.exeが見つかりません")
        self.__vrx_path = path



class PathSetError(Exception):
    pass
