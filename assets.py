from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sqlite3
from queue import Queue

font1 = QFont()
font1.setPointSize(22)
class ConnectionPool:
    def __init__(self, database, pool_size=5):
        self.database = database
        self.pool = Queue(pool_size)
        for _ in range(pool_size):
            self.pool.put(self.create_connection())

    def create_connection(self):
        return sqlite3.connect(self.database)

    def get_connection(self):
        return self.pool.get()

    def return_connection(self, conn):
        self.pool.put(conn)

def createComboBox(parent, name, geometry, font, item):
    combo_box = QComboBox(parent)
    combo_box.setObjectName(name)
    combo_box.setGeometry(geometry)
    combo_box.setFont(QFont("", font))

    for option in item:
        combo_box.addItem(option)
    return combo_box

def createTime(parent, name, geometry, font):
    time = QTimeEdit(parent)
    time.setObjectName(name)
    time.setGeometry(geometry)
    time.setFont(QFont("", font))
    return time

def createDate(parent, name, geometry, font):
    date = QDateEdit(parent)
    date.setObjectName(name)
    date.setGeometry(QRect(geometry))
    date.setFont(QFont("", font))
    return date

def createLabel(parent, name, geometry, text, font):
    label = QLabel(parent)
    label.setObjectName(name)
    label.setGeometry(geometry)
    label.setText(text)
    label.setFont(QFont(font))
    return label

def createLineInput(parent, name, geometry):
    line_input = QLineEdit(parent)
    line_input.setObjectName(name)
    line_input.setGeometry(geometry)
    return line_input

def createButton(parent, name, geometry, text, font_size, style_sheet):
    button = QPushButton(parent)
    button.setObjectName(name)
    button.setGeometry(geometry)
    button.setText(text)
    button.setFont(QFont("", font_size))
    button.setStyleSheet(style_sheet)
    return button
    
def setCurrentTime(time_input):
    current_time = QTime.currentTime()
    time = time_input
    time.setTime(current_time)

def setCurrentDate(date_input):
    current_date = QDate.currentDate()
    date = date_input
    date.setDate(current_date)