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


        self.open_member_page()
        self.add_member() 
        self.edit_member()
        self.view_member()


        self.verticalLayout.addWidget(self.stackedWidget)
        self.stackedWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(self)



    def show_member_page(self):
        self.update_table_widget()
        self.stackedWidget.setCurrentIndex(0)
    
    def show_add_member(self):
        self.generate_member_id()
        self.stackedWidget.setCurrentIndex(1)
    
    def show_edit_member(self):
        self.update_table_widget()
        self.stackedWidget.setCurrentIndex(2)

    def show_view_member(self):
        self.update_table_widget()
        self.stackedWidget.setCurrentIndex(3)

        


    def open_member_page(self):
        self.manage_member_page = QWidget()
        self.manage_member_page.setObjectName("manage_member_page")

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

        self.member_add_button.clicked.connect(self.show_add_member)
    
    def add_member(self):
        self.add_member_page = QWidget()
        self.add_member_page.setObjectName("member_page")
        self.stackedWidget.addWidget(self.add_member_page)

        # ===========================================
        #             MEMBER PAGE LABELS
        # ===========================================

        # MEMBER REGISTRATION TEXT LABEL
        self.add_member_registration_text_label = createLabel(
            parent = self.add_member_page,
            name = "member_registration_text_label",
            geometry = QRect(310, 50, 380, 40),
            text = "Member Registration",
            font = font4,
            style = "font: bold"
        )

        # MEMBER ID LABEL
        self.add_member_id_label = createLabel(
            parent = self.add_member_page,
            name = "member_id_label",
            geometry = QRect(40, 150, 191, 40),
            text = "Membership ID:",
            font = font1,
            style = ""
        )

        # MEMBER ID OUTPUT LABEL
        self.add_member_id_output_label = createLabel(
            parent = self.add_member_page,
            name = "member_id_output",
            geometry = QRect(240, 150, 410, 40),
            text = "",
            font = font1,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # FIRST NAME LABEL
        self.add_member_first_name_label = createLabel(
            parent = self.add_member_page,
            name = "first_name_label",
            geometry = QRect(40, 210, 130, 40),
            text = "First Name",
            font = font1,
            style = ""
        )

        # MIDDLE NAME LABEL
        self.add_member_middle_name_label = createLabel(
            parent = self.add_member_page,
            name = "middle_name_label",
            geometry = QRect(380, 210, 160, 40),
            text = "Middle Name",
            font = font1,
            style = ""
        )

        # LAST NAME LABEL
        self.add_member_last_name_label = createLabel(
            parent = self.add_member_page,
            name = "last_name_label",
            geometry = QRect(40, 310, 130, 40),
            text = "Last Name",
            font = font1,
            style = ""
        )

        # GENDER LABEL
        self.add_member_gender_label = createLabel(
            parent = self.add_member_page,
            name = "gender_label",
            geometry = QRect(380, 310, 130, 40),
            text = "Gender",
            font = font1,
            style = ""
        )

        # ADDRESS LABEL
        self.add_member_address_label = createLabel(
            parent = self.add_member_page,
            name = "addresslabel",
            geometry = QRect(40, 420, 130, 40),
            text = "Address",
            font = font1,
            style = ""
        )

        # BIRTHDATE LABEL
        self.add_member_birthdate_label = createLabel(
            parent = self.add_member_page,
            name = "birthdate_label",
            geometry = QRect(380, 420, 130, 40),
            text = "Birthdate",
            font = font1,
            style = ""
        )

        # PHONE NUMBER LABEL
        self.add_member_phone_number_label = createLabel(
            parent = self.add_member_page,
            name = "phone_number_label",
            geometry = QRect(40, 530, 180, 40),
            text = "Phone Number",
            font = font1,
            style = ""
        )

        # MEMBERSHIP TYPE LABEL
        self.add_member_membership_type_label = createLabel(
            parent = self.add_member_page,
            name = "membership_type_label",
            geometry = QRect(380, 530, 210, 40),
            text = "Membership Type",
            font = font1,
            style = ""
        )

        # START DATE LABEL
        self.add_member_start_date_label = createLabel(
            parent = self.add_member_page,
            name = "start_date_label",
            geometry = QRect(40, 630, 180, 40),
            text = "Start Date",
            font = font1,
            style = ""
        )

        # END DATE LABEL
        self.add_member_end_date_label = createLabel(
            parent = self.add_member_page,
            name = "end_date_label",
            geometry = QRect(280, 630, 180, 40),
            text = "End Date",
            font = font1,
            style = ""
        )

        # IMAGE LABEL 
        self.add_member_image_label = createLabel(
            parent = self.add_member_page,
            name = "image_label",
            geometry = QRect(680, 140, 250, 250),
            text = "",
            font = font1,
            style = "background-color: #F9F7FF; border: 1.5px solid black"
        )
        
        # SIGNATURE LABEL
        self.add_member_signature_label = createLabel(
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
        self.add_member_first_name_input = createLineInput(
            parent = self.add_member_page,
            name = "first_name_output",
            geometry = QRect(40, 260, 330, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # MIDDLE NAME INPUT
        self.add_member_middle_name_input = createLineInput(
            parent = self.add_member_page,
            name = "middle_name_output",
            geometry = QRect(380, 260, 280, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # LAST NAME INPUT
        self.add_member_last_name_input = createLineInput(
            parent = self.add_member_page,
            name = "last_name_output",
            geometry = QRect(40, 360, 330, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # ADDRESS INPUT
        self.add_member_address_input = createLineInput(
            parent = self.add_member_page,
            name = "address_output",
            geometry = QRect(40, 470, 330, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )
        # PHONE NUMBER INPUT
        self.add_member_phone_number_input = createLineInput(
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
        self.add_member_gender_combo_box = createComboBox(
            parent = self.add_member_page,
            name = "gender_combo_box",
            geometry = QRect(380, 360, 140, 40),
            font = font2,
            item = ['Male', 'Female'],
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # MEMBERSHIP TYPE BOX
        self.add_member_membership_type_combo_box = createComboBox(
            parent = self.add_member_page,
            name = "gender_combo_box",
            geometry = QRect(380, 570, 210, 40),
            font = font2,
            item = ['Standard', 'Lifetime'],
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.add_member_membership_type_combo_box.currentIndexChanged.connect(self.update_end_date)

        # ===========================================
        #              MEMBER PAGE DATE
        # ===========================================

        # BIRTH DATE
        self.add_member_birth_date = createDate(
            parent = self.add_member_page,
            name = "birthdate",
            geometry = QRect(380, 470, 200, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # START DATE
        self.add_member_start_date = createDate(
            parent = self.add_member_page,
            name = "member_start_date",
            geometry = QRect(40, 670, 200, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # END DATE
        self.add_member_end_date = createDate(
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
        self.add_member_back_button = createButton(
            parent = self.add_member_page,
            name = "back_button",
            geometry = QRect(40, 50, 70, 50),
            text = "Back",
            font = font3,
            style = "background-color: #004F9A"
        )

        # INSERT IMAGE BUTTON
        self.add_member_insert_image_button = createButton(
            parent = self.add_member_page,
            name = "insert_image_button",
            geometry = QRect(680, 400, 250, 50),
            text = "Insert Image",
            font = font3,
            style = "background-color: #004F9A"
        )

        # INSERT SIGNATURE BUTTON
        self.add_member_insert_signature_button = createButton(
            parent = self.add_member_page,
            name = "insert_signature_button",
            geometry = QRect(680, 560, 250, 50),
            text = "Insert Signature",
            font = font3,
            style = "background-color: #004F9A"
        )

        # CLEAR BUTTON
        self.add_member_clear_button = createButton(
            parent = self.add_member_page,
            name = "clear_button",
            geometry = QRect(510, 730, 170, 50),
            text = "Clear",
            font = font3,
            style = "background-color: #882400"
        )

        # REGISTER BUTTON
        self.add_member_register_button = createButton(
            parent = self.add_member_page,
            name = "register_button",
            geometry = QRect(690, 730, 250, 50),
            text = "Register",
            font = font3,
            style = "background-color: #006646"
        )
        self.add_member_register_button.clicked.connect(self.register_member)
        self.add_member_insert_image_button.clicked.connect(lambda: self.insert_image(self.add_member_image_label))
        self.add_member_insert_signature_button.clicked.connect(lambda: self.insert_image(self.add_member_signature_label))

    def edit_member(self):
        self.edit_member = QWidget()
        self.edit_member.setObjectName("member_page")
        self.stackedWidget.addWidget(self.edit_member)

        # ===========================================
        #             MEMBER PAGE LABELS
        # ===========================================

        # MEMBER REGISTRATION TEXT LABEL
        self.edit_member_registration_text_label = createLabel(
            parent = self.edit_member,
            name = "member_registration_text_label",
            geometry = QRect(310, 50, 380, 40),
            text = "Edit Member Details",
            font = font4,
            style = "font: bold"
        )

        # MEMBER ID LABEL
        self.edit_member_id_label = createLabel(
            parent = self.edit_member,
            name = "member_id_label",
            geometry = QRect(40, 150, 191, 40),
            text = "Membership ID:",
            font = font1,
            style = ""
        )

        # MEMBER ID OUTPUT LABEL
        self.edit_member_id_output_label = createLabel(
            parent = self.edit_member,
            name = "member_id_output",
            geometry = QRect(240, 150, 410, 40),
            text = "",
            font = font1,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # FIRST NAME LABEL
        self.edit_member_first_name_label = createLabel(
            parent = self.edit_member,
            name = "first_name_label",
            geometry = QRect(40, 210, 130, 40),
            text = "First Name",
            font = font1,
            style = ""
        )

        # MIDDLE NAME LABEL
        self.edit_member_middle_name_label = createLabel(
            parent = self.edit_member,
            name = "middle_name_label",
            geometry = QRect(380, 210, 160, 40),
            text = "Middle Name",
            font = font1,
            style = ""
        )

        # LAST NAME LABEL
        self.edit_member_last_name_label = createLabel(
            parent = self.edit_member,
            name = "last_name_label",
            geometry = QRect(40, 310, 130, 40),
            text = "Last Name",
            font = font1,
            style = ""
        )

        # GENDER LABEL
        self.edit_member_gender_label = createLabel(
            parent = self.edit_member,
            name = "gender_label",
            geometry = QRect(380, 310, 130, 40),
            text = "Gender",
            font = font1,
            style = ""
        )

        # ADDRESS LABEL
        self.edit_member_address_label = createLabel(
            parent = self.edit_member,
            name = "addresslabel",
            geometry = QRect(40, 420, 130, 40),
            text = "Address",
            font = font1,
            style = ""
        )

        # BIRTHDATE LABEL
        self.edit_member_birthdate_label = createLabel(
            parent = self.edit_member,
            name = "birthdate_label",
            geometry = QRect(380, 420, 130, 40),
            text = "Birthdate",
            font = font1,
            style = ""
        )

        # PHONE NUMBER LABEL
        self.edit_member_phone_number_label = createLabel(
            parent = self.edit_member,
            name = "phone_number_label",
            geometry = QRect(40, 530, 180, 40),
            text = "Phone Number",
            font = font1,
            style = ""
        )

        # MEMBERSHIP TYPE LABEL
        self.edit_member_membership_type_label = createLabel(
            parent = self.edit_member,
            name = "membership_type_label",
            geometry = QRect(380, 530, 210, 40),
            text = "Membership Type",
            font = font1,
            style = ""
        )

        # START DATE LABEL
        self.edit_member_start_date_label = createLabel(
            parent = self.edit_member,
            name = "start_date_label",
            geometry = QRect(40, 630, 180, 40),
            text = "Start Date",
            font = font1,
            style = ""
        )

        # END DATE LABEL
        self.edit_member_end_date_label = createLabel(
            parent = self.edit_member,
            name = "end_date_label",
            geometry = QRect(280, 630, 180, 40),
            text = "End Date",
            font = font1,
            style = ""
        )

        # IMAGE LABEL 
        self.edit_member_image_label = createLabel(
            parent = self.edit_member,
            name = "image_label",
            geometry = QRect(680, 140, 250, 250),
            text = "",
            font = font1,
            style = "background-color: #F9F7FF; border: 1.5px solid black"
        )
        
        # SIGNATURE LABEL
        self.edit_member_signature_label = createLabel(
            parent = self.edit_member,
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
        self.edit_member_first_name_input = createLineInput(
            parent = self.edit_member,
            name = "first_name_output",
            geometry = QRect(40, 260, 330, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # MIDDLE NAME INPUT
        self.edit_member_middle_name_input = createLineInput(
            parent = self.edit_member,
            name = "middle_name_output",
            geometry = QRect(380, 260, 280, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # LAST NAME INPUT
        self.edit_member_last_name_input = createLineInput(
            parent = self.edit_member,
            name = "last_name_output",
            geometry = QRect(40, 360, 330, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # ADDRESS INPUT
        self.edit_member_address_input = createLineInput(
            parent = self.edit_member,
            name = "address_output",
            geometry = QRect(40, 470, 330, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )
        # PHONE NUMBER INPUT
        self.edit_member_phone_number_input = createLineInput(
            parent = self.edit_member,
            name = "phone_number_output",
            geometry = QRect(40, 570, 330, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # ===========================================
        #            MEMBER PAGE COMBO BOX
        # ===========================================

        # GENDER BOX
        self.edit_member_gender_combo_box = createComboBox(
            parent = self.edit_member,
            name = "gender_combo_box",
            geometry = QRect(380, 360, 140, 40),
            font = font2,
            item = ['Male', 'Female'],
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # MEMBERSHIP TYPE BOX
        self.edit_member_membership_type_combo_box = createComboBox(
            parent = self.edit_member,
            name = "gender_combo_box",
            geometry = QRect(380, 570, 210, 40),
            font = font2,
            item = ['Standard', 'Lifetime'],
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.edit_member_membership_type_combo_box.currentIndexChanged.connect(self.update_end_date)

        # ===========================================
        #              MEMBER PAGE DATE
        # ===========================================

        # BIRTH DATE
        self.edit_member_birth_date = createDate(
            parent = self.edit_member,
            name = "birthdate",
            geometry = QRect(380, 470, 200, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # START DATE
        self.edit_member_start_date = createDate(
            parent = self.edit_member,
            name = "member_start_date",
            geometry = QRect(40, 670, 200, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # END DATE
        self.edit_member_end_date = createDate(
            parent = self.edit_member,
            name = "member_end_date",
            geometry = QRect(280, 670, 200, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # ===========================================
        #              MEMBER PAGE BUTTONS
        # ===========================================
    
        # BACK BUTTON
        self.edit_member_back_button = createButton(
            parent = self.edit_member,
            name = "back_button",
            geometry = QRect(40, 50, 70, 50),
            text = "Back",
            font = font3,
            style = "background-color: #004F9A"
        )

        # INSERT IMAGE BUTTON
        self.edit_member_insert_image_button = createButton(
            parent = self.edit_member,
            name = "insert_image_button",
            geometry = QRect(680, 400, 250, 50),
            text = "Insert Image",
            font = font3,
            style = "background-color: #004F9A"
        )

        # INSERT SIGNATURE BUTTON
        self.edit_member_insert_signature_button = createButton(
            parent = self.edit_member,
            name = "insert_signature_button",
            geometry = QRect(680, 560, 250, 50),
            text = "Insert Signature",
            font = font3,
            style = "background-color: #004F9A"
        )

        # CLEAR BUTTON
        self.edit_member_clear_button = createButton(
            parent = self.edit_member,
            name = "clear_button",
            geometry = QRect(510, 730, 170, 50),
            text = "Clear",
            font = font3,
            style = "background-color: #882400"
        )

        # REGISTER BUTTON
        self.edit_member_register_button = createButton(
            parent = self.edit_member,
            name = "register_button",
            geometry = QRect(690, 730, 250, 50),
            text = "Register",
            font = font3,
            style = "background-color: #006646"
        )
        self.edit_member_insert_image_button.clicked.connect(lambda: self.insert_image(self.edit_member_image_label))
        self.edit_member_insert_signature_button.clicked.connect(lambda: self.insert_image(self.edit_member_signature_label))
        self.edit_member_register_button.clicked.connect(self.update_member)
    
    def view_member(self):
        self.view_member = QWidget()
        self.view_member.setObjectName("member_page")
        self.stackedWidget.addWidget(self.view_member)

        # ===========================================
        #             MEMBER PAGE LABELS
        # ===========================================

        # MEMBER REGISTRATION TEXT LABEL
        self.view_member_registration_text_label = createLabel(
            parent=self.view_member,
            name="member_registration_text_label",
            geometry=QRect(310, 50, 380, 40),
            text="Member Details",
            font=font4,
            style="font: bold"
        )

        # MEMBER ID LABEL
        self.view_member_id_label = createLabel(
            parent=self.view_member,
            name="member_id_label",
            geometry=QRect(40, 150, 191, 40),
            text="Membership ID:",
            font=font1,
            style=""
        )

        # MEMBER ID OUTPUT LABEL
        self.view_member_id_output_label = createLabel(
            parent=self.view_member,
            name="member_id_output",
            geometry=QRect(240, 150, 410, 40),
            text="",
            font=font1,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        # FIRST NAME LABEL
        self.view_member_first_name_label = createLabel(
            parent=self.view_member,
            name="first_name_label",
            geometry=QRect(40, 210, 130, 40),
            text="First Name:",
            font=font1,
            style=""
        )

        # FIRST NAME OUTPUT LABEL
        self.view_member_first_name_output_label = createLabel(
            parent=self.view_member,
            name="first_name_output",
            geometry=QRect(40, 260, 330, 40),
            text="",
            font=font1,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        # MIDDLE NAME LABEL
        self.view_member_middle_name_label = createLabel(
            parent=self.view_member,
            name="middle_name_label",
            geometry=QRect(380, 210, 160, 40),
            text="Middle Name:",
            font=font1,
            style=""
        )

        # MIDDLE NAME OUTPUT LABEL
        self.view_member_middle_name_output_label = createLabel(
            parent=self.view_member,
            name="middle_name_output",
            geometry=QRect(380, 260, 280, 40),
            text="",
            font=font1,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        # LAST NAME LABEL
        self.view_member_last_name_label = createLabel(
            parent=self.view_member,
            name="last_name_label",
            geometry=QRect(40, 310, 130, 40),
            text="Last Name:",
            font=font1,
            style=""
        )

        # LAST NAME OUTPUT LABEL
        self.view_member_last_name_output_label = createLabel(
            parent=self.view_member,
            name="last_name_output",
            geometry=QRect(40, 360, 330, 40),
            text="",
            font=font1,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        # GENDER LABEL
        self.view_member_gender_label = createLabel(
            parent=self.view_member,
            name="gender_label",
            geometry=QRect(380, 310, 130, 40),
            text="Gender:",
            font=font1,
            style=""
        )

        # GENDER OUTPUT LABEL
        self.view_member_gender_output_label = createLabel(
            parent=self.view_member,
            name="gender_output",
            geometry=QRect(380, 360, 140, 40),
            text="",
            font=font1,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        # ADDRESS LABEL
        self.view_member_address_label = createLabel(
            parent=self.view_member,
            name="address_label",
            geometry=QRect(40, 420, 130, 40),
            text="Address:",
            font=font1,
            style=""
        )

        # ADDRESS OUTPUT LABEL
        self.view_member_address_output_label = createLabel(
            parent=self.view_member,
            name="address_output",
            geometry=QRect(40, 470, 330, 40),
            text="",
            font=font1,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        # BIRTHDATE LABEL
        self.view_member_birthdate_label = createLabel(
            parent=self.view_member,
            name="birthdate_label",
            geometry=QRect(380, 420, 130, 40),
            text="Birthdate:",
            font=font1,
            style=""
        )

        # BIRTHDATE OUTPUT LABEL
        self.view_member_birthdate_output_label = createLabel(
            parent=self.view_member,
            name="birthdate_output",
            geometry=QRect(380, 470, 200, 40),
            text="",
            font=font1,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        # PHONE NUMBER LABEL
        self.view_member_phone_number_label = createLabel(
            parent=self.view_member,
            name="phone_number_label",
            geometry=QRect(40, 530, 180, 40),
            text="Phone Number:",
            font=font1,
            style=""
        )

        # PHONE NUMBER OUTPUT LABEL
        self.view_member_phone_number_output_label = createLabel(
            parent=self.view_member,
            name="phone_number_output",
            geometry=QRect(40, 570, 330, 40),
            text="",
            font=font1,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        # MEMBERSHIP TYPE LABEL
        self.view_member_membership_type_label = createLabel(
            parent=self.view_member,
            name="membership_type_label",
            geometry=QRect(380, 530, 210, 40),
            text="Membership Type:",
            font=font1,
            style=""
        )

        # MEMBERSHIP TYPE OUTPUT LABEL
        self.view_member_membership_type_output_label = createLabel(
            parent=self.view_member,
            name="membership_type_output",
            geometry=QRect(380, 570, 210, 40),
            text="",
            font=font1,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        # START DATE LABEL
        self.view_member_start_date_label = createLabel(
            parent=self.view_member,
            name="start_date_label",
            geometry=QRect(40, 630, 180, 40),
            text="Start Date:",
            font=font1,
            style=""
        )

        # START DATE OUTPUT LABEL
        self.view_member_start_date_output_label = createLabel(
            parent=self.view_member,
            name="start_date_output",
            geometry=QRect(40, 670, 200, 40),
            text="",
            font=font1,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        # END DATE LABEL
        self.view_member_end_date_label = createLabel(
            parent=self.view_member,
            name="end_date_label",
            geometry=QRect(280, 630, 180, 40),
            text="End Date:",
            font=font1,
            style=""
        )

        # END DATE OUTPUT LABEL
        self.view_member_end_date_output_label = createLabel(
            parent=self.view_member,
            name="end_date_output",
            geometry=QRect(280, 670, 200, 40),
            text="",
            font=font1,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        # IMAGE LABEL 
        self.view_member_image_label = createLabel(
            parent=self.view_member,
            name="image_label",
            geometry=QRect(680, 140, 250, 250),
            text="",
            font=font1,
            style="background-color: #F9F7FF; border: 1.5px solid black"
        )

        # SIGNATURE LABEL
        self.view_member_signature_label = createLabel(
            parent=self.view_member,
            name="signature_label",
            geometry=QRect(750, 460, 180, 90),
            text="",
            font=font1,
            style="background-color: #F9F7FF; border: 1.5px solid black"
        )

        # ===========================================
        #              MEMBER PAGE BUTTONS
        # ===========================================

        # BACK BUTTON
        self.view_member_back_button = createButton(
            parent=self.view_member,
            name="back_button",
            geometry=QRect(40, 50, 70, 50),
            text="Back",
            font=font3,
            style="background-color: #004F9A"
        )

        # REGISTER BUTTON
        self.view_member_register_button = createButton(
            parent=self.view_member,
            name="register_button",
            geometry=QRect(690, 730, 250, 50),
            text="Edit",
            font=font3,
            style="background-color: #006646; color: #FFFFFF"
        )
        self.view_member_register_button.clicked.connect(self.edit_employee_button)
    def update_end_date(self):
        membership_type = self.add_member_membership_type_combo_box.currentText()
        if membership_type == "Lifetime":
            self.add_member_end_date.setDate(QDate(9999, 12, 31))  # Set to a far future date
            self.add_member_end_date.setDisabled(True)  # Optionally disable the end date field
        else:
            self.add_member_end_date.setDisabled(False)
            self.add_member_end_date.setDate(QDate.currentDate())  # Reset to the current date
    
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
    def register_member(self):
        # Retrieve all inputs
        self.member_id = self.add_member_id_output_label.text()
        self.first_name = self.add_member_first_name_input.text()
        self.middle_name = self.add_member_middle_name_input.text()
        self.last_name = self.add_member_last_name_input.text()
        self.address = self.add_member_address_input.text()
        self.phone_number = self.add_member_phone_number_input.text()
        self.gender = self.add_member_gender_combo_box.currentText()
        self.membership_type = self.add_member_membership_type_combo_box.currentText()
        self.birth_date = self.add_member_birth_date.date()
        self.start_date = self.add_member_start_date.date()
        self.end_date = self.add_member_end_date.date()
        self.photo = self.add_member_image_label.pixmap()
        self.signature = self.add_member_signature_label.pixmap()

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
    def show_view_member_temp(self, row):
        member_id = self.member_table_widget.item(row, 0).text()

        cursor.execute(
            """
            SELECT * 
            FROM Members
            WHERE member_id = ?
            """,
            (member_id,)
        )

        results = cursor.fetchone()

        employee_id, first_name, middle_name, last_name, address, gender, birthdate, phone, membership_type, start_date, end_date, photo, signature = results

        pixmap = QPixmap()
        pixmap_2 = QPixmap()
        self.view_member_id_output_label.setText(employee_id)
        self.view_member_first_name_output_label.setText(first_name)
        self.view_member_middle_name_output_label.setText(middle_name)
        self.view_member_last_name_output_label.setText(last_name)
        self.view_member_birthdate_output_label.setText(birthdate)
        self.view_member_gender_output_label.setText(gender)
        self.view_member_address_output_label.setText(address)
        self.view_member_phone_number_output_label.setText(phone)
        self.view_member_membership_type_output_label.setText(membership_type)
        self.view_member_start_date_output_label.setText(start_date)
        self.view_member_end_date_output_label.setText(end_date)

        pixmap.loadFromData(photo)
        self.view_member_image_label.setPixmap(pixmap)
        pixmap_2.loadFromData(signature)
        self.view_member_signature_label.setPixmap(pixmap_2)

        self.show_view_member()

    def fetch_employee_by_column(self):
        query = f"""SELECT member_id, 
                  first_name || ' ' || last_name,
                  membership_type,
                  phone_number,
                  membership_end_date
                  FROM Members """
        cursor.execute(query)
        data = cursor.fetchall()
        return data
    
    def edit_employee_button(self):
        employee_id =  self.view_member_id_output_label.text()
        first_name = self.view_member_first_name_output_label.text()
        middle_name = self.view_member_middle_name_output_label.text()
        last_name = self.view_member_last_name_output_label.text()
        birthdate = self.view_member_birthdate_output_label.text()
        gender = self.view_member_gender_output_label.text()
        address =self.view_member_address_output_label.text()
        phone = self.view_member_phone_number_output_label.text()
        membership_type = self.view_member_membership_type_output_label.text()
        start_date = self.view_member_start_date_output_label.text()
        end_date = self.view_member_end_date_output_label.text()
        photo = self.view_member_image_label.pixmap()
        signature = self.view_member_signature_label.pixmap()

        birthdate = datetime.strptime(birthdate, '%Y-%m-%d')
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')

        self.edit_member_id_output_label.setText(employee_id)
        self.edit_member_first_name_input.setText(first_name)
        self.edit_member_middle_name_input.setText(middle_name)
        self.edit_member_last_name_input.setText(last_name)
        self.edit_member_birth_date.setDate(birthdate)
        self.edit_member_gender_combo_box.setCurrentText(gender)
        self.edit_member_address_input.setText(address)
        self.edit_member_phone_number_input.setText(phone)
        self.edit_member_membership_type_combo_box.setCurrentText(membership_type)
        self.edit_member_start_date.setDate(start_date)
        self.edit_member_end_date.setDate(end_date)

        self.edit_member_image_label.setPixmap(photo)
        self.edit_member_signature_label.setPixmap(signature)


        self.update_table_widget()
        self.show_edit_member()

    def update_table_widget(self):
        data = self.fetch_employee_by_column()
        self.member_table_widget.setRowCount(len(data))
        for row_index, row_data in enumerate(data):
            for col_index, col_data in enumerate(row_data):
                self.member_table_widget.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))
            
        for self.row in range(self.member_table_widget.rowCount()):
            view_button = QPushButton("View")
            view_button.clicked.connect(partial(self.show_view_member_temp, self.row))
            self.member_table_widget.setCellWidget(self.row, 5, view_button)
            
    def update_member(self):
        member_id =  self.edit_member_id_output_label.text()
        first_name = self.edit_member_first_name_input.text()
        middle_name = self.edit_member_middle_name_input.text()
        last_name = self.edit_member_last_name_input.text()
        birthdate = self.edit_member_birth_date.date()
        gender = self.edit_member_gender_combo_box.currentText()
        address =self.edit_member_address_input.text()
        phone = self.edit_member_phone_number_input.text()
        start_date = self.edit_member_start_date.date()
        end_date = self.edit_member_end_date.date()
        membership_type = self.edit_member_membership_type_combo_box.currentText()
        photo = self.edit_member_image_label.pixmap()
        signature = self.edit_member_signature_label.pixmap()
        member_image_bytes = self.pixmap_to_bytes(photo)
        signature_image_bytes = self.pixmap_to_bytes(signature)

        cursor.execute(
            """
            UPDATE Members
            SET member_id = ?, first_name = ?, middle_name = ?, last_name = ?, birthdate = ?, gender = ?, 
            address = ?, phone_number = ?, membership_type = ?, membership_start_date =? , membership_end_date = ?, photo = ?, signature = ?
            """,
            (
                member_id,
                first_name,
                middle_name,
                last_name,
                birthdate.toString("yyyy-MM-dd"),
                gender,
                address,
                phone,
                membership_type,
                start_date.toString("yyyy-MM-dd"),
                end_date.toString("yyyy-MM-dd"),
                sqlite3.Binary(member_image_bytes),
                sqlite3.Binary(signature_image_bytes),
            )
        )
        connection.commit()
        QMessageBox.information(self, "Yippie", "Employee Updated")
        self.show_member_page()

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
    
    def generate_member_id(self):
        query = "SELECT COUNT(*) FROM Members"
        cursor.execute(query)
        count = cursor.fetchone()[0] + 1
        current_time = datetime.now()
        formatted_time = current_time.strftime('%m%d%y')
        prefix = "MEM"

        generated_id = f"{prefix}-{formatted_time}-{count:04}"
        self.add_member_id_output_label.setText(generated_id)
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Maintenance()
    window.show()
    sys.exit(app.exec_())
