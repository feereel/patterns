from pathlib import Path


class MP3:
    def process(self):
        print("processing MP3")
        Path('filename.mp3').touch()

class WAV:
    def process(self):
        print("Processing WAV")
        Path('filename.wav').touch()

class Data:
    def process(self):
        print("Processing analysis")
        Path('filename.dbbbs').touch()

class Render:
    def __init__(self):
        self.mp3 = MP3()
        self.wav = WAV()
        self.data = Data()
    
    def startRendering(self,mp3 = False, wav=True, data=False):
        if mp3: self.mp3.process()
        if wav: self.wav.process()
        if data: self.data.process()