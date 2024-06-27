from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from assets import *
from product_maintenance import *
from member_maintenance import *
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


        # ========================     MEMBER MAINTENANCE
        self.open_member_page()
        self.open_create_member() 
        self.open_edit_member()
        self.open_view_member()

        # =======================      EMPLOYEE MAINTENANCE

        self.open_employee_page()
        self.create_employee()
        self.edit_employee()
        self.view_employee()

        self.verticalLayout.addWidget(self.stackedWidget)
        self.stackedWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(self)



    def show_main_page(self):
        self.stackedWidget.setCurrentIndex(0)

    def show_member_page(self):
        self.update_table_widget()
        self.stackedWidget.setCurrentIndex(1)
    
    def show_add_member(self):
        generate_id("Members", self.member_id_output_label)
        clear_inputs(self.member_page)
        self.stackedWidget.setCurrentIndex(2)
    
    def show_edit_member(self):
        self.stackedWidget.setCurrentIndex(3)

    def show_view_member(self):
        self.stackedWidget.setCurrentIndex(4)

    def show_employee_page(self):
        self.update_table_widget()
        self.stackedWidget.setCurrentIndex(5)

    def show_create_employee(self):
        clear_inputs(self.create_employee_page)
        generate_id("Employees", self.create_employee_id_output_label)
        self.stackedWidget.setCurrentIndex(6)

    def show_edit_employee(self):
        self.stackedWidget.setCurrentIndex(7)

    def show_view_employee(self):
        self.stackedWidget.setCurrentIndex(8)

        
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

        self.switch_member_page_button.clicked.connect(self.show_member_page)
        self.switch_employee_page_button.clicked.connect(self.show_employee_page)
#========================================================================================================================
#                                     MEMBER MAINTENANCE
#========================================================================================================================

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

        self.manage_search_input.textChanged.connect(lambda: self.search_entity("Members", self.member_table_widget, self.manage_search_input))
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
        self.member_back_button.clicked.connect(self.show_main_page)
        self.member_add_button.clicked.connect(self.show_add_member)
    
    def open_create_member(self):
        self.member_page = QWidget()
        self.member_page.setObjectName("member_page")
        self.stackedWidget.addWidget(self.member_page)

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

        disable_past_date(self.member_start_date)
        # END DATE
        self.member_end_date = createDate(
            parent = self.member_page,
            name = "member_end_date",
            geometry = QRect(280, 670, 200, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        disable_past_date(self.member_end_date)

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
        
        self.member_back_button.clicked.connect(self.show_member_page)
        self.member_clear_button.clicked.connect(lambda: clear_inputs(self.member_page))
        self.member_register_button.clicked.connect(lambda: register_entity("Members", self.assigned_input("Members")))
        self.member_insert_image_button.clicked.connect(lambda: insert_image(self.member_image_label))
        self.member_insert_signature_button.clicked.connect(lambda: insert_image(self.member_signature_label))

    def open_edit_member(self):
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
        self.edit_member_cancel_button = createButton(
            parent = self.edit_member,
            name = "clear_button",
            geometry = QRect(510, 730, 170, 50),
            text = "Clear",
            font = font3,
            style = "background-color: #882400"
        )

        # REGISTER BUTTON
        self.edit_member_update_button = createButton(
            parent = self.edit_member,
            name = "register_button",
            geometry = QRect(690, 730, 250, 50),
            text = "Update Member",
            font = font3,
            style = "background-color: #006646"
        )

        self.edit_member_back_button.clicked.connect(self.show_view_member)
        self.edit_member_cancel_button.clicked.connect(self.show_view_member)
        self.edit_member_insert_image_button.clicked.connect(lambda: insert_image(self.edit_member_image_label))
        self.edit_member_insert_signature_button.clicked.connect(lambda: insert_image(self.edit_member_signature_label))
        self.edit_member_update_button.clicked.connect(lambda: update_entity("Members", self.assigned_input("Update Member")))
    def open_view_member(self):
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
        self.view_member_back_button.clicked.connect(self.show_member_page)
        self.view_member_register_button.clicked.connect(self.edit_employee_button)

    def update_end_date(self):
        membership_type = self.member_membership_type_combo_box.currentText()
        if membership_type == "Lifetime":
            self.member_end_date.setDate(QDate(9999, 12, 31))  # Set to a far future date
            self.member_end_date.setDisabled(True)  # Optionally disable the end date field
        else:
            self.member_end_date.setDisabled(False)
            self.member_end_date.setDate(QDate.currentDate())  # Reset to the current date
    
    def assigned_input(self, input):
        if input == "Members":
            image = pixmap_to_bytes(self.member_image_label.pixmap())
            signature = pixmap_to_bytes(self.member_signature_label.pixmap())

            INPUTS = {
                "member_id": self.member_id_output_label.text(),
                "first_name": self.member_first_name_input.text(),
                "middle_name":self.member_middle_name_input.text(),
                "last_name": self.member_last_name_input.text(),
                "address": self.member_address_input.text(),
                "phone": self.member_phone_number_input.text(),
                "gender": self.member_gender_combo_box.currentText(),
                "membership_type": self.member_membership_type_combo_box.currentText(),
                "birthdate": self.member_birth_date.date(),
                "start_date": self.member_start_date.date(),
                "end_date": self.member_end_date.date(),
                "image": sqlite3.Binary(image),
                "signature": sqlite3.Binary(signature),
            }
        elif input == "Update Member":
            image = pixmap_to_bytes(self.edit_member_image_label.pixmap())
            signature = pixmap_to_bytes(self.edit_member_signature_label.pixmap())

            INPUTS = {
                "first_name": self.edit_member_first_name_input.text(),
                "middle_name":self.edit_member_middle_name_input.text(),
                "last_name": self.edit_member_last_name_input.text(),
                "address": self.edit_member_address_input.text(),
                "phone": self.edit_member_phone_number_input.text(),
                "gender": self.edit_member_gender_combo_box.currentText(),
                "membership_type": self.edit_member_membership_type_combo_box.currentText(),
                "birthdate": self.edit_member_birth_date.date(),
                "start_date": self.edit_member_start_date.date(),
                "end_date": self.edit_member_end_date.date(),
                "image": sqlite3.Binary(image),
                "signature": sqlite3.Binary(signature),
            }


        return INPUTS
    
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

    
    def search_entity(self, entity_type, table_widget, input_text):
        search_term = input_text.text().strip()  # Get the search term from input widget

        if entity_type == "Members":
            query = """
                SELECT member_id, 
                        first_name || ' ' || last_name AS full_name, 
                        membership_type, 
                        phone_number, 
                        membership_start_date, 
                        membership_end_date
                FROM Members
                WHERE member_id LIKE ? OR first_name LIKE ? OR last_name LIKE ?;
            """
        elif entity_type == "Employees":
            query = """
                SELECT employee_id,
                        first_name || ' ' || last_name AS full_name,
                        position,
                        phone_number,
                        hire_date
                FROM Employees
                WHERE employee_id LIKE ? OR first_name LIKE ? OR last_name LIKE ?;
            """
        elif entity_type == "Equipments":
            query = """
                SELECT equipment_id,
                        name,
                        serial_number,
                        category,
                        status
                FROM Equipments
                WHERE equipment_id LIKE ? OR name LIKE ? OR serial_number LIKE ?;
            """
        elif entity_type == "Products":
            query = """
                SELECT product_id,
                        name,
                        quantity,
                        expiry_date,
                        status
                FROM Products
                WHERE product_id LIKE ? OR name LIKE ?;
            """
        elif entity_type == "UserAccounts":
            query = """
                SELECT employee_id,
                        username,
                        password,
                        role
                FROM UserAccounts
                WHERE employee_id LIKE ? OR username LIKE ?;
            """
        else:
            print(f"Unsupported entity type: {entity_type}")
            return

        try:
            cursor.execute(query, (f'%{search_term}%', f'%{search_term}%', f'%{search_term}%'))
            results = cursor.fetchall()

            table_widget.setRowCount(len(results))
            for row_idx, row_data in enumerate(results):
                for col_idx, col_data in enumerate(row_data):
                    table_widget.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))
                view_button = QPushButton("View")
                view_button.clicked.connect(partial(self.show_view_member_temp, row_idx))
                table_widget.setCellWidget(row_idx, len(row_data), view_button)
            self.add_view_buttons()

        except Exception as e:
            print(f"Error executing query: {e}")
    
    def add_view_buttons(self):
   
        for row in range(self.member_table_widget.rowCount()):
            view_button = QPushButton("View")
            view_button.clicked.connect(partial(self.show_view_member_temp, row))
            self.member_table_widget.setCellWidget(row, 5, view_button)

#========================================================================================================================
#                                     EMPLOYEE MAINTENANCE
#========================================================================================================================
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
        self.employee_table_widget = QTableWidget(self.employee_page)
        self.employee_table_widget.setGeometry(QRect(10, 200, 930, 590))
        self.employee_table_widget.setRowCount(0)
        self.employee_table_widget.setColumnCount(6)  # Limited columns
    
        self.manage_employee_search_input.textChanged.connect(lambda: self.search_employees(self.employee_table_widget, self.manage_employee_search_input))
        # Set the horizontal header labels
        self.employee_table_widget.setHorizontalHeaderLabels(
            ["Employee ID", "Full Name", "Position", "Phone", "Hire Date", "Actions"]
        )

        self.stackedWidget.addWidget(self.employee_page)
        self.employee_table_widget.resizeColumnsToContents()
        self.employee_table_widget.resizeRowsToContents()
        self.employee_table_widget.horizontalHeader().setStretchLastSection(True)
        self.employee_table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.update_table_widget_employee()

        #         MANAGE MEMBER BUTTONS
        # ===========================================
        self.employee_back_button = createButton(
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

        self.employee_back_button.clicked.connect(self.show_main_page)
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

    def update_table_widget_employee(self):
        data = self.fetch_employee_by_column()
        self.employee_table_widget.setRowCount(len(data))
        for row_index, row_data in enumerate(data):
            for col_index, col_data in enumerate(row_data):
                self.employee_table_widget.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))
            
        for self.row in range(self.employee_table_widget.rowCount()):
            view_button = QPushButton("View")
            view_button.clicked.connect(partial(self.show_view_employee_temp, self.row))
            self.employee_table_widget.setCellWidget(self.row, 5, view_button)

    def show_view_employee_temp(self, row):
        employee_id = self.employee_table_widget.item(row, 0).text()

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

#========================================================================================================================
#                                     USER ACCOUNTS MAINTENANCE
#========================================================================================================================
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Maintenance()
    window.show()
    sys.exit(app.exec_())
