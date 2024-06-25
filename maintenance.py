from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from assets import *
import sqlite3
import re
from functools import partial
from datetime import datetime
import uuid
import hashlib
from registration import *
# ==============================================================================
# ==============================================================================
#                           MAINTENANCE    CLASS
# ==============================================================================
# ==============================================================================
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
  
        self.open_main_page()           # MAINTENANCE MAIN PAGE
        self.open_manage_member_page()  # MAITENANCE MEMBER PAGE
        self.open_create_employee_page()
        self.open_create_equipment_page()
        self.open_create_member_page()
        self.open_create_user_page()
        self.verticalLayout.addWidget(self.stackedWidget)
        self.stackedWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(self)



    def show_main_page(self):
        self.stackedWidget.setCurrentIndex(0)

    def show_manage_member_page(self):
        self.update_table_widget()
        self.stackedWidget.setCurrentIndex(1)

    def show_manage_employee_page(self):
        self.generate_employee_id()
        self.stackedWidget.setCurrentIndex(2)

    def show_manage_equipment_page(self):
        self.generate_equipment_id()
        self.stackedWidget.setCurrentIndex(3)

    def show_manage_user_page(self):
        self.stackedWidget.setCurrentIndex(5)

    def show_create_member_page(self):
        self.generate_member_id()
        self.stackedWidget.setCurrentIndex(4)

    def open_main_page(self):
        self.main_page = QWidget()
        self.main_page.setObjectName("main_page")
        self.stackedWidget.addWidget(self.main_page)

        # ===========================================
        #             MAIN PAGE LABEL
        # ===========================================

        self.maintenance_text_label = createLabel(
            parent = self.main_page,
            name = "maintenance_text",
            geometry = QRect(360, 90, 230, 40),
            text = "Maintenance",
            font = font4,
            style = "font: bold"
        )


        # ===========================================
        #             MAIN PAGE BUTTONS
        # ===========================================
        self.switch_member_page_button = createButton(
            parent = self.main_page,
            name = "member_page_button",
            geometry = QRect(140, 190, 300, 100),
            text = "Manage Members",
            font = font3,
            style = "background-color: #004F9A; color: #FFFFFF"
        )

        self.switch_employee_page_button = createButton(
            parent = self.main_page,
            name = "employee_page_button",
            geometry = QRect(140, 340, 300, 100),
            text = "Manage Employees",
            font = font3,
            style = "background-color: #004F9A; color: #FFFFFF"
        )

        self.switch_user_page_button = createButton(
            parent = self.main_page,
            name = "user_page_button",
            geometry = QRect(140, 480, 300, 100),
            text = "Manage User Accounts",
            font = font3,
            style = "background-color: #004F9A; color: #FFFFFF"
        )

        self.switch_equipment_page_button = createButton(
            parent = self.main_page,
            name = "equipment_page_button",
            geometry = QRect(500, 190, 300, 100),
            text = "Manage Equipment",
            font = font3,
            style = "background-color: #004F9A; color: #FFFFFF"
        )

        self.switch_product_page_button = createButton(
            parent = self.main_page,
            name = "product_page_button",
            geometry = QRect(500, 340, 300, 100),
            text = "Manage Products",
            font = font3,
            style = "background-color: #004F9A; color: #FFFFFF"
        )

        self.switch_payment_page_button = createButton(
            parent = self.main_page,
            name = "payment_page_button",
            geometry = QRect(500, 480, 300, 100),
            text = "Manage Payments",
            font = font3,
            style = "background-color: #004F9A; color: #FFFFFF"
        )

        self.switch_backup_page_button = createButton(
            parent = self.main_page,
            name = "backup_page_button",
            geometry = QRect(330, 630, 300, 100),
            text = "Backup and Restore",
            font = font3,
            style = "background-color: #004F9A; color: #FFFFFF"
        )

        self.switch_user_page_button.clicked.connect(self.show_manage_user_page)
        self.switch_equipment_page_button.clicked.connect(self.show_manage_equipment_page)
        self.switch_member_page_button.clicked.connect(self.show_manage_member_page)
        self.switch_employee_page_button.clicked.connect(self.show_manage_employee_page)
    def open_manage_member_page(self):
        self.manage_member_page = QWidget()
        self.manage_member_page.setObjectName("manage_member_page")

        # ===========================================
        #            MANAGE MEMBER FRAMES
        # ===========================================

        # ===========================================
        #         MANAGE MEMBER PAGE LABELS
        # ===========================================
        self.manage_member_text_label = createLabel(
            parent=self.manage_member_page,
            name="manage_members_text",
            geometry=QRect(120, 40, 310, 40),
            text="Manage Members",
            font=font4,
            style="font: bold"
        )

        self.manage_search_text_label = createLabel(
            parent=self.manage_member_page,
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
            parent=self.manage_member_page,
            name="search_input",
            geometry=QRect(130, 140, 580, 40),
            font=font2,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        self.manage_search_input.setPlaceholderText("Member ID / Name")

        # ===========================================
        #         MANAGE MEMBER TABLE WIDGET
        # ===========================================
        self.member_table_widget = QTableWidget(self.manage_member_page)
        self.member_table_widget.setGeometry(QRect(10, 200, 930, 590))
        self.member_table_widget.setRowCount(0)
        self.member_table_widget.setColumnCount(6)  # Limited columns

        # Set the horizontal header labels
        self.member_table_widget.setHorizontalHeaderLabels(
            ["Member ID", "Full Name", "Membership Type", "Membership Start Date", "Membership End Date", "Actions"]
        )

        self.stackedWidget.addWidget(self.manage_member_page)

        self.member_table_widget.resizeColumnsToContents()
        self.member_table_widget.resizeRowsToContents()
        self.member_table_widget.horizontalHeader().setStretchLastSection(True)
        self.member_table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.update_table_widget()

        #         MANAGE MEMBER BUTTONS
        # ===========================================
        self.member_back_button = createButton(
            parent=self.manage_member_page,
            name="back_button",
            geometry=QRect(20, 40, 70, 50),
            text="Back",
            font=font2,
            style=""
        )

        self.member_add_button = createButton(
            parent=self.manage_member_page,
            name="add_button",
            geometry=QRect(680, 40, 250, 50),
            text="Add Member",
            font=font2,
            style="background-color: #28a745; color: #FFFFFF"
        )
        self.member_back_button.clicked.connect(lambda: self.back_main_button(self.manage_member_page))
        self.member_add_button.clicked.connect(self.show_create_member_page)

    def open_manage_employee_page(self): 
        self.manage_employee_page = QWidget()
        self.manage_employee_page.setObjectName("manage_employee_page")

        # ===========================================
        #            MANAGE MEMBER FRAMES
        # ===========================================

        # ===========================================
        #         MANAGE MEMBER PAGE LABELS
        # ===========================================
        self.manage_member_text_label = createLabel(
            parent=self.manage_employee_page,
            name="manage_members_text",
            geometry=QRect(120, 40, 310, 40),
            text="Manage Members",
            font=font4,
            style="font: bold"
        )

        self.manage_search_text_label = createLabel(
            parent=self.manage_employee_page,
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
            parent=self.manage_employee_page,
            name="search_input",
            geometry=QRect(130, 140, 580, 40),
            font=font2,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        self.manage_search_input.setPlaceholderText("Employee ID / Name")

        # ===========================================
        #         MANAGE MEMBER TABLE WIDGET
        # ===========================================
        self.employee_table_widget = QTableWidget(self.manage_employee_page)
        self.employee_table_widget.setGeometry(QRect(10, 200, 930, 590))
        self.employee_table_widget.setRowCount(0)
        self.employee_table_widget.setColumnCount(6)  # Limited columns

        # Set the horizontal header labels
        self.employee_table_widget.setHorizontalHeaderLabels(
            ["Employee ID", "Full Name", "Position", "Phone", "Hire Date", "Actions"]
        )

        self.stackedWidget.addWidget(self.manage_employee_page)

        self.employee_table_widget.resizeColumnsToContents()
        self.employee_table_widget.resizeRowsToContents()
        self.employee_table_widget.horizontalHeader().setStretchLastSection(True)
        self.employee_table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.update_employee_table_widget()
        self.employee_table_widget.itemChanged.connect(self.item_changed)
        #         MANAGE MEMBER BUTTONS
        # ===========================================
        self.member_back_button = createButton(
            parent=self.manage_employee_page,
            name="back_button",
            geometry=QRect(20, 40, 70, 50),
            text="Back",
            font=font2,
            style=""
        )

        self.member_add_button = createButton(
            parent=self.manage_employee_page,
            name="add_button",
            geometry=QRect(680, 40, 250, 50),
            text="Add Member",
            font=font2,
            style="background-color: #28a745; color: #FFFFFF"
        )

        self.member_add_button.clicked.connect(self.show_create_member_page)

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
        self.employee_hire_date_label = createLabel(
            parent = self.employee_page,
            name = "start_label",
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
        self.employee_position_input = createLineInput(
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
        self.employee_hire_date = createDate(
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


        self.employee_register_button.clicked.connect(self.register_employee)
        self.employee_insert_image_button.clicked.connect(lambda: self.insert_image(self.employee_image_label))
        self.employee_insert_signature_button.clicked.connect(lambda: self.insert_image(self.employee_signature_label))
        self.employee_clear_button.clicked.connect(lambda : self.clear_inputs(self.employee_page))
        self.employee_back_button.clicked.connect(self.show_main_page)
        self.stackedWidget.addWidget(self.employee_page)
        

# =============================================================
#                     CREATE EQUIPMENTS PAGE
# ============================================================= 
    def open_create_equipment_page(self):
        self.equipment_page = QWidget()
        self.equipment_page.setObjectName("main_page")
        self.stackedWidget.addWidget(self.equipment_page)
       
        # ===========================================
        #            EQUIPMENT PAGE LABELS
        # ===========================================

        self.equipment_text_label = createLabel(
            parent = self.equipment_page,
            name = "equipment_text",
            geometry = QRect(280, 50, 430, 40),
            text = "Register Equipment",
            font = font4,
            style = "font: bold"
        )

        self.equipment_id_label = createLabel(
            parent = self.equipment_page,
            name = "equipment_id",
            geometry = QRect(40, 150, 165, 40),
            text = "Equipment ID:",
            font = font1,
            style = ""
        )

        self.equipment_name_label = createLabel(
            parent = self.equipment_page,
            name = "equipment_name",
            geometry = QRect(40, 230, 210, 40),
            text = "Equipment Name",
            font = font1,
            style = ""
        )

        self.equipment_serial_number_label = createLabel(
            parent = self.equipment_page,
            name = "serial_number",
            geometry = QRect(40, 350, 170, 40),
            text = "Serial Number",
            font = font1,
            style = ""
        )

        self.equipment_category_label = createLabel(
            parent = self.equipment_page,
            name = "equipment_category",
            geometry = QRect(490, 350, 110, 40),
            text = "Category",
            font = font1,
            style = ""
        )

        self.equipment_status_label = createLabel(
            parent = self.equipment_page,
            name = "equipment_status",
            geometry = QRect(750, 350, 110, 40),
            text = "Status",
            font = font1,
            style = ""
        )

        self.equipment_purchase_date_label = createLabel(
            parent = self.equipment_page,
            name = "purchase_date",
            geometry = QRect(40, 470, 170, 40),
            text = "Purchase Date",
            font = font1,
            style = ""
        )

        self.equipment_warranty_date_label = createLabel(
            parent = self.equipment_page,
            name = "warranty_date",
            geometry = QRect(260, 470, 190, 40),
            text = "Warranty Expiry",
            font = font1,
            style = ""
        )

        self.equipment_price_label = createLabel(
            parent = self.equipment_page,
            name = "price",
            geometry = QRect(480, 470, 190, 40),
            text = "Equipment Price",
            font = font1,
            style = ""
        )

        self.equipment_manufacturer_label = createLabel(
            parent = self.equipment_page,
            name = "manufacturer",
            geometry = QRect(40, 590, 160, 40),
            text = "Manufacturer",
            font = font1,
            style = ""
        )

        self.equipment_location_label = createLabel(
            parent = self.equipment_page,
            name = "location",
            geometry = QRect(490, 590, 130, 40),
            text = "Location",
            font = font1,
            style = ""
        )


        self.equipment_id_output_label = createLabel(
            parent = self.equipment_page,
            name = "id_output",
            geometry = QRect(220, 150, 300, 40),
            text = "",
            font = font1,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # ===========================================
        #            EQUIPMENT PAGE INPUTS
        # ===========================================

        self.equipment_name_input = createLineInput(
            parent = self.equipment_page,
            name = "name_input",
            geometry = QRect(40, 280, 430, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.equipment_serial_number_input = createLineInput(
            parent = self.equipment_page,
            name = "serial_number_input ",
            geometry = QRect(40, 400, 430, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.equipment_price_input = createLineInput(
            parent = self.equipment_page,
            name = "price_input",
            geometry = QRect(480, 520, 250, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.equipment_manufacturer_input = createLineInput(
            parent = self.equipment_page,
            name = "manufacturer_input",
            geometry = QRect(40, 630, 430, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.equipment_location_input = createLineInput(
            parent = self.equipment_page,
            name = "location_input",
            geometry = QRect(490, 630, 430, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # ===========================================
        #            EQUIPMENT COMBO BOX
        # ===========================================


        self.equipment_category_combo_box = createComboBox(
            parent = self.equipment_page,
            name = "category",
            geometry = QRect(490, 400, 250, 40),
            font = font2,
            item = ["Cardio", "Strength", "Flexibility", "Functional Training", "Bodyweight", "Core and Stability", "Others"],
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.equipment_status_combo_box = createComboBox(
            parent = self.equipment_page,
            name = "status",
            geometry = QRect(750, 400, 180, 40),
            font = font2,
            item = ["Active", "Repair", "Retired"],
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # ===========================================
        #               EQUIPMENT DATE
        # ===========================================

        self.equipment_purchase_date = createDate(
            parent = self.equipment_page,
            name = "purchase_date",
            geometry = QRect(40, 520, 200, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.equipment_warranty_date = createDate(
            parent = self.equipment_page,
            name = "warranty_expiry",
            geometry = QRect(260, 520, 200, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"

        )

        # ===========================================
        #               EQUIPMENT BUTTONS
        # ===========================================

        self.equipment_back_button = createButton(
            parent = self.equipment_page,
            name = "back_button",
            geometry = QRect(40, 50, 70, 50),
            text = "Back",
            font = font3,
            style = "background-color: #004F9A"
        )

        self.equipment_clear_button = createButton(
            parent = self.equipment_page,
            name = "clear_button",
            geometry = QRect(510, 730, 170, 50),
            text = "Clear",
            font = font3,
            style = "background-color: #882400"
        )

        # REGISTER BUTTON
        self.equipment_register_button = createButton(
            parent = self.equipment_page,
            name = "register_button",
            geometry = QRect(690, 730, 250, 50),
            text = "Register Equipment",
            font = font3,
            style = "background-color: #006646"
        )

        self.equipment_back_button.clicked.connect(self.show_main_page)
        self.equipment_clear_button.clicked.connect(lambda: self.clear_inputs(self.equipment_page))
        self.equipment_register_button.clicked.connect(self.register_equipment)
        
    def open_create_user_page(self):
        self.user_page = QWidget()
        self.user_page.setObjectName("user_page")
        self.stackedWidget.addWidget(self.user_page)
        # ===========================================
        #             USER ACCOUNTS LABELS
        # ===========================================


        self.user_registration_label = createLabel(
            parent = self.user_page,
            name = "user_registration",
            geometry = QRect(270, 50, 430, 40),
            text = "User Registration",
            font = font4,
            style = "font: bold"
        )

        self.user_member_name_label = createLabel(
            parent = self.user_page,
            name = "member_name",
            geometry = QRect(40, 150, 190, 40),
            text = "Employee Name:",
            font = font1,
            style = ""
        )

        self.user_membership_id_label = createLabel(
            parent = self.user_page,
            name = "membership_id",
            geometry = QRect(40, 210, 190, 40),
            text = "Employee ID",
            font = font1,
            style = ""
        )

        self.user_membership_id_output_label = createLabel(
            parent = self.user_page,
            name = "output",
            geometry = QRect(40, 260, 330, 40),
            text = "",
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.user_gender_label = createLabel(
            parent = self.user_page,
            name = "gender",
            geometry = QRect(380, 210, 130, 40),
            text = "Gender",
            font = font1,
            style = ""
        )

        self.user_gender_output_label = createLabel(
            parent = self.user_page,
            name = "output",
            geometry = QRect(380, 260, 260, 40),
            text = "",
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.user_phone_number_label = createLabel(
            parent = self.user_page,
            name = "phone_number",
            geometry = QRect(40, 320, 180, 40),
            text = "Phone Number",
            font = font1,
            style = ""
        )

        self.user_phone_number_output_label = createLabel(
            parent = self.user_page,
            name = "output",
            geometry = QRect(40, 360, 330, 40),
            text = "",
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.user_hire_date_label = createLabel(
            parent = self.user_page,
            name = "hire_date",
            geometry = QRect(380, 320, 210, 40),
            text = "Hire Date",
            font = font1,
            style = ""
        )

        self.user_hire_date_output_label = createLabel(
            parent = self.user_page,
            name = "output",
            geometry = QRect(380, 360, 260, 40),
            text = "",
            font = font1,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.user_image_output_label = createLabel(
            parent = self.user_page,
            name = "output",
            geometry = QRect(680, 140, 250, 250),
            text = "",
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.username_label = createLabel(
            parent = self.user_page,
            name = "username",
            geometry = QRect(40, 480, 130, 40),
            text = "Username",
            font = font2,
            style = ""
        )

        self.user_password_label = createLabel(
            parent = self.user_page,
            name = "password",
            geometry = QRect(470, 480, 130, 40),
            text = "Password",
            font = font2,
            style = ""
        )

        self.user_re_password_label = createLabel(
            parent = self.user_page,
            name = "re_password",
            geometry = QRect(470, 580, 210, 40),
            text = "Re-type Password",
            font = font2,
            style = ""
        )

        self.user_role_label = createLabel(
            parent = self.user_page,
            name = "role",
            geometry = QRect(40, 580, 60, 40),
            text = "Role",
            font = font2,
            style = ""
        )
    


        # ===========================================
        #            USER ACCOUNT INPUTS
        # ===========================================

        self.user_member_name_input = createLineInput(
            parent = self.user_page,
            name = "member_name_input",
            geometry = QRect(240, 150, 410, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )
        self.user_member_name_input.setPlaceholderText("Search Employee Name")
        self.user_member_name_input.textChanged.connect(self.update_search_results)
        self.username_input = createLineInput(
            parent = self.user_page,
            name = "user_name_input",
            geometry = QRect(40 ,530, 410, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.password_input = createLineInput(
            parent = self.user_page,
            name = "password_input",
            geometry = QRect(470 ,530, 410, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"

        )

        self.re_password_input = createLineInput(
            parent = self.user_page,
            name = "re_password_input",
            geometry = QRect(470 ,630, 410, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"

        )

        # ===========================================
        #         USER ACCOUNT COMBO BOX
        # =========================================== 

        self.role_combo_box = createComboBox(
            parent = self.user_page,
            name = "role",
            geometry = QRect(40, 630, 190, 40),
            font = font2,
            item = ["Staff", "Admin"],
            style = "background-color: #F9F7FF; border: 1px solid black"

        )

        # ===========================================
        #         USER ACCOUNT LIST WIDGETS
        # =========================================== 

        self.search_results = QListWidget(self.user_page)
        self.search_results.hide()  # Hide initially
        self.search_results.setGeometry(240, 190, 410, 400)
        self.search_results.setFont(font2)
        self.search_results.itemClicked.connect(self.handle_item_selection)

        # ===========================================
        #           user_a PAGE BUTTONS
        # ===========================================

        # CLEAR BUTTON
        self.user_clear_button = createButton(
            parent = self.user_page,
            name = "clear_button",
            geometry = QRect(510, 730, 170, 50),
            text = "Clear",
            font = font3,
            style = "background-color: #882400"
        )

        # REGISTER BUTTON
        self.user_register_button = createButton(
            parent = self.user_page,
            name = "register_button",
            geometry = QRect(690, 730, 250, 50),
            text = "Register",
            font = font3,
            style = "background-color: #006646"
        )

        # BACK BUTTON
        self.user_back_button = createButton(
            parent = self.user_page,
            name = "back_button",
            geometry = QRect(40, 50, 70, 50),
            text = "Back",
            font = font3,
            style = "background-color: #004F9A"
        )

        self.user_register_button.clicked.connect(self.register_user)
        self.user_back_button.clicked.connect(lambda: self.back_main_button(self.user_page))
        self.user_clear_button.clicked.connect(lambda: self.clear_inputs(self.user_page))

    def open_create_member_page(self):
        self.add_member_page = QWidget()
        self.add_member_page.setObjectName("member_page")


        # ===========================================
        #             MEMBER PAGE LABELS
        # ===========================================

        # MEMBER REGISTRATION TEXT LABEL
        self.member_registration_text_label = createLabel(
            parent = self.add_member_page,
            name = "member_registration_text_label",
            geometry = QRect(310, 50, 380, 40),
            text = "Member Registration",
            font = font4,
            style = "font: bold"
        )

        # MEMBER ID LABEL
        self.member_id_label = createLabel(
            parent = self.add_member_page,
            name = "member_id_label",
            geometry = QRect(40, 150, 191, 40),
            text = "Membership ID:",
            font = font1,
            style = ""
        )

        # MEMBER ID OUTPUT LABEL
        self.member_id_output_label = createLabel(
            parent = self.add_member_page,
            name = "member_id_output",
            geometry = QRect(240, 150, 410, 40),
            text = "",
            font = font1,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # FIRST NAME LABEL
        self.member_first_name_label = createLabel(
            parent = self.add_member_page,
            name = "first_name_label",
            geometry = QRect(40, 210, 130, 40),
            text = "First Name",
            font = font1,
            style = ""
        )

        # MIDDLE NAME LABEL
        self.member_middle_name_label = createLabel(
            parent = self.add_member_page,
            name = "middle_name_label",
            geometry = QRect(380, 210, 160, 40),
            text = "Middle Name",
            font = font1,
            style = ""
        )

        # LAST NAME LABEL
        self.member_last_name_label = createLabel(
            parent = self.add_member_page,
            name = "last_name_label",
            geometry = QRect(40, 310, 130, 40),
            text = "Last Name",
            font = font1,
            style = ""
        )

        # GENDER LABEL
        self.member_gender_label = createLabel(
            parent = self.add_member_page,
            name = "gender_label",
            geometry = QRect(380, 310, 130, 40),
            text = "Gender",
            font = font1,
            style = ""
        )

        # ADDRESS LABEL
        self.member_address_label = createLabel(
            parent = self.add_member_page,
            name = "addresslabel",
            geometry = QRect(40, 420, 130, 40),
            text = "Address",
            font = font1,
            style = ""
        )

        # BIRTHDATE LABEL
        self.member_birthdate_label = createLabel(
            parent = self.add_member_page,
            name = "birthdate_label",
            geometry = QRect(380, 420, 130, 40),
            text = "Birthdate",
            font = font1,
            style = ""
        )

        # PHONE NUMBER LABEL
        self.member_phone_number_label = createLabel(
            parent = self.add_member_page,
            name = "phone_number_label",
            geometry = QRect(40, 530, 180, 40),
            text = "Phone Number",
            font = font1,
            style = ""
        )

        # MEMBERSHIP TYPE LABEL
        self.member_membership_type_label = createLabel(
            parent = self.add_member_page,
            name = "membership_type_label",
            geometry = QRect(380, 530, 210, 40),
            text = "Membership Type",
            font = font1,
            style = ""
        )

        # START DATE LABEL
        self.member_start_date_label = createLabel(
            parent = self.add_member_page,
            name = "start_date_label",
            geometry = QRect(40, 630, 180, 40),
            text = "Start Date",
            font = font1,
            style = ""
        )

        # END DATE LABEL
        self.member_end_date_label = createLabel(
            parent = self.add_member_page,
            name = "end_date_label",
            geometry = QRect(280, 630, 180, 40),
            text = "End Date",
            font = font1,
            style = ""
        )

        # IMAGE LABEL 
        self.member_image_label = createLabel(
            parent = self.add_member_page,
            name = "image_label",
            geometry = QRect(680, 140, 250, 250),
            text = "",
            font = font1,
            style = "background-color: #F9F7FF; border: 1.5px solid black"
        )
        
        # SIGNATURE LABEL
        self.member_signature_label = createLabel(
            parent = self.add_member_page,
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
            parent = self.add_member_page,
            name = "first_name_output",
            geometry = QRect(40, 260, 330, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # MIDDLE NAME INPUT
        self.member_middle_name_input = createLineInput(
            parent = self.add_member_page,
            name = "middle_name_output",
            geometry = QRect(380, 260, 280, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # LAST NAME INPUT
        self.member_last_name_input = createLineInput(
            parent = self.add_member_page,
            name = "last_name_output",
            geometry = QRect(40, 360, 330, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # ADDRESS INPUT
        self.member_address_input = createLineInput(
            parent = self.add_member_page,
            name = "address_output",
            geometry = QRect(40, 470, 330, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )
        # PHONE NUMBER INPUT
        self.member_phone_number_input = createLineInput(
            parent = self.add_member_page,
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
            parent = self.add_member_page,
            name = "gender_combo_box",
            geometry = QRect(380, 360, 140, 40),
            font = font2,
            item = ['Male', 'Female'],
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # MEMBERSHIP TYPE BOX
        self.member_membership_type_combo_box = createComboBox(
            parent = self.add_member_page,
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
            parent = self.add_member_page,
            name = "birthdate",
            geometry = QRect(380, 470, 200, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # START DATE
        self.member_start_date = createDate(
            parent = self.add_member_page,
            name = "member_start_date",
            geometry = QRect(40, 670, 200, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # END DATE
        self.member_end_date = createDate(
            parent = self.add_member_page,
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
            parent = self.add_member_page,
            name = "back_button",
            geometry = QRect(40, 50, 70, 50),
            text = "Back",
            font = font3,
            style = "background-color: #004F9A"
        )

        # INSERT IMAGE BUTTON
        self.member_insert_image_button = createButton(
            parent = self.add_member_page,
            name = "insert_image_button",
            geometry = QRect(680, 400, 250, 50),
            text = "Insert Image",
            font = font3,
            style = "background-color: #004F9A"
        )

        # INSERT SIGNATURE BUTTON
        self.member_insert_signature_button = createButton(
            parent = self.add_member_page,
            name = "insert_signature_button",
            geometry = QRect(680, 560, 250, 50),
            text = "Insert Signature",
            font = font3,
            style = "background-color: #004F9A"
        )

        # CLEAR BUTTON
        self.member_clear_button = createButton(
            parent = self.add_member_page,
            name = "clear_button",
            geometry = QRect(510, 730, 170, 50),
            text = "Clear",
            font = font3,
            style = "background-color: #882400"
        )

        # REGISTER BUTTON
        self.member_register_button = createButton(
            parent = self.add_member_page,
            name = "register_button",
            geometry = QRect(690, 730, 250, 50),
            text = "Register",
            font = font3,
            style = "background-color: #006646"
        )


        self.member_insert_image_button.clicked.connect(lambda: self.insert_image(self.member_image_label))
        self.member_insert_signature_button.clicked.connect(lambda: self.insert_image(self.member_signature_label))
        self.member_register_button.clicked.connect(self.register_member)
        self.member_clear_button.clicked.connect(lambda : self.clear_inputs(self.add_member_page))
        self.member_back_button.clicked.connect(lambda: self.back_button(self.add_member_page))
        self.stackedWidget.addWidget(self.add_member_page)
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


    def generate_employee_id(self):
        current_time = datetime.now()
        formatted_time = current_time.strftime('%m%d%y%H%M%S')
        prefix = '20'

        generated_id = f"{prefix}{formatted_time}"
        self.employee_id_output_label.setText(generated_id)
    def generate_equipment_id(self):
        current_time = datetime.now()
        formatted_time = current_time.strftime('%m%H%M%S')
        prefix = '80'

        generated_id = f"{prefix}{formatted_time}"
        self.equipment_id_output_label.setText(generated_id)

    def validate_equipment_inputs(self):

        # Check if all required fields are filled
        if not all([self.equipment_id, self.equipment_name, self.serial_number,
                    self.category, self.status, self.purchase_date, self.warranty_expiry,
                    self.price, self.manufacturer, self.location]):
            QMessageBox.warning(self, "Input Error", "All fields must be filled")
            return False

        # Validate that the phone number is numeric
        if not self.price.isdigit():
            QMessageBox.warning(self, "Input Error", "Price must be number.")
            return False

        # Ensure birth date, start date, and end date are valid
        if not isinstance(self.purchase_date, QDate) or not isinstance(self.warranty_expiry, QDate):
            QMessageBox.warning(self, "Input Error", "Purchase Date and Expiry Date must be valid dates.")
            return False

        return True
    def register_equipment(self):
        self.equipment_id = int(self.equipment_id_output_label.text())
        self.equipment_name = self.equipment_name_input.text()
        self.serial_number = self.equipment_serial_number_input.text()
        self.category = self.equipment_category_combo_box.currentText()
        self.status = self.equipment_status_combo_box.currentText()
        self.purchase_date = self.equipment_purchase_date.date()
        self.warranty_expiry = self.equipment_warranty_date.date()
        self.price = self.equipment_price_input.text()
        self.manufacturer = self.equipment_manufacturer_input.text()
        self.location = self.equipment_location_input.text()

        if self.validate_equipment_inputs():

            cursor.execute(
                """
                INSERT INTO Equipments
                (equipment_id, equipment_name, equipment_serial_number, equipment_category, equipment_status,
                equipment_purchase_date, equipment_warranty_expiry, equipment_price, equipment_manufacturer, equipment_location)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    self.equipment_id,
                    self.equipment_name,
                    self.serial_number,
                    self.category,
                    self.status,
                    self.purchase_date.toString("yyyy-MM-dd"),
                    self.warranty_expiry.toString("yyyy-MM-dd"),
                    int(self.price),
                    self.manufacturer,
                    self.location
                )
            )
        connection.commit()
        QMessageBox.information(self, "Success", "Member registered successfully!")

    def update_search_results(self):
        search_text = self.user_member_name_input.text()
        self.search_results.clear()
        if search_text:
            # Fetch members from database based on search text
            query = "SELECT first_name, last_name FROM Employees WHERE first_name || ' ' || last_name LIKE ?"
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
            SELECT employee_id, gender, phone, hire_date, photo
            FROM Employees
            WHERE first_name = ? AND last_name = ?
        ''', (first_name, last_name))

        # Fetch the results
        results = cursor.fetchone()

        # Check if the results are found
        if results:
            self.employee_id, gender, phone_number, hire_date, photo = results
            print("Membership ID:", self.employee_id)
            print("Membership Type:", gender)
            print("Start Date:", phone_number)
            print("End Date:", hire_date)
            print("Image")

            pixmap = QPixmap()
            if photo:
                pixmap.loadFromData(photo, 'PNG')  # 'PNG' is the format of the image. Change if necessary.
                self.user_image_output_label.setPixmap(pixmap)
                self.user_image_output_label.show()
            else:
                print("No photo found.")

        else:
            print("No matching member found.")

        self.user_membership_id_output_label.setText(str(self.employee_id))
        self.user_gender_output_label.setText(gender)
        self.user_phone_number_output_label.setText(phone_number)
        self.user_hire_date_output_label.setText(hire_date)

    def handle_item_selection(self, item):
        selected_name = item.text()
        # Handle item selection (e.g., perform an action with the selected name)
        self.user_member_name_input.setText(selected_name)
        self.search_member(selected_name)

        self.search_results.hide()  # Hide list widget after selection

    def register_user(self):

        username = self.username_input.text()
        password = self.password_input.text()
        retry_password = self.re_password_input.text()
        role = self.role_combo_box.currentText()
        if password == retry_password:
            password_bytes = password.encode()
            hashed_password = hashlib.sha256(password_bytes).hexdigest()
            cursor.execute(
                """
                INSERT INTO Users
                (employee_id, username, password_hash, role) VALUES
                (?, ?, ?, ?)
                """,
                (
                    self.employee_id,
                    username,
                    hashed_password,
                    role
                )
            )

            connection.commit()

            QMessageBox.information(self, "Registered", "Account Sucessfully Registered")

    def register_employee(self):
        self.employee_id = self.employee_id_output_label.text()
        self.first_name = self.employee_first_name_input.text()
        self.middle_name = self.employee_middle_name_input.text()
        self.last_name = self.employee_last_name_input.text()
        gender = self.employee_gender_combo_box.currentText()
        self.address = self.employee_address_input.text()
        self.birth_date = self.employee_birth_date.date()
        self.phone_number = self.employee_phone_number_input.text()
        self.position = self.employee_position_input.text()
        self.hire_date = self.employee_hire_date.date()
        self.photo = self.employee_image_label.pixmap()
        print(gender)
        member_image_bytes = self.pixmap_to_bytes(self.photo)
        
        cursor.execute(
            """
            INSERT INTO Employees
            (employee_id, first_name, middle_name, last_name, birthdate, gender, address, phone, hire_date, position, photo)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                int(self.employee_id),
                self.first_name,
                self.middle_name,
                self.last_name,
                gender,
                self.address,
                self.birth_date.toString("yyyy-MM-dd"),
                self.phone_number,
                self.position,
                self.hire_date.toString("yyyy-MM-dd"),
                sqlite3.Binary(member_image_bytes)
            )
        )

        connection.commit()
        QMessageBox.information(self, "Yippie", "Employee Registered")

    def generate_member_id(self):
        current_time = datetime.now()
        formatted_time = current_time.strftime('%m%d%y%H%M%S')
        prefix = '10'

        generated_id = f"{prefix}{formatted_time}"
        self.member_id_output_label.setText(generated_id)

    def back_button(self, page):
        self.clear_inputs(page)
        self.show_manage_member_page()

    def back_main_button(self, page):
        self.clear_inputs(page)
        self.show_main_page()

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
    
    def fetch_members_by_column(self):
        query = f"""SELECT member_id, 
                  first_name || ' ' || middle_name || ' ' || last_name AS member_name,
                  membership_type,
                  membership_start_date,
                  membership_end_date 
                  FROM Members"""
        cursor.execute(query)
        data = cursor.fetchall()
        return data

    def update_table_widget(self):
        data = self.fetch_members_by_column()
        self.member_table_widget.setRowCount(len(data))
        for row_index, row_data in enumerate(data):
            for col_index, col_data in enumerate(row_data):
                self.member_table_widget.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))

    def fetch_employees_by_column(self):
        query = f"""SELECT employee_id, 
                  first_name || ' ' || middle_name || ' ' || last_name AS member_name,
                  position,
                  phone,
                  hire_date
                  FROM Employees """
        cursor.execute(query)
        data = cursor.fetchall()
        return data

    def update_employee_table_widget(self):
        data = self.fetch_employees_by_column()
        self.employee_table_widget.setRowCount(len(data))
        for row_index, row_data in enumerate(data):
            for col_index, col_data in enumerate(row_data):
                self.employee_table_widget.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))

    def pixmap_to_bytes(self, pixmap):
        byte_array = QByteArray()
        buffer = QBuffer(byte_array)
        buffer.open(QBuffer.WriteOnly)
        pixmap.save(buffer, "PNG")
        return byte_array.data()

    def item_changed(self, item):
        row = item.row()
        column = item.column()
        new_value = item.text()
        column_name = self.employee_table_widget.horizontalHeaderItem(column).text()
        self.confirm_change(row, column_name, new_value)

    def update_database(self, row, column_name, new_value):
        try:
            member_id = self.employee_table_widget.item(row, 0).text()  # Assuming first column is ID
            query = f"UPDATE Employees SET {column_name} = ? WHERE employee_id = ?"
            cursor.execute(query, (new_value, member_id))
            connection.commit()
        except Exception as e:
            print(f"An error occurred: {e}")

    
    def confirm_change(self, row, column_name, new_value):
        member_id = self.employee_table_widget.item(row, 0).text()  # Assuming first column is ID
        old_value = self.get_old_value(row, column_name)

        if old_value == new_value:
            return  # No actual change

        confirmation = QMessageBox.question(
            self, "Confirm Change",
            f"Are you sure you want to change {column_name} from '{old_value}' to '{new_value}' for Member ID {member_id}?",
            QMessageBox.Yes | QMessageBox.No
        )       
        

        if confirmation == QMessageBox.Yes:
            self.update_database(row, column_name, new_value)
        else:
            self.update_employee_table_widget()  # Revert the changes in the table

    def get_old_value(self, row, column_name):
        employee_id = self.employee_table_widget.item(row, 0).text()  # Assuming first column is ID
        query = f"SELECT {column_name} FROM Employees WHERE employee_id = ?"
        cursor.execute(query, (employee_id),)
        old_value = cursor.fetchone()[0]
        connection.close()
        return str(old_value)
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Maintenance()
    window.show()
    sys.exit(app.exec_())
