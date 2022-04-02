import tkinter as tk

from wReminder_tkinter_mvc.core.view import ControlFrame
from wReminder_tkinter_mvc.core.controller import Controller


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Global Reminder')
        self.geometry('750x600')
        self.resizable(False, False)


if __name__ == "__main__":
    reminder_app = App()
    controller = Controller()
    controller.view = ControlFrame(reminder_app, controller)
    reminder_app.mainloop()
