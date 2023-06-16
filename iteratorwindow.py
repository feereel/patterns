from tkinter import *
from behavioral.iterator import *

class Extra(Toplevel):
    def __init__(self):
        super().__init__()
        self.title('Render window') 
        self.geometry('200x700')
        self.samples = Samples(['hat', 'kick', 'kicker', '808'])

        self.entry = Entry(self)
        self.entry.pack()
        self.entry.bind('<KeyRelease>', self.parse)

        self.listbox = Listbox(self)
        self.listbox.pack()

        self.baseparse()

    def parse(self, e):
        char = e.widget.get()
        if not e:
            self.baseparse()
            return

        data = []

        for item in self.samples:
            if char in item:
                data.append(item)
            
        self.listbox.delete(0, 'end')
        for item in data:
            self.listbox.insert(0, item)

    def baseparse(self):
        self.listbox.delete(0, 'end')
        for item in self.samples:
            self.listbox.insert(0, item)