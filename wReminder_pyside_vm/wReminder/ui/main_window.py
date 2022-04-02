# -*- coding: utf-8 -*-

##############################################################################
# Form generated from reading UI file 'mainwindow.ui'

# Created by: Qt User Interface Compiler version 6.2.4

# WARNING! All changes made in this file will be lost when recompiling UI file!
##############################################################################

from PySide6.QtCore import (
    QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt
)
from PySide6.QtGui import (
    QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform
)
from PySide6.QtWidgets import (
    QApplication, QComboBox, QDateTimeEdit, QLabel,
    QLineEdit, QListView, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QTabWidget, QWidget,
    QCalendarWidget, QTextEdit
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(410, 510)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(410, 510))
        MainWindow.setMaximumSize(QSize(410, 510))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(410, 510))
        self.menu_tabWidget = QTabWidget(self.centralwidget)
        self.menu_tabWidget.setObjectName(u"menu_tabWidget")
        self.menu_tabWidget.setGeometry(QRect(0, 0, 411, 631))
        self.display_reminder_tab = QWidget()
        self.display_reminder_tab.setObjectName(u"display_reminder_tab")
        self.label = QLabel(self.display_reminder_tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 30, 111, 41))
        self.label.setStyleSheet(u"font: 700 9pt \"Calibri\";")
        self.display_reminderView = QListView(self.display_reminder_tab)
        self.display_reminderView.setObjectName(u"display_reminderView")
        self.display_reminderView.setGeometry(QRect(40, 90, 321, 301))
        self.display_reminderView.setStyleSheet(
            u"font: 9pt \"Century Gothic\";\n"
            u"border-width : 1.2px;\nborder-color: lightblue;"
        )
        self.cancel_reminder_pushButton = QPushButton(
            self.display_reminder_tab
        )
        self.cancel_reminder_pushButton.setObjectName(
            u"cancel_reminder_pushButton"
        )
        self.cancel_reminder_pushButton.setGeometry(
            QRect(110, 410, 171, 41)
        )
        self.cancel_reminder_pushButton.setStyleSheet(
            u"font: 12pt \"Century Gothic\";\n"
            u"border-color: lightblue;\nborder-width : 1.2px;"
        )
        self.menu_tabWidget.addTab(self.display_reminder_tab, "")
        self.add_reminder_tab = QWidget()
        self.add_reminder_tab.setObjectName(u"add_reminder_tab")
        self.reminder_title_label = QLabel(self.add_reminder_tab)
        self.reminder_title_label.setObjectName(u"reminder_title_label")
        self.reminder_title_label.setGeometry(QRect(10, 50, 121, 20))
        self.reminder_title_label.setStyleSheet(
            u"font: 700 12pt \"Century Gothic\";"
        )
        self.reminder_title_input = QLineEdit(self.add_reminder_tab)
        self.reminder_title_input.setObjectName(u"reminder_title_input")
        self.reminder_title_input.setGeometry(QRect(160, 50, 221, 24))
        self.reminder_title_input.setStyleSheet(
            u"font: 11pt \"Century Gothic\";\n"
            u"border-color: lightblue;\nborder-width : 1.2px;"
        )
        self.reminder_message_label = QLabel(self.add_reminder_tab)
        self.reminder_message_label.setObjectName(u"reminder_message_label")
        self.reminder_message_label.setGeometry(QRect(0, 130, 161, 21))
        self.reminder_message_label.setStyleSheet(
            u"font: 11pt \"Century Gothic\";"
        )
        self.reminder_message_input = QLineEdit(self.add_reminder_tab)
        self.reminder_message_input.setObjectName(u"reminder_message_input")
        self.reminder_message_input.setGeometry(QRect(160, 130, 221, 24))
        self.reminder_message_input.setStyleSheet(
            u"font: 11pt \"Century Gothic\";\n"
            u"border-color: lightblue;\nborder-width : 1.2px;"
        )
        self.reminder_timezone_label = QLabel(self.add_reminder_tab)
        self.reminder_timezone_label.setObjectName(u"reminder_timezone_label")
        self.reminder_timezone_label.setGeometry(QRect(0, 210, 101, 16))
        self.reminder_timezone_label.setStyleSheet(
            u"font: 12pt \"Century Gothic\";"
        )
        self.reminder_timezone_comboBox = QComboBox(self.add_reminder_tab)
        self.reminder_timezone_comboBox.setObjectName(
            u"reminder_timezone_comboBox"
        )
        self.reminder_timezone_comboBox.setGeometry(QRect(120, 210, 261, 24))
        self.reminder_timezone_comboBox.setStyleSheet(
            u"font: 10pt \"Century Gothic\";"
        )
        self.reminder_datetime_label = QLabel(self.add_reminder_tab)
        self.reminder_datetime_label.setObjectName(u"reminder_datetime_label")
        self.reminder_datetime_label.setGeometry(QRect(10, 310, 121, 16))
        self.reminder_datetime_label.setStyleSheet(
            u"font: 12pt \"Century Gothic\";"
        )
        self.reminder_dateTimeEdit = QDateTimeEdit(self.add_reminder_tab)
        self.reminder_dateTimeEdit.setDate(QDate.currentDate())
        self.reminder_dateTimeEdit.setDisplayFormat("MM/yyyy/dd hh:mm")
        self.reminder_dateTimeEdit.setCalendarPopup(True)
        self.reminder_dateTimeEdit.setCalendarWidget(QCalendarWidget())
        self.reminder_dateTimeEdit.setObjectName(u"reminder_dateTimeEdit")
        self.reminder_dateTimeEdit.setGeometry(QRect(150, 310, 231, 25))
        self.reminder_dateTimeEdit.setStyleSheet(
            u"font: 11pt \"Century Gothic\";"
        )
        self.add_reminder_pushButton = QPushButton(self.add_reminder_tab)
        self.add_reminder_pushButton.setObjectName(u"add_reminder_pushButton")
        self.add_reminder_pushButton.setGeometry(QRect(130, 400, 141, 41))
        self.add_reminder_pushButton.setStyleSheet(
            u"font: 12pt \"Century Gothic\";\n"
            u"border-color: lightblue;\nborder-width : 1.2px;"
        )

        self.display_reminders_lineEdit = QLineEdit(self.display_reminder_tab)
        self.display_reminders_lineEdit.setObjectName(
            u"display_reminders_lineEdit"
        )
        self.display_reminders_lineEdit.setGeometry(QRect(140, 30, 221, 41))
        self.display_reminders_lineEdit.setStyleSheet(
            u"font: 10pt \"Century Gothic\";\nborder-style: none;"
        )

        self.add_reminder_lineEdit = QLineEdit(self.add_reminder_tab)
        self.add_reminder_lineEdit.setObjectName(u"add_reminder_lineEdit")
        self.add_reminder_lineEdit.setGeometry(QRect(0, 350, 401, 41))
        self.add_reminder_lineEdit.setStyleSheet(
            u"font: 11pt \"Century Gothic\";\nborder-style: none;"
        )
        self.add_reminder_lineEdit.setReadOnly(True)
        self.display_reminders_lineEdit.setReadOnly(True)

        self.menu_tabWidget.addTab(self.add_reminder_tab, "")
        self.reminder_title_label.raise_()
        self.reminder_title_input.raise_()
        self.reminder_message_label.raise_()
        self.reminder_message_input.raise_()
        self.reminder_timezone_label.raise_()
        self.reminder_timezone_comboBox.raise_()
        self.reminder_datetime_label.raise_()
        self.reminder_dateTimeEdit.raise_()
        self.add_reminder_lineEdit.raise_()
        self.display_reminders_lineEdit.raise_()
        self.add_reminder_pushButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        self.menu_tabWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None
        ))
        self.label.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p align=\"center\"><span style=\" "
            u"font-size:16pt;\">Reminders :</span></p></body></html>",
            None
        ))
        self.cancel_reminder_pushButton.setText(QCoreApplication.translate(
            "MainWindow", u"Cancel Reminder", None
        ))
        self.menu_tabWidget.setTabText(
            self.menu_tabWidget.indexOf(self.display_reminder_tab),
            QCoreApplication.translate(
                "MainWindow", u"Display Reminders", None
            )
        )
        self.add_reminder_pushButton.setText(QCoreApplication.translate(
            "MainWindow", u"Add Reminder", None
        ))
        self.reminder_title_label.setText(
            QCoreApplication.translate(
                "MainWindow",
                u"<html><head/><body><p><span style=\" font-weight:400;\">"
                u"Reminder Title</span></p></body></html>", None
            )
        )
        self.reminder_datetime_label.setText(
            QCoreApplication.translate("MainWindow", u"Date & Time", None)
        )
        self.reminder_timezone_label.setText(
            QCoreApplication.translate(
                "MainWindow",
                u"<html><head/><body><p align=\"center\">"
                u"Time Zone</p></body></html>",
                None
            )
        )
        self.reminder_message_label.setText(
            QCoreApplication.translate(
                "MainWindow",
                u"<html><head/><body><p align=\"center\">"
                u"Reminder Message</p></body></html>",
                None
            )
        )
        self.menu_tabWidget.setTabText(
            self.menu_tabWidget.indexOf(self.add_reminder_tab),
            QCoreApplication.translate("MainWindow", u"Add Reminder", None)
        )
