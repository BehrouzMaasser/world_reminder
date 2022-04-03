import datetime as dt
import pytz


# Reminder Model
class Reminder:

    def __init__(
            self,
            aware_datetime_obj_in_utc_timezone,
            aware_datetime_obj_in_country_timezone,
            reminder_id
    ):
        self.reminder_id = reminder_id
        self.datetime_in_utc = aware_datetime_obj_in_utc_timezone
        self.datetime_in_country = aware_datetime_obj_in_country_timezone
        self.timer_obj = None


# Function validates user-inputs
def validate_inputs(
        timezone_listbox, calendar, hours_entry, minutes_entry
):
    try:
        timezone_str = timezone_listbox.get(
            timezone_listbox.curselection()[0]
        )
    except IndexError:
        return {'error': "Select a Time Zone", 'data': None}
    try:
        date_str_list = calendar.get_date().split('/')
        naive_datetime = dt.datetime(
            2000 + int(date_str_list[2]),
            int(date_str_list[0]),
            int(date_str_list[1]),
            hours_entry.curselection()[0],
            minutes_entry.curselection()[0]
        )
        country_datetime = pytz.timezone(timezone_str).localize(
            naive_datetime
        )
        utc_datetime = country_datetime.astimezone(pytz.utc)
        if utc_datetime >= dt.datetime.now(tz=pytz.utc):
            return {'error': '', 'data': (utc_datetime, country_datetime)}
        else:
            return {'error': "Datetime is in the past!", 'data': None}
    except IndexError:
        return {'error': "Select Hour and Minute", 'data': None}
