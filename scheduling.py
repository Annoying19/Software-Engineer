from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sqlite3
import sys
from assets import *

class Scheduling(QWidget):
    def __init__(self, parent=None):
        super(Scheduling, self).__init__(parent)
        self.setObjectName(u"Inventory")
        self.resize(950, 800)
        self.setStyleSheet(u"background-color: #FFFFFF;")

        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)  # Add margins here

        # Additional scheduling components
        self.layout = QVBoxLayout()
        self.verticalLayout.addLayout(self.layout)

        self.calendar = QCalendarWidget()
        self.calendar.clicked.connect(self.show_appointments)
        self.layout.addWidget(self.calendar)

        # Apply style sheet to change navigation bar and selection highlight colors
        self.calendar.setStyleSheet("""
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
                selection-color: #FFFFFF; /* White highlight text color */
            }
        """)

        self.date_label = QLabel("Select Date:")
        self.layout.addWidget(self.date_label)

        self.date_edit = QDateEdit(QDate.currentDate())
        self.date_edit.setCalendarPopup(True)
        self.layout.addWidget(self.date_edit)

        self.time_label = QLabel("Select Start and End Time:")
        self.layout.addWidget(self.time_label)

        time_layout = QHBoxLayout()

        self.start_time_edit = QTimeEdit(QTime.currentTime())
        self.start_time_edit.setDisplayFormat("HH:mm:ss")
        time_layout.addWidget(self.start_time_edit)

        self.end_time_edit = QTimeEdit(QTime.currentTime().addSecs(3600))
        self.end_time_edit.setDisplayFormat("HH:mm:ss")
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

        self.add_appointment_button = QPushButton("Add Appointment")
        self.add_appointment_button.clicked.connect(self.add_appointment)
        self.layout.addWidget(self.add_appointment_button)

        self.appointments_table = QTableWidget(0, 6)
        self.appointments_table.setHorizontalHeaderLabels(
            ["Schedule ID", "Member ID", "Type", "Name", "Date", "Start Time", "End Time"])
        self.layout.addWidget(self.appointments_table)

        self.load_appointments()

   

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

    def add_appointment(self):
        member_id = 1  # Example member ID, replace with actual member ID as needed
        appointment_type = self.type_of_appointment_combo.currentText()
        appointment_name = self.name_of_appointment_combo.currentText()
        appointment_date = self.date_edit.date().toString("yyyy-MM-dd")
        appointment_start_time = self.start_time_edit.time().toString("HH:mm:ss")
        appointment_end_time = self.end_time_edit.time().toString("HH:mm:ss")

        cursor.execute('''
            INSERT INTO Schedule (member_id, appointment_type, appointment_name, appointment_date, appointment_start_time, appointment_end_time)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (
        member_id, appointment_type, appointment_name, appointment_date, appointment_start_time, appointment_end_time))
        connection.commit()

        self.load_appointments()
        self.update_calendar()

    def load_appointments(self):
        self.appointments_table.setRowCount(0)
        cursor.execute(
            'SELECT schedule_id, member_id, appointment_type, appointment_name, appointment_date, appointment_start_time, appointment_end_time FROM Schedule')
        for row in cursor.fetchall():
            row_position = self.appointments_table.rowCount()
            self.appointments_table.insertRow(row_position)
            for column, data in enumerate(row):
                self.appointments_table.setItem(row_position, column, QTableWidgetItem(data))

    def update_calendar(self):
        cursor.execute('SELECT appointment_date FROM Schedule')
        dates = set(row[0] for row in cursor.fetchall())
        fmt = QTextCharFormat()
        fmt.setBackground(QColor("lightblue"))
        self.calendar.setDateTextFormat(QDate(), QTextCharFormat())  # Clear previous highlights
        for date in dates:
            qdate = QDate.fromString(date, "yyyy-MM-dd")
            self.calendar.setDateTextFormat(qdate, fmt)

    def show_appointments(self, date):
        self.appointments_table.setRowCount(0)
        date_str = date.toString("yyyy-MM-dd")
        cursor.execute(
            'SELECT schedule_id, member_id, appointment_type, appointment_name, appointment_date, appointment_start_time, appointment_end_time FROM Schedule WHERE appointment_date = ?',
            (date_str,))
        for row in cursor.fetchall():
            row_position = self.appointments_table.rowCount()
            self.appointments_table.insertRow(row_position)
            for column, data in enumerate(row):
                self.appointments_table.setItem(row_position, column, QTableWidgetItem(data))

    def closeEvent(self, event):
        self.conn.close()
        super().closeEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Scheduling()
    window.show()
    sys.exit(app.exec_())
