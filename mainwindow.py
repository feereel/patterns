from tkinter import *
from creational import Singleton
import eqswindow, footerwindow, convertwindow, decoratorwindow
import renderwidnow, iteratorwindow, groupwindow, strategy

class Window(Tk, Singleton):
    def init(self):
        super().__init__()

        self.button = Button(self, text = 'open footer', command=self.create_footer_window)
        self.button.pack(expand=True)

        self.button = Button(self, text = 'open eqs window', command=self.create_window_eqs)
        self.button.pack(expand=True)

        self.button = Button(self, text = 'open converter', command=self.create_converter_window)
        self.button.pack(expand=True)

        self.button = Button(self, text = 'decorator', command=self.create_decorator_window)
        self.button.pack(expand=True)

        self.button = Button(self, text = 'export', command=self.create_export_window)
        self.button.pack(expand=True)

        self.button = Button(self, text = 'iterator', command=self.create_iterator_window)
        self.button.pack(expand=True)

        self.button = Button(self, text = 'observer', command=self.create_observer_window)
        self.button.pack(expand=True)

        self.button = Button(self, text = 'strategy', command=self.create_strategy_window)
        self.button.pack(expand=True)

    def create_strategy_window(self):
        global extraWindow
        extraWindow = strategy.Extra()

    def create_observer_window(self):
        global extraWindow
        extraWindow = groupwindow.Extra()

    def create_iterator_window(self):
        global extraWindow
        extraWindow = iteratorwindow.Extra()

    def create_export_window(self):
        global extraWindow
        extraWindow = renderwidnow.Extra()

    def create_decorator_window(self):
        global extraWindow
        extraWindow = decoratorwindow.Extra()

    def create_converter_window(self):
        global extraWindow
        extraWindow = convertwindow.Extra()

    def create_footer_window(self):
        global extraWindow
        extraWindow = footerwindow.Extra()

    def create_window_eqs(self):
        global extraWindow
        extraWindow = eqswindow.Extra()

    def __init__(self):
        pass