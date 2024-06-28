
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


class EquipmentMaintenance(QWidget):
    def __init__(self, parent=None):
        super(EquipmentMaintenance, self).__init__(parent)
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

        self.open_equipment_page()
        self.create_equipment()
        self.view_equipment()
        self.edit_equipment()
        self.verticalLayout.addWidget(self.stackedWidget)
        self.stackedWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(self)


    def show_equipment_page(self):
        self.update_equipment_table_widget()
        self.stackedWidget.setCurrentIndex(0)
    
    def show_create_equipment_page(self):
        generate_id("Equipments", self.create_equipment_id_output_label)
        self.stackedWidget.setCurrentIndex(1)
    
    def show_view_equipment_page(self):
        self.stackedWidget.setCurrentIndex(2)

    def show_edit_equipment_page(self):
        self.stackedWidget.setCurrentIndex(3)

    def open_equipment_page(self):
        self.equipment_page = QWidget()
        self.equipment_page.setObjectName("equipment_page")

        # ===========================================
        #         MANAGE MEMBER PAGE LABELS
        # ===========================================
        self.manage_employee_text_label = createLabel(
            parent=self.equipment_page,
            name="manage_members_text",
            geometry=QRect(120, 40, 350, 40),
            text="Manage Equipments",
            font=font4,
            style="font: bold"
        )

        self.manage_search_text_label = createLabel(
            parent=self.equipment_page,
            name="manage_members_text",
            geometry=QRect(30, 140, 90, 40),
            text="Search:",
            font=font1,
            style=""
        )

        # ===========================================
        #      MANAGE MEMBER PAGE LINE INPUTS
        # ===========================================
        self.equipment_manage_input = createLineInput(
            parent=self.equipment_page,
            name="search_input",
            geometry=QRect(130, 140, 580, 40),
            font=font2,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        self.equipment_manage_input.setPlaceholderText("Equipment ID / Name")
        self.equipment_manage_input.textChanged.connect(lambda: self.search_equipment(self.equipment_table_widget, self.equipment_manage_input))
        # ===========================================
        #         MANAGE MEMBER TABLE WIDGET
        # ===========================================
        self.equipment_table_widget = QTableWidget(self.equipment_page)
        self.equipment_table_widget.setGeometry(QRect(10, 200, 930, 590))
        self.equipment_table_widget.setRowCount(0)
        self.equipment_table_widget.setColumnCount(6)  # Limited columns

        # Set the horizontal header labels
        self.equipment_table_widget.setHorizontalHeaderLabels(
            ["Equipment ID", "Name", "Serial Number", "Category", "Status", "Actions"]
        )

        self.stackedWidget.addWidget(self.equipment_page)
        self.equipment_table_widget.resizeColumnsToContents()
        self.equipment_table_widget.resizeRowsToContents()
        self.equipment_table_widget.horizontalHeader().setStretchLastSection(True)
        self.equipment_table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


        #         MANAGE MEMBER BUTTONS
        # ===========================================
        self.equipment_back_button = createButton(
            parent=self.equipment_page,
            name="back_button",
            geometry=QRect(20, 40, 70, 50),
            text="Back",
            font=font2,
            style=""
        )

        self.equipment_add_button = createButton(
            parent=self.equipment_page,
            name="add_button",
            geometry=QRect(680, 40, 250, 50),
            text="Add Equipments",
            font=font2,
            style="background-color: #28a745; color: #FFFFFF"
        )
        self.equipment_add_button.clicked.connect(self.show_create_equipment_page)

    def create_equipment(self):
        self.create_equipment_page = QWidget()
        self.create_equipment_page.setObjectName("main_page")
        self.stackedWidget.addWidget(self.create_equipment_page)
       
        # ===========================================
        #            EQUIPMENT PAGE LABELS
        # ===========================================

        self.create_equipment_text_label = createLabel(
            parent = self.create_equipment_page,
            name = "create_equipment_text",
            geometry = QRect(280, 50, 430, 40),
            text = "Register Equipment",
            font = font4,
            style = "font: bold"
        )

        self.create_equipment_id_label = createLabel(
            parent = self.create_equipment_page,
            name = "create_equipment_id",
            geometry = QRect(40, 150, 165, 40),
            text = "Equipment ID:",
            font = font1,
            style = ""
        )

        self.create_equipment_name_label = createLabel(
            parent = self.create_equipment_page,
            name = "create_equipment_name",
            geometry = QRect(40, 230, 210, 40),
            text = "Equipment Name",
            font = font1,
            style = ""
        )

        self.create_equipment_serial_number_label = createLabel(
            parent = self.create_equipment_page,
            name = "serial_number",
            geometry = QRect(40, 350, 170, 40),
            text = "Serial Number",
            font = font1,
            style = ""
        )

        self.create_equipment_category_label = createLabel(
            parent = self.create_equipment_page,
            name = "create_equipment_category",
            geometry = QRect(490, 350, 110, 40),
            text = "Category",
            font = font1,
            style = ""
        )

        self.create_equipment_status_label = createLabel(
            parent = self.create_equipment_page,
            name = "create_equipment_status",
            geometry = QRect(750, 350, 110, 40),
            text = "Status",
            font = font1,
            style = ""
        )

        self.create_equipment_purchase_date_label = createLabel(
            parent = self.create_equipment_page,
            name = "purchase_date",
            geometry = QRect(40, 470, 170, 40),
            text = "Purchase Date",
            font = font1,
            style = ""
        )

        self.create_equipment_warranty_date_label = createLabel(
            parent = self.create_equipment_page,
            name = "warranty_date",
            geometry = QRect(260, 470, 190, 40),
            text = "Warranty Expiry",
            font = font1,
            style = ""
        )

        self.create_equipment_price_label = createLabel(
            parent = self.create_equipment_page,
            name = "price",
            geometry = QRect(480, 470, 190, 40),
            text = "Equipment Price",
            font = font1,
            style = ""
        )

        self.create_equipment_manufacturer_label = createLabel(
            parent = self.create_equipment_page,
            name = "manufacturer",
            geometry = QRect(40, 590, 160, 40),
            text = "Manufacturer",
            font = font1,
            style = ""
        )

        self.create_equipment_location_label = createLabel(
            parent = self.create_equipment_page,
            name = "location",
            geometry = QRect(490, 590, 130, 40),
            text = "Location",
            font = font1,
            style = ""
        )


        self.create_equipment_id_output_label = createLabel(
            parent = self.create_equipment_page,
            name = "id_output",
            geometry = QRect(220, 150, 300, 40),
            text = "",
            font = font1,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # ===========================================
        #            EQUIPMENT PAGE INPUTS
        # ===========================================

        self.create_equipment_name_input = createLineInput(
            parent = self.create_equipment_page,
            name = "name_input",
            geometry = QRect(40, 280, 430, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.create_equipment_serial_number_input = createLineInput(
            parent = self.create_equipment_page,
            name = "serial_number_input ",
            geometry = QRect(40, 400, 430, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.create_equipment_price_input = createLineInput(
            parent = self.create_equipment_page,
            name = "price_input",
            geometry = QRect(480, 520, 250, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.create_equipment_manufacturer_input = createLineInput(
            parent = self.create_equipment_page,
            name = "manufacturer_input",
            geometry = QRect(40, 630, 430, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.create_equipment_location_input = createLineInput(
            parent = self.create_equipment_page,
            name = "location_input",
            geometry = QRect(490, 630, 430, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # ===========================================
        #            EQUIPMENT COMBO BOX
        # ===========================================


        self.create_equipment_category_combo_box = createComboBox(
            parent = self.create_equipment_page,
            name = "category",
            geometry = QRect(490, 400, 250, 40),
            font = font2,
            item = ["Cardio", "Strength", "Flexibility", "Functional Training", "Bodyweight", "Core and Stability", "Others"],
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.create_equipment_status_combo_box = createComboBox(
            parent = self.create_equipment_page,
            name = "status",
            geometry = QRect(750, 400, 180, 40),
            font = font2,
            item = ["Active", "Repair", "Retired"],
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # ===========================================
        #               EQUIPMENT DATE
        # ===========================================

        self.create_equipment_purchase_date = createDate(
            parent = self.create_equipment_page,
            name = "purchase_date",
            geometry = QRect(40, 520, 200, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )


        self.create_equipment_warranty_date = createDate(
            parent = self.create_equipment_page,
            name = "warranty_expiry",
            geometry = QRect(260, 520, 200, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"

        )

        # ===========================================
        #               EQUIPMENT BUTTONS
        # ===========================================

        self.create_equipment_back_button = createButton(
            parent = self.create_equipment_page,
            name = "back_button",
            geometry = QRect(40, 50, 70, 50),
            text = "Back",
            font = font3,
            style = "background-color: #004F9A"
        )

        self.create_equipment_clear_button = createButton(
            parent = self.create_equipment_page,
            name = "clear_button",
            geometry = QRect(510, 730, 170, 50),
            text = "Clear",
            font = font3,
            style = "background-color: #882400"
        )

        # REGISTER BUTTON
        self.create_equipment_register_button = createButton(
            parent = self.create_equipment_page,
            name = "register_button",
            geometry = QRect(690, 730, 250, 50),
            text = "Register Equipment",
            font = font3,
            style = "background-color: #006646"
        )
        self.update_equipment_table_widget()
        self.create_equipment_back_button.clicked.connect(self.show_equipment_page)
        self.create_equipment_register_button.clicked.connect(lambda: register_entity("Equipments", self.assigned_inputs("Equipments")))

    def edit_equipment(self):
        self.edit_equipment_page = QWidget()
        self.edit_equipment_page.setObjectName("main_page")
        self.stackedWidget.addWidget(self.edit_equipment_page)
       
        # ===========================================
        #            EQUIPMENT PAGE LABELS
        # ===========================================

        self.edit_equipment_text_label = createLabel(
            parent = self.edit_equipment_page,
            name = "edit_equipment_text",
            geometry = QRect(280, 50, 430, 40),
            text = "Register Equipment",
            font = font4,
            style = "font: bold"
        )

        self.edit_equipment_id_label = createLabel(
            parent = self.edit_equipment_page,
            name = "edit_equipment_id",
            geometry = QRect(40, 150, 165, 40),
            text = "Equipment ID:",
            font = font1,
            style = ""
        )

        self.edit_equipment_name_label = createLabel(
            parent = self.edit_equipment_page,
            name = "edit_equipment_name",
            geometry = QRect(40, 230, 210, 40),
            text = "Equipment Name",
            font = font1,
            style = ""
        )

        self.edit_equipment_serial_number_label = createLabel(
            parent = self.edit_equipment_page,
            name = "serial_number",
            geometry = QRect(40, 350, 170, 40),
            text = "Serial Number",
            font = font1,
            style = ""
        )

        self.edit_equipment_category_label = createLabel(
            parent = self.edit_equipment_page,
            name = "edit_equipment_category",
            geometry = QRect(490, 350, 110, 40),
            text = "Category",
            font = font1,
            style = ""
        )

        self.edit_equipment_status_label = createLabel(
            parent = self.edit_equipment_page,
            name = "edit_equipment_status",
            geometry = QRect(750, 350, 110, 40),
            text = "Status",
            font = font1,
            style = ""
        )

        self.edit_equipment_purchase_date_label = createLabel(
            parent = self.edit_equipment_page,
            name = "purchase_date",
            geometry = QRect(40, 470, 170, 40),
            text = "Purchase Date",
            font = font1,
            style = ""
        )

        self.edit_equipment_warranty_date_label = createLabel(
            parent = self.edit_equipment_page,
            name = "warranty_date",
            geometry = QRect(260, 470, 190, 40),
            text = "Warranty Expiry",
            font = font1,
            style = ""
        )

        self.edit_equipment_price_label = createLabel(
            parent = self.edit_equipment_page,
            name = "price",
            geometry = QRect(480, 470, 190, 40),
            text = "Equipment Price",
            font = font1,
            style = ""
        )

        self.edit_equipment_manufacturer_label = createLabel(
            parent = self.edit_equipment_page,
            name = "manufacturer",
            geometry = QRect(40, 590, 160, 40),
            text = "Manufacturer",
            font = font1,
            style = ""
        )

        self.edit_equipment_location_label = createLabel(
            parent = self.edit_equipment_page,
            name = "location",
            geometry = QRect(490, 590, 130, 40),
            text = "Location",
            font = font1,
            style = ""
        )


        self.edit_equipment_id_output_label = createLabel(
            parent = self.edit_equipment_page,
            name = "id_output",
            geometry = QRect(220, 150, 300, 40),
            text = "",
            font = font1,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # ===========================================
        #            EQUIPMENT PAGE INPUTS
        # ===========================================

        self.edit_equipment_name_input = createLineInput(
            parent = self.edit_equipment_page,
            name = "name_input",
            geometry = QRect(40, 280, 430, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.edit_equipment_serial_number_input = createLineInput(
            parent = self.edit_equipment_page,
            name = "serial_number_input ",
            geometry = QRect(40, 400, 430, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.edit_equipment_price_input = createLineInput(
            parent = self.edit_equipment_page,
            name = "price_input",
            geometry = QRect(480, 520, 250, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.edit_equipment_manufacturer_input = createLineInput(
            parent = self.edit_equipment_page,
            name = "manufacturer_input",
            geometry = QRect(40, 630, 430, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.edit_equipment_location_input = createLineInput(
            parent = self.edit_equipment_page,
            name = "location_input",
            geometry = QRect(490, 630, 430, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # ===========================================
        #            EQUIPMENT COMBO BOX
        # ===========================================


        self.edit_equipment_category_combo_box = createComboBox(
            parent = self.edit_equipment_page,
            name = "category",
            geometry = QRect(490, 400, 250, 40),
            font = font2,
            item = ["Cardio", "Strength", "Flexibility", "Functional Training", "Bodyweight", "Core and Stability", "Others"],
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.edit_equipment_status_combo_box = createComboBox(
            parent = self.edit_equipment_page,
            name = "status",
            geometry = QRect(750, 400, 180, 40),
            font = font2,
            item = ["Active", "Repair", "Retired"],
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # ===========================================
        #               EQUIPMENT DATE
        # ===========================================

        self.edit_equipment_purchase_date = createDate(
            parent = self.edit_equipment_page,
            name = "purchase_date",
            geometry = QRect(40, 520, 200, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.edit_equipment_warranty_date = createDate(
            parent = self.edit_equipment_page,
            name = "warranty_expiry",
            geometry = QRect(260, 520, 200, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"

        )

        # ===========================================
        #               EQUIPMENT BUTTONS
        # ===========================================

        self.edit_equipment_back_button = createButton(
            parent = self.edit_equipment_page,
            name = "back_button",
            geometry = QRect(40, 50, 70, 50),
            text = "Back",
            font = font3,
            style = "background-color: #004F9A"
        )

        self.edit_equipment_clear_button = createButton(
            parent = self.edit_equipment_page,
            name = "clear_button",
            geometry = QRect(510, 730, 170, 50),
            text = "Cance;",
            font = font3,
            style = "background-color: #882400"
        )

        # REGISTER BUTTON
        self.edit_equipment_register_button = createButton(
            parent = self.edit_equipment_page,
            name = "register_button",
            geometry = QRect(690, 730, 250, 50),
            text = "Edit",
            font = font3,
            style = "background-color: #006646"
        )

        self.edit_equipment_back_button.clicked.connect(self.show_view_equipment_page)
        self.edit_equipment_register_button.clicked.connect(lambda: update_entity("Equipments", self.assigned_inputs('Update Equipments')))

    def view_equipment(self):
        self.view_equipment_page = QWidget()
        self.view_equipment_page.setObjectName("main_page")
        self.stackedWidget.addWidget(self.view_equipment_page)

        # ===========================================
        #            EQUIPMENT PAGE LABELS
        # ===========================================

        self.view_equipment_text_label = createLabel(
            parent=self.view_equipment_page,
            name="view_equipment_text",
            geometry=QRect(280, 50, 430, 40),
            text="Register Equipment",
            font=font4,
            style="font: bold"
        )

        self.view_equipment_id_label = createLabel(
            parent=self.view_equipment_page,
            name="view_equipment_id",
            geometry=QRect(40, 150, 165, 40),
            text="Equipment ID:",
            font=font1,
            style=""
        )

        self.view_equipment_name_label = createLabel(
            parent=self.view_equipment_page,
            name="view_equipment_name",
            geometry=QRect(40, 230, 210, 40),
            text="Equipment Name",
            font=font1,
            style=""
        )

        self.view_equipment_serial_number_label = createLabel(
            parent=self.view_equipment_page,
            name="serial_number",
            geometry=QRect(40, 350, 170, 40),
            text="Serial Number",
            font=font1,
            style=""
        )

        self.view_equipment_category_label = createLabel(
            parent=self.view_equipment_page,
            name="view_equipment_category",
            geometry=QRect(490, 350, 110, 40),
            text="Category",
            font=font1,
            style=""
        )

        self.view_equipment_status_label = createLabel(
            parent=self.view_equipment_page,
            name="view_equipment_status",
            geometry=QRect(750, 350, 110, 40),
            text="Status",
            font=font1,
            style=""
        )

        self.view_equipment_purchase_date_label = createLabel(
            parent=self.view_equipment_page,
            name="purchase_date",
            geometry=QRect(40, 470, 170, 40),
            text="Purchase Date",
            font=font1,
            style=""
        )

        self.view_equipment_warranty_date_label = createLabel(
            parent=self.view_equipment_page,
            name="warranty_date",
            geometry=QRect(260, 470, 190, 40),
            text="Warranty Expiry",
            font=font1,
            style=""
        )

        self.view_equipment_price_label = createLabel(
            parent=self.view_equipment_page,
            name="price",
            geometry=QRect(480, 470, 190, 40),
            text="Equipment Price",
            font=font1,
            style=""
        )

        self.view_equipment_manufacturer_label = createLabel(
            parent=self.view_equipment_page,
            name="manufacturer",
            geometry=QRect(40, 590, 160, 40),
            text="Manufacturer",
            font=font1,
            style=""
        )

        self.view_equipment_location_label = createLabel(
            parent=self.view_equipment_page,
            name="location",
            geometry=QRect(490, 590, 130, 40),
            text="Location",
            font=font1,
            style=""
        )

        self.view_equipment_id_output_label = createLabel(
            parent=self.view_equipment_page,
            name="id_output",
            geometry=QRect(220, 150, 300, 40),
            text="",
            font=font1,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        # ===========================================
        #            EQUIPMENT PAGE INPUTS
        # ===========================================

        self.view_equipment_name_input = createLabel(
            parent=self.view_equipment_page,
            name="name_input",
            geometry=QRect(40, 280, 430, 40),
            text="",
            font=font2,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        self.view_equipment_serial_number_input = createLabel(
            parent=self.view_equipment_page,
            name="serial_number_input",
            geometry=QRect(40, 400, 430, 40),
            text="",
            font=font2,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        self.view_equipment_price_input = createLabel(
            parent=self.view_equipment_page,
            name="price_input",
            geometry=QRect(480, 520, 250, 40),
            text="",
            font=font2,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        self.view_equipment_manufacturer_input = createLabel(
            parent=self.view_equipment_page,
            name="manufacturer_input",
            geometry=QRect(40, 630, 430, 40),
            text="",
            font=font2,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        self.view_equipment_location_input = createLabel(
            parent=self.view_equipment_page,
            name="location_input",
            geometry=QRect(490, 630, 430, 40),
            text="",
            font=font2,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        # ===========================================
        #            EQUIPMENT COMBO BOX
        # ===========================================

        self.view_equipment_category_combo_box = createLabel(
            parent=self.view_equipment_page,
            name="category",
            geometry=QRect(490, 400, 250, 40),
            text="",
            font=font2,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        self.view_equipment_status_combo_box = createLabel(
            parent=self.view_equipment_page,
            name="status",
            geometry=QRect(750, 400, 180, 40),
            text="",
            font=font2,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        # ===========================================
        #               EQUIPMENT DATE
        # ===========================================

        self.view_equipment_purchase_date = createLabel(
            parent=self.view_equipment_page,
            name="purchase_date",
            geometry=QRect(40, 520, 200, 40),
            text="",
            font=font2,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        self.view_equipment_warranty_date = createLabel(
            parent=self.view_equipment_page,
            name="warranty_expiry",
            geometry=QRect(260, 520, 200, 40),
            text="",
            font=font2,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        # ===========================================
        #               EQUIPMENT BUTTONS
        # ===========================================

        self.view_equipment_back_button = createButton(
            parent=self.view_equipment_page,
            name="back_button",
            geometry=QRect(40, 50, 70, 50),
            text="Back",
            font=font3,
            style="background-color: #004F9A"
        )

        self.view_equipment_edit_button = createButton(
            parent=self.view_equipment_page,
            name="register_button",
            geometry=QRect(690, 730, 250, 50),
            text="Register Equipment",
            font=font3,
            style="background-color: #006646"
        )
        self.view_equipment_back_button.clicked.connect(self.show_equipment_page)
        self.view_equipment_edit_button.clicked.connect(lambda: self.edit_equipment_button())

    def edit_equipment_button(self):
        # Get the equipment details from the UI labels
        equipment_id = self.view_equipment_id_output_label.text()
        equipment_name = self.view_equipment_name_input.text()
        equipment_serial_number = self.view_equipment_serial_number_input.text()
        equipment_category = self.view_equipment_category_combo_box.text()
        equipment_purchase_date = self.view_equipment_purchase_date.text()
        equipment_warranty_expiry = self.view_equipment_warranty_date.text()
        equipment_price = self.view_equipment_price_input.text()
        equipment_manufacturer = self.view_equipment_manufacturer_input.text()
        equipment_location = self.view_equipment_location_input.text()
        equipment_status = self.view_equipment_status_combo_box.text()

        # Convert string dates to datetime objects
        equipment_purchase_date = datetime.strptime(equipment_purchase_date, '%Y-%m-%d')
        equipment_warranty_expiry = datetime.strptime(equipment_warranty_expiry, '%Y-%m-%d')

        # Set the fetched data into the corresponding input fields for editing
        self.edit_equipment_id_output_label.setText(equipment_id)
        self.edit_equipment_name_input.setText(equipment_name)
        self.edit_equipment_serial_number_input.setText(equipment_serial_number)
        self.edit_equipment_category_combo_box.setCurrentText(equipment_category)
        self.edit_equipment_purchase_date.setDate(equipment_purchase_date)
        self.edit_equipment_warranty_date.setDate(equipment_warranty_expiry)
        self.edit_equipment_price_input.setText(equipment_price)
        self.edit_equipment_manufacturer_input.setText(equipment_manufacturer)
        self.edit_equipment_location_input.setText(equipment_location)
        self.edit_equipment_status_combo_box.setCurrentText(equipment_status)

        # Update the table widget if necessary
        self.update_equipment_table_widget()

        # Show the edit equipment page
        self.show_edit_equipment_page()


    def show_view_equipment_temp(self, row):
        # Get the equipment_id from the table widget
        equipment_id = self.equipment_table_widget.item(row, 0).text()

        # Execute SQL query to fetch equipment details
        cursor.execute(
            """
            SELECT * 
            FROM Equipments
            WHERE equipment_id = ?
            """,
            (equipment_id,)
        )

        results = cursor.fetchone()

        # Unpack the results into corresponding variables
        (
            equipment_id, 
            equipment_name, 
            equipment_serial_number, 
            equipment_category, 
            equipment_purchase_date, 
            equipment_warranty_expiry, 
            equipment_price, 
            equipment_manufacturer, 
            equipment_location, 
            equipment_status
        ) = results

        # Update the UI elements with the fetched data
        self.view_equipment_id_output_label.setText(equipment_id)
        self.view_equipment_name_input.setText(equipment_name)
        self.view_equipment_serial_number_input.setText(equipment_serial_number)
        self.view_equipment_category_combo_box.setText(equipment_category)
        self.view_equipment_purchase_date.setText(equipment_purchase_date)
        self.view_equipment_warranty_date.setText(equipment_warranty_expiry)
        self.view_equipment_price_input.setText(str(equipment_price))
        self.view_equipment_manufacturer_input.setText(equipment_manufacturer)
        self.view_equipment_location_input.setText(equipment_location)
        self.view_equipment_status_combo_box.setText(equipment_status)

        # Show the equipment details view
        self.show_view_equipment_page()
        
    def assigned_inputs(self, entity_type):
        if entity_type == 'Equipments':
            INPUTS = {
            'equipment_id': self.create_equipment_id_output_label.text(), 
            'equipment_name': self.create_equipment_name_input.text(), 
            'equipment_serial_number': self.create_equipment_serial_number_input.text(), 
            'equipment_category': self.create_equipment_category_combo_box.currentText(), 
            'equipment_purchase_date': self.create_equipment_purchase_date.date().toString('yyyy-MM-dd'),
            'equipment_warranty_expiry': self.create_equipment_warranty_date.date().toString('yyyy-MM-dd'),
            'equipment_price': self.create_equipment_price_input.text(),
            'equipment_manufacturer': self.create_equipment_manufacturer_input.text(),
            'equipment_location': self.create_equipment_location_input.text(),
            'equipment_status': self.create_equipment_status_combo_box.currentText(),
        }
            
        elif entity_type == 'Update Equipments':
            INPUTS = {
            'equipment_id': self.edit_equipment_id_output_label.text(),
            'equipment_name': self.edit_equipment_name_input.text(),
            'equipment_serial_number': self.edit_equipment_serial_number_input.text(),
            'equipment_category': self.edit_equipment_category_combo_box.currentText(),
            'equipment_purchase_date': self.edit_equipment_purchase_date.date(),
            'equipment_warranty_expiry': self.edit_equipment_warranty_date.date(),
            'equipment_price': self.edit_equipment_price_input.text(),
            'equipment_manufacturer': self.edit_equipment_manufacturer_input.text(),
            'equipment_location': self.edit_equipment_location_input.text(),
            'equipment_status': self.edit_equipment_status_combo_box.currentText(),
        }
            

        return INPUTS

    def update_equipment_table_widget(self):
        data = self.fetch_equipment_by_column()
        self.equipment_table_widget.setRowCount(len(data))
        for row_index, row_data in enumerate(data):
            for col_index, col_data in enumerate(row_data):
                self.equipment_table_widget.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))
            
        for self.row in range(self.equipment_table_widget.rowCount()):
            view_button = QPushButton("View")
            view_button.clicked.connect(partial(self.show_view_equipment_temp, self.row))
            self.equipment_table_widget.setCellWidget(self.row, 5, view_button)

    def fetch_equipment_by_column(self):
        # Define your SQL query to select columns from the Equipments table
        query = """SELECT 
                    equipment_id, 
                    equipment_name,
                    equipment_serial_number,
                    equipment_category,
                    equipment_status
                FROM Equipments"""
        # Execute the query
        cursor.execute(query)
        # Fetch all results from the query
        data = cursor.fetchall()
        # Return the fetched data
        return data
    
    def search_equipment(self, table_widget, input_text):
        search_term = input_text.text()
        query = """
            SELECT equipment_id,
                equipment_name,
                equipment_serial_number,
                equipment_category,
                equipment_status,
                equipment_purchase_date
            FROM Equipments
            WHERE equipment_id LIKE ? 
            OR equipment_name LIKE ? 
            OR equipment_serial_number LIKE ?;
        """
        try:
            cursor.execute(query, (f'%{search_term}%', f'%{search_term}%', f'%{search_term}%'))
            results = cursor.fetchall()

            table_widget.setRowCount(len(results))
            for row_idx, row_data in enumerate(results):
                for col_idx, col_data in enumerate(row_data):
                    table_widget.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))
                view_button = QPushButton("View")
                view_button.clicked.connect(partial(self.show_view_equipment_temp, row_idx))
                table_widget.setCellWidget(row_idx, len(row_data), view_button)

            self.add_equipment_view_button(table_widget)  # Call the function to add view buttons

        except Exception as e:
            print(f"Error executing query for Equipment: {e}")

    def add_equipment_view_button(self, table_widget):
        for row_idx in range(table_widget.rowCount()):
            view_button = QPushButton("View")
            view_button.clicked.connect(partial(self.show_view_equipment_temp, row_idx))
            table_widget.setCellWidget(row_idx, 5, view_button)  # Adjusted for the number of columns
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = EquipmentMaintenance()
    window.show()
    sys.exit(app.exec_())