from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sqlite3
from queue import Queue
import re
from datetime import date
from PyQt5.QtWidgets import QMessageBox
from datetime import datetime
from functools import partial
import hashlib
# DATABASE
connection = sqlite3.connect("database.db")
cursor = connection.cursor()


font1 = QFont()
font2 = QFont()
font3 = QFont() 
font4 = QFont()
font5 = QFont()
font6 = QFont()

font1.setPointSize(20)
font2.setPointSize(18)
font3.setPointSize(16)
font4.setPointSize(26)
font5.setPointSize(8)
font6.setPointSize(12)




# ===============================================
#          DYNAMIC REGISTRATION FUNCTION
# ===============================================

def validate_input(field_name, value, rules):
    """Validate a field against given rules."""
    for rule in rules:
        if rule == "required" and not value:
            return False, f"{field_name} is required."
        if rule == "numeric" and not str(value).isdigit():
            return False, f"{field_name} must be numeric."
        if rule == "email":
            pattern = r"[^@]+@[^@]+\.[^@]+"
            if not re.match(pattern, value):
                return False, f"{field_name} must be a valid email."
        if rule == "date" and not isinstance(value, date):
            return False, f"{field_name} must be a valid date."
        if rule == "phone":
            pattern = r"^\+?\d{10,15}$"
            if not re.match(pattern, value):
                return False, f"{field_name} must be a valid phone number."
        # Add more rules as needed
    return True, ""
def validate_all_inputs(entity_type, inputs):
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
            'phone': ["required"],
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
            'password': ["required"],
            'role': ["required"]
        }
    }

    rules = VALIDATION_RULES.get(entity_type, {})
    for field, value in inputs.items():
        field_rules = rules.get(field, [])
        valid, message = validate_input(field, value, field_rules)
        if not valid:
            QMessageBox.warning(None, "Validation Error", message)
            return False
    return True

def get_table_name(entity_type):
    return {
        'Attendance': 'Attendance', # ATTENDANCE TABLE
        'Member': 'Members', # MEMBERS TABLE
        'Employee': 'Employees', # EMPLOYEES TABLE
        'Equipment': 'Equipments', # EQUIPMENTS TABLE
        'Product': 'Products', # PRODUCTS TABLE
        'Schedule': 'Schedule', # SCHEDULE TABLE
        'User': 'Users', # USERS TABLE
    }[entity_type]


def register_entity(entity_type, inputs):
    """Generic registration function."""
    if validate_all_inputs(entity_type, inputs):
        if entity_type == "Attendance":
            cursor.execute(
                '''
                SELECT attendance_id, entry_time, exit_time 
                FROM Attendance 
                WHERE member_id = ? AND date = ? 
                ORDER BY attendance_id DESC LIMIT 1
                ''', 
                (inputs["member_id"], inputs["date"].toString('yyyy-MM-dd'))
            )
            print(inputs["member_id"], inputs["date"], inputs["attendance"])
            last_record = cursor.fetchone()

            if inputs["attendance"] == "Entry":
                if last_record and not last_record[2]:  # If there's a record with entry_time but no exit_time
                    print("Error: Member already has an entry record with no exit recorded.")
                else:
                    cursor.execute("""
                        INSERT INTO Attendance (member_id, entry_time, date) 
                        VALUES (?, ?, ?)
                        """, (inputs["member_id"], inputs["time"].toString(), inputs["date"].toString("yyyy-MM-dd")))
                    QMessageBox.information(None, "Success", "Entry registered successfully!")
            else:
                if last_record and not last_record[2]:  # If there's a record with entry_time but no exit_time
                    cursor.execute("""  
                        UPDATE Attendance 
                        SET exit_time = ? 
                        WHERE attendance_id = ?
                        """, (inputs["time"].toString(), last_record[0]))
                    QMessageBox.information(None, "Success", "Exit registered successfully!")
                else:
                    print("Error: No entry record found or already exited.")

            connection.commit()

        elif entity_type == "Members":
            cursor.execute(
                '''
                INSERT INTO Members 
                (member_id, first_name, middle_name, last_name, address, phone_number, birthdate, membership_type,
                gender, membership_start_date, membership_end_date, photo, signature) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''',
                (
                    inputs["member_id"],
                    inputs["first_name"],
                    inputs["middle_name"],
                    inputs["last_name"],
                    inputs["address"],
                    inputs["phone"],
                    inputs["birthdate"].toString("yyyy-MM-dd"),
                    inputs["membership_type"],
                    inputs["gender"],
                    inputs["start_date"].toString("yyyy-MM-dd"),
                    inputs["end_date"].toString("yyyy-MM-dd"),
                    inputs["image"],
                    inputs["signature"],
                )
            )
            connection.commit()
            QMessageBox.information(None, "Success", "Member registered successfully!")
        
        elif entity_type == "Employees":
            cursor.execute(
                '''
                INSERT INTO Employees 
                (employee_id, first_name, middle_name, last_name, birthdate, gender, address, phone,
                hire_date, position, photo) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''',
                (
                    inputs["employee_id"],
                    inputs["first_name"],
                    inputs["middle_name"],  # Handle cases where middle_name might be missing
                    inputs["last_name"],
                    inputs["birthdate"].toString("yyyy-MM-dd"),  # Format date correctly
                    inputs["gender"],
                    inputs["address"],
                    inputs["phone"],
                    inputs["hire_date"].toString("yyyy-MM-dd"),  # Format date correctly
                    inputs["position"],
                    inputs["photo"],

                )
            )
        elif entity_type == "Users":
            cursor.execute
            if inputs["password"] == inputs["retry_password"]:
                password_bytes = inputs["password"].encode()
                hashed_password = hashlib.sha256(password_bytes).hexdigest()
                cursor.execute(
                    """
                    INSERT INTO Users
                    (employee_id, username, password_hash, role) VALUES
                    (?, ?, ?, ?)
                    """,
                    (
                        inputs["employee_id"],
                        inputs["username"],
                        hashed_password,
                        inputs["role"]
                    )
                )

                connection.commit()

                QMessageBox.information(None, "Registered", "Account Sucessfully Registered")
            else: 
                QMessageBox.warning(None, "Error", "Password Unidentical")





def update_entity(entity_type, inputs):
    """Generic registration function."""
    if validate_all_inputs(entity_type, inputs):
        if entity_type == "Members":
            cursor.execute(
                '''
                UPDATE Members
                SET first_name = ?, middle_name = ?, last_name = ?,address = ?,   phone_number = ?, birthdate = ?, membership_type = ?, 
                gender = ?,  membership_start_date = ? , membership_end_date = ?, photo = ?, signature = ?
                ''',
         
                (
                    inputs["first_name"],
                    inputs["middle_name"],
                    inputs["last_name"],
                    inputs["address"],
                    inputs["phone"],
                    inputs["birthdate"].toString("yyyy-MM-dd"),
                    inputs["membership_type"],
                    inputs["gender"],
                    inputs["start_date"].toString("yyyy-MM-dd"),
                    inputs["end_date"].toString("yyyy-MM-dd"),
                    inputs["image"],
                    inputs["signature"],
                )
            )
            connection.commit()
            QMessageBox.information(None, "Success", "Member Information Update")

        elif entity_type == "Users":
            cursor.execute(
                '''
                UPDATE Users
                SET username = ?, password_hash = ?, role = ?
                ''',
                (
                    inputs["username"],
                    inputs["password"],
                    inputs["role"]
                )
            )
            connection.commit()
            QMessageBox.information(None, "Success", "User Information Update")
    else:
        QMessageBox.warning(None, "Validation Error", "Please correct the highlighted errors.")



            
# CONVERTING ALL THE QLABELS IN TO QEDITS
def edit_entity_button(entity_type, inputs):
    for field, value in inputs.items():
        element = inputs.get(f"edit_member_{field}_input")
        if element:
            if isinstance(value, QPixmap):
                element.setPixmap(value)
            elif field in ["birthdate", "start_date", "end_date"]:
                date_value = datetime.strptime(value, '%Y-%m-%d')
                element.setDate(date_value)
            else:
                element.setText(str(value))

def disable_past_date(label):
    label.setMinimumDate(QDate.currentDate())
        # Disable selection of past dates
    label.setDateRange(QDate.currentDate(), QDate(2099, 12, 31))

    
def generate_id(entity_type, label):

    current_time = datetime.now()
    formatted_time = current_time.strftime('%m%d%y')
    if entity_type == "Members":
        query = f"SELECT COUNT(*) FROM {entity_type}"
        prefix = "MEM"
    elif entity_type == "Employees":
        query = f"SELECT COUNT(*) FROM {entity_type}"
        prefix = "EMP"
    elif entity_type == "Equipments":
        query = f"SELECT COUNT(*) FROM {entity_type}"
        prefix = "EMP"
    elif entity_type == "Products":
        query = f"SELECT COUNT(*) FROM {entity_type}"
        prefix = "EMP"

    cursor.execute(query)
    count = cursor.fetchone()[0] + 1
    generated_id = f"{prefix}-{formatted_time}-{count:04}"

    label.setText(generated_id)




# UPDATING THE TABLE WIDGET OF THE ENTITY

def clear_inputs(page):
    for widget in page.findChildren(QWidget):
        if isinstance(widget, QLineEdit):
            widget.clear()
        elif isinstance(widget, QComboBox):
            widget.setCurrentIndex(-1)  # Reset the selection
        elif isinstance(widget, QDateEdit):
            current_date = QDate.currentDate()
            widget.setDate(current_date)
            widget.clear()
        elif isinstance(widget, QTimeEdit):
            current_time = QTime.currentTime()
            widget.setTime(current_time)
            widget.clear()
        elif isinstance(widget, QLabel):
            if widget.objectName() in ["image_label", "signature_label", "output"]:
                widget.clear()  # Clears the label content
                widget.setPixmap(QPixmap())  # Clears any image or signature

def insert_image(image):
    # Open a file dialog to select an image file
        file_dialog = QFileDialog()
        file_name, _ = file_dialog.getOpenFileName(
            None, "Select Image", "", "Image Files (*.png *.jpg *.bmp *.gif)"
        )

        if file_name:
            # Load the image and set it to the label
            pixmap = QPixmap(file_name)
            image.setPixmap(pixmap.scaled(image.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

def pixmap_to_bytes(pixmap):
    byte_array = QByteArray()
    buffer = QBuffer(byte_array)
    buffer.open(QBuffer.WriteOnly)
    pixmap.save(buffer, "PNG")
    return byte_array.data()


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

def createLabel(parent, name, geometry, text, font, style = ""):
    label = QLabel(parent)
    label.setObjectName(name)
    label.setGeometry(geometry)
    label.setText(text)
    label.setFont(QFont(font))
    label.setStyleSheet(style)
    return label

def createLineInput(parent, name, geometry, font, style, placeholder = ""):
    line_input = QLineEdit(parent)
    line_input.setObjectName(name)
    line_input.setGeometry(geometry)
    line_input.setFont(font)
    line_input.setStyleSheet(style)
    line_input.setPlaceholderText(placeholder)
    return line_input

def createButton(parent, name, geometry, text, font, style):
    button = QPushButton(parent)
    button.setObjectName(name)
    button.setGeometry(geometry)
    button.setText(text)
    button.setFont(QFont(font))
    button.setStyleSheet(style)
    return button

