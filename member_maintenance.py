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


        self.open_edit_member()
        self.view_member_details()
        self.open_add_member()
        self.open_member_page()  # MAITENANCE MEMBER PAGE

        self.verticalLayout.addWidget(self.stackedWidget)
        self.stackedWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(self)



    def show_member_page(self):
        self.update_table_widget()
        self.stackedWidget.setCurrentIndex(0)


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
    
    def open_add_member(self):
        self.add_member_page = QWidget()
        self.add_member_page.setObjectName("member_page")
        self.stackedWidget.addWidget(self.add_member_page)

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

    def open_edit_member(self):
        self.edit_member = QWidget()
        self.edit_member.setObjectName("member_page")
        self.stackedWidget.addWidget(self.edit_member)

        # ===========================================
        #             MEMBER PAGE LABELS
        # ===========================================

        # MEMBER REGISTRATION TEXT LABEL
        self.member_registration_text_label = createLabel(
            parent = self.edit_member,
            name = "member_registration_text_label",
            geometry = QRect(310, 50, 380, 40),
            text = "Edit Member Details",
            font = font4,
            style = "font: bold"
        )

        # MEMBER ID LABEL
        self.member_id_label = createLabel(
            parent = self.edit_member,
            name = "member_id_label",
            geometry = QRect(40, 150, 191, 40),
            text = "Membership ID:",
            font = font1,
            style = ""
        )

        # MEMBER ID OUTPUT LABEL
        self.member_id_output_label = createLabel(
            parent = self.edit_member,
            name = "member_id_output",
            geometry = QRect(240, 150, 410, 40),
            text = "",
            font = font1,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # FIRST NAME LABEL
        self.member_first_name_label = createLabel(
            parent = self.edit_member,
            name = "first_name_label",
            geometry = QRect(40, 210, 130, 40),
            text = "First Name",
            font = font1,
            style = ""
        )

        # MIDDLE NAME LABEL
        self.member_middle_name_label = createLabel(
            parent = self.edit_member,
            name = "middle_name_label",
            geometry = QRect(380, 210, 160, 40),
            text = "Middle Name",
            font = font1,
            style = ""
        )

        # LAST NAME LABEL
        self.member_last_name_label = createLabel(
            parent = self.edit_member,
            name = "last_name_label",
            geometry = QRect(40, 310, 130, 40),
            text = "Last Name",
            font = font1,
            style = ""
        )

        # GENDER LABEL
        self.member_gender_label = createLabel(
            parent = self.edit_member,
            name = "gender_label",
            geometry = QRect(380, 310, 130, 40),
            text = "Gender",
            font = font1,
            style = ""
        )

        # ADDRESS LABEL
        self.member_address_label = createLabel(
            parent = self.edit_member,
            name = "addresslabel",
            geometry = QRect(40, 420, 130, 40),
            text = "Address",
            font = font1,
            style = ""
        )

        # BIRTHDATE LABEL
        self.member_birthdate_label = createLabel(
            parent = self.edit_member,
            name = "birthdate_label",
            geometry = QRect(380, 420, 130, 40),
            text = "Birthdate",
            font = font1,
            style = ""
        )

        # PHONE NUMBER LABEL
        self.member_phone_number_label = createLabel(
            parent = self.edit_member,
            name = "phone_number_label",
            geometry = QRect(40, 530, 180, 40),
            text = "Phone Number",
            font = font1,
            style = ""
        )

        # MEMBERSHIP TYPE LABEL
        self.member_membership_type_label = createLabel(
            parent = self.edit_member,
            name = "membership_type_label",
            geometry = QRect(380, 530, 210, 40),
            text = "Membership Type",
            font = font1,
            style = ""
        )

        # START DATE LABEL
        self.member_start_date_label = createLabel(
            parent = self.edit_member,
            name = "start_date_label",
            geometry = QRect(40, 630, 180, 40),
            text = "Start Date",
            font = font1,
            style = ""
        )

        # END DATE LABEL
        self.member_end_date_label = createLabel(
            parent = self.edit_member,
            name = "end_date_label",
            geometry = QRect(280, 630, 180, 40),
            text = "End Date",
            font = font1,
            style = ""
        )

        # IMAGE LABEL 
        self.member_image_label = createLabel(
            parent = self.edit_member,
            name = "image_label",
            geometry = QRect(680, 140, 250, 250),
            text = "",
            font = font1,
            style = "background-color: #F9F7FF; border: 1.5px solid black"
        )
        
        # SIGNATURE LABEL
        self.member_signature_label = createLabel(
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
        self.member_first_name_input = createLineInput(
            parent = self.edit_member,
            name = "first_name_output",
            geometry = QRect(40, 260, 330, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # MIDDLE NAME INPUT
        self.member_middle_name_input = createLineInput(
            parent = self.edit_member,
            name = "middle_name_output",
            geometry = QRect(380, 260, 280, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # LAST NAME INPUT
        self.member_last_name_input = createLineInput(
            parent = self.edit_member,
            name = "last_name_output",
            geometry = QRect(40, 360, 330, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # ADDRESS INPUT
        self.member_address_input = createLineInput(
            parent = self.edit_member,
            name = "address_output",
            geometry = QRect(40, 470, 330, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )
        # PHONE NUMBER INPUT
        self.member_phone_number_input = createLineInput(
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
        self.member_gender_combo_box = createComboBox(
            parent = self.edit_member,
            name = "gender_combo_box",
            geometry = QRect(380, 360, 140, 40),
            font = font2,
            item = ['Male', 'Female'],
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # MEMBERSHIP TYPE BOX
        self.member_membership_type_combo_box = createComboBox(
            parent = self.edit_member,
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
            parent = self.edit_member,
            name = "birthdate",
            geometry = QRect(380, 470, 200, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # START DATE
        self.member_start_date = createDate(
            parent = self.edit_member,
            name = "member_start_date",
            geometry = QRect(40, 670, 200, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # END DATE
        self.member_end_date = createDate(
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
        self.member_back_button = createButton(
            parent = self.edit_member,
            name = "back_button",
            geometry = QRect(40, 50, 70, 50),
            text = "Back",
            font = font3,
            style = "background-color: #004F9A"
        )

        # INSERT IMAGE BUTTON
        self.member_insert_image_button = createButton(
            parent = self.edit_member,
            name = "insert_image_button",
            geometry = QRect(680, 400, 250, 50),
            text = "Insert Image",
            font = font3,
            style = "background-color: #004F9A"
        )

        # INSERT SIGNATURE BUTTON
        self.member_insert_signature_button = createButton(
            parent = self.edit_member,
            name = "insert_signature_button",
            geometry = QRect(680, 560, 250, 50),
            text = "Insert Signature",
            font = font3,
            style = "background-color: #004F9A"
        )

        # CLEAR BUTTON
        self.member_clear_button = createButton(
            parent = self.edit_member,
            name = "clear_button",
            geometry = QRect(510, 730, 170, 50),
            text = "Clear",
            font = font3,
            style = "background-color: #882400"
        )

        # REGISTER BUTTON
        self.member_register_button = createButton(
            parent = self.edit_member,
            name = "register_button",
            geometry = QRect(690, 730, 250, 50),
            text = "Register",
            font = font3,
            style = "background-color: #006646"
        )
    
    def view_member_details(self):
        self.view_member = QWidget()
        self.view_member.setObjectName("member_page")
        self.stackedWidget.addWidget(self.view_member)

        # ===========================================
        #             MEMBER PAGE LABELS
        # ===========================================

        # MEMBER REGISTRATION TEXT LABEL
        self.member_registration_text_label = createLabel(
            parent=self.view_member,
            name="member_registration_text_label",
            geometry=QRect(310, 50, 380, 40),
            text="Member Details",
            font=font4,
            style="font: bold"
        )

        # MEMBER ID LABEL
        self.member_id_label = createLabel(
            parent=self.view_member,
            name="member_id_label",
            geometry=QRect(40, 150, 191, 40),
            text="Membership ID:",
            font=font1,
            style=""
        )

        # MEMBER ID OUTPUT LABEL
        self.member_id_output_label = createLabel(
            parent=self.view_member,
            name="member_id_output",
            geometry=QRect(240, 150, 410, 40),
            text="",
            font=font1,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        # FIRST NAME LABEL
        self.member_first_name_label = createLabel(
            parent=self.view_member,
            name="first_name_label",
            geometry=QRect(40, 210, 130, 40),
            text="First Name:",
            font=font1,
            style=""
        )

        # FIRST NAME OUTPUT LABEL
        self.member_first_name_output_label = createLabel(
            parent=self.view_member,
            name="first_name_output",
            geometry=QRect(40, 260, 330, 40),
            text="",
            font=font1,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        # MIDDLE NAME LABEL
        self.member_middle_name_label = createLabel(
            parent=self.view_member,
            name="middle_name_label",
            geometry=QRect(380, 210, 160, 40),
            text="Middle Name:",
            font=font1,
            style=""
        )

        # MIDDLE NAME OUTPUT LABEL
        self.member_middle_name_output_label = createLabel(
            parent=self.view_member,
            name="middle_name_output",
            geometry=QRect(380, 260, 280, 40),
            text="",
            font=font1,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        # LAST NAME LABEL
        self.member_last_name_label = createLabel(
            parent=self.view_member,
            name="last_name_label",
            geometry=QRect(40, 310, 130, 40),
            text="Last Name:",
            font=font1,
            style=""
        )

        # LAST NAME OUTPUT LABEL
        self.member_last_name_output_label = createLabel(
            parent=self.view_member,
            name="last_name_output",
            geometry=QRect(40, 360, 330, 40),
            text="",
            font=font1,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        # GENDER LABEL
        self.member_gender_label = createLabel(
            parent=self.view_member,
            name="gender_label",
            geometry=QRect(380, 310, 130, 40),
            text="Gender:",
            font=font1,
            style=""
        )

        # GENDER OUTPUT LABEL
        self.member_gender_output_label = createLabel(
            parent=self.view_member,
            name="gender_output",
            geometry=QRect(380, 360, 140, 40),
            text="",
            font=font1,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        # ADDRESS LABEL
        self.member_address_label = createLabel(
            parent=self.view_member,
            name="address_label",
            geometry=QRect(40, 420, 130, 40),
            text="Address:",
            font=font1,
            style=""
        )

        # ADDRESS OUTPUT LABEL
        self.member_address_output_label = createLabel(
            parent=self.view_member,
            name="address_output",
            geometry=QRect(40, 470, 330, 40),
            text="",
            font=font1,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        # BIRTHDATE LABEL
        self.member_birthdate_label = createLabel(
            parent=self.view_member,
            name="birthdate_label",
            geometry=QRect(380, 420, 130, 40),
            text="Birthdate:",
            font=font1,
            style=""
        )

        # BIRTHDATE OUTPUT LABEL
        self.member_birthdate_output_label = createLabel(
            parent=self.view_member,
            name="birthdate_output",
            geometry=QRect(380, 470, 200, 40),
            text="",
            font=font1,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        # PHONE NUMBER LABEL
        self.member_phone_number_label = createLabel(
            parent=self.view_member,
            name="phone_number_label",
            geometry=QRect(40, 530, 180, 40),
            text="Phone Number:",
            font=font1,
            style=""
        )

        # PHONE NUMBER OUTPUT LABEL
        self.member_phone_number_output_label = createLabel(
            parent=self.view_member,
            name="phone_number_output",
            geometry=QRect(40, 570, 330, 40),
            text="",
            font=font1,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        # MEMBERSHIP TYPE LABEL
        self.member_membership_type_label = createLabel(
            parent=self.view_member,
            name="membership_type_label",
            geometry=QRect(380, 530, 210, 40),
            text="Membership Type:",
            font=font1,
            style=""
        )

        # MEMBERSHIP TYPE OUTPUT LABEL
        self.member_membership_type_output_label = createLabel(
            parent=self.view_member,
            name="membership_type_output",
            geometry=QRect(380, 570, 210, 40),
            text="",
            font=font1,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        # START DATE LABEL
        self.member_start_date_label = createLabel(
            parent=self.view_member,
            name="start_date_label",
            geometry=QRect(40, 630, 180, 40),
            text="Start Date:",
            font=font1,
            style=""
        )

        # START DATE OUTPUT LABEL
        self.member_start_date_output_label = createLabel(
            parent=self.view_member,
            name="start_date_output",
            geometry=QRect(40, 670, 200, 40),
            text="",
            font=font1,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        # END DATE LABEL
        self.member_end_date_label = createLabel(
            parent=self.view_member,
            name="end_date_label",
            geometry=QRect(280, 630, 180, 40),
            text="End Date:",
            font=font1,
            style=""
        )

        # END DATE OUTPUT LABEL
        self.member_end_date_output_label = createLabel(
            parent=self.view_member,
            name="end_date_output",
            geometry=QRect(280, 670, 200, 40),
            text="",
            font=font1,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        # IMAGE LABEL 
        self.member_image_label = createLabel(
            parent=self.view_member,
            name="image_label",
            geometry=QRect(680, 140, 250, 250),
            text="",
            font=font1,
            style="background-color: #F9F7FF; border: 1.5px solid black"
        )

        # SIGNATURE LABEL
        self.member_signature_label = createLabel(
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
        self.member_back_button = createButton(
            parent=self.view_member,
            name="back_button",
            geometry=QRect(40, 50, 70, 50),
            text="Back",
            font=font3,
            style="background-color: #004F9A"
        )

        # REGISTER BUTTON
        self.member_register_button = createButton(
            parent=self.view_member,
            name="register_button",
            geometry=QRect(690, 730, 250, 50),
            text="Edit",
            font=font3,
            style="background-color: #006646; color: #FFFFFF"
        )



    def update_end_date(self):
        membership_type = self.member_membership_type_combo_box.currentText()
        if membership_type == "Lifetime":
            self.member_end_date.setDate(QDate(9999, 12, 31))  # Set to a far future date
            self.member_end_date.setDisabled(True)  # Optionally disable the end date field
        else:
            self.member_end_date.setDisabled(False)
            self.member_end_date.setDate(QDate.currentDate())  # Reset to the current date
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Maintenance()
    window.show()
    sys.exit(app.exec_())
