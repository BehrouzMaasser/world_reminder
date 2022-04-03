import datetime as dt
import pytz
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror
from tkcalendar import Calendar


# Control Frame
class ControlFrame(ttk.LabelFrame):
    def __init__(self, container, controller):

        super().__init__(container)
        self['text'] = 'Options'
        self.container = container
        self.controller = controller
        self.current_frame_on = '1'

        # initialize frames
        self.frames = {
            '0': AddReminder(container, self.controller),
            '1': DisplayReminders(container, self.controller)
        }

        # Display Reminders Button
        display_reminders_menu_button = ttk.Button(
            self,
            text="Display Reminders",
            command=lambda: self.change_frame('1')
        )
        display_reminders_menu_button.grid(column=0, row=0, padx=5, pady=5)

        # Add Reminder Button
        add_reminder_menu_button = ttk.Button(
            self,
            text="Add Reminder",
            command=lambda: self.change_frame('0')
        )
        add_reminder_menu_button.grid(column=1, row=0, padx=5, pady=5)

        # Set The Control Frame
        self.grid(column=0, row=0, padx=5, pady=5, sticky='w')

    # Switch to Frames Add Reminder or Display Reminders
    def change_frame(self, frame_number=None):
        if frame_number == None:
            frame_number = self.current_frame_on
        if frame_number == '1':
            self.frames['1'] = DisplayReminders(
                self.container, self.controller
            )
        self.frames[frame_number].tkraise()
        self.current_frame_on = frame_number

    # Display Message Dialogs to User
    def display_message(self, message_type, message, title=''):
        if message_type == 'error':
            showerror(title, message)
        elif message_type == 'success':
            showinfo(title, message)


# Add Reminder Frame
class AddReminder(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)

        self.controller = controller

        # Options
        options = {'padx': 5, 'pady': 5}
        time_font = ('Times', 16)

        # Reminder notification title Label
        self.reminder_notification_title_label = ttk.Label(
            self, text='Reminder Title: '
        )
        self.reminder_notification_title_label.grid(
            column=0, row=1, sticky='w', **options
        )

        # Reminder notification title Entry
        self.reminder_notification_title = tk.StringVar()
        self.reminder_notification_title_entry = ttk.Entry(
            self,
            textvariable=self.reminder_notification_title
        )
        self.reminder_notification_title_entry.grid(
            column=1, columnspan=1, row=1, sticky='w', **options
        )
        self.reminder_notification_title_entry.focus()

        # Reminder notification message Label
        self.reminder_notification_message_label = ttk.Label(
            self, text='Reminder Message: '
        )
        self.reminder_notification_message_label.grid(
            column=2, row=1, sticky='w', **options
        )

        # Reminder notification message Entry
        self.reminder_notification_message = tk.StringVar()
        self.reminder_notification_message_entry = ttk.Entry(
            self,
            textvariable=self.reminder_notification_message
        )
        self.reminder_notification_message_entry.grid(
            column=3, columnspan=1, row=1, sticky='w', **options
        )

        # Date Label
        self.country_year_label = ttk.Label(self, text='Date: ')
        self.country_year_label.grid(column=0, row=2, sticky='w', **options)

        # Calendar
        self.cal = Calendar(
            self,
            selectmode='day',
            year=dt.datetime.now().year,
            month=dt.datetime.now().month,
            day=dt.datetime.now().day
        )
        self.cal.grid(
            column=1, row=2, columnspan=3, rowspan=4, sticky='nsew', **options
        )

        # Hour Label
        self.hour_label = ttk.Label(self, text='Hour : ')
        self.hour_label.grid(column=0, row=7, sticky='w', **options)

        # Hour Entry
        self.hours = tk.StringVar(value=tuple(range(24)))
        self.hours_entry = tk.Listbox(
            self,
            listvariable=self.hours,
            font=time_font, justify='center', exportselection=0, height=4
        )
        self.hours_entry.grid(column=1, row=7, sticky='w', **options)

        # Minute Label
        self.hour_label = ttk.Label(self, text='Minute : ')
        self.hour_label.grid(column=2, row=7, sticky='w', **options)

        # Minute Entry
        self.minutes = tk.StringVar(value=tuple(range(60)))
        self.minutes_entry = tk.Listbox(
            self,
            listvariable=self.minutes,
            font=time_font, justify='center', exportselection=0, height=4
        )
        self.minutes_entry.grid(column=3, row=7, sticky='w', **options)

        # Timezone Label
        self.timezone_label = ttk.Label(self, text='Select a Timezone: ')
        self.timezone_label.grid(column=0, row=8, sticky='w', **options)

        # Timezone ListBox
        self.timezones = tk.StringVar(value=tuple(pytz.all_timezones))
        self.timezone_listbox = tk.Listbox(
            self,
            height=10,
            listvariable=self.timezones,
            selectmode='browse',
        )
        self.timezone_listbox.grid(
            column=1, row=8, columnspan=1, sticky='nsew', **options
        )

        # Timezone ListBox Scrollbar
        self.scrollbar = ttk.Scrollbar(
            self,
            orient='vertical',
            command=self.timezone_listbox.yview
        )

        self.timezone_listbox['yscrollcommand'] = self.scrollbar.set
        self.scrollbar.grid(column=2, row=8, sticky='nsw', **options)

        # Add Reminder Button
        self.add_reminder_button = ttk.Button(
            self,
            text="Add Reminder",
            command=lambda: self.add_reminder()
        )
        self.add_reminder_button.grid(column=3, row=8, **options)

        # Set Add Reminder Frame
        self.grid(column=0, row=1, padx=5, pady=5, sticky="nsew")

    def add_reminder(self):
        timezone = self.get_validated_timezone()
        naive_datetime = self.get_datetime_from_inputs()
        if timezone == None:
            showerror(title="Invalid Time Zone", message="Select A Time Zone")
            return
        if naive_datetime == None:
            showerror(
                title="Invalid Date & Time", message="Select Date & Time"
            )
            return
        if self.controller.add_reminder_and_run_timer(
                timezone,
                naive_datetime,
                self.reminder_notification_title.get(),
                self.reminder_notification_message.get()
        ):
            showinfo(title="Success", message="Reminder's Set Successfully!")
        else:
            showerror(
                title="Invalid Date & Time",
                message="Date & Time Is In The Past"
            )

    def get_validated_timezone(self):
        try:
            return self.timezone_listbox.get(
                self.timezone_listbox.curselection()[0]
            )
        except IndexError:
            return None

    def get_datetime_from_inputs(self):
        date_str_list = self.cal.get_date().split('/')
        try:
            return dt.datetime(
                2000 + int(date_str_list[2]),
                int(date_str_list[0]),
                int(date_str_list[1]),
                self.hours_entry.curselection()[0],
                self.minutes_entry.curselection()[0]
            )
        except IndexError:
            return None


# Display Reminders Frame
class DisplayReminders(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)
        # field options
        options = {'padx': 5, 'pady': 5}

        # If there are Reminders
        if controller.reminders:
            for index, reminder in enumerate(controller.reminders):

                # Display Reminder Info
                reminder_label = ttk.Label(
                    self,
                    text=f"{index + 1}. {str(reminder.country_datetime())} in"
                         f" {reminder.country_datetime().tzinfo}"
                )
                reminder_label.grid(
                    column=0, row=index + 1, columnspan=3,
                    sticky='ew', **options
                )

                # A Cancel button for each Reminder
                reminder_cancel_button = ttk.Button(
                    self,
                    text="Cancel Reminder",
                    command=lambda: controller.cancel_reminder(
                        controller.reminders[index]
                    )
                )
                reminder_cancel_button.grid(
                    column=4, row=index + 1, **options
                )
        else:
            ttk.Label(self, text="No Reminders Available!").grid(
                column=2, row=2, sticky='ew', **options
            )

        # Set Display Reminders Frame
        self.grid(column=0, row=1, padx=5, pady=5, sticky="nsew")
