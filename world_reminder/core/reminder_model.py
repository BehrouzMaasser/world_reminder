import pytz


class Reminder:

    def __init__(
            self,
            aware_datetime_obj_in_utc_timezone,
            timezone,
            reminder_id
    ):
        self.reminder_id = reminder_id
        self.datetime_in_utc = aware_datetime_obj_in_utc_timezone
        self.timezone = timezone
        self.timer_obj = None

    def country_datetime(self):
        return self.datetime_in_utc.astimezone(pytz.timezone(self.timezone))
