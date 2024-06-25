
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

        self.view_equipment()
        self.open_equipment_page()
        self.verticalLayout.addWidget(self.stackedWidget)
        self.stackedWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(self)

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
        self.manage_search_input = createLineInput(
            parent=self.equipment_page,
            name="search_input",
            geometry=QRect(130, 140, 580, 40),
            font=font2,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        self.manage_search_input.setPlaceholderText("Equipment ID / Name")

        # ===========================================
        #         MANAGE MEMBER TABLE WIDGET
        # ===========================================
        self.table_widget = QTableWidget(self.equipment_page)
        self.table_widget.setGeometry(QRect(10, 200, 930, 590))
        self.table_widget.setRowCount(0)
        self.table_widget.setColumnCount(6)  # Limited columns

        # Set the horizontal header labels
        self.table_widget.setHorizontalHeaderLabels(
            ["Equipment ID", "Name", "Serial Number", "Category", "Status", "Actions"]
        )

        self.stackedWidget.addWidget(self.equipment_page)
        self.table_widget.resizeColumnsToContents()
        self.table_widget.resizeRowsToContents()
        self.table_widget.horizontalHeader().setStretchLastSection(True)
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


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

    def create_equipment(self):
        self.create_equipment_page = QWidget()
        self.create_equipment_page.setObjectName("main_page")
        self.stackedWidget.addWidget(self.create_equipment_page)
       
        # ===========================================
        #            EQUIPMENT PAGE LABELS
        # ===========================================

        self.equipment_text_label = createLabel(
            parent = self.create_equipment_page,
            name = "equipment_text",
            geometry = QRect(280, 50, 430, 40),
            text = "Register Equipment",
            font = font4,
            style = "font: bold"
        )

        self.equipment_id_label = createLabel(
            parent = self.create_equipment_page,
            name = "equipment_id",
            geometry = QRect(40, 150, 165, 40),
            text = "Equipment ID:",
            font = font1,
            style = ""
        )

        self.equipment_name_label = createLabel(
            parent = self.create_equipment_page,
            name = "equipment_name",
            geometry = QRect(40, 230, 210, 40),
            text = "Equipment Name",
            font = font1,
            style = ""
        )

        self.equipment_serial_number_label = createLabel(
            parent = self.create_equipment_page,
            name = "serial_number",
            geometry = QRect(40, 350, 170, 40),
            text = "Serial Number",
            font = font1,
            style = ""
        )

        self.equipment_category_label = createLabel(
            parent = self.create_equipment_page,
            name = "equipment_category",
            geometry = QRect(490, 350, 110, 40),
            text = "Category",
            font = font1,
            style = ""
        )

        self.equipment_status_label = createLabel(
            parent = self.create_equipment_page,
            name = "equipment_status",
            geometry = QRect(750, 350, 110, 40),
            text = "Status",
            font = font1,
            style = ""
        )

        self.equipment_purchase_date_label = createLabel(
            parent = self.create_equipment_page,
            name = "purchase_date",
            geometry = QRect(40, 470, 170, 40),
            text = "Purchase Date",
            font = font1,
            style = ""
        )

        self.equipment_warranty_date_label = createLabel(
            parent = self.create_equipment_page,
            name = "warranty_date",
            geometry = QRect(260, 470, 190, 40),
            text = "Warranty Expiry",
            font = font1,
            style = ""
        )

        self.equipment_price_label = createLabel(
            parent = self.create_equipment_page,
            name = "price",
            geometry = QRect(480, 470, 190, 40),
            text = "Equipment Price",
            font = font1,
            style = ""
        )

        self.equipment_manufacturer_label = createLabel(
            parent = self.create_equipment_page,
            name = "manufacturer",
            geometry = QRect(40, 590, 160, 40),
            text = "Manufacturer",
            font = font1,
            style = ""
        )

        self.equipment_location_label = createLabel(
            parent = self.create_equipment_page,
            name = "location",
            geometry = QRect(490, 590, 130, 40),
            text = "Location",
            font = font1,
            style = ""
        )


        self.equipment_id_output_label = createLabel(
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

        self.equipment_name_input = createLineInput(
            parent = self.create_equipment_page,
            name = "name_input",
            geometry = QRect(40, 280, 430, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.equipment_serial_number_input = createLineInput(
            parent = self.create_equipment_page,
            name = "serial_number_input ",
            geometry = QRect(40, 400, 430, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.equipment_price_input = createLineInput(
            parent = self.create_equipment_page,
            name = "price_input",
            geometry = QRect(480, 520, 250, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.equipment_manufacturer_input = createLineInput(
            parent = self.create_equipment_page,
            name = "manufacturer_input",
            geometry = QRect(40, 630, 430, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.equipment_location_input = createLineInput(
            parent = self.create_equipment_page,
            name = "location_input",
            geometry = QRect(490, 630, 430, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # ===========================================
        #            EQUIPMENT COMBO BOX
        # ===========================================


        self.equipment_category_combo_box = createComboBox(
            parent = self.create_equipment_page,
            name = "category",
            geometry = QRect(490, 400, 250, 40),
            font = font2,
            item = ["Cardio", "Strength", "Flexibility", "Functional Training", "Bodyweight", "Core and Stability", "Others"],
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.equipment_status_combo_box = createComboBox(
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

        self.equipment_purchase_date = createDate(
            parent = self.create_equipment_page,
            name = "purchase_date",
            geometry = QRect(40, 520, 200, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.equipment_warranty_date = createDate(
            parent = self.create_equipment_page,
            name = "warranty_expiry",
            geometry = QRect(260, 520, 200, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"

        )

        # ===========================================
        #               EQUIPMENT BUTTONS
        # ===========================================

        self.equipment_back_button = createButton(
            parent = self.create_equipment_page,
            name = "back_button",
            geometry = QRect(40, 50, 70, 50),
            text = "Back",
            font = font3,
            style = "background-color: #004F9A"
        )

        self.equipment_clear_button = createButton(
            parent = self.create_equipment_page,
            name = "clear_button",
            geometry = QRect(510, 730, 170, 50),
            text = "Clear",
            font = font3,
            style = "background-color: #882400"
        )

        # REGISTER BUTTON
        self.equipment_register_button = createButton(
            parent = self.create_equipment_page,
            name = "register_button",
            geometry = QRect(690, 730, 250, 50),
            text = "Register Equipment",
            font = font3,
            style = "background-color: #006646"
        )

    def edit_equipment(self):
        self.edit_equipment_page = QWidget()
        self.edit_equipment_page.setObjectName("main_page")
        self.stackedWidget.addWidget(self.edit_equipment_page)
       
        # ===========================================
        #            EQUIPMENT PAGE LABELS
        # ===========================================

        self.equipment_text_label = createLabel(
            parent = self.edit_equipment_page,
            name = "equipment_text",
            geometry = QRect(280, 50, 430, 40),
            text = "Register Equipment",
            font = font4,
            style = "font: bold"
        )

        self.equipment_id_label = createLabel(
            parent = self.edit_equipment_page,
            name = "equipment_id",
            geometry = QRect(40, 150, 165, 40),
            text = "Equipment ID:",
            font = font1,
            style = ""
        )

        self.equipment_name_label = createLabel(
            parent = self.edit_equipment_page,
            name = "equipment_name",
            geometry = QRect(40, 230, 210, 40),
            text = "Equipment Name",
            font = font1,
            style = ""
        )

        self.equipment_serial_number_label = createLabel(
            parent = self.edit_equipment_page,
            name = "serial_number",
            geometry = QRect(40, 350, 170, 40),
            text = "Serial Number",
            font = font1,
            style = ""
        )

        self.equipment_category_label = createLabel(
            parent = self.edit_equipment_page,
            name = "equipment_category",
            geometry = QRect(490, 350, 110, 40),
            text = "Category",
            font = font1,
            style = ""
        )

        self.equipment_status_label = createLabel(
            parent = self.edit_equipment_page,
            name = "equipment_status",
            geometry = QRect(750, 350, 110, 40),
            text = "Status",
            font = font1,
            style = ""
        )

        self.equipment_purchase_date_label = createLabel(
            parent = self.edit_equipment_page,
            name = "purchase_date",
            geometry = QRect(40, 470, 170, 40),
            text = "Purchase Date",
            font = font1,
            style = ""
        )

        self.equipment_warranty_date_label = createLabel(
            parent = self.edit_equipment_page,
            name = "warranty_date",
            geometry = QRect(260, 470, 190, 40),
            text = "Warranty Expiry",
            font = font1,
            style = ""
        )

        self.equipment_price_label = createLabel(
            parent = self.edit_equipment_page,
            name = "price",
            geometry = QRect(480, 470, 190, 40),
            text = "Equipment Price",
            font = font1,
            style = ""
        )

        self.equipment_manufacturer_label = createLabel(
            parent = self.edit_equipment_page,
            name = "manufacturer",
            geometry = QRect(40, 590, 160, 40),
            text = "Manufacturer",
            font = font1,
            style = ""
        )

        self.equipment_location_label = createLabel(
            parent = self.edit_equipment_page,
            name = "location",
            geometry = QRect(490, 590, 130, 40),
            text = "Location",
            font = font1,
            style = ""
        )


        self.equipment_id_output_label = createLabel(
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

        self.equipment_name_input = createLineInput(
            parent = self.edit_equipment_page,
            name = "name_input",
            geometry = QRect(40, 280, 430, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.equipment_serial_number_input = createLineInput(
            parent = self.edit_equipment_page,
            name = "serial_number_input ",
            geometry = QRect(40, 400, 430, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.equipment_price_input = createLineInput(
            parent = self.edit_equipment_page,
            name = "price_input",
            geometry = QRect(480, 520, 250, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.equipment_manufacturer_input = createLineInput(
            parent = self.edit_equipment_page,
            name = "manufacturer_input",
            geometry = QRect(40, 630, 430, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.equipment_location_input = createLineInput(
            parent = self.edit_equipment_page,
            name = "location_input",
            geometry = QRect(490, 630, 430, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # ===========================================
        #            EQUIPMENT COMBO BOX
        # ===========================================


        self.equipment_category_combo_box = createComboBox(
            parent = self.edit_equipment_page,
            name = "category",
            geometry = QRect(490, 400, 250, 40),
            font = font2,
            item = ["Cardio", "Strength", "Flexibility", "Functional Training", "Bodyweight", "Core and Stability", "Others"],
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.equipment_status_combo_box = createComboBox(
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

        self.equipment_purchase_date = createDate(
            parent = self.edit_equipment_page,
            name = "purchase_date",
            geometry = QRect(40, 520, 200, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.equipment_warranty_date = createDate(
            parent = self.edit_equipment_page,
            name = "warranty_expiry",
            geometry = QRect(260, 520, 200, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"

        )

        # ===========================================
        #               EQUIPMENT BUTTONS
        # ===========================================

        self.equipment_back_button = createButton(
            parent = self.edit_equipment_page,
            name = "back_button",
            geometry = QRect(40, 50, 70, 50),
            text = "Back",
            font = font3,
            style = "background-color: #004F9A"
        )

        self.equipment_clear_button = createButton(
            parent = self.edit_equipment_page,
            name = "clear_button",
            geometry = QRect(510, 730, 170, 50),
            text = "Clear",
            font = font3,
            style = "background-color: #882400"
        )

        # REGISTER BUTTON
        self.equipment_register_button = createButton(
            parent = self.edit_equipment_page,
            name = "register_button",
            geometry = QRect(690, 730, 250, 50),
            text = "Register Equipment",
            font = font3,
            style = "background-color: #006646"
        )

    def view_equipment(self):
        self.view_equipment_page = QWidget()
        self.view_equipment_page.setObjectName("main_page")
        self.stackedWidget.addWidget(self.view_equipment_page)

        # ===========================================
        #            EQUIPMENT PAGE LABELS
        # ===========================================

        self.equipment_text_label = createLabel(
            parent=self.view_equipment_page,
            name="equipment_text",
            geometry=QRect(280, 50, 430, 40),
            text="Register Equipment",
            font=font4,
            style="font: bold"
        )

        self.equipment_id_label = createLabel(
            parent=self.view_equipment_page,
            name="equipment_id",
            geometry=QRect(40, 150, 165, 40),
            text="Equipment ID:",
            font=font1,
            style=""
        )

        self.equipment_name_label = createLabel(
            parent=self.view_equipment_page,
            name="equipment_name",
            geometry=QRect(40, 230, 210, 40),
            text="Equipment Name",
            font=font1,
            style=""
        )

        self.equipment_serial_number_label = createLabel(
            parent=self.view_equipment_page,
            name="serial_number",
            geometry=QRect(40, 350, 170, 40),
            text="Serial Number",
            font=font1,
            style=""
        )

        self.equipment_category_label = createLabel(
            parent=self.view_equipment_page,
            name="equipment_category",
            geometry=QRect(490, 350, 110, 40),
            text="Category",
            font=font1,
            style=""
        )

        self.equipment_status_label = createLabel(
            parent=self.view_equipment_page,
            name="equipment_status",
            geometry=QRect(750, 350, 110, 40),
            text="Status",
            font=font1,
            style=""
        )

        self.equipment_purchase_date_label = createLabel(
            parent=self.view_equipment_page,
            name="purchase_date",
            geometry=QRect(40, 470, 170, 40),
            text="Purchase Date",
            font=font1,
            style=""
        )

        self.equipment_warranty_date_label = createLabel(
            parent=self.view_equipment_page,
            name="warranty_date",
            geometry=QRect(260, 470, 190, 40),
            text="Warranty Expiry",
            font=font1,
            style=""
        )

        self.equipment_price_label = createLabel(
            parent=self.view_equipment_page,
            name="price",
            geometry=QRect(480, 470, 190, 40),
            text="Equipment Price",
            font=font1,
            style=""
        )

        self.equipment_manufacturer_label = createLabel(
            parent=self.view_equipment_page,
            name="manufacturer",
            geometry=QRect(40, 590, 160, 40),
            text="Manufacturer",
            font=font1,
            style=""
        )

        self.equipment_location_label = createLabel(
            parent=self.view_equipment_page,
            name="location",
            geometry=QRect(490, 590, 130, 40),
            text="Location",
            font=font1,
            style=""
        )

        self.equipment_id_output_label = createLabel(
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

        self.equipment_name_input = createLabel(
            parent=self.view_equipment_page,
            name="name_input",
            geometry=QRect(40, 280, 430, 40),
            text="(Equipment Name Input)",
            font=font2,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        self.equipment_serial_number_input = createLabel(
            parent=self.view_equipment_page,
            name="serial_number_input",
            geometry=QRect(40, 400, 430, 40),
            text="(Serial Number Input)",
            font=font2,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        self.equipment_price_input = createLabel(
            parent=self.view_equipment_page,
            name="price_input",
            geometry=QRect(480, 520, 250, 40),
            text="(Equipment Price Input)",
            font=font2,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        self.equipment_manufacturer_input = createLabel(
            parent=self.view_equipment_page,
            name="manufacturer_input",
            geometry=QRect(40, 630, 430, 40),
            text="(Manufacturer Input)",
            font=font2,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        self.equipment_location_input = createLabel(
            parent=self.view_equipment_page,
            name="location_input",
            geometry=QRect(490, 630, 430, 40),
            text="(Location Input)",
            font=font2,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        # ===========================================
        #            EQUIPMENT COMBO BOX
        # ===========================================

        self.equipment_category_combo_box = createLabel(
            parent=self.view_equipment_page,
            name="category",
            geometry=QRect(490, 400, 250, 40),
            text="(Category Combo Box)",
            font=font2,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        self.equipment_status_combo_box = createLabel(
            parent=self.view_equipment_page,
            name="status",
            geometry=QRect(750, 400, 180, 40),
            text="(Status Combo Box)",
            font=font2,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        # ===========================================
        #               EQUIPMENT DATE
        # ===========================================

        self.equipment_purchase_date = createLabel(
            parent=self.view_equipment_page,
            name="purchase_date",
            geometry=QRect(40, 520, 200, 40),
            text="(Purchase Date Input)",
            font=font2,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        self.equipment_warranty_date = createLabel(
            parent=self.view_equipment_page,
            name="warranty_expiry",
            geometry=QRect(260, 520, 200, 40),
            text="(Warranty Expiry Date Input)",
            font=font2,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        # ===========================================
        #               EQUIPMENT BUTTONS
        # ===========================================

        self.equipment_back_button = createButton(
            parent=self.view_equipment_page,
            name="back_button",
            geometry=QRect(40, 50, 70, 50),
            text="Back",
            font=font3,
            style="background-color: #004F9A"
        )

        self.equipment_clear_button = createButton(
            parent=self.view_equipment_page,
            name="clear_button",
            geometry=QRect(510, 730, 170, 50),
            text="Clear",
            font=font3,
            style="background-color: #882400"
        )

        self.equipment_register_button = createButton(
            parent=self.view_equipment_page,
            name="register_button",
            geometry=QRect(690, 730, 250, 50),
            text="Register Equipment",
            font=font3,
            style="background-color: #006646"
        )





if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Maintenance()
    window.show()
    sys.exit(app.exec_())