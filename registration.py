<<<<<<< HEAD
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from assets import *
import sqlite3
import re
from datetime import datetime
import uuid

# ==============================================================================
# ==============================================================================
#                           REGISTRATION     CLASS
# ==============================================================================
# ==============================================================================
class Registration(QWidget):
    def __init__(self, parent=None):
        super(Registration, self).__init__(parent)
        self.setObjectName("Form")
        self.resize(950, 800)
        self.setStyleSheet("background-color: #FFFFFF")
        self.open_registration_interface()


    def insert_image(self, image):
    # Open a file dialog to select an image file
        file_dialog = QFileDialog()
        file_name, _ = file_dialog.getOpenFileName(
            None, "Select Image", "", "Image Files (*.png *.jpg *.bmp *.gif)"
        )

        if file_name:
            # Load the image and set it to the label
            pixmap = QPixmap(file_name)
            image.setPixmap(pixmap.scaled(image.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def open_registration_interface(self):

        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.stackedWidget = QStackedWidget(self)
        self.stackedWidget.setObjectName("stackedWidget")

        self.open_main_page()               # MAIN PAGE
        self.open_create_member_page()      # MEMBER PAGE
        self.open_create_attendance_page()  # ATTENDANCE PAGE

        self.verticalLayout.addWidget(self.stackedWidget)
        self.stackedWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(self)

    def show_main_page(self):
        self.stackedWidget.setCurrentIndex(0)
        
    def show_member_page(self):
        self.generate_member_id()
        self.clear_inputs(self.member_page)
        self.stackedWidget.setCurrentIndex(1)
        
    def show_attendance_page(self):
        self.clear_inputs(self.attendance_page)
        self.stackedWidget.setCurrentIndex(2)
        
    def show_employee_page(self):
        self.clear_inputs(self.employee_page)
        self.stackedWidget.setCurrentIndex(3)



# =============================================================
#                     STAFF MAIN PAGE
# ============================================================= 
    def open_main_page(self):
        self.main_page = QWidget()
        self.main_page.setObjectName("main_page")
        self.stackedWidget.addWidget(self.main_page)
        # ===========================================
        #             MAIN PAGE BUTTONS
        # ===========================================
        self.switch_member_page_button = createButton(
            parent = self.main_page,
            name = "member_page_button",
            geometry = QRect(300, 250, 350, 100),
            text = "Register Member",
            font = font3,
            style = "background-color: #004F9A; color: #FFFFFF"
        )

        self.switch_attendance_page_button = createButton(
            parent = self.main_page,
            name = "attendance_page_button",
            geometry = QRect(300, 440, 350, 100),
            text = "Register Attendance",
            font = font3,
            style = "background-color: #004F9A; color: #FFFFFF"
        )

        self.switch_member_page_button.clicked.connect(self.show_member_page)
        self.switch_attendance_page_button.clicked.connect(self.show_attendance_page)

# =============================================================
#                     CREATE MEMBER PAGE
# =============================================================    
    def open_create_member_page(self):
        self.member_page = QWidget()
        self.member_page.setObjectName("member_page")


        # ===========================================
        #             MEMBER PAGE LABELS
        # ===========================================

        # MEMBER REGISTRATION TEXT LABEL
        self.member_registration_text_label = createLabel(
            parent = self.member_page,
            name = "member_registration_text_label",
            geometry = QRect(310, 50, 380, 40),
            text = "Member Registration",
            font = font4,
            style = "font: bold"
        )

        # MEMBER ID LABEL
        self.member_id_label = createLabel(
            parent = self.member_page,
            name = "member_id_label",
            geometry = QRect(40, 150, 191, 40),
            text = "Membership ID:",
            font = font1,
            style = ""
        )

        # MEMBER ID OUTPUT LABEL
        self.member_id_output_label = createLabel(
            parent = self.member_page,
            name = "member_id_output",
            geometry = QRect(240, 150, 410, 40),
            text = "",
            font = font1,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # FIRST NAME LABEL
        self.member_first_name_label = createLabel(
            parent = self.member_page,
            name = "first_name_label",
            geometry = QRect(40, 210, 130, 40),
            text = "First Name",
            font = font1,
            style = ""
        )

        # MIDDLE NAME LABEL
        self.member_middle_name_label = createLabel(
            parent = self.member_page,
            name = "middle_name_label",
            geometry = QRect(380, 210, 160, 40),
            text = "Middle Name",
            font = font1,
            style = ""
        )

        # LAST NAME LABEL
        self.member_last_name_label = createLabel(
            parent = self.member_page,
            name = "last_name_label",
            geometry = QRect(40, 310, 130, 40),
            text = "Last Name",
            font = font1,
            style = ""
        )

        # GENDER LABEL
        self.member_gender_label = createLabel(
            parent = self.member_page,
            name = "gender_label",
            geometry = QRect(380, 310, 130, 40),
            text = "Gender",
            font = font1,
            style = ""
        )

        # ADDRESS LABEL
        self.member_address_label = createLabel(
            parent = self.member_page,
            name = "addresslabel",
            geometry = QRect(40, 420, 130, 40),
            text = "Address",
            font = font1,
            style = ""
        )

        # BIRTHDATE LABEL
        self.member_birthdate_label = createLabel(
            parent = self.member_page,
            name = "birthdate_label",
            geometry = QRect(380, 420, 130, 40),
            text = "Birthdate",
            font = font1,
            style = ""
        )

        # PHONE NUMBER LABEL
        self.member_phone_number_label = createLabel(
            parent = self.member_page,
            name = "phone_number_label",
            geometry = QRect(40, 530, 180, 40),
            text = "Phone Number",
            font = font1,
            style = ""
        )

        # MEMBERSHIP TYPE LABEL
        self.member_membership_type_label = createLabel(
            parent = self.member_page,
            name = "membership_type_label",
            geometry = QRect(380, 530, 210, 40),
            text = "Membership Type",
            font = font1,
            style = ""
        )

        # START DATE LABEL
        self.member_start_date_label = createLabel(
            parent = self.member_page,
            name = "start_date_label",
            geometry = QRect(40, 630, 180, 40),
            text = "Start Date",
            font = font1,
            style = ""
        )

        # END DATE LABEL
        self.member_end_date_label = createLabel(
            parent = self.member_page,
            name = "end_date_label",
            geometry = QRect(280, 630, 180, 40),
            text = "End Date",
            font = font1,
            style = ""
        )

        # IMAGE LABEL 
        self.member_image_label = createLabel(
            parent = self.member_page,
            name = "image_label",
            geometry = QRect(680, 140, 250, 250),
            text = "",
            font = font1,
            style = "background-color: #F9F7FF; border: 1.5px solid black"
        )
        
        # SIGNATURE LABEL
        self.member_signature_label = createLabel(
            parent = self.member_page,
            name = "signature_label",
            geometry = QRect(750, 460, 180, 90),
            text = "",
            font = font1,
            style = "background-color: #F9F7FF; border: 1.5px solid black"
        )
        
        # ===========================================
        #             MEMBER PAGE INPUTS
        # ===========================================

        # FIRST NAME INPUT
        self.member_first_name_input = createLineInput(
            parent = self.member_page,
            name = "first_name_output",
            geometry = QRect(40, 260, 330, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # MIDDLE NAME INPUT
        self.member_middle_name_input = createLineInput(
            parent = self.member_page,
            name = "middle_name_output",
            geometry = QRect(380, 260, 280, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # LAST NAME INPUT
        self.member_last_name_input = createLineInput(
            parent = self.member_page,
            name = "last_name_output",
            geometry = QRect(40, 360, 330, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # ADDRESS INPUT
        self.member_address_input = createLineInput(
            parent = self.member_page,
            name = "address_output",
            geometry = QRect(40, 470, 330, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )
        # PHONE NUMBER INPUT
        self.member_phone_number_input = createLineInput(
            parent = self.member_page,
            name = "phone_number_output",
            geometry = QRect(40, 570, 330, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # ===========================================
        #            MEMBER PAGE COMBO BOX
        # ===========================================

        # GENDER BOX
        self.member_gender_combo_box = createComboBox(
            parent = self.member_page,
            name = "gender_combo_box",
            geometry = QRect(380, 360, 140, 40),
            font = font2,
            item = ['Male', 'Female'],
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # MEMBERSHIP TYPE BOX
        self.member_membership_type_combo_box = createComboBox(
            parent = self.member_page,
            name = "gender_combo_box",
            geometry = QRect(380, 570, 210, 40),
            font = font2,
            item = ['Standard', 'Lifetime'],
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.member_membership_type_combo_box.currentIndexChanged.connect(self.update_end_date)

        # ===========================================
        #              MEMBER PAGE DATE
        # ===========================================

        # BIRTH DATE
        self.member_birth_date = createDate(
            parent = self.member_page,
            name = "birthdate",
            geometry = QRect(380, 470, 200, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # START DATE
        self.member_start_date = createDate(
            parent = self.member_page,
            name = "member_start_date",
            geometry = QRect(40, 670, 200, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # END DATE
        self.member_end_date = createDate(
            parent = self.member_page,
            name = "member_end_date",
            geometry = QRect(280, 670, 200, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # ===========================================
        #              MEMBER PAGE BUTTONS
        # ===========================================
    
        # BACK BUTTON
        self.member_back_button = createButton(
            parent = self.member_page,
            name = "back_button",
            geometry = QRect(40, 50, 70, 50),
            text = "Back",
            font = font3,
            style = "background-color: #004F9A"
        )

        # INSERT IMAGE BUTTON
        self.member_insert_image_button = createButton(
            parent = self.member_page,
            name = "insert_image_button",
            geometry = QRect(680, 400, 250, 50),
            text = "Insert Image",
            font = font3,
            style = "background-color: #004F9A"
        )

        # INSERT SIGNATURE BUTTON
        self.member_insert_signature_button = createButton(
            parent = self.member_page,
            name = "insert_signature_button",
            geometry = QRect(680, 560, 250, 50),
            text = "Insert Signature",
            font = font3,
            style = "background-color: #004F9A"
        )

        # CLEAR BUTTON
        self.member_clear_button = createButton(
            parent = self.member_page,
            name = "clear_button",
            geometry = QRect(510, 730, 170, 50),
            text = "Clear",
            font = font3,
            style = "background-color: #882400"
        )

        # REGISTER BUTTON
        self.member_register_button = createButton(
            parent = self.member_page,
            name = "register_button",
            geometry = QRect(690, 730, 250, 50),
            text = "Register",
            font = font3,
            style = "background-color: #006646"
        )


        self.member_insert_image_button.clicked.connect(lambda: self.insert_image(self.member_image_label))
        self.member_insert_signature_button.clicked.connect(lambda: self.insert_image(self.member_signature_label))
        self.member_register_button.clicked.connect(self.register_member)
        self.member_clear_button.clicked.connect(lambda : self.clear_inputs(self.member_page))
        self.member_back_button.clicked.connect(lambda: self.back_button(self.member_page))
        self.stackedWidget.addWidget(self.member_page)



# =============================================================
#                   CREATE ATTENDANCE PAGE
# ============================================================= 
    def open_create_attendance_page(self):
        self.attendance_page = QWidget()
        self.attendance_page.setObjectName("attendance_page")
        self.stackedWidget.addWidget(self.attendance_page)
        # ===========================================
        #             ATTENDANCE  LABELS
        # ===========================================


        self.attendance_registration_label = createLabel(
            parent = self.attendance_page,
            name = "attendance_registration",
            geometry = QRect(270, 50, 430, 40),
            text = "Attendance Registration",
            font = font4,
            style = "font: bold"
        )

        self.attendance_member_name_label = createLabel(
            parent = self.attendance_page,
            name = "member_name",
            geometry = QRect(40, 150, 190, 40),
            text = "Member Name:",
            font = font1,
            style = ""
        )

        self.attendance_membership_id_label = createLabel(
            parent = self.attendance_page,
            name = "membership_id",
            geometry = QRect(40, 210, 190, 40),
            text = "Membership ID",
            font = font1,
            style = ""
        )

        self.attendance_membership_id_output_label = createLabel(
            parent = self.attendance_page,
            name = "output",
            geometry = QRect(40, 260, 330, 40),
            text = "",
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.attendance_gender_label = createLabel(
            parent = self.attendance_page,
            name = "gender",
            geometry = QRect(380, 210, 130, 40),
            text = "Gender",
            font = font1,
            style = ""
        )

        self.attendance_gender_output_label = createLabel(
            parent = self.attendance_page,
            name = "output",
            geometry = QRect(380, 260, 140, 40),
            text = "",
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.attendance_phone_number_label = createLabel(
            parent = self.attendance_page,
            name = "phone_number",
            geometry = QRect(40, 320, 180, 40),
            text = "Phone Number",
            font = font1,
            style = ""
        )

        self.attendance_phone_number_output_label = createLabel(
            parent = self.attendance_page,
            name = "output",
            geometry = QRect(40, 360, 330, 40),
            text = "",
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.attendance_membership_type_label = createLabel(
            parent = self.attendance_page,
            name = "membership_type",
            geometry = QRect(380, 320, 210, 40),
            text = "Membership Type",
            font = font1,
            style = ""
        )

        self.attendance_membership_type_output_label = createLabel(
            parent = self.attendance_page,
            name = "output",
            geometry = QRect(380, 360, 260, 40),
            text = "",
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.attendance_start_date_label = createLabel(
            parent = self.attendance_page,
            name = "start_date",
            geometry = QRect(40, 420, 130, 40),
            text = "Start Date",
            font = font1,
            style = ""
        )

        self.attendance_start_date_output_label = createLabel(
            parent = self.attendance_page,
            name = "output",
            geometry = QRect(40, 470, 200, 40),
            text = "",
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )   
    
        self.attendance_end_date_label = createLabel(
            parent = self.attendance_page,
            name = "end_date",
            geometry = QRect(270, 420, 180, 40),
            text = "End Date",
            font = font1,
            style = ""
        )

        self.attendance_end_date_output_label = createLabel(
            parent = self.attendance_page,
            name = "output",
            geometry = QRect(270, 470, 200, 40),
            text = "",
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.attendance_image_output_label = createLabel(
            parent = self.attendance_page,
            name = "output",
            geometry = QRect(680, 140, 250, 250),
            text = "",
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.attendance_time_label = createLabel(
            parent = self.attendance_page,
            name = "time",
            geometry = QRect(490, 420, 130, 40),
            text = "Time",
            font = font1,
            style = ""
        )

        self.attendance_type_label = createLabel(
            parent = self.attendance_page,
            name = "type_of_attendance",
            geometry= QRect(690, 420, 230, 40),
            text = "Type of Attendance",
            font = font1,
            style = ""
        )

        self.attendance_date_label = createLabel(
            parent = self.attendance_page,
            name = "date",
            geometry = QRect(40, 520, 230, 40),
            text = "Date of Attendance",
            font = font1,
            style = ""
        )
        # ===========================================
        #            ATTENDANCE  INPUTS
        # ===========================================

        self.attendance_member_name_input = createLineInput(
            parent = self.attendance_page,
            name = "member_name_input",
            geometry = QRect(240, 150, 410, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )
        self.attendance_member_name_input.setPlaceholderText("Search Member Name")
        self.attendance_member_name_input.textChanged.connect(self.update_search_results)
        
        self.search_results = QListWidget(self)
        self.search_results.hide()  # Hide initially
        self.search_results.setGeometry(240, 190, 410, 400)
        self.search_results.setFont(font2)
        # Connect signals
        self.search_results.itemClicked.connect(self.handle_item_selection)


        # ===========================================
        #            ATTENDANCE  TIME
        # ===========================================
        self.attendance_time_input = createTime(
            parent = self.attendance_page,
            name = "time_input",
            geometry = QRect(490, 470, 190, 40),
            font = font2, 
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # ===========================================
        #           ATTENDANCE COMBO BOX
        # ===========================================

        self.attendance_type_combo_box = createComboBox(
            parent = self.attendance_page,
            name = 'type_of_attendance_input',
            geometry = QRect(690,470,140,40),
            font = font2,
            item = ['Entry', 'Exit'],
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # ===========================================
        #               ATTENDANCE DATES
        # ===========================================

        self.attendance_date_input = createDate(
            parent = self.attendance_page,
            name = "date",
            geometry = QRect(40, 560, 190, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )
        # ===========================================
        #           ATTENDANCE PAGE BUTTONS
        # ===========================================

        # CLEAR BUTTON
        self.attendance_clear_button = createButton(
            parent = self.attendance_page,
            name = "clear_button",
            geometry = QRect(510, 730, 170, 50),
            text = "Clear",
            font = font3,
            style = "background-color: #882400"
        )

        # REGISTER BUTTON
        self.attendance_register_button = createButton(
            parent = self.attendance_page,
            name = "register_button",
            geometry = QRect(690, 730, 250, 50),
            text = "Register",
            font = font3,
            style = "background-color: #006646"
        )

        # BACK BUTTON
        self.attendance_back_button = createButton(
            parent = self.attendance_page,
            name = "back_button",
            geometry = QRect(40, 50, 70, 50),
            text = "Back",
            font = font3,
            style = "background-color: #004F9A"
        )

        self.attendance_register_button.clicked.connect(self.register_attendance)
        self.attendance_back_button.clicked.connect(lambda: self.back_button(self.attendance_page))
        self.attendance_clear_button.clicked.connect(lambda: self.clear_inputs(self.attendance_page))

# =============================================================
#                      BACK-END FUNCTIONS
# ============================================================= 
    def clear_inputs(self, page):
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
    
    def pixmap_to_bytes(self, pixmap):
        byte_array = QByteArray()
        buffer = QBuffer(byte_array)
        buffer.open(QBuffer.WriteOnly)
        pixmap.save(buffer, "PNG")
        return byte_array.data()

    def register_member(self):
        # Retrieve all inputs
        self.member_id = int(self.member_id_output_label.text())
        self.first_name = self.member_first_name_input.text()
        self.middle_name = self.member_middle_name_input.text()
        self.last_name = self.member_last_name_input.text()
        self.address = self.member_address_input.text()
        self.phone_number = self.member_phone_number_input.text()
        self.gender = self.member_gender_combo_box.currentText()
        self.membership_type = self.member_membership_type_combo_box.currentText()
        self.birth_date = self.member_birth_date.date()
        self.start_date = self.member_start_date.date()
        self.end_date = self.member_end_date.date()
        self.photo = self.member_image_label.pixmap()
        self.signature = self.member_signature_label.pixmap()

        if self.validate_member_inputs():
            # Convert photo and signature to bytes
            if self.photo:
                member_image_bytes = self.pixmap_to_bytes(self.photo)
            if self.signature:
                signature_image_bytes = self.pixmap_to_bytes(self.signature)


            cursor.execute(
                '''
                INSERT INTO Members 
                (member_id, first_name, middle_name, last_name, address, phone_number, birthdate, membership_type,
                gender, membership_start_date, membership_end_date, photo, signature) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''',
                (
                    self.member_id,
                    self.first_name,
                    self.middle_name,
                    self.last_name,
                    self.address,
                    self.phone_number,
                    self.birth_date.toString("yyyy-MM-dd"),
                    self.membership_type,
                    self.gender,
                    self.start_date.toString("yyyy-MM-dd"),
                    self.end_date.toString("yyyy-MM-dd"),
                    sqlite3.Binary(member_image_bytes),
                    sqlite3.Binary(signature_image_bytes)
                )
            )
            # Commit the transaction and close the connection
            connection.commit()
            QMessageBox.information(self, "Success", "Member registered successfully!")
        else:
            # Validation failed, do not proceed
            pass

    def update_end_date(self):
        membership_type = self.member_membership_type_combo_box.currentText()
        if membership_type == "Lifetime":
            self.member_end_date.setDate(QDate(9999, 12, 31))  # Set to a far future date
            self.member_end_date.setDisabled(True)  # Optionally disable the end date field
        else:
            self.member_end_date.setDisabled(False)
            self.member_end_date.setDate(QDate.currentDate())  # Reset to the current date


    def validate_member_inputs(self):

        # Check if all required fields are filled
        if not all([self.first_name, self.last_name, self.address, self.phone_number, self.gender, self.membership_type, self.photo, self.signature]):
            QMessageBox.warning(self, "Input Error", "All fields must be filled")
            return False

        # Validate that specific fields contain only letters
        if not all(re.match("^[A-Za-z ]+$", field) for field in [self.first_name, self.middle_name, self.last_name]):
            QMessageBox.warning(self, "Input Error", "First Name, Middle Name, and Last Name must contain only letters and spaces.")
            return False

        # Validate that the address is a string
        if not isinstance(self.address, str):
            QMessageBox.warning(self, "Input Error", "Address must be a string.")
            return False

        # Validate that the phone number is numeric
        if not self.phone_number.isdigit():
            QMessageBox.warning(self, "Input Error", "Phone Number must be numeric.")
            return False

        # Ensure birth date, start date, and end date are valid
        if not isinstance(self.birth_date, QDate) or not isinstance(self.start_date, QDate) or (self.membership_type != 'Lifetime' and not isinstance(self.end_date, QDate)):
            QMessageBox.warning(self, "Input Error", "Birth Date, Start Date, and End Date must be valid dates.")
            return False

        return True

    def update_search_results(self):
        search_text = self.attendance_member_name_input.text()
        self.search_results.clear()

        if search_text:
            # Fetch members from database based on search text
            query = "SELECT first_name, last_name FROM Members WHERE first_name || ' ' || last_name LIKE ?"
            cursor.execute(query, ('%' + search_text + '%',))
            results = cursor.fetchall()
            # Add results to list widget
            for first_name, last_name in results:
                full_name = f"{first_name} {last_name}"
                self.search_results.addItem(full_name)
            self.search_results.show()  # Show list widget when there are results
        else:
            self.search_results.hide()  # Hide list widget if search text is empty


    def search_member(self, member_input):
        # Split the full name into first name and last name
        name_parts = member_input.rsplit(' ', 1)
        
        if len(name_parts) < 2:
            print("Please enter both first name and last name.")
            return
        
        first_name = name_parts[0].strip()
        last_name = name_parts[1].strip()

        # Debug: Print the first and last name
        print(f"Searching for: first_name = '{first_name}', last_name = '{last_name}'")

        # Execute the SQL query with placeholders for the first name and last name
        cursor.execute('''
            SELECT member_id, gender, phone_number, membership_type, membership_start_date, membership_end_date, photo
            FROM Members
            WHERE first_name = ? AND last_name = ?
        ''', (first_name, last_name))

        # Fetch the results
        results = cursor.fetchone()

        # Check if the results are found
        if results:
            membership_id, gender, phone_number, membership_type, start_date, end_date, photo= results
            print("Membership ID:", membership_id)
            print("Membership Type:", membership_type)
            print("Start Date:", start_date)
            print("End Date:", end_date)
            print("Image")

            pixmap = QPixmap()
            if photo:
                pixmap.loadFromData(photo, 'PNG')  # 'PNG' is the format of the image. Change if necessary.
                self.attendance_image_output_label.setPixmap(pixmap)
                self.attendance_image_output_label.show()
            else:
                print("No photo found.")

        else:
            print("No matching member found.")

        self.attendance_membership_id_output_label.setText(str(membership_id))
        self.attendance_gender_output_label.setText(gender)
        self.attendance_phone_number_output_label.setText(phone_number)
        self.attendance_membership_type_output_label.setText(membership_type)
        self.attendance_start_date_output_label.setText(start_date)
        self.attendance_end_date_output_label.setText(end_date)


    def handle_item_selection(self, item):
        selected_name = item.text()
        # Handle item selection (e.g., perform an action with the selected name)
        self.attendance_member_name_input.setText(selected_name)
        self.search_member(selected_name)

        self.search_results.hide()  # Hide list widget after selection

    def generate_member_id(self):
        current_time = datetime.now()
        formatted_time = current_time.strftime('%m%d%y%H%M%S')
        prefix = '10'

        generated_id = f"{prefix}{formatted_time}"
        self.member_id_output_label.setText(generated_id)

    def back_button(self, page):
        self.clear_inputs(page)
        self.show_main_page()

    
    def register_attendance(self):

        today = self.attendance_date_input.date()
        member_id = int(self.attendance_membership_id_output_label.text())
        time = self.attendance_time_input.time()
        attendance = self.attendance_type_combo_box.currentText()

        print(type(member_id))
        print(type(time))
        print(type(attendance))
        print(type(today))
        # Check the last attendance record for the member
        cursor.execute("""
            SELECT attendance_id, entry_time, exit_time 
            FROM Attendance 
            WHERE member_id = ? AND date = ? 
            ORDER BY attendance_id DESC LIMIT 1
        """, (member_id, today.toString("yyyy-MM-dd")))
        
        last_record = cursor.fetchone()


        if attendance == "Entry":
            if last_record and not last_record[2]:  # If there's a record with entry_time but no exit_time
                print("Error: Member already has an entry record with no exit recorded.")
            else:
                cursor.execute("""
                    INSERT INTO Attendance (member_id, entry_time, date) 
                    VALUES (?, ?, ?)
                    """, (member_id, time.toString(), today.toString("yyyy-MM-dd")))
                print("Entry registered.")
        else:
            if last_record and not last_record[2]:  # If there's a record with entry_time but no exit_time
                cursor.execute("""  
                    UPDATE Attendance 
                    SET exit_time = ? 
                    WHERE attendance_id = ?
                    """, (time.toString(), last_record[0]))
                print("Exit registered.")
            else:
                print("Error: No entry record found or already exited.")

        connection.commit()
   

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Registration()
    window.show()
    sys.exit(app.exec_())
=======
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from assets import *
import sqlite3
import re
from datetime import datetime
import uuid

# ==============================================================================
# ==============================================================================
#                           REGISTRATION     CLASS
# ==============================================================================
# ==============================================================================
class Registration(QWidget):
    def __init__(self, parent=None):
        super(Registration, self).__init__(parent)
        self.setObjectName("Form")
        self.resize(950, 800)
        self.setStyleSheet("background-color: #FFFFFF")
        self.open_registration_interface()


    def insert_image(self, image):
    # Open a file dialog to select an image file
        file_dialog = QFileDialog()
        file_name, _ = file_dialog.getOpenFileName(
            None, "Select Image", "", "Image Files (*.png *.jpg *.bmp *.gif)"
        )

        if file_name:
            # Load the image and set it to the label
            pixmap = QPixmap(file_name)
            image.setPixmap(pixmap.scaled(image.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def open_registration_interface(self):

        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.stackedWidget = QStackedWidget(self)
        self.stackedWidget.setObjectName("stackedWidget")

        self.open_main_page()               # MAIN PAGE
        self.open_create_member_page()      # MEMBER PAGE
        self.open_create_attendance_page()  # ATTENDANCE PAGE
        self.open_create_employee_page()    # EMPLOYEE PAGE

        self.verticalLayout.addWidget(self.stackedWidget)
        self.stackedWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(self)

    def show_main_page(self):
        self.stackedWidget.setCurrentIndex(0)
        
    def show_member_page(self):
        self.generate_employee_id()
        self.clear_inputs(self.member_page)
        self.stackedWidget.setCurrentIndex(1)
        
    def show_attendance_page(self):
        self.clear_inputs(self.attendance_page)
        self.stackedWidget.setCurrentIndex(2)
        
    def show_employee_page(self):
        self.clear_inputs(self.employee_page)
        self.stackedWidget.setCurrentIndex(3)



# =============================================================
#                     STAFF MAIN PAGE
# ============================================================= 
    def open_main_page(self):
        self.main_page = QWidget()
        self.main_page.setObjectName("main_page")
        self.stackedWidget.addWidget(self.main_page)
        # ===========================================
        #             MAIN PAGE BUTTONS
        # ===========================================
        self.switch_member_page_button = createButton(
            parent = self.main_page,
            name = "member_page_button",
            geometry = QRect(300, 250, 350, 100),
            text = "Register Member",
            font = font3,
            style = "background-color: #004F9A; color: #FFFFFF"
        )

        self.switch_attendance_page_button = createButton(
            parent = self.main_page,
            name = "attendance_page_button",
            geometry = QRect(300, 440, 350, 100),
            text = "Register Attendance",
            font = font3,
            style = "background-color: #004F9A; color: #FFFFFF"
        )

        self.switch_member_page_button.clicked.connect(self.show_member_page)
        self.switch_attendance_page_button.clicked.connect(self.show_attendance_page)

# =============================================================
#                     CREATE MEMBER PAGE
# =============================================================    
    def open_create_member_page(self):
        self.member_page = QWidget()
        self.member_page.setObjectName("member_page")


        # ===========================================
        #             MEMBER PAGE LABELS
        # ===========================================

        # MEMBER REGISTRATION TEXT LABEL
        self.member_registration_text_label = createLabel(
            parent = self.member_page,
            name = "member_registration_text_label",
            geometry = QRect(310, 50, 380, 40),
            text = "Member Registration",
            font = font4,
            style = "font: bold"
        )

        # MEMBER ID LABEL
        self.member_id_label = createLabel(
            parent = self.member_page,
            name = "member_id_label",
            geometry = QRect(40, 150, 191, 40),
            text = "Membership ID:",
            font = font1,
            style = ""
        )

        # MEMBER ID OUTPUT LABEL
        self.member_id_output_label = createLabel(
            parent = self.member_page,
            name = "member_id_output",
            geometry = QRect(240, 150, 410, 40),
            text = "",
            font = font1,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # FIRST NAME LABEL
        self.member_first_name_label = createLabel(
            parent = self.member_page,
            name = "first_name_label",
            geometry = QRect(40, 210, 130, 40),
            text = "First Name",
            font = font1,
            style = ""
        )

        # MIDDLE NAME LABEL
        self.member_middle_name_label = createLabel(
            parent = self.member_page,
            name = "middle_name_label",
            geometry = QRect(380, 210, 160, 40),
            text = "Middle Name",
            font = font1,
            style = ""
        )

        # LAST NAME LABEL
        self.member_last_name_label = createLabel(
            parent = self.member_page,
            name = "last_name_label",
            geometry = QRect(40, 310, 130, 40),
            text = "Last Name",
            font = font1,
            style = ""
        )

        # GENDER LABEL
        self.member_gender_label = createLabel(
            parent = self.member_page,
            name = "gender_label",
            geometry = QRect(380, 310, 130, 40),
            text = "Gender",
            font = font1,
            style = ""
        )

        # ADDRESS LABEL
        self.member_address_label = createLabel(
            parent = self.member_page,
            name = "addresslabel",
            geometry = QRect(40, 420, 130, 40),
            text = "Address",
            font = font1,
            style = ""
        )

        # BIRTHDATE LABEL
        self.member_birthdate_label = createLabel(
            parent = self.member_page,
            name = "birthdate_label",
            geometry = QRect(380, 420, 130, 40),
            text = "Birthdate",
            font = font1,
            style = ""
        )

        # PHONE NUMBER LABEL
        self.member_phone_number_label = createLabel(
            parent = self.member_page,
            name = "phone_number_label",
            geometry = QRect(40, 530, 180, 40),
            text = "Phone Number",
            font = font1,
            style = ""
        )

        # MEMBERSHIP TYPE LABEL
        self.member_membership_type_label = createLabel(
            parent = self.member_page,
            name = "membership_type_label",
            geometry = QRect(380, 530, 210, 40),
            text = "Membership Type",
            font = font1,
            style = ""
        )

        # START DATE LABEL
        self.member_start_date_label = createLabel(
            parent = self.member_page,
            name = "start_date_label",
            geometry = QRect(40, 630, 180, 40),
            text = "Start Date",
            font = font1,
            style = ""
        )

        # END DATE LABEL
        self.member_end_date_label = createLabel(
            parent = self.member_page,
            name = "end_date_label",
            geometry = QRect(280, 630, 180, 40),
            text = "End Date",
            font = font1,
            style = ""
        )

        # IMAGE LABEL 
        self.member_image_label = createLabel(
            parent = self.member_page,
            name = "image_label",
            geometry = QRect(680, 140, 250, 250),
            text = "",
            font = font1,
            style = "background-color: #F9F7FF; border: 1.5px solid black"
        )
        
        # SIGNATURE LABEL
        self.member_signature_label = createLabel(
            parent = self.member_page,
            name = "signature_label",
            geometry = QRect(750, 460, 180, 90),
            text = "",
            font = font1,
            style = "background-color: #F9F7FF; border: 1.5px solid black"
        )
        
        # ===========================================
        #             MEMBER PAGE INPUTS
        # ===========================================

        # FIRST NAME INPUT
        self.member_first_name_input = createLineInput(
            parent = self.member_page,
            name = "first_name_output",
            geometry = QRect(40, 260, 330, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # MIDDLE NAME INPUT
        self.member_middle_name_input = createLineInput(
            parent = self.member_page,
            name = "middle_name_output",
            geometry = QRect(380, 260, 280, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # LAST NAME INPUT
        self.member_last_name_input = createLineInput(
            parent = self.member_page,
            name = "last_name_output",
            geometry = QRect(40, 360, 330, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # ADDRESS INPUT
        self.member_address_input = createLineInput(
            parent = self.member_page,
            name = "address_output",
            geometry = QRect(40, 470, 330, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )
        # PHONE NUMBER INPUT
        self.member_phone_number_input = createLineInput(
            parent = self.member_page,
            name = "phone_number_output",
            geometry = QRect(40, 570, 330, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # ===========================================
        #            MEMBER PAGE COMBO BOX
        # ===========================================

        # GENDER BOX
        self.member_gender_combo_box = createComboBox(
            parent = self.member_page,
            name = "gender_combo_box",
            geometry = QRect(380, 360, 140, 40),
            font = font2,
            item = ['Male', 'Female'],
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # MEMBERSHIP TYPE BOX
        self.member_membership_type_combo_box = createComboBox(
            parent = self.member_page,
            name = "gender_combo_box",
            geometry = QRect(380, 570, 210, 40),
            font = font2,
            item = ['Standard', 'Lifetime'],
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.member_membership_type_combo_box.currentIndexChanged.connect(self.update_end_date)

        # ===========================================
        #              MEMBER PAGE DATE
        # ===========================================

        # BIRTH DATE
        self.member_birth_date = createDate(
            parent = self.member_page,
            name = "birthdate",
            geometry = QRect(380, 470, 200, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # START DATE
        self.member_start_date = createDate(
            parent = self.member_page,
            name = "member_start_date",
            geometry = QRect(40, 670, 200, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # END DATE
        self.member_end_date = createDate(
            parent = self.member_page,
            name = "member_end_date",
            geometry = QRect(280, 670, 200, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # ===========================================
        #              MEMBER PAGE BUTTONS
        # ===========================================
    
        # BACK BUTTON
        self.member_back_button = createButton(
            parent = self.member_page,
            name = "back_button",
            geometry = QRect(40, 50, 70, 50),
            text = "Back",
            font = font3,
            style = "background-color: #004F9A"
        )

        # INSERT IMAGE BUTTON
        self.member_insert_image_button = createButton(
            parent = self.member_page,
            name = "insert_image_button",
            geometry = QRect(680, 400, 250, 50),
            text = "Insert Image",
            font = font3,
            style = "background-color: #004F9A"
        )

        # INSERT SIGNATURE BUTTON
        self.member_insert_signature_button = createButton(
            parent = self.member_page,
            name = "insert_signature_button",
            geometry = QRect(680, 560, 250, 50),
            text = "Insert Signature",
            font = font3,
            style = "background-color: #004F9A"
        )

        # CLEAR BUTTON
        self.member_clear_button = createButton(
            parent = self.member_page,
            name = "clear_button",
            geometry = QRect(510, 730, 170, 50),
            text = "Clear",
            font = font3,
            style = "background-color: #882400"
        )

        # REGISTER BUTTON
        self.member_register_button = createButton(
            parent = self.member_page,
            name = "register_button",
            geometry = QRect(690, 730, 250, 50),
            text = "Register",
            font = font3,
            style = "background-color: #006646"
        )


        self.member_insert_image_button.clicked.connect(lambda: self.insert_image(self.member_image_label))
        self.member_insert_signature_button.clicked.connect(lambda: self.insert_image(self.member_signature_label))
        self.member_register_button.clicked.connect(self.register_member)
        self.member_clear_button.clicked.connect(lambda : self.clear_inputs(self.member_page))
        self.member_back_button.clicked.connect(lambda: self.back_button(self.member_page))
        self.stackedWidget.addWidget(self.member_page)



# =============================================================
#                   CREATE ATTENDANCE PAGE
# ============================================================= 
    def open_create_attendance_page(self):
        self.attendance_page = QWidget()
        self.attendance_page.setObjectName("attendance_page")
        self.stackedWidget.addWidget(self.attendance_page)
        # ===========================================
        #             ATTENDANCE  LABELS
        # ===========================================


        self.attendance_registration_label = createLabel(
            parent = self.attendance_page,
            name = "attendance_registration",
            geometry = QRect(270, 50, 430, 40),
            text = "Attendance Registration",
            font = font4,
            style = "font: bold"
        )

        self.attendance_member_name_label = createLabel(
            parent = self.attendance_page,
            name = "member_name",
            geometry = QRect(40, 150, 190, 40),
            text = "Member Name:",
            font = font1,
            style = ""
        )

        self.attendance_membership_id_label = createLabel(
            parent = self.attendance_page,
            name = "membership_id",
            geometry = QRect(40, 210, 190, 40),
            text = "Membership ID",
            font = font1,
            style = ""
        )

        self.attendance_membership_id_output_label = createLabel(
            parent = self.attendance_page,
            name = "output",
            geometry = QRect(40, 260, 330, 40),
            text = "",
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.attendance_gender_label = createLabel(
            parent = self.attendance_page,
            name = "gender",
            geometry = QRect(380, 210, 130, 40),
            text = "Gender",
            font = font1,
            style = ""
        )

        self.attendance_gender_output_label = createLabel(
            parent = self.attendance_page,
            name = "output",
            geometry = QRect(380, 260, 140, 40),
            text = "",
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.attendance_phone_number_label = createLabel(
            parent = self.attendance_page,
            name = "phone_number",
            geometry = QRect(40, 320, 180, 40),
            text = "Phone Number",
            font = font1,
            style = ""
        )

        self.attendance_phone_number_output_label = createLabel(
            parent = self.attendance_page,
            name = "output",
            geometry = QRect(40, 360, 330, 40),
            text = "",
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.attendance_membership_type_label = createLabel(
            parent = self.attendance_page,
            name = "membership_type",
            geometry = QRect(380, 320, 210, 40),
            text = "Membership Type",
            font = font1,
            style = ""
        )

        self.attendance_membership_type_output_label = createLabel(
            parent = self.attendance_page,
            name = "output",
            geometry = QRect(380, 360, 260, 40),
            text = "",
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.attendance_start_date_label = createLabel(
            parent = self.attendance_page,
            name = "start_date",
            geometry = QRect(40, 420, 130, 40),
            text = "Start Date",
            font = font1,
            style = ""
        )

        self.attendance_start_date_output_label = createLabel(
            parent = self.attendance_page,
            name = "output",
            geometry = QRect(40, 470, 200, 40),
            text = "",
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )   
    
        self.attendance_end_date_label = createLabel(
            parent = self.attendance_page,
            name = "end_date",
            geometry = QRect(270, 420, 180, 40),
            text = "End Date",
            font = font1,
            style = ""
        )

        self.attendance_end_date_output_label = createLabel(
            parent = self.attendance_page,
            name = "output",
            geometry = QRect(270, 470, 200, 40),
            text = "",
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.attendance_image_output_label = createLabel(
            parent = self.attendance_page,
            name = "output",
            geometry = QRect(680, 140, 250, 250),
            text = "",
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.attendance_time_label = createLabel(
            parent = self.attendance_page,
            name = "time",
            geometry = QRect(490, 420, 130, 40),
            text = "Time",
            font = font1,
            style = ""
        )

        self.attendance_type_label = createLabel(
            parent = self.attendance_page,
            name = "type_of_attendance",
            geometry= QRect(690, 420, 230, 40),
            text = "Type of Attendance",
            font = font1,
            style = ""
        )

        self.attendance_date_label = createLabel(
            parent = self.attendance_page,
            name = "date",
            geometry = QRect(40, 520, 230, 40),
            text = "Date of Attendance",
            font = font1,
            style = ""
        )
        # ===========================================
        #            ATTENDANCE  INPUTS
        # ===========================================

        self.attendance_member_name_input = createLineInput(
            parent = self.attendance_page,
            name = "member_name_input",
            geometry = QRect(240, 150, 410, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )
        self.attendance_member_name_input.setPlaceholderText("Search Member Name")
        self.attendance_member_name_input.textChanged.connect(self.update_search_results)
        
        self.search_results = QListWidget(self)
        self.search_results.hide()  # Hide initially
        self.search_results.setGeometry(240, 190, 410, 400)
        self.search_results.setFont(font2)
        # Connect signals
        self.search_results.itemClicked.connect(self.handle_item_selection)


        # ===========================================
        #            ATTENDANCE  TIME
        # ===========================================
        self.attendance_time_input = createTime(
            parent = self.attendance_page,
            name = "time_input",
            geometry = QRect(490, 470, 190, 40),
            font = font2, 
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # ===========================================
        #           ATTENDANCE COMBO BOX
        # ===========================================

        self.attendance_type_combo_box = createComboBox(
            parent = self.attendance_page,
            name = 'type_of_attendance_input',
            geometry = QRect(690,470,140,40),
            font = font2,
            item = ['Entry', 'Exit'],
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # ===========================================
        #               ATTENDANCE DATES
        # ===========================================

        self.attendance_date_input = createDate(
            parent = self.attendance_page,
            name = "date",
            geometry = QRect(40, 560, 190, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )
        # ===========================================
        #           ATTENDANCE PAGE BUTTONS
        # ===========================================

        # CLEAR BUTTON
        self.attendance_clear_button = createButton(
            parent = self.attendance_page,
            name = "clear_button",
            geometry = QRect(510, 730, 170, 50),
            text = "Clear",
            font = font3,
            style = "background-color: #882400"
        )

        # REGISTER BUTTON
        self.attendance_register_button = createButton(
            parent = self.attendance_page,
            name = "register_button",
            geometry = QRect(690, 730, 250, 50),
            text = "Register",
            font = font3,
            style = "background-color: #006646"
        )

        # BACK BUTTON
        self.attendance_back_button = createButton(
            parent = self.attendance_page,
            name = "back_button",
            geometry = QRect(40, 50, 70, 50),
            text = "Back",
            font = font3,
            style = "background-color: #004F9A"
        )

        self.attendance_register_button.clicked.connect(self.register_attendance)
        self.attendance_back_button.clicked.connect(lambda: self.back_button(self.attendance_page))
        self.attendance_clear_button.clicked.connect(lambda: self.clear_inputs(self.attendance_page))

        
# =============================================================
#                     CREATE EMPLOYEE PAGE
# =============================================================    
    def open_create_employee_page(self):
        self.employee_page = QWidget()
        self.employee_page.setObjectName("employee_page")
        # ===========================================
        #             EMPLOYEE PAGE LABELS
        # ===========================================

        # employee REGISTRATION TEXT LABEL
        self.employee_registration_text_label = createLabel(
            parent = self.employee_page,
            name = "employee_registration_text_label",
            geometry = QRect(305, 50, 385, 40),
            text = "Employee Registration",
            font = font4,
            style = "font: bold"
        )

        # employee ID LABEL
        self.employee_id_label = createLabel(
            parent = self.employee_page,
            name = "employee_id_label",
            geometry = QRect(40, 150, 191, 40),
            text = "Employee ID:",
            font = font1,
            style = ""
        )

        # employee ID OUTPUT LABEL
        self.employee_id_output_label = createLabel(
            parent = self.employee_page,
            name = "employee_id_output",
            geometry = QRect(240, 150, 410, 40),
            text = "",
            font = font1,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # FIRST NAME LABEL
        self.employee_first_name_label = createLabel(
            parent = self.employee_page,
            name = "first_name_label",
            geometry = QRect(40, 210, 130, 40),
            text = "First Name",
            font = font1,
            style = ""
        )

        # MIDDLE NAME LABEL
        self.employee_middle_name_label = createLabel(
            parent = self.employee_page,
            name = "middle_name_label",
            geometry = QRect(380, 210, 160, 40),
            text = "Middle Name",
            font = font1,
            style = ""
        )

        # LAST NAME LABEL
        self.employee_last_name_label = createLabel(
            parent = self.employee_page,
            name = "last_name_label",
            geometry = QRect(40, 310, 130, 40),
            text = "Last Name",
            font = font1,
            style = ""
        )

        # GENDER LABEL
        self.employee_gender_label = createLabel(
            parent = self.employee_page,
            name = "gender_label",
            geometry = QRect(380, 310, 130, 40),
            text = "Gender",
            font = font1,
            style = ""
        )

        # ADDRESS LABEL
        self.employee_address_label = createLabel(
            parent = self.employee_page,
            name = "addresslabel",
            geometry = QRect(40, 420, 130, 40),
            text = "Address",
            font = font1,
            style = ""
        )

        # BIRTHDATE LABEL
        self.employee_birthdate_label = createLabel(
            parent = self.employee_page,
            name = "birthdate_label",
            geometry = QRect(380, 420, 130, 40),
            text = "Birthdate",
            font = font1,
            style = ""
        )

        # PHONE NUMBER LABEL
        self.employee_phone_number_label = createLabel(
            parent = self.employee_page,
            name = "phone_number_label",
            geometry = QRect(40, 530, 180, 40),
            text = "Phone Number",
            font = font1,
            style = ""
        )

        # EMPLOYEE TYPE LABEL
        self.employee_position_label = createLabel(
            parent = self.employee_page,
            name = "position_label",
            geometry = QRect(380, 530, 210, 40),
            text = "Position",
            font = font1,
            style = ""
        )

        # START DATE LABEL
        self.employee_start_date_label = createLabel(
            parent = self.employee_page,
            name = "start_date_label",
            geometry = QRect(40, 630, 180, 40),
            text = "Hire Date",
            font = font1,
            style = ""
        )

        # IMAGE LABEL 
        self.employee_image_label = createLabel(
            parent = self.employee_page,
            name = "image_label",
            geometry = QRect(680, 140, 250, 250),
            text = "",
            font = font1,
            style = "background-color: #F9F7FF; border: 1.5px solid black"
        )
        
        # SIGNATURE LABEL
        self.employee_signature_label = createLabel(
            parent = self.employee_page,
            name = "signature_label",
            geometry = QRect(750, 460, 180, 90),
            text = "",
            font = font1,
            style = "background-color: #F9F7FF; border: 1.5px solid black"
        )
        
        # ===========================================
        #             EMPLOYEE PAGE INPUTS
        # ===========================================

        # FIRST NAME INPUT
        self.employee_first_name_input = createLineInput(
            parent = self.employee_page,
            name = "first_name_output",
            geometry = QRect(40, 260, 330, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # MIDDLE NAME INPUT
        self.employee_middle_name_input = createLineInput(
            parent = self.employee_page,
            name = "middle_name_output",
            geometry = QRect(380, 260, 280, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # LAST NAME INPUT
        self.employee_last_name_input = createLineInput(
            parent = self.employee_page,
            name = "last_name_output",
            geometry = QRect(40, 360, 330, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # ADDRESS INPUT
        self.employee_address_input = createLineInput(
            parent = self.employee_page,
            name = "address_output",
            geometry = QRect(40, 470, 330, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )
        # PHONE NUMBER INPUT
        self.employee_phone_number_input = createLineInput(
            parent = self.employee_page,
            name = "phone_number_output",
            geometry = QRect(40, 570, 330, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # ===========================================
        #            EMPLOYEE PAGE COMBO BOX
        # ===========================================

        # GENDER BOX
        self.employee_gender_combo_box = createComboBox(
            parent = self.employee_page,
            name = "gender_combo_box",
            geometry = QRect(380, 360, 140, 40),
            font = font2,
            item = ['Male', 'Female'],
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # EMPLOYEE TYPE BOX
        self.employee_position_combo_box = createLineInput(
            parent = self.employee_page,
            name = "position",
            geometry = QRect(380, 570, 210, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # ===========================================
        #              EMPLOYEE PAGE DATE
        # ===========================================

        # BIRTH DATE
        self.employee_birth_date = createDate(
            parent = self.employee_page,
            name = "birthdate",
            geometry = QRect(380, 470, 200, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # START DATE
        self.employee_start_date = createDate(
            parent = self.employee_page,
            name = "employee_start_date",
            geometry = QRect(40, 670, 200, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # ===========================================
        #              EMPLOYEE PAGE BUTTONS
        # ===========================================
    
        # BACK BUTTON
        self.employee_back_button = createButton(
            parent = self.employee_page,
            name = "back_button",
            geometry = QRect(40, 50, 70, 50),
            text = "Back",
            font = font3,
            style = "background-color: #004F9A"
        )

        # INSERT IMAGE BUTTON
        self.employee_insert_image_button = createButton(
            parent = self.employee_page,
            name = "insert_image_button",
            geometry = QRect(680, 400, 250, 50),
            text = "Insert Image",
            font = font3,
            style = "background-color: #004F9A"
        )

        # INSERT SIGNATURE BUTTON
        self.employee_insert_signature_button = createButton(
            parent = self.employee_page,
            name = "insert_signature_button",
            geometry = QRect(680, 560, 250, 50),
            text = "Insert Signature",
            font = font3,
            style = "background-color: #004F9A"
        )

        # CLEAR BUTTON
        self.employee_clear_button = createButton(
            parent = self.employee_page,
            name = "clear_button",
            geometry = QRect(510, 730, 170, 50),
            text = "Clear",
            font = font3,
            style = "background-color: #882400"
        )

        # REGISTER BUTTON
        self.employee_register_button = createButton(
            parent = self.employee_page,
            name = "register_button",
            geometry = QRect(690, 730, 250, 50),
            text = "Register",
            font = font3,
            style = "background-color: #006646"
        )


        self.employee_insert_image_button.clicked.connect(lambda: self.insert_image(self.employee_image_label))
        self.employee_insert_signature_button.clicked.connect(lambda: self.insert_image(self.employee_signature_label))
        self.employee_clear_button.clicked.connect(lambda : self.clear_inputs(self.employee_page))
        self.employee_back_button.clicked.connect(self.show_main_page)
        self.stackedWidget.addWidget(self.employee_page)


# =============================================================
#                      BACK-END FUNCTIONS
# ============================================================= 
    def clear_inputs(self, page):
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
    
    def pixmap_to_bytes(self, pixmap):
        byte_array = QByteArray()
        buffer = QBuffer(byte_array)
        buffer.open(QBuffer.WriteOnly)
        pixmap.save(buffer, "PNG")
        return byte_array.data()

    def register_member(self):
        # Retrieve all inputs
        self.member_id = int(self.member_id_output_label.text())
        self.first_name = self.member_first_name_input.text()
        self.middle_name = self.member_middle_name_input.text()
        self.last_name = self.member_last_name_input.text()
        self.address = self.member_address_input.text()
        self.phone_number = self.member_phone_number_input.text()
        self.gender = self.member_gender_combo_box.currentText()
        self.membership_type = self.member_membership_type_combo_box.currentText()
        self.birth_date = self.member_birth_date.date()
        self.start_date = self.member_start_date.date()
        self.end_date = self.member_end_date.date()
        self.photo = self.member_image_label.pixmap()
        self.signature = self.member_signature_label.pixmap()

        if self.validate_member_inputs():
            # Convert photo and signature to bytes
            if self.photo:
                member_image_bytes = self.pixmap_to_bytes(self.photo)
            if self.signature:
                signature_image_bytes = self.pixmap_to_bytes(self.signature)


            cursor.execute(
                '''
                INSERT INTO Members 
                (member_id, first_name, middle_name, last_name, address, phone_number, birthdate, membership_type,
                gender, membership_start_date, membership_end_date, photo, signature) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''',
                (
                    self.member_id,
                    self.first_name,
                    self.middle_name,
                    self.last_name,
                    self.address,
                    self.phone_number,
                    self.birth_date.toString("yyyy-MM-dd"),
                    self.membership_type,
                    self.gender,
                    self.start_date.toString("yyyy-MM-dd"),
                    self.end_date.toString("yyyy-MM-dd"),
                    sqlite3.Binary(member_image_bytes),
                    sqlite3.Binary(signature_image_bytes)
                )
            )
            # Commit the transaction and close the connection
            connection.commit()
            QMessageBox.information(self, "Success", "Member registered successfully!")
        else:
            # Validation failed, do not proceed
            pass

    def update_end_date(self):
        membership_type = self.member_membership_type_combo_box.currentText()
        if membership_type == "Lifetime":
            self.member_end_date.setDate(QDate(9999, 12, 31))  # Set to a far future date
            self.member_end_date.setDisabled(True)  # Optionally disable the end date field
        else:
            self.member_end_date.setDisabled(False)
            self.member_end_date.setDate(QDate.currentDate())  # Reset to the current date


    def validate_member_inputs(self):

        # Check if all required fields are filled
        if not all([self.first_name, self.last_name, self.address, self.phone_number, self.gender, self.membership_type, self.photo, self.signature]):
            QMessageBox.warning(self, "Input Error", "All fields must be filled")
            return False

        # Validate that specific fields contain only letters
        if not all(re.match("^[A-Za-z ]+$", field) for field in [self.first_name, self.middle_name, self.last_name]):
            QMessageBox.warning(self, "Input Error", "First Name, Middle Name, and Last Name must contain only letters and spaces.")
            return False

        # Validate that the address is a string
        if not isinstance(self.address, str):
            QMessageBox.warning(self, "Input Error", "Address must be a string.")
            return False

        # Validate that the phone number is numeric
        if not self.phone_number.isdigit():
            QMessageBox.warning(self, "Input Error", "Phone Number must be numeric.")
            return False

        # Ensure birth date, start date, and end date are valid
        if not isinstance(self.birth_date, QDate) or not isinstance(self.start_date, QDate) or (self.membership_type != 'Lifetime' and not isinstance(self.end_date, QDate)):
            QMessageBox.warning(self, "Input Error", "Birth Date, Start Date, and End Date must be valid dates.")
            return False

        return True

    def update_search_results(self):
        search_text = self.attendance_member_name_input.text()
        self.search_results.clear()
        self.cursor = cursor
        if search_text:
            # Fetch members from database based on search text
            query = "SELECT first_name, last_name FROM Members WHERE first_name || ' ' || last_name LIKE ?"
            self.cursor.execute(query, ('%' + search_text + '%',))
            results = self.cursor.fetchall()
            # Add results to list widget
            for first_name, last_name in results:
                full_name = f"{first_name} {last_name}"
                self.search_results.addItem(full_name)
            self.search_results.show()  # Show list widget when there are results
        else:
            self.search_results.hide()  # Hide list widget if search text is empty


    def search_member(self, member_input):
        # Split the full name into first name and last name
        name_parts = member_input.rsplit(' ', 1)
        
        if len(name_parts) < 2:
            print("Please enter both first name and last name.")
            return
        
        first_name = name_parts[0].strip()
        last_name = name_parts[1].strip()

        # Debug: Print the first and last name
        print(f"Searching for: first_name = '{first_name}', last_name = '{last_name}'")

        # Execute the SQL query with placeholders for the first name and last name
        cursor.execute('''
            SELECT member_id, gender, phone_number, membership_type, membership_start_date, membership_end_date, photo
            FROM Members
            WHERE first_name = ? AND last_name = ?
        ''', (first_name, last_name))

        # Fetch the results
        results = cursor.fetchone()

        # Check if the results are found
        if results:
            membership_id, gender, phone_number, membership_type, start_date, end_date, photo= results
            print("Membership ID:", membership_id)
            print("Membership Type:", membership_type)
            print("Start Date:", start_date)
            print("End Date:", end_date)
            print("Image")

            pixmap = QPixmap()
            if photo:
                pixmap.loadFromData(photo, 'PNG')  # 'PNG' is the format of the image. Change if necessary.
                self.attendance_image_output_label.setPixmap(pixmap)
                self.attendance_image_output_label.show()
            else:
                print("No photo found.")

        else:
            print("No matching member found.")

        self.attendance_membership_id_output_label.setText(str(membership_id))
        self.attendance_gender_output_label.setText(gender)
        self.attendance_phone_number_output_label.setText(phone_number)
        self.attendance_membership_type_output_label.setText(membership_type)
        self.attendance_start_date_output_label.setText(start_date)
        self.attendance_end_date_output_label.setText(end_date)

        self.attendance_membership_id_output_label.show()
        self.attendance_gender_output_label.show()
        self.attendance_phone_number_output_label.show()
        self.attendance_membership_type_output_label.show()
        self.attendance_start_date_output_label.show()
        self.attendance_end_date_output_label.show()


    def handle_item_selection(self, item):
        selected_name = item.text()
        # Handle item selection (e.g., perform an action with the selected name)
        self.attendance_member_name_input.setText(selected_name)
        self.search_member(selected_name)

        self.search_results.hide()  # Hide list widget after selection

    def generate_employee_id(self):
        current_time = datetime.now()
        formatted_time = current_time.strftime('%m%d%y%H%M%S')
        prefix = '10'

        generated_id = f"{prefix}{formatted_time}"
        self.member_id_output_label.setText(generated_id)

    def back_button(self, page):
        self.clear_inputs(page)
        self.show_main_page()

    
    def register_attendance(self):

        today = self.attendance_date_input.date()
        member_id = int(self.attendance_membership_id_output_label.text())
        time = self.attendance_time_input.time()
        attendance = self.attendance_type_combo_box.currentText()

        print(type(member_id))
        print(type(time))
        print(type(attendance))
        print(type(today))
        # Check the last attendance record for the member
        cursor.execute("""
            SELECT attendance_id, entry_time, exit_time 
            FROM Attendance 
            WHERE member_id = ? AND date = ? 
            ORDER BY attendance_id DESC LIMIT 1
        """, (member_id, today.toString("yyyy-MM-dd")))
        
        last_record = cursor.fetchone()


        if attendance == "Entry":
            if last_record and not last_record[2]:  # If there's a record with entry_time but no exit_time
                print("Error: Member already has an entry record with no exit recorded.")
            else:
                cursor.execute("""
                    INSERT INTO Attendance (member_id, entry_time, date) 
                    VALUES (?, ?, ?)
                    """, (member_id, time.toString(), today.toString("yyyy-MM-dd")))
                print("Entry registered.")
        else:
            if last_record and not last_record[2]:  # If there's a record with entry_time but no exit_time
                cursor.execute("""  
                    UPDATE Attendance 
                    SET exit_time = ? 
                    WHERE attendance_id = ?
                    """, (time.toString(), last_record[0]))
                print("Exit registered.")
            else:
                print("Error: No entry record found or already exited.")

        connection.commit()
   

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Registration()
    window.show()
    sys.exit(app.exec_())
>>>>>>> 3b07da491695c9983258646c3e525513bc5f42ed
