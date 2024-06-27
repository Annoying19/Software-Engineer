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

class EmployeeMaintenance(QWidget):
    def __init__(self, parent=None):
        super(EmployeeMaintenance, self).__init__(parent)
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

        self.open_employee_page()
        self.create_employee()
        self.edit_employee()
        self.view_employee()
        self.verticalLayout.addWidget(self.stackedWidget)
        self.stackedWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(self)

    def show_employee_page(self):
        self.update_table_widget()
        self.stackedWidget.setCurrentIndex(0)

    def show_create_employee(self):
        clear_inputs(self.create_employee_page)
        generate_id("Employees", self.create_employee_id_output_label)
        self.stackedWidget.setCurrentIndex(1)

    def show_edit_employee(self):
        self.stackedWidget.setCurrentIndex(2)

    def show_view_employee(self):
        self.stackedWidget.setCurrentIndex(3)


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
        self.manage_employee_search_input = createLineInput(
            parent=self.employee_page,
            name="search_input",
            geometry=QRect(130, 140, 580, 40),
            font=font2,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        self.manage_employee_search_input.setPlaceholderText("Employee ID / Name")

        # ===========================================
        #         MANAGE MEMBER TABLE WIDGET
        # ===========================================
        self.employee_table_wigdet = QTableWidget(self.employee_page)
        self.employee_table_wigdet.setGeometry(QRect(10, 200, 930, 590))
        self.employee_table_wigdet.setRowCount(0)
        self.employee_table_wigdet.setColumnCount(6)  # Limited columns
    
        self.manage_employee_search_input.textChanged.connect(lambda: self.search_employees(self.employee_table_wigdet, self.manage_employee_search_input))
        # Set the horizontal header labels
        self.employee_table_wigdet.setHorizontalHeaderLabels(
            ["Employee ID", "Full Name", "Position", "Phone", "Hire Date", "Actions"]
        )

        self.stackedWidget.addWidget(self.employee_page)
        self.employee_table_wigdet.resizeColumnsToContents()
        self.employee_table_wigdet.resizeRowsToContents()
        self.employee_table_wigdet.horizontalHeader().setStretchLastSection(True)
        self.employee_table_wigdet.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.update_table_widget()

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

        self.member_add_button.clicked.connect(self.show_create_employee)

    def create_employee(self):
        self.create_employee_page = QWidget()
        self.create_employee_page.setObjectName("create_employee_page")
        self.stackedWidget.addWidget(self.create_employee_page)
        # ===========================================
        #             EMPLOYEE PAGE LABELS
        # ===========================================

        # employee REGISTRATION TEXT LABEL
        self.create_employee_registration_text_label = createLabel(
            parent = self.create_employee_page,
            name = "employee_registration_text_label",
            geometry = QRect(305, 50, 385, 40),
            text = "Employee Registration",
            font = font4,
            style = "font: bold"
        )

        # employee ID LABEL
        self.create_employee_id_label = createLabel(
            parent = self.create_employee_page,
            name = "employee_id_label",
            geometry = QRect(40, 150, 191, 40),
            text = "Employee ID:",
            font = font1,
            style = ""
        )

        # employee ID OUTPUT LABEL
        self.create_employee_id_output_label = createLabel(
            parent = self.create_employee_page,
            name = "employee_id_output",
            geometry = QRect(240, 150, 410, 40),
            text = "",
            font = font1,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # FIRST NAME LABEL
        self.create_employee_first_name_label = createLabel(
            parent = self.create_employee_page,
            name = "first_name_label",
            geometry = QRect(40, 210, 130, 40),
            text = "First Name",
            font = font1,
            style = ""
        )

        # MIDDLE NAME LABEL
        self.create_employee_middle_name_label = createLabel(
            parent = self.create_employee_page,
            name = "middle_name_label",
            geometry = QRect(380, 210, 160, 40),
            text = "Middle Name",
            font = font1,
            style = ""
        )

        # LAST NAME LABEL
        self.create_employee_last_name_label = createLabel(
            parent = self.create_employee_page,
            name = "last_name_label",
            geometry = QRect(40, 310, 130, 40),
            text = "Last Name",
            font = font1,
            style = ""
        )

        # GENDER LABEL
        self.create_employee_gender_label = createLabel(
            parent = self.create_employee_page,
            name = "gender_label",
            geometry = QRect(380, 310, 130, 40),
            text = "Gender",
            font = font1,
            style = ""
        )

        # ADDRESS LABEL
        self.create_employee_address_label = createLabel(
            parent = self.create_employee_page,
            name = "addresslabel",
            geometry = QRect(40, 420, 130, 40),
            text = "Address",
            font = font1,
            style = ""
        )

        # BIRTHDATE LABEL
        self.create_employee_birthdate_label = createLabel(
            parent = self.create_employee_page,
            name = "birthdate_label",
            geometry = QRect(380, 420, 130, 40),
            text = "Birthdate",
            font = font1,
            style = ""
        )

        # PHONE NUMBER LABEL
        self.create_employee_phone_number_label = createLabel(
            parent = self.create_employee_page,
            name = "phone_number_label",
            geometry = QRect(40, 530, 180, 40),
            text = "Phone Number",
            font = font1,
            style = ""
        )

        # EMPLOYEE TYPE LABEL
        self.create_employee_position_label = createLabel(
            parent = self.create_employee_page,
            name = "position_label",
            geometry = QRect(380, 530, 210, 40),
            text = "Position",
            font = font1,
            style = ""
        )

        # START DATE LABEL
        self.create_employee_hire_date_label = createLabel(
            parent = self.create_employee_page,
            name = "start_label",
            geometry = QRect(40, 630, 180, 40),
            text = "Hire Date",
            font = font1,
            style = ""
        )

        # IMAGE LABEL 
        self.create_employee_image_label = createLabel(
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
        self.create_employee_first_name_input = createLineInput(
            parent = self.create_employee_page,
            name = "first_name_output",
            geometry = QRect(40, 260, 330, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # MIDDLE NAME INPUT
        self.create_employee_middle_name_input = createLineInput(
            parent = self.create_employee_page,
            name = "middle_name_output",
            geometry = QRect(380, 260, 280, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # LAST NAME INPUT
        self.create_employee_last_name_input = createLineInput(
            parent = self.create_employee_page,
            name = "last_name_output",
            geometry = QRect(40, 360, 330, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # ADDRESS INPUT
        self.create_employee_address_input = createLineInput(
            parent = self.create_employee_page,
            name = "address_output",
            geometry = QRect(40, 470, 330, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )
        # PHONE NUMBER INPUT
        self.create_employee_phone_number_input = createLineInput(
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
        self.create_employee_gender_combo_box = createComboBox(
            parent = self.create_employee_page,
            name = "gender_combo_box",
            geometry = QRect(380, 360, 140, 40),
            font = font2,
            item = ['Male', 'Female'],
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # EMPLOYEE TYPE BOX
        self.create_employee_position_input = createLineInput(
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
        self.create_employee_birth_date = createDate(
            parent = self.create_employee_page,
            name = "birthdate",
            geometry = QRect(380, 470, 200, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # START DATE
        self.create_employee_hire_date = createDate(
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
        self.create_employee_back_button = createButton(
            parent = self.create_employee_page,
            name = "back_button",
            geometry = QRect(40, 50, 70, 50),
            text = "Back",
            font = font3,
            style = "background-color: #004F9A"
        )

        # INSERT IMAGE BUTTON
        self.create_employee_insert_image_button = createButton(
            parent = self.create_employee_page,
            name = "insert_image_button",
            geometry = QRect(680, 400, 250, 50),
            text = "Insert Image",
            font = font3,
            style = "background-color: #004F9A"
        )

        # CLEAR BUTTON
        self.create_employee_clear_button = createButton(
            parent = self.create_employee_page,
            name = "clear_button",
            geometry = QRect(510, 730, 170, 50),
            text = "Clear",
            font = font3,
            style = "background-color: #882400"
        )

        # REGISTER BUTTON
        self.create_employee_register_button = createButton(
            parent = self.create_employee_page,
            name = "register_button",
            geometry = QRect(690, 730, 250, 50),
            text = "Register",
            font = font3,
            style = "background-color: #006646"
        )
        self.create_employee_clear_button.clicked.connect(lambda: clear_inputs(self.create_employee_page))
        self.create_employee_insert_image_button.clicked.connect(lambda: insert_image(self.create_employee_image_label))
        self.create_employee_back_button.clicked.connect(self.show_employee_page)
        self.create_employee_register_button.clicked.connect(lambda: register_entity("Employees", self.assigned_input("Employees")))
    
    def assigned_input(self, entity):
        if entity == "Employees":
            image = pixmap_to_bytes(self.create_employee_image_label.pixmap())
            INPUTS = {
                "employee_id": self.create_employee_id_output_label.text(),
                "first_name": self.create_employee_first_name_input.text(),
                "middle_name": self.create_employee_middle_name_input.text(),
                "last_name": self.create_employee_last_name_input.text(),
                "birthdate":self.create_employee_birth_date.date(),
                "address":self.create_employee_address_input.text(),
                "phone": self.create_employee_phone_number_input.text,
                "hire_date": self.create_employee_hire_date.date(),
                "position": self.create_employee_position_input.text(),
                "photo": sqlite3.Binary(image),

            }

        return INPUTS
        
    def view_employee(self):
        self.view_employee_page = QWidget()
        self.view_employee_page.setObjectName("view_employee_page")
        self.stackedWidget.addWidget(self.view_employee_page)

        # ===========================================
        #             EMPLOYEE PAGE LABELS
        # ===========================================

        # EMPLOYEE REGISTRATION TEXT LABEL
        self.view_employee_registration_text_label = createLabel(
            parent=self.view_employee_page,
            name="employee_registration_text_label",
            geometry=QRect(305, 50, 385, 40),
            text="Employee Registration",
            font=font4,
            style="font: bold"
        )

        # EMPLOYEE ID LABEL
        self.view_employee_id_label = createLabel(
            parent=self.view_employee_page,
            name="employee_id_label",
            geometry=QRect(40, 150, 191, 40),
            text="Employee ID:",
            font=font1,
            style=""
        )

        # EMPLOYEE ID OUTPUT LABEL
        self.view_employee_id_output_label = createLabel(
            parent=self.view_employee_page,
            name="employee_id_output",
            geometry=QRect(240, 150, 410, 40),
            text="",
            font=font1,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        # FIRST NAME LABEL
        self.view_employee_first_name_label = createLabel(
            parent=self.view_employee_page,
            name="first_name_label",
            geometry=QRect(40, 210, 130, 40),
            text="First Name:",
            font=font1,
            style=""
        )

        # FIRST NAME OUTPUT LABEL
        self.view_employee_first_name_output_label = createLabel(
            parent=self.view_employee_page,
            name="first_name_output",
            geometry=QRect(40, 260, 330, 40),
            text="",
            font=font1,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        # MIDDLE NAME LABEL
        self.view_employee_middle_name_label = createLabel(
            parent=self.view_employee_page,
            name="middle_name_label",
            geometry=QRect(380, 210, 160, 40),
            text="Middle Name:",
            font=font1,
            style=""
        )

        # MIDDLE NAME OUTPUT LABEL
        self.view_employee_middle_name_output_label = createLabel(
            parent=self.view_employee_page,
            name="middle_name_output",
            geometry=QRect(380, 260, 280, 40),
            text="",
            font=font1,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        # LAST NAME LABEL
        self.view_employee_last_name_label = createLabel(
            parent=self.view_employee_page,
            name="last_name_label",
            geometry=QRect(40, 310, 130, 40),
            text="Last Name:",
            font=font1,
            style=""
        )

        # LAST NAME OUTPUT LABEL
        self.view_employee_last_name_output_label = createLabel(
            parent=self.view_employee_page,
            name="last_name_output",
            geometry=QRect(40, 360, 330, 40),
            text="",
            font=font1,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        # GENDER LABEL
        self.view_employee_gender_label = createLabel(
            parent=self.view_employee_page,
            name="gender_label",
            geometry=QRect(380, 310, 130, 40),
            text="Gender:",
            font=font1,
            style=""
        )

        # GENDER OUTPUT LABEL
        self.view_employee_gender_output_label = createLabel(
            parent=self.view_employee_page,
            name="gender_output",
            geometry=QRect(380, 360, 140, 40),
            text="",
            font=font1,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        # ADDRESS LABEL
        self.view_employee_address_label = createLabel(
            parent=self.view_employee_page,
            name="address_label",
            geometry=QRect(40, 420, 130, 40),
            text="Address:",
            font=font1,
            style=""
        )

        # ADDRESS OUTPUT LABEL
        self.view_employee_address_output_label = createLabel(
            parent=self.view_employee_page,
            name="address_output",
            geometry=QRect(40, 470, 330, 40),
            text="",
            font=font1,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        # BIRTHDATE LABEL
        self.view_employee_birthdate_label = createLabel(
            parent=self.view_employee_page,
            name="birthdate_label",
            geometry=QRect(380, 420, 130, 40),
            text="Birthdate:",
            font=font1,
            style=""
        )

        # BIRTHDATE OUTPUT LABEL
        self.view_employee_birthdate_output_label = createLabel(
            parent=self.view_employee_page,
            name="birthdate_output",
            geometry=QRect(380, 470, 200, 40),
            text="",
            font=font1,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        # PHONE NUMBER LABEL
        self.view_employee_phone_number_label = createLabel(
            parent=self.view_employee_page,
            name="phone_number_label",
            geometry=QRect(40, 530, 180, 40),
            text="Phone Number:",
            font=font1,
            style=""
        )

        # PHONE NUMBER OUTPUT LABEL
        self.view_employee_phone_number_output_label = createLabel(
            parent=self.view_employee_page,
            name="phone_number_output",
            geometry=QRect(40, 570, 330, 40),
            text="",
            font=font1,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        # EMPLOYEE POSITION LABEL
        self.view_employee_position_label = createLabel(
            parent=self.view_employee_page,
            name="position_label",
            geometry=QRect(380, 530, 210, 40),
            text="Position:",
            font=font1,
            style=""
        )

        # EMPLOYEE POSITION OUTPUT LABEL
        self.view_employee_position_output_label = createLabel(
            parent=self.view_employee_page,
            name="position_output",
            geometry=QRect(380, 570, 210, 40),
            text="",
            font=font1,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        # HIRE DATE LABEL
        self.view_employee_hire_date_label = createLabel(
            parent=self.view_employee_page,
            name="hire_date_label",
            geometry=QRect(40, 630, 180, 40),
            text="Hire Date:",
            font=font1,
            style=""
        )

        # HIRE DATE OUTPUT LABEL
        self.view_employee_hire_date_output_label = createLabel(
            parent=self.view_employee_page,
            name="hire_date_output",
            geometry=QRect(40, 670, 200, 40),
            text="",
            font=font1,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        # IMAGE LABEL 
        self.view_employee_image_label = createLabel(
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
        self.view_employee_back_button = createButton(
            parent=self.view_employee_page,
            name="back_button",
            geometry=QRect(40, 50, 70, 50),
            text="Back",
            font=font3,
            style="background-color: #004F9A"
        )

        # EDIT BUTTON
        self.view_employee_register_button = createButton(
            parent=self.view_employee_page,
            name="register_button",
            geometry=QRect(690, 730, 250, 50),
            text="Edit",
            font=font3,
            style="background-color: #006646; color: #FFFFFF"
        )

        self.view_employee_back_button.clicked.connect(self.show_employee_page)
        self.view_employee_register_button.clicked.connect(self.edit_employee_button)


    def edit_employee(self):
        self.edit_employee_page = QWidget()
        self.edit_employee_page.setObjectName("edit_employee_page")
        self.stackedWidget.addWidget(self.edit_employee_page)
        # ===========================================
        #             EMPLOYEE PAGE LABELS
        # ===========================================

        # employee REGISTRATION TEXT LABEL
        self.edit_employee_registration_text_label = createLabel(
            parent = self.edit_employee_page,
            name = "employee_registration_text_label",
            geometry = QRect(305, 50, 385, 40),
            text = "Employee Registration",
            font = font4,
            style = "font: bold"
        )

        # employee ID LABEL
        self.edit_employee_id_label = createLabel(
            parent = self.edit_employee_page,
            name = "employee_id_label",
            geometry = QRect(40, 150, 191, 40),
            text = "Employee ID:",
            font = font1,
            style = ""
        )

        # employee ID OUTPUT LABEL
        self.edit_employee_id_output_label = createLabel(
            parent = self.edit_employee_page,
            name = "employee_id_output",
            geometry = QRect(240, 150, 410, 40),
            text = "",
            font = font1,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # FIRST NAME LABEL
        self.edit_employee_first_name_label = createLabel(
            parent = self.edit_employee_page,
            name = "first_name_label",
            geometry = QRect(40, 210, 130, 40),
            text = "First Name",
            font = font1,
            style = ""
        )

        # MIDDLE NAME LABEL
        self.edit_employee_middle_name_label = createLabel(
            parent = self.edit_employee_page,
            name = "middle_name_label",
            geometry = QRect(380, 210, 160, 40),
            text = "Middle Name",
            font = font1,
            style = ""
        )

        # LAST NAME LABEL
        self.edit_employee_last_name_label = createLabel(
            parent = self.edit_employee_page,
            name = "last_name_label",
            geometry = QRect(40, 310, 130, 40),
            text = "Last Name",
            font = font1,
            style = ""
        )

        # GENDER LABEL
        self.edit_employee_gender_label = createLabel(
            parent = self.edit_employee_page,
            name = "gender_label",
            geometry = QRect(380, 310, 130, 40),
            text = "Gender",
            font = font1,
            style = ""
        )

        # ADDRESS LABEL
        self.edit_employee_address_label = createLabel(
            parent = self.edit_employee_page,
            name = "addresslabel",
            geometry = QRect(40, 420, 130, 40),
            text = "Address",
            font = font1,
            style = ""
        )

        # BIRTHDATE LABEL
        self.edit_employee_birthdate_label = createLabel(
            parent = self.edit_employee_page,
            name = "birthdate_label",
            geometry = QRect(380, 420, 130, 40),
            text = "Birthdate",
            font = font1,
            style = ""
        )

        # PHONE NUMBER LABEL
        self.edit_employee_phone_number_label = createLabel(
            parent = self.edit_employee_page,
            name = "phone_number_label",
            geometry = QRect(40, 530, 180, 40),
            text = "Phone Number",
            font = font1,
            style = ""
        )

        # EMPLOYEE TYPE LABEL
        self.edit_employee_position_label = createLabel(
            parent = self.edit_employee_page,
            name = "position_label",
            geometry = QRect(380, 530, 210, 40),
            text = "Position",
            font = font1,
            style = ""
        )

        # START DATE LABEL
        self.edit_employee_hire_date_label = createLabel(
            parent = self.edit_employee_page,
            name = "start_label",
            geometry = QRect(40, 630, 180, 40),
            text = "Hire Date",
            font = font1,
            style = ""
        )

        # IMAGE LABEL 
        self.edit_employee_image_label = createLabel(
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
        self.edit_employee_first_name_input = createLineInput(
            parent = self.edit_employee_page,
            name = "first_name_output",
            geometry = QRect(40, 260, 330, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # MIDDLE NAME INPUT
        self.edit_employee_middle_name_input = createLineInput(
            parent = self.edit_employee_page,
            name = "middle_name_output",
            geometry = QRect(380, 260, 280, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # LAST NAME INPUT
        self.edit_employee_last_name_input = createLineInput(
            parent = self.edit_employee_page,
            name = "last_name_output",
            geometry = QRect(40, 360, 330, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # ADDRESS INPUT
        self.edit_employee_address_input = createLineInput(
            parent = self.edit_employee_page,
            name = "address_output",
            geometry = QRect(40, 470, 330, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )
        # PHONE NUMBER INPUT
        self.edit_employee_phone_number_input = createLineInput(
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
        self.edit_employee_gender_combo_box = createComboBox(
            parent = self.edit_employee_page,
            name = "gender_combo_box",
            geometry = QRect(380, 360, 140, 40),
            font = font2,
            item = ['Male', 'Female'],
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # EMPLOYEE TYPE BOX
        self.edit_employee_position_input = createLineInput(
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
        self.edit_employee_birth_date = createDate(
            parent = self.edit_employee_page,
            name = "birthdate",
            geometry = QRect(380, 470, 200, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # START DATE
        self.edit_employee_hire_date = createDate(
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
        self.edit_employee_back_button = createButton(
            parent = self.edit_employee_page,
            name = "back_button",
            geometry = QRect(40, 50, 70, 50),
            text = "Back",
            font = font3,
            style = "background-color: #004F9A"
        )

        # INSERT IMAGE BUTTON
        self.edit_employee_insert_image_button = createButton(
            parent = self.edit_employee_page,
            name = "insert_image_button",
            geometry = QRect(680, 400, 250, 50),
            text = "Insert Image",
            font = font3,
            style = "background-color: #004F9A"
        )

        # CLEAR BUTTON
        self.edit_employee_cancel_button = createButton(
            parent = self.edit_employee_page,
            name = "clear_button",
            geometry = QRect(510, 730, 170, 50),
            text = "Cancel",
            font = font3,
            style = "background-color: #882400"
        )

        # REGISTER BUTTON
        self.edit_employee_register_button = createButton(
            parent = self.edit_employee_page,
            name = "register_button",
            geometry = QRect(690, 730, 250, 50),
            text = "Change",
            font = font3,
            style = "background-color: #006646"

        )
        self.edit_employee_back_button.clicked.connect(self.show_view_employee)
        self.edit_employee_cancel_button.clicked.connect(self.show_view_employee)
        self.edit_employee_insert_image_button.clicked.connect(lambda: insert_image(self.edit_employee_image_label))
        self.edit_employee_register_button.clicked.connect(self.update_employee)

    def update_table_widget(self):
        data = self.fetch_employee_by_column()
        self.employee_table_wigdet.setRowCount(len(data))
        for row_index, row_data in enumerate(data):
            for col_index, col_data in enumerate(row_data):
                self.employee_table_wigdet.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))
            
        for self.row in range(self.employee_table_wigdet.rowCount()):
            view_button = QPushButton("View")
            view_button.clicked.connect(partial(self.show_view_employee_temp, self.row))
            self.employee_table_wigdet.setCellWidget(self.row, 5, view_button)

    def show_view_employee_temp(self, row):
        employee_id = self.employee_table_wigdet.item(row, 0).text()

        cursor.execute(
            """
            SELECT * 
            FROM Employees
            WHERE employee_id = ?
            """,
            (employee_id,)
        )

        results = cursor.fetchone()

        employee_id, first_name, middle_name, last_name, birth_date, gender, address, phone, hire_date, position, photo = results

        pixmap = QPixmap()
        self.view_employee_id_output_label.setText(str(employee_id))
        self.view_employee_first_name_output_label.setText(first_name)
        self.view_employee_middle_name_output_label.setText(middle_name)
        self.view_employee_last_name_output_label.setText(last_name)
        self.view_employee_birthdate_output_label.setText(birth_date)
        self.view_employee_gender_output_label.setText(gender)
        self.view_employee_address_output_label.setText(address)
        self.view_employee_phone_number_output_label.setText(phone)
        self.view_employee_hire_date_output_label.setText(hire_date)
        self.view_employee_position_output_label.setText(position)
        pixmap.loadFromData(photo)
        self.view_employee_image_label.setPixmap(pixmap)

        self.show_view_employee()

    def fetch_employee_by_column(self):
        query = f"""SELECT employee_id, 
                  first_name || ' ' || last_name,
                  position,
                  phone,
                  hire_date
                  FROM Employees """
        cursor.execute(query)
        data = cursor.fetchall()
        return data
    
    def edit_employee_button(self):
        employee_id =  self.view_employee_id_output_label.text()
        first_name = self.view_employee_first_name_output_label.text()
        middle_name = self.view_employee_middle_name_output_label.text()
        last_name = self.view_employee_last_name_output_label.text()
        birthdate = self.view_employee_birthdate_output_label.text()
        gender = self.view_employee_gender_output_label.text()
        address =self.view_employee_address_output_label.text()
        phone = self.view_employee_phone_number_output_label.text()
        hire_date = self.view_employee_hire_date_output_label.text()
        position = self.view_employee_position_output_label.text()
        photo = self.view_employee_image_label.pixmap()

        birthdate = datetime.strptime(birthdate, '%Y-%m-%d')
        hire_date = datetime.strptime(hire_date, '%Y-%m-%d')

        self.edit_employee_id_output_label.setText(employee_id)
        self.edit_employee_first_name_input.setText(first_name)
        self.edit_employee_middle_name_input.setText(middle_name)
        self.edit_employee_last_name_input.setText(last_name)
        self.edit_employee_birth_date.setDate(birthdate)
        self.edit_employee_gender_combo_box.setCurrentText(gender)
        self.edit_employee_address_input.setText(address)
        self.edit_employee_phone_number_input.setText(phone)
        self.edit_employee_hire_date.setDate(hire_date)
        self.edit_employee_position_input.setText(position)

        self.edit_employee_image_label.setPixmap(photo)


        self.update_table_widget()
        self.show_edit_employee()



    def update_employee(self):
        employee_id =  self.edit_employee_id_output_label.text()
        first_name = self.edit_employee_first_name_input.text()
        middle_name = self.edit_employee_middle_name_input.text()
        last_name = self.edit_employee_last_name_input.text()
        birthdate = self.edit_employee_birth_date.date()
        gender = self.edit_employee_gender_combo_box.currentText()
        address =self.edit_employee_address_input.text()
        phone = self.edit_employee_phone_number_input.text()
        hire_date = self.edit_employee_hire_date.date()
        position = self.edit_employee_position_input.text()
        photo = self.edit_employee_image_label.pixmap()
        member_image_bytes = pixmap_to_bytes(photo)

        cursor.execute(
            """
            UPDATE Employees
            SET employee_id = ?, first_name = ?, middle_name = ?, last_name = ?, birthdate = ?, gender = ?, address = ?, phone = ?, hire_date = ?, position =? , photo = ?
            """,
            (
                employee_id,
                first_name,
                middle_name,
                last_name,
                birthdate.toString("yyyy-MM-dd"),
                gender,
                address,
                phone,
                hire_date.toString("yyyy-MM-dd"),
                position,
                sqlite3.Binary(member_image_bytes)
            )
        )
        connection.commit()
        QMessageBox.information(None, "Yippie", "Employee Updated")
        self.show_employee_page()
    def search_employees(self, table_widget, input_text):
        search_term = input_text.text()
        query = """
            SELECT employee_id,
                    first_name || ' ' || last_name AS full_name,
                    position,
                    phone,
                    hire_date
            FROM Employees
            WHERE employee_id LIKE ? OR first_name LIKE ? OR last_name LIKE ?;
        """
        try:
            cursor.execute(query, (f'%{search_term}%', f'%{search_term}%', f'%{search_term}%'))
            results = cursor.fetchall()

            table_widget.setRowCount(len(results))
            for row_idx, row_data in enumerate(results):
                for col_idx, col_data in enumerate(row_data):
                    table_widget.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))
                view_button = QPushButton("View")
                view_button.clicked.connect(partial(self.show_view_employee_temp, row_idx))
                table_widget.setCellWidget(row_idx, len(row_data), view_button)

            self.add_employee_view_button(table_widget)  # Call the function to add view buttons

        except Exception as e:
            print(f"Error executing query for Employees: {e}")

    def add_employee_view_button(self, table_widget):
        for row_idx in range(table_widget.rowCount()):
            view_button = QPushButton("View")
            view_button.clicked.connect(partial(self.show_view_employee_temp, row_idx))
            table_widget.setCellWidget(row_idx, 5, view_button)

            


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = EmployeeMaintenance()
    window.show()
    sys.exit(app.exec_())