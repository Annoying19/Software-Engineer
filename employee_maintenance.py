from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from  assets import *
import sqlite3
import re
from functools import partial
from datetime import datetime
import uuid
import hashlib
from registration import *

class Maintenance(QWidget):
    def __init__(self, parent=None):
        super(Maintenance, self).__init__(parent)
        self.setObjectName("Form")
        self.resize(950, 800)
        self.setStyleSheet("background-color: #FFFFFF")
        self.open_maintenance_interface()

    def open_maintenance_interface(self):

        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.stackedWidget = QStackedWidget(self)
        self.stackedWidget.setObjectName("stackedWidget")


        self.view_employee()
        self.create_employee()
        self.open_employee_page()
        self.verticalLayout.addWidget(self.stackedWidget)
        self.stackedWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(self)

    def open_employee_page(self):
        self.employee_page = QWidget()
        self.employee_page.setObjectName("employee_page")

        # ===========================================
        #         MANAGE MEMBER PAGE LABELS
        # ===========================================
        self.manage_employee_text_label = createLabel(
            parent=self.employee_page,
            name="manage_members_text",
            geometry=QRect(120, 40, 310, 40),
            text="Manage Employees",
            font=font4,
            style="font: bold"
        )

        self.manage_search_text_label = createLabel(
            parent=self.employee_page,
            name="manage_members_text",
            geometry=QRect(30, 140, 90, 40),
            text="Search:",
            font=font1,
            style=""
        )

        # ===========================================
        #      MANAGE MEMBER PAGE LINE INPUTS
        # ===========================================
        self.manage_search_input = createLineInput(
            parent=self.employee_page,
            name="search_input",
            geometry=QRect(130, 140, 580, 40),
            font=font2,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        self.manage_search_input.setPlaceholderText("Employee ID / Name")

        # ===========================================
        #         MANAGE MEMBER TABLE WIDGET
        # ===========================================
        self.table_widget = QTableWidget(self.employee_page)
        self.table_widget.setGeometry(QRect(10, 200, 930, 590))
        self.table_widget.setRowCount(0)
        self.table_widget.setColumnCount(6)  # Limited columns

        # Set the horizontal header labels
        self.table_widget.setHorizontalHeaderLabels(
            ["Employee ID", "Full Name", "Position", "Phone", "Hire Date", "Actions"]
        )

        self.stackedWidget.addWidget(self.employee_page)
        self.table_widget.resizeColumnsToContents()
        self.table_widget.resizeRowsToContents()
        self.table_widget.horizontalHeader().setStretchLastSection(True)
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


        #         MANAGE MEMBER BUTTONS
        # ===========================================
        self.member_back_button = createButton(
            parent=self.employee_page,
            name="back_button",
            geometry=QRect(20, 40, 70, 50),
            text="Back",
            font=font2,
            style=""
        )

        self.member_add_button = createButton(
            parent=self.employee_page,
            name="add_button",
            geometry=QRect(680, 40, 250, 50),
            text="Add Employee",
            font=font2,
            style="background-color: #28a745; color: #FFFFFF"
        )

    def create_employee(self):
        self.create_employee_page = QWidget()
        self.create_employee_page.setObjectName("create_employee_page")
        self.stackedWidget.addWidget(self.create_employee_page)
        # ===========================================
        #             EMPLOYEE PAGE LABELS
        # ===========================================

        # employee REGISTRATION TEXT LABEL
        self.employee_registration_text_label = createLabel(
            parent = self.create_employee_page,
            name = "employee_registration_text_label",
            geometry = QRect(305, 50, 385, 40),
            text = "Employee Registration",
            font = font4,
            style = "font: bold"
        )

        # employee ID LABEL
        self.employee_id_label = createLabel(
            parent = self.create_employee_page,
            name = "employee_id_label",
            geometry = QRect(40, 150, 191, 40),
            text = "Employee ID:",
            font = font1,
            style = ""
        )

        # employee ID OUTPUT LABEL
        self.employee_id_output_label = createLabel(
            parent = self.create_employee_page,
            name = "employee_id_output",
            geometry = QRect(240, 150, 410, 40),
            text = "",
            font = font1,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # FIRST NAME LABEL
        self.employee_first_name_label = createLabel(
            parent = self.create_employee_page,
            name = "first_name_label",
            geometry = QRect(40, 210, 130, 40),
            text = "First Name",
            font = font1,
            style = ""
        )

        # MIDDLE NAME LABEL
        self.employee_middle_name_label = createLabel(
            parent = self.create_employee_page,
            name = "middle_name_label",
            geometry = QRect(380, 210, 160, 40),
            text = "Middle Name",
            font = font1,
            style = ""
        )

        # LAST NAME LABEL
        self.employee_last_name_label = createLabel(
            parent = self.create_employee_page,
            name = "last_name_label",
            geometry = QRect(40, 310, 130, 40),
            text = "Last Name",
            font = font1,
            style = ""
        )

        # GENDER LABEL
        self.employee_gender_label = createLabel(
            parent = self.create_employee_page,
            name = "gender_label",
            geometry = QRect(380, 310, 130, 40),
            text = "Gender",
            font = font1,
            style = ""
        )

        # ADDRESS LABEL
        self.employee_address_label = createLabel(
            parent = self.create_employee_page,
            name = "addresslabel",
            geometry = QRect(40, 420, 130, 40),
            text = "Address",
            font = font1,
            style = ""
        )

        # BIRTHDATE LABEL
        self.employee_birthdate_label = createLabel(
            parent = self.create_employee_page,
            name = "birthdate_label",
            geometry = QRect(380, 420, 130, 40),
            text = "Birthdate",
            font = font1,
            style = ""
        )

        # PHONE NUMBER LABEL
        self.employee_phone_number_label = createLabel(
            parent = self.create_employee_page,
            name = "phone_number_label",
            geometry = QRect(40, 530, 180, 40),
            text = "Phone Number",
            font = font1,
            style = ""
        )

        # EMPLOYEE TYPE LABEL
        self.employee_position_label = createLabel(
            parent = self.create_employee_page,
            name = "position_label",
            geometry = QRect(380, 530, 210, 40),
            text = "Position",
            font = font1,
            style = ""
        )

        # START DATE LABEL
        self.employee_hire_date_label = createLabel(
            parent = self.create_employee_page,
            name = "start_label",
            geometry = QRect(40, 630, 180, 40),
            text = "Hire Date",
            font = font1,
            style = ""
        )

        # IMAGE LABEL 
        self.employee_image_label = createLabel(
            parent = self.create_employee_page,
            name = "image_label",
            geometry = QRect(680, 140, 250, 250),
            text = "",
            font = font1,
            style = "background-color: #F9F7FF; border: 1.5px solid black"
        )
        
        
        # ===========================================
        #             EMPLOYEE PAGE INPUTS
        # ===========================================

        # FIRST NAME INPUT
        self.employee_first_name_input = createLineInput(
            parent = self.create_employee_page,
            name = "first_name_output",
            geometry = QRect(40, 260, 330, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # MIDDLE NAME INPUT
        self.employee_middle_name_input = createLineInput(
            parent = self.create_employee_page,
            name = "middle_name_output",
            geometry = QRect(380, 260, 280, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # LAST NAME INPUT
        self.employee_last_name_input = createLineInput(
            parent = self.create_employee_page,
            name = "last_name_output",
            geometry = QRect(40, 360, 330, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # ADDRESS INPUT
        self.employee_address_input = createLineInput(
            parent = self.create_employee_page,
            name = "address_output",
            geometry = QRect(40, 470, 330, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )
        # PHONE NUMBER INPUT
        self.employee_phone_number_input = createLineInput(
            parent = self.create_employee_page,
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
            parent = self.create_employee_page,
            name = "gender_combo_box",
            geometry = QRect(380, 360, 140, 40),
            font = font2,
            item = ['Male', 'Female'],
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # EMPLOYEE TYPE BOX
        self.employee_position_input = createLineInput(
            parent = self.create_employee_page,
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
            parent = self.create_employee_page,
            name = "birthdate",
            geometry = QRect(380, 470, 200, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # START DATE
        self.employee_hire_date = createDate(
            parent = self.create_employee_page,
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
            parent = self.create_employee_page,
            name = "back_button",
            geometry = QRect(40, 50, 70, 50),
            text = "Back",
            font = font3,
            style = "background-color: #004F9A"
        )

        # INSERT IMAGE BUTTON
        self.employee_insert_image_button = createButton(
            parent = self.create_employee_page,
            name = "insert_image_button",
            geometry = QRect(680, 400, 250, 50),
            text = "Insert Image",
            font = font3,
            style = "background-color: #004F9A"
        )

        # CLEAR BUTTON
        self.employee_clear_button = createButton(
            parent = self.create_employee_page,
            name = "clear_button",
            geometry = QRect(510, 730, 170, 50),
            text = "Clear",
            font = font3,
            style = "background-color: #882400"
        )

        # REGISTER BUTTON
        self.employee_register_button = createButton(
            parent = self.create_employee_page,
            name = "register_button",
            geometry = QRect(690, 730, 250, 50),
            text = "Register",
            font = font3,
            style = "background-color: #006646"
        )
    
    def view_employee(self):
        self.view_employee_page = QWidget()
        self.view_employee_page.setObjectName("view_employee_page")
        self.stackedWidget.addWidget(self.view_employee_page)

        # ===========================================
        #             EMPLOYEE PAGE LABELS
        # ===========================================

        # EMPLOYEE REGISTRATION TEXT LABEL
        self.employee_registration_text_label = createLabel(
            parent=self.view_employee_page,
            name="employee_registration_text_label",
            geometry=QRect(305, 50, 385, 40),
            text="Employee Registration",
            font=font4,
            style="font: bold"
        )

        # EMPLOYEE ID LABEL
        self.employee_id_label = createLabel(
            parent=self.view_employee_page,
            name="employee_id_label",
            geometry=QRect(40, 150, 191, 40),
            text="Employee ID:",
            font=font1,
            style=""
        )

        # EMPLOYEE ID OUTPUT LABEL
        self.employee_id_output_label = createLabel(
            parent=self.view_employee_page,
            name="employee_id_output",
            geometry=QRect(240, 150, 410, 40),
            text="",
            font=font1,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        # FIRST NAME LABEL
        self.employee_first_name_label = createLabel(
            parent=self.view_employee_page,
            name="first_name_label",
            geometry=QRect(40, 210, 130, 40),
            text="First Name:",
            font=font1,
            style=""
        )

        # FIRST NAME OUTPUT LABEL
        self.employee_first_name_output_label = createLabel(
            parent=self.view_employee_page,
            name="first_name_output",
            geometry=QRect(40, 260, 330, 40),
            text="",
            font=font1,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        # MIDDLE NAME LABEL
        self.employee_middle_name_label = createLabel(
            parent=self.view_employee_page,
            name="middle_name_label",
            geometry=QRect(380, 210, 160, 40),
            text="Middle Name:",
            font=font1,
            style=""
        )

        # MIDDLE NAME OUTPUT LABEL
        self.employee_middle_name_output_label = createLabel(
            parent=self.view_employee_page,
            name="middle_name_output",
            geometry=QRect(380, 260, 280, 40),
            text="",
            font=font1,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        # LAST NAME LABEL
        self.employee_last_name_label = createLabel(
            parent=self.view_employee_page,
            name="last_name_label",
            geometry=QRect(40, 310, 130, 40),
            text="Last Name:",
            font=font1,
            style=""
        )

        # LAST NAME OUTPUT LABEL
        self.employee_last_name_output_label = createLabel(
            parent=self.view_employee_page,
            name="last_name_output",
            geometry=QRect(40, 360, 330, 40),
            text="",
            font=font1,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        # GENDER LABEL
        self.employee_gender_label = createLabel(
            parent=self.view_employee_page,
            name="gender_label",
            geometry=QRect(380, 310, 130, 40),
            text="Gender:",
            font=font1,
            style=""
        )

        # GENDER OUTPUT LABEL
        self.employee_gender_output_label = createLabel(
            parent=self.view_employee_page,
            name="gender_output",
            geometry=QRect(380, 360, 140, 40),
            text="",
            font=font1,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        # ADDRESS LABEL
        self.employee_address_label = createLabel(
            parent=self.view_employee_page,
            name="address_label",
            geometry=QRect(40, 420, 130, 40),
            text="Address:",
            font=font1,
            style=""
        )

        # ADDRESS OUTPUT LABEL
        self.employee_address_output_label = createLabel(
            parent=self.view_employee_page,
            name="address_output",
            geometry=QRect(40, 470, 330, 40),
            text="",
            font=font1,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        # BIRTHDATE LABEL
        self.employee_birthdate_label = createLabel(
            parent=self.view_employee_page,
            name="birthdate_label",
            geometry=QRect(380, 420, 130, 40),
            text="Birthdate:",
            font=font1,
            style=""
        )

        # BIRTHDATE OUTPUT LABEL
        self.employee_birthdate_output_label = createLabel(
            parent=self.view_employee_page,
            name="birthdate_output",
            geometry=QRect(380, 470, 200, 40),
            text="",
            font=font1,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        # PHONE NUMBER LABEL
        self.employee_phone_number_label = createLabel(
            parent=self.view_employee_page,
            name="phone_number_label",
            geometry=QRect(40, 530, 180, 40),
            text="Phone Number:",
            font=font1,
            style=""
        )

        # PHONE NUMBER OUTPUT LABEL
        self.employee_phone_number_output_label = createLabel(
            parent=self.view_employee_page,
            name="phone_number_output",
            geometry=QRect(40, 570, 330, 40),
            text="",
            font=font1,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        # EMPLOYEE POSITION LABEL
        self.employee_position_label = createLabel(
            parent=self.view_employee_page,
            name="position_label",
            geometry=QRect(380, 530, 210, 40),
            text="Position:",
            font=font1,
            style=""
        )

        # EMPLOYEE POSITION OUTPUT LABEL
        self.employee_position_output_label = createLabel(
            parent=self.view_employee_page,
            name="position_output",
            geometry=QRect(380, 570, 210, 40),
            text="",
            font=font1,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        # HIRE DATE LABEL
        self.employee_hire_date_label = createLabel(
            parent=self.view_employee_page,
            name="hire_date_label",
            geometry=QRect(40, 630, 180, 40),
            text="Hire Date:",
            font=font1,
            style=""
        )

        # HIRE DATE OUTPUT LABEL
        self.employee_hire_date_output_label = createLabel(
            parent=self.view_employee_page,
            name="hire_date_output",
            geometry=QRect(40, 670, 200, 40),
            text="",
            font=font1,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        # IMAGE LABEL 
        self.employee_image_label = createLabel(
            parent=self.view_employee_page,
            name="image_label",
            geometry=QRect(680, 140, 250, 250),
            text="",
            font=font1,
            style="background-color: #F9F7FF; border: 1.5px solid black"
        )

        # ===========================================
        #              EMPLOYEE PAGE BUTTONS
        # ===========================================

        # BACK BUTTON
        self.employee_back_button = createButton(
            parent=self.view_employee_page,
            name="back_button",
            geometry=QRect(40, 50, 70, 50),
            text="Back",
            font=font3,
            style="background-color: #004F9A"
        )

        # EDIT BUTTON
        self.employee_register_button = createButton(
            parent=self.view_employee_page,
            name="register_button",
            geometry=QRect(690, 730, 250, 50),
            text="Edit",
            font=font3,
            style="background-color: #006646; color: #FFFFFF"
        )


    def edit_employee(self):
        self.edit_employee_page = QWidget()
        self.edit_employee_page.setObjectName("edit_employee_page")
        self.stackedWidget.addWidget(self.edit_employee_page)
        # ===========================================
        #             EMPLOYEE PAGE LABELS
        # ===========================================

        # employee REGISTRATION TEXT LABEL
        self.employee_registration_text_label = createLabel(
            parent = self.edit_employee_page,
            name = "employee_registration_text_label",
            geometry = QRect(305, 50, 385, 40),
            text = "Employee Registration",
            font = font4,
            style = "font: bold"
        )

        # employee ID LABEL
        self.employee_id_label = createLabel(
            parent = self.edit_employee_page,
            name = "employee_id_label",
            geometry = QRect(40, 150, 191, 40),
            text = "Employee ID:",
            font = font1,
            style = ""
        )

        # employee ID OUTPUT LABEL
        self.employee_id_output_label = createLabel(
            parent = self.edit_employee_page,
            name = "employee_id_output",
            geometry = QRect(240, 150, 410, 40),
            text = "",
            font = font1,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # FIRST NAME LABEL
        self.employee_first_name_label = createLabel(
            parent = self.edit_employee_page,
            name = "first_name_label",
            geometry = QRect(40, 210, 130, 40),
            text = "First Name",
            font = font1,
            style = ""
        )

        # MIDDLE NAME LABEL
        self.employee_middle_name_label = createLabel(
            parent = self.edit_employee_page,
            name = "middle_name_label",
            geometry = QRect(380, 210, 160, 40),
            text = "Middle Name",
            font = font1,
            style = ""
        )

        # LAST NAME LABEL
        self.employee_last_name_label = createLabel(
            parent = self.edit_employee_page,
            name = "last_name_label",
            geometry = QRect(40, 310, 130, 40),
            text = "Last Name",
            font = font1,
            style = ""
        )

        # GENDER LABEL
        self.employee_gender_label = createLabel(
            parent = self.edit_employee_page,
            name = "gender_label",
            geometry = QRect(380, 310, 130, 40),
            text = "Gender",
            font = font1,
            style = ""
        )

        # ADDRESS LABEL
        self.employee_address_label = createLabel(
            parent = self.edit_employee_page,
            name = "addresslabel",
            geometry = QRect(40, 420, 130, 40),
            text = "Address",
            font = font1,
            style = ""
        )

        # BIRTHDATE LABEL
        self.employee_birthdate_label = createLabel(
            parent = self.edit_employee_page,
            name = "birthdate_label",
            geometry = QRect(380, 420, 130, 40),
            text = "Birthdate",
            font = font1,
            style = ""
        )

        # PHONE NUMBER LABEL
        self.employee_phone_number_label = createLabel(
            parent = self.edit_employee_page,
            name = "phone_number_label",
            geometry = QRect(40, 530, 180, 40),
            text = "Phone Number",
            font = font1,
            style = ""
        )

        # EMPLOYEE TYPE LABEL
        self.employee_position_label = createLabel(
            parent = self.edit_employee_page,
            name = "position_label",
            geometry = QRect(380, 530, 210, 40),
            text = "Position",
            font = font1,
            style = ""
        )

        # START DATE LABEL
        self.employee_hire_date_label = createLabel(
            parent = self.edit_employee_page,
            name = "start_label",
            geometry = QRect(40, 630, 180, 40),
            text = "Hire Date",
            font = font1,
            style = ""
        )

        # IMAGE LABEL 
        self.employee_image_label = createLabel(
            parent = self.edit_employee_page,
            name = "image_label",
            geometry = QRect(680, 140, 250, 250),
            text = "",
            font = font1,
            style = "background-color: #F9F7FF; border: 1.5px solid black"
        )
        
        
        # ===========================================
        #             EMPLOYEE PAGE INPUTS
        # ===========================================

        # FIRST NAME INPUT
        self.employee_first_name_input = createLineInput(
            parent = self.edit_employee_page,
            name = "first_name_output",
            geometry = QRect(40, 260, 330, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # MIDDLE NAME INPUT
        self.employee_middle_name_input = createLineInput(
            parent = self.edit_employee_page,
            name = "middle_name_output",
            geometry = QRect(380, 260, 280, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # LAST NAME INPUT
        self.employee_last_name_input = createLineInput(
            parent = self.edit_employee_page,
            name = "last_name_output",
            geometry = QRect(40, 360, 330, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # ADDRESS INPUT
        self.employee_address_input = createLineInput(
            parent = self.edit_employee_page,
            name = "address_output",
            geometry = QRect(40, 470, 330, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )
        # PHONE NUMBER INPUT
        self.employee_phone_number_input = createLineInput(
            parent = self.edit_employee_page,
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
            parent = self.edit_employee_page,
            name = "gender_combo_box",
            geometry = QRect(380, 360, 140, 40),
            font = font2,
            item = ['Male', 'Female'],
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # EMPLOYEE TYPE BOX
        self.employee_position_input = createLineInput(
            parent = self.edit_employee_page,
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
            parent = self.edit_employee_page,
            name = "birthdate",
            geometry = QRect(380, 470, 200, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # START DATE
        self.employee_hire_date = createDate(
            parent = self.edit_employee_page,
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
            parent = self.edit_employee_page,
            name = "back_button",
            geometry = QRect(40, 50, 70, 50),
            text = "Back",
            font = font3,
            style = "background-color: #004F9A"
        )

        # INSERT IMAGE BUTTON
        self.employee_insert_image_button = createButton(
            parent = self.edit_employee_page,
            name = "insert_image_button",
            geometry = QRect(680, 400, 250, 50),
            text = "Insert Image",
            font = font3,
            style = "background-color: #004F9A"
        )

        # CLEAR BUTTON
        self.employee_clear_button = createButton(
            parent = self.edit_employee_page,
            name = "clear_button",
            geometry = QRect(510, 730, 170, 50),
            text = "Clear",
            font = font3,
            style = "background-color: #882400"
        )

        # REGISTER BUTTON
        self.employee_register_button = createButton(
            parent = self.edit_employee_page,
            name = "register_button",
            geometry = QRect(690, 730, 250, 50),
            text = "Register",
            font = font3,
            style = "background-color: #006646"
        )
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Maintenance()
    window.show()
    sys.exit(app.exec_())