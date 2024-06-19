from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sqlite3
from queue import Queue

# DATABASE
connection = sqlite3.connect("database.db")
cursor = connection.cursor()


font1 = QFont()
font2 = QFont()
font3 = QFont() 
font4 = QFont()

font1.setPointSize(20)
font2.setPointSize(18)
font3.setPointSize(16)
font4.setPointSize(26)




def createDate(parent, name, geometry, font, style):
    current_date = QDate.currentDate()
    date = QDateEdit(parent)
    date.setObjectName(name)
    date.setGeometry(QRect(geometry))
    date.setFont(QFont(font))
    date.setCalendarPopup(True)
    date.setStyleSheet(style)
    date.setDate(current_date)
    return date
def createComboBox(parent, name, geometry, font, item, style):
    combo_box = QComboBox(parent)
    combo_box.setObjectName(name)
    combo_box.setGeometry(geometry)
    combo_box.setFont(QFont(font))
    combo_box.setStyleSheet(style)
    combo_box.setCurrentIndex(-1) 
    for option in item:
        combo_box.addItem(option)
    return combo_box

def createTime(parent, name, geometry, font, style):
    current_time = QTime.currentTime()
    time = QTimeEdit(parent)
    time.setObjectName(name)
    time.setGeometry(geometry)
    time.setFont(QFont(font))
    time.setTime(current_time)
    time.setStyleSheet(style)
    return time

def createLabel(parent, name, geometry, text, font, style):
    label = QLabel(parent)
    label.setObjectName(name)
    label.setGeometry(geometry)
    label.setText(text)
    label.setFont(QFont(font))
    label.setStyleSheet(style)
    return label

def createLineInput(parent, name, geometry, font, style):
    line_input = QLineEdit(parent)
    line_input.setObjectName(name)
    line_input.setGeometry(geometry)
    line_input.setFont(font)
    line_input.setStyleSheet(style)
    return line_input

def createButton(parent, name, geometry, text, font, style):
    button = QPushButton(parent)
    button.setObjectName(name)
    button.setGeometry(geometry)
    button.setText(text)
    button.setFont(QFont(font))
    button.setStyleSheet(style)
    return button

