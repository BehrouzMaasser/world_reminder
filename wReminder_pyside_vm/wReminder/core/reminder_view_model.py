import datetime as dt
import os
import platform as plt
from plyer import notification
from PySide6 import QtWidgets
import pytz
from threading import Timer

# from  import Ui_MainWindow
from reminder_model import ReminderModel


class Reminder:

    def __init__(self,
                 aware_datetime_obj_in_utc_timezone,
                 aware_datetime_obj_in_country_timezone,
                 reminder_id
                 ):
        self.reminder_id = reminder_id
        self.datetime_in_utc = aware_datetime_obj_in_utc_timezone
        self.country_datetime = aware_datetime_obj_in_country_timezone
        self.timer_obj = None


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.reminder_id = 0
        self.setupUi(self)
        self.model = ReminderModel()
        self.reminder_timezone_comboBox.addItems(list(pytz.all_timezones))
        self.display_reminderView.setModel(self.model)
        self.add_reminder_pushButton.pressed.connect(self.validate_inputs)
        self.cancel_reminder_pushButton.pressed.connect(self.cancel_reminder)

    def validate_inputs(self):
        # country datetime as a list of strings. format:
        # ['month/year/day', 'hour:minute']
        country_datetime = self.reminder_dateTimeEdit.text().split()
        naive_country_datetime = dt.datetime(
            int(country_datetime[0].split("/")[1]),
            int(country_datetime[0].split("/")[0]),
            int(country_datetime[0].split("/")[2]),
            int(country_datetime[1].split(":")[0]),
            int(country_datetime[1].split(":")[1])
        )
        aware_country_datetime = pytz.timezone(
            self.reminder_timezone_comboBox.currentText()
        ).localize(naive_country_datetime)

        # If Datetime is not in the past
        if (
                aware_country_datetime.astimezone(pytz.utc) >
                dt.datetime.now(pytz.utc)
        ):
            self.add_reminder(aware_country_datetime)
            display_message_event(
                2,
                "Success: Reminder is Set",
                self.add_reminder_lineEdit,
                'green'
            )
        else:
            display_message_event(
                2.5,
                "Wrong Datetime: Datetime is in the PAST",
                self.add_reminder_lineEdit,
                'red'
            )

    def add_reminder(self, aware_country_datetime):
        self.reminder_id += 1
        reminder = Reminder(
                aware_country_datetime.astimezone(pytz.utc),
                aware_country_datetime,
                self.reminder_id
            )
        self.model.reminders.append(
            reminder
        )
        time_difference = reminder.datetime_in_utc - \
                          dt.datetime.now(tz=pytz.utc)
        reminder.timer_obj = Timer(
            time_difference.seconds,
            self.run_notify, args=[reminder.reminder_id]
        )
        reminder.timer_obj.start()

        # Sort self.model.reminders based on the timezone
        self.model.reminders.sort(
            key=lambda rem: str(rem.country_datetime.tzinfo)
        )

        # Tell Model that model has changed to refresh
        self.model.layoutChanged.emit()

    def run_notify(self, reminder_id):
        notify(
            self.reminder_title_input.text(),
            self.reminder_message_input.text()
        )

        #  Remove the reminder from reminders when finish reminding
        for index, reminder in enumerate(self.model.reminders):
            if reminder_id == reminder.reminder_id:
                self.model.reminders.pop(index)

        # Sort self.model.reminders based on the timezone
        self.model.reminders.sort(
            key=lambda rem: str(rem.country_datetime.tzinfo)
        )

        # Tell Model that model has changed to refresh
        self.model.layoutChanged.emit()

    def cancel_reminder(self):
        # Selected reminder index from reminderViewList
        index = None
        try:
            index = self.display_reminderView.selectedIndexes()[0].row()
        except IndexError:
            display_message_event(
                2,
                "Error: Select a Reminder!",
                self.display_reminders_lineEdit,
                'red'
            )
            # Print a message
        if index in range(len(self.model.reminders)):
            self.model.reminders[index].timer_obj.cancel()
            self.model.reminders.pop(index)

            # Sort self.model.reminders based on the timezone
            self.model.reminders.sort(
                key=lambda rem: str(rem.country_datetime.tzinfo)
            )

            # Tell Model that model has changed to refresh
            self.model.layoutChanged.emit()

            display_message_event(
                2,
                "Reminder is Canceled",
                self.display_reminders_lineEdit,
                'green'
            )

            self.display_reminderView.clearSelection()
        elif index != None:
            display_message_event(
                2,
                "Error: Reminder Doesn't Exist!",
                self.display_reminders_lineEdit,
                'red'
            )


def display_message_event(wait_time_in_seconds, message, text_box, color):
    text_box.setText(message)
    text_box.setStyleSheet(
        f"font: 12pt \"Century Gothic\";\n"
        f"border-style: none;\ncolor: {color};"
    )
    Timer(
        wait_time_in_seconds,
        remove_message_event,
        args=[text_box]
    ).start()


def remove_message_event(text_box):
    text_box.setText("")


def notify(title, message):
    if plt.system() == 'Windows':
        notification.notify(
            title=title,
            message=message,
            app_icon='pythontutorial-1-150x150.ico',
            timeout=6
        )
    elif plt.system() == 'Darwin':
        os.system(f'''
        osascript -e 'display notification "{message}" with title "{title}" sound name "Submarine"'
                    ''')
    elif plt.system() == 'Linux':
        os.system(f'''
                            notify-send "{message}" "{title}"'
                    ''')
