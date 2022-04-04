import datetime as dt
import pytz

from threading import Timer

from core.notification import notify
from core.reminder_model import Reminder


class Controller:
    def __init__(self):
        self.view = None
        self.reminders = []
        self.reminder_id_counter = 0

    def add_reminder_and_run_timer(
            self, timezone, naive_datetime, reminder_title, reminder_message
    ):
        country_datetime = pytz.timezone(timezone).localize(naive_datetime)
        utc_datetime = country_datetime.astimezone(pytz.utc)
        if self.datetime_is_in_future(utc_datetime):
            self.reminder_id_counter += 1
            self.reminders.append(Reminder(
                utc_datetime, timezone, self.reminder_id_counter
            ))
            self.run_reminder_timer(
                self.reminders[-1], reminder_title, reminder_message
            )
            self.sort_reminders()
            return True
        else:
            return False

    def run_reminder_timer(self, reminder, reminder_title, reminder_message):
        time_difference = \
            reminder.datetime_in_utc - dt.datetime.now(tz=pytz.utc)
        reminder.timer_obj = Timer(
            time_difference.seconds, self.run_notify, args=[
                reminder_title,
                reminder_message,
                reminder.reminder_id
            ])
        reminder.timer_obj.start()

    def run_notify(self, title, message, reminder_id):
        notify(title, message)
        self.remove_reminder_from_list(reminder_id)
        self.sort_reminders()

    def remove_reminder_from_list(self, reminder_id):
        for index, reminder in enumerate(self.reminders):
            if reminder.reminder_id == reminder_id:
                self.reminders.pop(index)
                self.view.change_frame()
                break

    def cancel_reminder(self, reminder):
        reminder.timer_obj.cancel()
        self.remove_reminder_from_list(reminder.reminder_id)
        self.sort_reminders()

    def sort_reminders(self):
        """ Sort the reminders based on reminder time zone """
        self.reminders.sort(
            key=lambda reminder: str(reminder.timezone)
        )

    def datetime_is_in_future(self, utc_datetime):
        return utc_datetime >= dt.datetime.now(tz=pytz.utc)
