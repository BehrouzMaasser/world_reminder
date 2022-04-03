import os
import datetime as dt
import pytz
import platform as plt
from plyer import notification

from threading import Timer

from core.reminder_model import Reminder, validate_inputs


# Controller
class Controller:
    def __init__(self):
        self.view = None
        self.reminders = []
        self.reminder_id_counter = 0

    def add_reminder(
            self, timezone_listbox, calendar, hours_entry, minutes_entry
    ):
        # Get mo
        result = validate_inputs(
            timezone_listbox, calendar, hours_entry, minutes_entry
        )
        if result['data']:
            self.reminder_id_counter += 1
            reminder = Reminder(
                result['data'][0], result['data'][1], self.reminder_id_counter
            )
            self.reminders.append(reminder)

            # Sort the reminders based on reminder time zone
            self.reminders.sort(
                key=lambda rem: str(rem.datetime_in_country.tzinfo)
            )
            self.run_reminder(reminder)
            self.view.display_message(
                message_type='success', message="Reminder's Set Successfully!"
            )
        else:
            self.view.display_message(
                message_type='error', message=result['error']
            )

    def run_reminder(self, reminder):
        time_difference = \
            reminder.datetime_in_utc - dt.datetime.now(tz=pytz.utc)
        reminder.timer_obj = Timer(
            time_difference.seconds, self.run_notify, args=[
                self.view.frames['0'].reminder_notification_title.get(),
                self.view.frames['0'].reminder_notification_message.get(),
                reminder.reminder_id
            ])
        reminder.timer_obj.start()

    def run_notify(self, title, message, reminder_id):
        notify(title, message)
        self.cancel_reminder(reminder_id)

    def cancel_reminder(self, reminder_id):
        for index, reminder in enumerate(self.reminders):
            if reminder.reminder_id == reminder_id:
                reminder.timer_obj.cancel()
                self.reminders.pop(index)

                # Sort the reminders based on reminder time zone
                self.reminders.sort(
                    key=lambda rem: str(rem.datetime_in_country.tzinfo)
                )
                self.view.change_frame(self.view.current_frame_on)
                break


def notify(title, message):
    if plt.system() == 'Windows':
        notification.notify(
            title=title,
            message=message,
            app_icon='app_icon.ico',
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
