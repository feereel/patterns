from tkinter import *
from tkinter.messagebox import askquestion
from structural.facade import *

class Extra(Toplevel):
    def __init__(self):
        super().__init__()
        self.title('Render window') 
        self.geometry('200x700')

        self.button = Button(self, text='Start rendering', command=self.start_rendering)
        self.button.pack(expand=True)

        self.mp3 = BooleanVar(value=False)
        self.wav = BooleanVar(value=True)
        self.data = BooleanVar(value=False)
        first = Checkbutton(self, text='mp3', variable=self.mp3)
        second = Checkbutton(self, text='wav', variable=self.wav)
        third = Checkbutton(self, text='data', variable=self.data)
        first.pack()
        second.pack() 
        third.pack()

    def start_rendering(self):
        renderTrack = Render()
        askquestion("...", message="Start rendering?")
        renderTrack.startRendering(self.mp3.get(), self.wav.get(), self.data.get())

 