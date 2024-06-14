from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from assets import *
import sqlite3
import re
from datetime import datetime
class Registration(QWidget):
    def __init__(self, parent=None):
        super(Registration, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Connect buttons to page switching methods
        self.ui.member_button.clicked.connect(self.showMemberPage)
        self.ui.attendance_button.clicked.connect(self.showAttendancePage)
        self.ui.back_button.clicked.connect(self.showMainPage)
        self.ui.attendance_back_button.clicked.connect(self.showMainPage)
        self.ui.register_member_button.clicked.connect(self.handle_register)
        self.ui.insert_image_button.clicked.connect(lambda: self.insert_image(self.ui.image_label))
        self.ui.insert_signature_button.clicked.connect(lambda: self.insert_image(self.ui.signature_label))
        self.ui.search_button.clicked.connect(self.search_member)
        self.ui.attendance_clear_button.clicked.connect(self.clear_text)

    def showMainPage(self): 
        self.ui.stackedWidget.setCurrentIndex(0)

    def showMemberPage(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def showAttendancePage(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def handle_register(self):
        try:
            # Convert membership_id to integer
            membership_id = int(self.ui.membership_id_input.text().strip())
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Invalid membership ID. Please enter a valid number.")
            return

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        try:
            # Retrieve and validate form inputs
            first_name = self.ui.first_name_input.text().strip()
            middle_name = self.ui.middle_name_input.text().strip()
            last_name = self.ui.last_name_input.text().strip()
            gender = self.ui.gender_combo_box.currentText()
            birth_date = self.ui.birthday_date.date().toString('yyyy-MM-dd')
            address = self.ui.address_input.text().strip()
            phone_number = self.ui.phone_number_input.text().strip()
            membership_type = self.ui.membership_combo_box.currentText()
            start_date = self.ui.start_date_edit.date().toString('yyyy-MM-dd')
            end_date = self.ui.end_date_edit.date().toString('yyyy-MM-dd')
            member_image = self.ui.image_label
            signature_image = self.ui.signature_label
            
            def qpixmap_to_bytes(pixmap):
                byte_array = QByteArray()
                buffer = QBuffer(byte_array)
                buffer.open(QBuffer.WriteOnly)
                pixmap.save(buffer, "PNG")
                return byte_array.data()

            # Get QPixmap from QLabel
            member_pixmap = member_image.pixmap()
            signature_pixmap = signature_image.pixmap()

            member_image_bytes = None
            signature_image_bytes = None
            if member_pixmap:
                member_image_bytes = qpixmap_to_bytes(member_pixmap)
            if signature_pixmap:
                signature_image_bytes = qpixmap_to_bytes(signature_pixmap)

            cursor.execute('SELECT COUNT(*) FROM Members WHERE member_id=?', (membership_id,))
            result = cursor.fetchone()

            if result[0] == 0:
                # Insert new member record
                cursor.execute('''
                    INSERT INTO Members (
                        member_id, first_name, middle_name, last_name, gender, birthdate, address, phone_number, 
                        membership_type, membership_start_date, membership_end_date, photo, signature
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (membership_id, first_name, middle_name, last_name, gender, birth_date, address, phone_number, 
                    membership_type, start_date, end_date, sqlite3.Binary(member_image_bytes), sqlite3.Binary(signature_image_bytes)))
                conn.commit()

                QMessageBox.information(self, "Success", "Registered successfully.")
            else:
                QMessageBox.warning(self, "Duplicate Error", "Member ID already exists.")

        except sqlite3.IntegrityError as e:
            print(f"Database error: {e}")
            QMessageBox.critical(self, "Database Error", "An error occurred while registering. Please try again.")
        finally:
            cursor.close()
            conn.close()

    def pixmap_to_bytes(self, pixmap):
        """Convert QPixmap to bytes."""
        import io
        buffer = io.BytesIO()
        pixmap.save(buffer, format='JPG')
        return buffer.getvalue()

    def search_member(self):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        member_input = self.ui.search_member_input.text().strip()

        # Check if member_input is empty
        if not member_input:
            print("Please enter a member's name.")
            conn.close()
            return

        # Split the full name into first name and last name
        name_parts = member_input.rsplit(' ', 1)
        
        if len(name_parts) < 2:
            print("Please enter both first name and last name.")
            conn.close()
            return
        
        first_name = name_parts[0].strip()
        last_name = name_parts[1].strip()

        # Debug: Print the first and last name
        print(f"Searching for: first_name = '{first_name}', last_name = '{last_name}'")

        # Execute the SQL query with placeholders for the first name and last name
        cursor.execute('''
            SELECT member_id, membership_type, membership_start_date, membership_end_date, photo
            FROM Members
            WHERE first_name = ? AND last_name = ?
        ''', (first_name, last_name))

        # Fetch the results
        results = cursor.fetchone()

        # Check if the results are found
        if results:
            membership_id, membership_type, start_date, end_date, photo= results
            print("Membership ID:", membership_id)
            print("Membership Type:", membership_type)
            print("Start Date:", start_date)
            print("End Date:", end_date)
            print("Image")

            pixmap = QPixmap()
            if photo:
                pixmap.loadFromData(photo, 'PNG')  # 'PNG' is the format of the image. Change if necessary.
                self.ui.a_image_label.setPixmap(pixmap)
                self.ui.a_image_label.show()
            else:
                print("No photo found.")

        else:
            print("No matching member found.")


        self.member_id_output = createLabel(
            parent = self.ui.attendance_page,
            name = "member_id_output",
            geometry = QRect(30,300,211,40),
            text = f"{membership_id}",
            font = font1
        )

        self.membership_type_output = createLabel(
            parent = self.ui.attendance_page,
            name = "membership_type_output",
            geometry = QRect(350,300,211,40),
            text = f"{membership_type}",
            font = font1
        )

        self.start_date_output = createLabel(
            parent = self.ui.attendance_page,
            name = "start_date_output",
            geometry = QRect(190,380,190,40),
            text = f"{start_date}",
            font = font1
        )

        self.end_date_output = createLabel(
            parent = self.ui.attendance_page,
            name = "end_date_output",
            geometry = QRect(570,380,190,40),
            text = f"{end_date}",
            font = font1
        )

        self.image_output = createLabel(
            parent = self.ui.attendance_page,
            name = "image_output",
            geometry = QRect(680, 30, 250, 250),
            text = f"{photo}",
            font = font1
        )
        self.member_id_output.show()
        self.membership_type_output.show()
        self.start_date_output.show()
        self.end_date_output.show()
        # Close the connection
        conn.close()

    def clear_text(self):
        self.member_id_output.clear()
        self.membership_type_output.clear()
        self.ui.search_member_input.clear()
        self.start_date_output.clear()
        self.end_date_output.clear()

    def insert_image(self, image):
        # Open a file dialog to select an image file
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Image Files (*.png *.jpg *.bmp *.gif)")
        image_label = image
        if file_name:
            # Load the image and set it to the label
            pixmap = QPixmap(file_name)
            image_label.setPixmap(pixmap.scaled(image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(950, 800)
        Form.setStyleSheet("background-color: #FFFFFF")

        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName("stackedWidget")

        # Setup pages
        self.setupMainPage()
        self.setupMemberPage()
        self.setupAttendancePage()

        self.verticalLayout.addWidget(self.stackedWidget)
        self.stackedWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(Form)

    def setupMainPage(self):
        self.main_page = QWidget()
        self.main_page.setObjectName("main_page")

        button_style = "background-color: #002877; color: #FFFFFF"

        self.member_button = createButton(
            parent=self.main_page, 
            name="member_button",
            geometry=QRect(240, 190, 450, 100), 
            text="Members", 
            font_size=25, 
            style_sheet=button_style
        )

        self.attendance_button = createButton(
            parent=self.main_page, 
            name="attendance_button", 
            geometry=QRect(240, 430, 450, 100), 
            text="Attendance", 
            font_size=25, 
            style_sheet=button_style
        )

        self.stackedWidget.addWidget(self.main_page)

    def setupMemberPage(self):
        self.member_page = QWidget()
        self.member_page.setObjectName("member_page")
        self.createMemberInputs()
        self.stackedWidget.addWidget(self.member_page)

    def createMemberInputs(self):

        # LABELS
        self.membership_id_label = createLabel(
            parent=self.member_page,
            name="membership_label", 
            geometry=QRect(20, 590, 231, 50), 
            text="Membership Type", 
            font= font1
        )

        self.end_date_label = createLabel(
            parent=self.member_page,
            name="end_date_label",
            geometry=QRect(410, 660, 131, 50),
            text="End Date",
            font=font1
        )

        self.phone_number_label = createLabel(
            parent=self.member_page,
            name="phone_number_label",
            geometry=QRect(20, 520, 221, 50),
            text="Phone Number",
            font=font1
        )

        self.last_name_label = createLabel(
            parent=self.member_page,
            name="last_name_label",
            geometry=QRect(20, 240, 160, 40),
            text="Last Name",
            font=font1
        )

        self.first_name_label = createLabel(
            parent=self.member_page,
            name="first_name_label",
            geometry=QRect(20, 120, 160, 40),
            text="First Name",
            font=font1
        )

        self.address_label = createLabel(
            parent=self.member_page,
            name="address_label",
            geometry=QRect(20, 370, 121, 40),
            text="Address",
            font=font1
        )

        self.start_date_label = createLabel(
            parent=self.member_page,
            name="start_date_label",
            geometry=QRect(20, 660, 161, 50),
            text="Start Date",
            font=font1
        )

        self.birthday_label = createLabel(
            parent=self.member_page,
            name="birthday_label",
            geometry=QRect(310, 300, 121, 50),
            text="Birthday",
            font=font1
        )

        self.membership_label = createLabel(
            parent=self.member_page,
            name="membership_label",
            geometry=QRect(20, 590, 231, 50),
            text="Membership Type",
            font=font1
        )

        self.membership_id_label = createLabel(
            parent=self.member_page,
            name="membership_id_label",
            geometry=QRect(20, 60, 225, 40),
            text="Membership ID",
            font=font1
        )

        self.duration_label = createLabel(
            parent=self.member_page,
            name="duration_label",
            geometry=QRect(460, 590, 131, 50),
            text="Duration",
            font=font1
        )

        self.gender_label = createLabel(
            parent=self.member_page,
            name="gender_label",
            geometry=QRect(20, 300, 121, 50),
            text="Gender",
            font=font1
        )

        self.middle_name_label = createLabel(
            parent=self.member_page,
            name="middle_name_label",
            geometry=QRect(20, 180, 190, 40),
            text="Middle Name",
            font=font1
        )


        # INPUTS
        self.membership_id_input = createLineInput(
            parent=self.member_page, 
            name="membership_id_input", 
            geometry=QRect(260, 60, 391, 50)
        )

        self.first_name_input = createLineInput(
            parent=self.member_page, 
            name="first_name_input", 
            geometry=QRect(190, 120, 461, 50)
        )

        self.middle_name_input = createLineInput(
            parent=self.member_page, 
            name="middle_name_input", 
            geometry=QRect(220, 180, 431, 50)
        )

        self.last_name_input = createLineInput(
            parent=self.member_page, 
            name="last_name_input", 
            geometry=QRect(190, 240, 461, 50)
        )

        self.phone_number_input = createLineInput(
            parent=self.member_page, 
            name="phone_number_input", 
            geometry=QRect(240, 520, 401, 50)
        )

        self.address_input = createLineInput(
            parent=self.member_page, 
            name="address_input", 
            geometry=QRect(150, 370, 501, 141)
        )

        self.duration_input = createLineInput(
            parent=self.member_page, 
            name="duration_input", 
            geometry=QRect(600, 590, 261, 50)
        )

        self.start_date_edit = createDate(
            parent = self.member_page,
            name = "start_date_edit",
            geometry = QRect(180, 660, 211, 50),
            font = 20
        )
        setCurrentDate(self.start_date_edit)

        self.end_date_edit = createDate(
            parent = self.member_page,
            name = "enf_date_edit",
            geometry = QRect(560, 660, 211, 50),
            font = 20
        )
        setCurrentDate(self.end_date_edit)

        self.birthday_date = createDate(
            parent = self.member_page,
            name = "birthday_date",
            geometry = QRect(440, 300, 211, 50),
            font = 20
        )
        setCurrentDate(self.birthday_date)


        self.gender_combo_box = createComboBox(
            parent = self.member_page,
            name = "gender_combo_box",
            geometry = QRect(140, 300, 151, 50),
            font = 20,
            item = ["Male", "Female"]
        )        

        self.membership_combo_box = createComboBox(
            parent = self.member_page,
            name = "membership_combo_box",
            geometry = QRect(280, 590, 161, 50),
            font = 20,
            item = ["Standard", "Lifetime"]
        )        
                          

        self.signature_label = createLabel(
            parent = self.member_page,
            name = "signature_label",
            geometry = QRect(670, 370, 250, 91),
            text = "",
            font = font1
        )
        self.signature_label.setStyleSheet(
            "border: 1px solid black; background-color: #BDBDBD"
        )

        self.image_label = createLabel(
            parent = self.member_page,
            name = "image_label",
            geometry = QRect(670, 10, 250, 250),
            text = "",
            font = font1,
        )
        self.image_label.setStyleSheet(
            "border: 1px solid black; background-color: #BDBDBD"
        )

        self.register_member_button = createButton(
            parent=self.member_page, 
            name="register_member_button", 
            geometry=QRect(680, 730, 251, 50),
            text="Register Member", 
            font_size=16, 
            style_sheet="background-color: #28a745"
        )

        self.insert_signature_button = createButton(
            parent=self.member_page, 
            name="insert_signature_button", 
            geometry=QRect(670, 470, 251, 50),
            text="Insert Signature", 
            font_size=16, 
            style_sheet="background-color: #007bff"
        )

        self.insert_image_button = createButton(
            parent=self.member_page, 
            name="insert_image_button", 
            geometry=QRect(670, 270, 251, 50),
            text="Insert Image", 
            font_size=16, 
            style_sheet="background-color: #007bff"
        )

        self.clear_button = createButton(
            parent=self.member_page, 
            name="clear_button", 
            geometry=QRect(500, 730, 171, 50), 
            text="Clear", 
            font_size=16,
            style_sheet="background-color: #ff9800"
        )

        self.back_button = createButton(
            parent=self.member_page, 
            name="back_button", 
            geometry=QRect(20, 10, 121, 41), 
            text="Back", 
            font_size=16,
            style_sheet="background-color: #002877; color: #FFFFFF"
        )

    def createAttendanceInputs(self):
        font1 = QFont()
        font1.setPointSize(22)

        # CREATION OF LABELS
        self.member_name_label = createLabel(
            parent=self.attendance_page, 
            name="member_name_label", 
            geometry=QRect(30, 80, 225, 40), 
            text="Name of Member", 
            font=font1
        )
        self.member_id_label = createLabel(
            parent=self.attendance_page, 
            name="membership_id_label", 
            geometry=QRect(30, 250, 225, 40), 
            text="Membership ID", 
            font=font1
        )

        self.membership_type_label = createLabel(
            parent=self.attendance_page, 
            name="membership_type_label", 
            geometry=QRect(350, 250, 231, 40), 
            text="Membership Type", 
            font=font1
        )

        self.start_date_label = createLabel(
            parent=self.attendance_page, 
            name="start_date_label", 
            geometry=QRect(30, 380, 140, 40),
            text="Start Date", 
            font=font1
        )

        self.end_date_label = createLabel(
            parent=self.attendance_page, 
            name="end_date_label", 
            geometry=QRect(420, 380, 130, 40), 
            text="End Date", 
            font=font1
        )

        self.type_of_attendance_label = createLabel(
            parent=self.attendance_page, 
            name="type_of_attendance_label", 
            geometry=QRect(30, 450, 260, 40), 
            text="Type of Attendance", 
            font=font1
        )

        self.date_label = createLabel(
            parent=self.attendance_page, 
            name="date_label", 
            geometry=QRect(30, 590, 70, 40), 
            text="Date", 
            font=font1
        )

        self.time_label = createLabel(
            parent=self.attendance_page, 
            name="time_label", 
            geometry=QRect(290, 590, 70, 40), 
            text="Time", 
            font=font1
        )

        self.a_image_label = createLabel(
            parent=self.attendance_page, 
            name="image_label", 
            geometry=QRect(670, 10, 250, 250),
            text="",
            font= font1
        )

       
        self.a_image_label.setStyleSheet(
            "border: 1px solid black; background-color: #BDBDBD"
        )


        self.attendance_combo_box = createComboBox(
            parent = self.attendance_page,
            name = "attendance_combo_box",
            geometry = QRect(30, 500, 150, 50),
            font = 20,
            item = ["Entry", "Exit"]
        )
     
        self.a_start_date_edit = createDate(
            parent = self.attendance_page,
            name = "start_date_edit",
            geometry = QRect(30, 650, 210, 40),
            font = 20,
        )
        setCurrentDate(date_input = self.a_start_date_edit)

        self.attendance_time_input = createTime(
            parent = self.attendance_page,
            name = "attendance_time",
            geometry = QRect(290, 650, 210, 40),
            font = 20
        )
        setCurrentTime(self.attendance_time_input)

    def setupAttendancePage(self):
        self.attendance_page = QWidget()
        self.attendance_page.setObjectName("attendance_page")

        self.attendance_back_button = createButton(
            parent=self.attendance_page, 
            name="attendance_back_button", 
            geometry=QRect(30, 20, 121, 41), 
            text="Back", 
            font_size=16,
            style_sheet="background-color: #002877; color: #FFFFFF"
        )

        self.attendance_submit_button = createButton(
            parent=self.attendance_page, 
            name="submit_button",
            geometry=QRect(680, 730, 251, 50),
            text="Submit", 
            font_size=16, 
            style_sheet="background-color: #28a745"
        )

        self.attendance_clear_button = createButton(
            parent=self.attendance_page, 
            name="attendance_clear_button", 
            geometry=QRect(500, 730, 171, 50),
            text="Clear", 
            font_size=16, 
            style_sheet="background-color: #ff9800"
        )

        self.search_button = createButton(
            parent=self.attendance_page, 
            name="search_button", 
            geometry=QRect(520, 190, 141, 50),
            text="Search",
            font_size=16, 
            style_sheet="background-color: #007bff"
        )

        self.search_member_input = createLineInput(
            parent = self.attendance_page,
            name = "search_member_input",
            geometry = QRect(30, 130, 630, 50)
        )

        self.createAttendanceInputs()
        self.stackedWidget.addWidget(self.attendance_page)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Registration()
    window.show()
    sys.exit(app.exec_())
