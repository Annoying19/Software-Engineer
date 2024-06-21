from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sqlite3
import sys
import random


class AddAppointmentWindow(QWidget):
    def __init__(self, parent=None):
        super(AddAppointmentWindow, self).__init__(parent)
        self.setWindowTitle("Add Appointment")
        self.resize(800, 600)
        self.layout = QVBoxLayout(self)

        self.member_label = QLabel("Member Name:")
        self.layout.addWidget(self.member_label)

        self.member_search = QLineEdit()
        self.member_search.setPlaceholderText("Search for member")
        self.member_search.textChanged.connect(self.filter_members)
        self.layout.addWidget(self.member_search)

        self.member_list_widget = QListWidget()
        self.member_list_widget.itemClicked.connect(self.handle_member_selection)
        self.layout.addWidget(self.member_list_widget)

        self.employee_label = QLabel("Employee Name:")
        self.layout.addWidget(self.employee_label)

        self.employee_search = QLineEdit()
        self.employee_search.setPlaceholderText("Search for employee")
        self.employee_search.textChanged.connect(self.filter_employees)
        self.layout.addWidget(self.employee_search)

        self.employee_list_widget = QListWidget()
        self.employee_list_widget.itemClicked.connect(self.handle_employee_selection)
        self.layout.addWidget(self.employee_list_widget)

        self.date_label = QLabel("Select Date:")
        self.layout.addWidget(self.date_label)

        self.date_edit = QDateEdit(QDate.currentDate())
        self.date_edit.setCalendarPopup(True)
        self.layout.addWidget(self.date_edit)

        self.time_label = QLabel("Select Start and End Time:")
        self.layout.addWidget(self.time_label)

        time_layout = QHBoxLayout()

        self.start_time_edit = QTimeEdit(QTime.currentTime())
        self.start_time_edit.setDisplayFormat("HH:mm")
        time_layout.addWidget(self.start_time_edit)

        self.end_time_edit = QTimeEdit(QTime.currentTime().addSecs(3600))
        self.end_time_edit.setDisplayFormat("HH:mm")
        time_layout.addWidget(self.end_time_edit)

        self.layout.addLayout(time_layout)

        self.type_of_appointment_label = QLabel("Type of Appointment:")
        self.layout.addWidget(self.type_of_appointment_label)

        self.type_of_appointment_combo = QComboBox()
        self.type_of_appointment_combo.addItems(["Body Treatments", "Fitness Programs", "Face & Skin Programs"])
        self.type_of_appointment_combo.currentIndexChanged.connect(self.update_appointments)
        self.layout.addWidget(self.type_of_appointment_combo)

        self.name_of_appointment_label = QLabel("Name of Appointment:")
        self.layout.addWidget(self.name_of_appointment_label)

        self.name_of_appointment_combo = QComboBox()
        self.layout.addWidget(self.name_of_appointment_combo)

        self.update_appointments()

        self.add_button = QPushButton("Add")
        self.add_button.clicked.connect(self.add_appointment)
        self.layout.addWidget(self.add_button)

        self.scheduling_widget = parent
        self.load_member_names()
        self.load_employee_names()

        self.selected_member = None
        self.selected_employee = None

    def load_member_names(self):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT member_id, first_name, middle_name, last_name FROM members")
        self.members = cursor.fetchall()
        self.filter_members()
        conn.close()

    def load_employee_names(self):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT employee_id, first_name, last_name FROM employees")
        self.employees = cursor.fetchall()
        self.filter_employees()
        conn.close()

    def filter_members(self):
        search_text = self.member_search.text().lower()
        self.member_list_widget.clear()
        for member_id, first_name, middle_name, last_name in self.members:
            full_name = f"{first_name} {middle_name} {last_name}".strip()
            if search_text in full_name.lower():
                item = QListWidgetItem(f"{full_name} ({member_id})")
                item.setData(Qt.UserRole, (member_id, full_name))
                self.member_list_widget.addItem(item)

    def filter_employees(self):
        search_text = self.employee_search.text().lower()
        self.employee_list_widget.clear()
        for employee_id, first_name, last_name in self.employees:
            full_name = f"{first_name} {last_name}".strip()
            if search_text in full_name.lower():
                item = QListWidgetItem(f"{full_name} ({employee_id})")
                item.setData(Qt.UserRole, (employee_id, full_name))
                self.employee_list_widget.addItem(item)

    def update_appointments(self):
        appointment_type = self.type_of_appointment_combo.currentText()
        self.name_of_appointment_combo.clear()

        if appointment_type == "Body Treatments":
            self.name_of_appointment_combo.addItems([
                "Aromatherapy", "Biolift", "Body Former", "Bodytight FX",
                "Cellu-O", "Cellulite Cure Massage", "Chili Masque", "Coreshape",
                "emPULSE 360", "Endoslim", "G5", "Hot Masque", "Hot Stone Massage",
                "Le Shape", "Liposure", "Maximus", "Megaslim", "Pro Trim",
                "Quick Slim", "Reflexology", "Swedish Massage", "Thermasque",
                "Thermoslim", "Ultra Cellulite Treatment", "Ultraflex", "Ultraform",
                "Venus Freeze", "Vitastin"
            ])
        elif appointment_type == "Fitness Programs":
            self.name_of_appointment_combo.addItems([
                "Aerobics Class", "Biometric Intensive Inch Loss Program",
                "Biometrics Intensive Weight Loss Program", "Corefit", "Cykl Squad",
                "Passive Slimming Program", "Personal Training", "Power Stretching",
                "Powerbox", "Squad Core"
            ])
        elif appointment_type == "Face & Skin Programs":
            self.name_of_appointment_combo.addItems([
                "Aquafacial", "Back Cleansing Regimen", "Black Swan", "Body Scrub",
                "Botox", "Caviar Collagen Masque", "Cosmelan", "Cosmetic Filler",
                "Diamond Ultrapeel", "Electrocautery", "Exohair", "Exosomes",
                "Facial Skin System", "Fibrolift", "Glutathione", "Glycolic Acid Peel",
                "Goldfit", "iGlow", "Intralesional Injection", "IPL - Hair Removal",
                "IPL - Skin Rejuvenation", "iRejuve", "iReplenish", "iSlim",
                "Keloid Treatment", "Laser Acne Treatment", "Laser Hair Removal",
                "Laser White", "Liftera", "Madonna Facial", "Masque De Visage",
                "Meladerm", "Meso- Rejuvenation", "Mesolift", "Mesowhite", "Milk Bath",
                "Nasolift", "Neckfirme", "Nutracell-Face", "Oxygeneo", "PINS Therapy",
                "Profhilo", "PRP", "Pure White Collagen Masque", "Reboost", "Sclerotherapy",
                "Skin Whitening System", "Skinfirme", "TCA", "Thread Lift", "Tornado Lift",
                "Ultimate Body Whitening", "Ultralift", "V-Contour", "Vitaderm", "Volite"
            ])

    def handle_member_selection(self, item):
        self.selected_member = item.data(Qt.UserRole)
        self.member_search.setText(self.selected_member[1])

    def handle_employee_selection(self, item):
        self.selected_employee = item.data(Qt.UserRole)
        self.employee_search.setText(self.selected_employee[1])

    def add_appointment(self):
        if not self.selected_member or not self.selected_employee:
            QMessageBox.warning(self, "Selection Error", "Please select both a member and an employee.")
            return

        member_id, member_name = self.selected_member
        employee_id, employee_name = self.selected_employee
        appointment_type = self.type_of_appointment_combo.currentText()
        appointment_name = self.name_of_appointment_combo.currentText()
        appointment_date = self.date_edit.date().toString("yyyy-MM-dd")
        appointment_start_time = self.start_time_edit.time().toString("HH:mm")
        appointment_end_time = self.end_time_edit.time().toString("HH:mm")

        if not self.check_for_conflicts(appointment_date, appointment_start_time, appointment_end_time):
            schedule_id = "09" + str(random.randint(100000, 999999))

            self.scheduling_widget.cursor.execute('''
                INSERT INTO schedule (schedule_id, member_id, employee_id, appointment_type, appointment_name, appointment_date, appointment_start_time, appointment_end_time, status)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'ongoing')
            ''', (schedule_id, member_id, employee_id, appointment_type, appointment_name, appointment_date, appointment_start_time, appointment_end_time))
            self.scheduling_widget.conn.commit()

            self.scheduling_widget.load_appointments()
            self.scheduling_widget.update_calendar()

            self.close()
        else:
            QMessageBox.warning(self, "Conflict", "The selected time slot is already booked.")

    def check_for_conflicts(self, date, start_time, end_time):
        self.scheduling_widget.cursor.execute('''
            SELECT * FROM schedule
            WHERE appointment_date = ? AND 
                  ((appointment_start_time <= ? AND appointment_end_time > ?) OR
                   (appointment_start_time < ? AND appointment_end_time >= ?))
        ''', (date, start_time, start_time, end_time, end_time))

        return self.scheduling_widget.cursor.fetchone() is not None


class Scheduling(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Scheduling")
        self.resize(800, 600)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)
        self.calendar.clicked.connect(self.show_appointments)
        self.layout.addWidget(self.calendar)

        self.calendar.setStyleSheet("""
            QCalendarWidget QWidget {
                background-color: #FFFFFF; /* White background */
                alternate-background-color: #E0E0E0; /* Light gray alternate background */
            }
            QCalendarWidget QAbstractItemView:enabled {
                background-color: #FFFFFF; /* Background color for dates */
                color: #000000; /* Text color for dates */
                selection-background-color: #0000FF; /* Blue highlight for selected date */
                selection-color: #FFFFFF; /* White text color for selected date */
            }
            QCalendarWidget QAbstractItemView:disabled {
                color: #CCCCCC; /* Gray color for disabled dates */
            }
            QCalendarWidget QWidget#qt_calendar_navigationbar {
                background-color: #0000FF; /* Blue background */
                color: #FFFFFF; /* White text color */
            }
            QCalendarWidget QToolButton {
                background-color: #0000FF; /* Blue background for buttons */
                color: #FFFFFF; /* White text color for buttons */
                border: none; /* Remove border */
                margin: 5px; /* Add margin */
                padding: 5px; /* Add padding */
            }
            QCalendarWidget QToolButton::hover {
                background-color: #0000CC; /* Slightly darker blue for hover */
            }
            QCalendarWidget QAbstractItemView:enabled {
                selection-background-color: #0000FF; /* Blue highlight background */
                selection-color: #FFFFFF; /* White highlight text */
            }
        """)

        self.appointments_table = QTableWidget(0, 9)
        self.appointments_table.setHorizontalHeaderLabels(
            ["Schedule ID", "Member Name", "Employee Name", "Date", "Start Time", "End Time", "Type", "Name", "Status"])
        self.appointments_table.horizontalHeader().setStretchLastSection(True)
        self.appointments_table.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)  # Stretch table to occupy dead space
        self.layout.addWidget(self.appointments_table)

        self.button_layout = QHBoxLayout()
        self.layout.addLayout(self.button_layout)

        self.add_appointment_button = QPushButton("Add Appointment")
        self.add_appointment_button.clicked.connect(self.open_add_appointment_window)
        self.button_layout.addStretch()
        self.button_layout.addWidget(self.add_appointment_button)

        self.cancel_appointment_button = QPushButton("Cancel Appointment")
        self.cancel_appointment_button.clicked.connect(self.cancel_appointment)
        self.cancel_appointment_button.setEnabled(False)
        self.button_layout.addWidget(self.cancel_appointment_button)

        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()

        self.load_appointments()

        self.appointments_table.itemSelectionChanged.connect(self.toggle_cancel_button)

    def open_add_appointment_window(self):
        self.add_appointment_window = AddAppointmentWindow(self)
        self.add_appointment_window.show()

    def load_appointments(self):
        self.appointments_table.setRowCount(0)
        self.cursor.execute('''
            SELECT s.schedule_id, 
                   m.first_name || ' ' || m.middle_name || ' ' || m.last_name AS member_name, 
                   e.first_name || ' ' || e.last_name AS employee_name, 
                   s.appointment_date, 
                   s.appointment_start_time, 
                   s.appointment_end_time, 
                   s.appointment_type, 
                   s.appointment_name, 
                   s.status 
            FROM schedule s
            JOIN members m ON s.member_id = m.member_id
            JOIN employees e ON s.employee_id = e.employee_id
        ''')
        for row in self.cursor.fetchall():
            row_position = self.appointments_table.rowCount()
            self.appointments_table.insertRow(row_position)
            for column, data in enumerate(row):
                self.appointments_table.setItem(row_position, column, QTableWidgetItem(data))

    def update_calendar(self):
        self.cursor.execute('SELECT appointment_date FROM schedule')
        dates = set(row[0] for row in self.cursor.fetchall())
        fmt = QTextCharFormat()
        fmt.setBackground(QColor("lightblue"))
        self.calendar.setDateTextFormat(QDate(), QTextCharFormat())  # Clear previous highlights
        for date in dates:
            qdate = QDate.fromString(date, "yyyy-MM-dd")
            self.calendar.setDateTextFormat(qdate, fmt)

    def show_appointments(self, date):
        self.appointments_table.setRowCount(0)
        date_str = date.toString("yyyy-MM-dd")
        self.cursor.execute('''
            SELECT s.schedule_id, 
                   m.first_name || ' ' || m.middle_name || ' ' || m.last_name AS member_name, 
                   e.first_name || ' ' || e.last_name AS employee_name, 
                   s.appointment_date, 
                   s.appointment_start_time, 
                   s.appointment_end_time, 
                   s.appointment_type, 
                   s.appointment_name, 
                   s.status 
            FROM schedule s
            JOIN members m ON s.member_id = m.member_id
            JOIN employees e ON s.employee_id = e.employee_id
            WHERE s.appointment_date = ?
        ''', (date_str,))
        for row in self.cursor.fetchall():
            row_position = self.appointments_table.rowCount()
            self.appointments_table.insertRow(row_position)
            for column, data in enumerate(row):
                self.appointments_table.setItem(row_position, column, QTableWidgetItem(data))

    def toggle_cancel_button(self):
        if self.appointments_table.selectedItems():
            self.cancel_appointment_button.setEnabled(True)
        else:
            self.cancel_appointment_button.setEnabled(False)

    def cancel_appointment(self):
        selected_row = self.appointments_table.currentRow()
        schedule_id_item = self.appointments_table.item(selected_row, 0)
        if schedule_id_item:
            schedule_id = schedule_id_item.text()
            reply = QMessageBox.question(self, 'Cancel Appointment', 'Are you sure you want to cancel this appointment?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.cursor.execute('UPDATE schedule SET status = "cancelled" WHERE schedule_id = ?', (schedule_id,))
                self.conn.commit()
                self.load_appointments()
                self.update_calendar()

    def closeEvent(self, event):
        self.conn.close()
        super().closeEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Scheduling()
    window.show()
    sys.exit(app.exec_())
