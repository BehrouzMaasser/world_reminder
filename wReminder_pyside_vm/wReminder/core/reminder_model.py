from PySide6.QtCore import Qt, QAbstractListModel


class ReminderModel(QAbstractListModel):
    def __init__(self, reminders=None):
        super().__init__()
        self.reminders = reminders or []

    def data(self, index, role):
        if role == Qt.DisplayRole:
            reminder_obj = self.reminders[index.row()]
            return str(reminder_obj.country_datetime.tzinfo) + \
                   " On " + \
                   reminder_obj.country_datetime.strftime('%Y/%b/%d At %H:%M')

    def rowCount(self, index):
        return len(self.reminders)
