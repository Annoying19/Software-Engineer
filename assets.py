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


# ===============================================
#          DYNAMIC REGISTRATION FUNCTION
# ===============================================

ENTITY_FIELDS = {
        # ATTENDANCE TABLE
        'Attendance': [
            'attendance_id', 
            'member_id', 
            'entry_time', 
            'exit_time', 
            'date',
        ],
        # MEMBERS TABLE
        'Members': [
            'member_id', 
            'first_name', 
            'middle_name', 
            'last_name', 
            'address',
            'gender',
            'birthdate',
            'phone_number',
            'membership_type',
            'membership_start_date',
            'membership_end_date',
            'photo',
            'signature'
            ],
        # EMPLOYEES TABLE
        'Employees': [
            'employee_id', 
            'first_name', 
            'middle_name', 
            'last_name', 
            'birthdate',
            'gender',
            'address',
            'phone',
            'hire_date',
            'position',
            'photo',
        ],
        # EQUIPMENTS TABLE
        'Equipments': [
            'equipment_id', 
            'equipment_name', 
            'equipment_serial_number', 
            'equipment_category', 
            'equipment_purchase_date',
            'equipment_warranty_expiry',
            'equipment_price',
            'equipment_manufacturer',
            'equipment_location',
            'equipment_status',
        ],
        # PRODUCTS TABLE
        'Products': [
            'product_id',
            'product_name',
            'quantity',
            'price',
            'product_expiry_date'
        ],
        # SCHEDULE TABLE
        'Schedule': [
            'schedule_id',
            'member_id',
            'employee_id',
            'appointment_type',
            'appointment_name',
            'appointment_date',
            'appointment_start_time',
            'appointment_end_time',
            'status'
        ],
        # USERS TABLE
        'Users': [
            'employee_id',
            'username',
            'password_hash',
            'role'
        ]
}

VALIDATION_RULES = {
    # ATTENDANCE TABLE
    'Attendance': {
        'attendance_id': ["required"], 
        'member_id': ["required"], 
        'entry_time': ["required"], 
        'exit_time': ["required"], 
        'date': ["required"],
    },
    # MEMBERS TABLE
    'Members': {
        'member_id': ["required"], 
        'first_name': ["required"], 
        'middle_name': ["required"], 
        'last_name': ["required"], 
        'address': ["required"],
        'gender': ["required"],
        'birthdate': ["required"],
        'phone_number': ["required"],
        'membership_type': ["required"],
        'membership_start_date': ["required"],
        'membership_end_date': ["required"],
        'photo': ["required"],
        'signature': ["required"]
    },
    # EMPLOYEES TABLE
    'Employees': {
        'employee_id': ["required"], 
        'first_name': ["required"], 
        'middle_name': ["required"], 
        'last_name': ["required"], 
        'birthdate': ["required"],
        'gender': ["required"],
        'address': ["required"],
        'phone': ["required"],
        'hire_date': ["required"],
        'position': ["required"],
        'photo': ["required"],
    },
    # EQUIPMENTS TABLE
    'Equipments': {
        'equipment_id': ["required"], 
        'equipment_name': ["required"], 
        'equipment_serial_number': ["required"], 
        'equipment_category': ["required"], 
        'equipment_purchase_date': ["required"],
        'equipment_warranty_expiry': ["required"],
        'equipment_price': ["required"],
        'equipment_manufacturer': ["required"],
        'equipment_location': ["required"],
        'equipment_status': ["required"],
    },
    # PRODUCTS TABLE
    'Products': {
        'product_id': ["required"],
        'product_name': ["required"],
        'quantity': ["required"],
        'price': ["required"],
        'product_expiry_date': ["required"]
    },
    # SCHEDULE TABLE
    'Schedule': {
        'schedule_id': ["required"],
        'member_id': ["required"],
        'employee_id': ["required"],
        'appointment_type': ["required"],
        'appointment_name': ["required"],
        'appointment_date': ["required"],
        'appointment_start_time': ["required"],
        'appointment_end_time': ["required"],
        'status': ["required"]
    },
    # USERS TABLE
    'Users': {
        'employee_id': ["required"],
        'username': ["required"],
        'password_hash': ["required"],
        'role': ["required"]
    }
}
def get_table_name(entity_type):
    return {
        'Attendance': 'Attendance', # ATTENDANCE TABLE
        'Members': 'Members', # MEMBERS TABLE
        'Employees': 'Employees', # EMPLOYEES TABLE
        'Equipments': 'Equipments', # EQUIPMENTS TABLE
        'Products': 'Products', # PRODUCTS TABLE
        'Schedule': 'Schedule', # SCHEDULE TABLE
        'Users': 'Users', # USERS TABLE
    }[entity_type]

def register(entity_type, **kwargs):
    if entity_type not in ENTITY_FIELDS:
        raise ValueError(f"Unsupported entity type: {entity_type}")
    
    required_fields = ENTITY_FIELDS[entity_type]
    
    # Validate required fields
    for field in required_fields:
        if field not in kwargs:
            raise ValueError(f"Missing required field: {field}")
    
    # Prepare the SQL insert query
    table_name = get_table_name(entity_type)
    columns = ', '.join(required_fields)
    placeholders = ', '.join(['?' for _ in required_fields])
    values = tuple(kwargs[field] for field in required_fields)

    query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

    try:
        with connection:
            connection.execute(query, values)
        print(f"Successfully registered {entity_type}: {values}")
    except sqlite3.IntegrityError as e:
        print(f"Error: {e}")



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
    combo_box.addItems(item)

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

