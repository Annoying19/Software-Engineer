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

        self.open_product_page()
        self.create_product()
        self.verticalLayout.addWidget(self.stackedWidget)
        self.stackedWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(self)


    def show_create_product(self):
        self.generate_product_id()
        self.stackedWidget.setCurrentIndex(1)

    def open_product_page(self):
        self.product_page = QWidget()
        self.product_page.setObjectName("product_page")

        # ===========================================
        #         MANAGE MEMBER PAGE LABELS
        # ===========================================
        self.manage_employee_text_label = createLabel(
            parent=self.product_page,
            name="manage_members_text",
            geometry=QRect(120, 40, 350, 40),
            text="Manage products",
            font=font4,
            style="font: bold"
        )

        self.manage_search_text_label = createLabel(
            parent=self.product_page,
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
            parent=self.product_page,
            name="search_input",
            geometry=QRect(130, 140, 580, 40),
            font=font2,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        self.manage_search_input.setPlaceholderText("product ID / Name")

        # ===========================================
        #         MANAGE MEMBER TABLE WIDGET
        # ===========================================
        self.table_widget = QTableWidget(self.product_page)
        self.table_widget.setGeometry(QRect(10, 200, 930, 590))
        self.table_widget.setRowCount(0)
        self.table_widget.setColumnCount(6)  # Limited columns

        # Set the horizontal header labels
        self.table_widget.setHorizontalHeaderLabels(
            ["Product ID", "Name", "Serial Number", "Category", "Status", "Actions"]
        )

        self.stackedWidget.addWidget(self.product_page)
        self.table_widget.resizeColumnsToContents()
        self.table_widget.resizeRowsToContents()
        self.table_widget.horizontalHeader().setStretchLastSection(True)
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


        #         MANAGE MEMBER BUTTONS
        # ===========================================
        self.product_back_button = createButton(
            parent=self.product_page,
            name="back_button",
            geometry=QRect(20, 40, 70, 50),
            text="Back",
            font=font2,
            style=""
        )

        self.product_add_button = createButton(
            parent=self.product_page,
            name="add_button",
            geometry=QRect(680, 40, 250, 50),
            text="Add products",
            font=font2,
            style="background-color: #28a745; color: #FFFFFF"
        )

        self.product_add_button.clicked.connect(self.show_create_product)

    def create_product(self):
        self.create_product_page = QWidget()
        self.create_product_page.setObjectName("main_page")
        self.stackedWidget.addWidget(self.create_product_page)
       
        # ===========================================
        #            product PAGE LABELS
        # ===========================================

        self.product_text_label = createLabel(
            parent = self.create_product_page,
            name = "product_text",
            geometry = QRect(280, 50, 430, 40),
            text = "Register Product",
            font = font4,
            style = "font: bold"
        )

        self.product_id_label = createLabel(
            parent = self.create_product_page,
            name = "product_text",
            geometry = QRect(40, 150, 160, 40),
            text = "Product ID:",
            font = font1,
            style = ""
        )

        self.product_name_label = createLabel(
            parent = self.create_product_page,
            name = "product_text",
            geometry = QRect(40, 210, 170, 40),
            text = "Product Name",
            font = font1,
            style = ""
        )

        self.product_brand_label = createLabel(
            parent = self.create_product_page,
            name = "product_text",
            geometry = QRect(380, 210, 170, 40),
            text = "Brand",
            font = font1,
            style = ""
        )

        self.product_sku_label = createLabel(
            parent = self.create_product_page,
            name = "product_text",
            geometry = QRect(40, 310, 130, 40),
            text = "SKU",
            font = font1,
            style = ""
        )

        self.product_quantity_label = createLabel(
            parent = self.create_product_page,
            name = "product_text",
            geometry = QRect(380, 310, 170, 40),
            text = "Quantity",
            font = font1,
            style = ""
        )

        self.product_supplier_label = createLabel(
            parent = self.create_product_page,
            name = "product_text",
            geometry = QRect(40, 420, 130, 40),
            text = "Supplier",
            font = font1,
            style = ""
        )

        self.product_price_label = createLabel(
            parent = self.create_product_page,
            name = "product_text",
            geometry = QRect(380, 420, 160, 40),
            text = "Price",
            font = font1,
            style = ""
        )

        self.product_purchase_label = createLabel(
            parent = self.create_product_page,
            name = "product_text",
            geometry = QRect(40, 530, 180, 40),
            text = "Purchase Date",
            font = font1,
            style = ""
        )

        self.product_price_label = createLabel(
            parent = self.create_product_page,
            name = "product_text",
            geometry = QRect(380, 530, 160, 40),
            text = "Expiry Date",
            font = font1,
            style = ""
        )

        self.product_id_output_label = createLabel(
            parent = self.create_product_page,
            name = "product_text",
            geometry = QRect(210, 150, 360, 40),
            text = "",
            font = font1,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # =================================================================

        self.name_input = createLineInput(
            parent = self.create_product_page,
            name = "name_input",
            geometry = QRect(40, 260, 330, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.brand_input = createLineInput(
            parent = self.create_product_page,
            name = "name_input",
            geometry = QRect(380, 260, 330, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.sku_input = createLineInput(
            parent = self.create_product_page,
            name = "name_input",
            geometry = QRect(40, 360, 330, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.quantity_input = createLineInput(
            parent = self.create_product_page,
            name = "name_input",
            geometry = QRect(380, 360, 200, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.supplier_input = createLineInput(
            parent = self.create_product_page,
            name = "name_input",
            geometry = QRect(40, 470, 330, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.price_input = createLineInput(
            parent = self.create_product_page,
            name = "name_input",
            geometry = QRect(380, 470, 200, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # ===================================================

        self.purchase_date = createDate(
            parent = self.create_product_page,
            name = "purchase_date",
            geometry = QRect(40, 580, 230, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.expiry_date = createDate(
            parent = self.create_product_page,
            name = "purchase_date",
            geometry = QRect(380, 580, 230, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # ====================================================
        self.back_button = createButton(
            parent = self.create_product_page,
            name = "back_button",
            geometry = QRect(40, 50, 70, 50),
            text = "Back",
            font = font3,
            style = "background-color: #004F9A"
        )

        self.clear_button = createButton(
            parent = self.create_product_page,
            name = "clear_button",
            geometry = QRect(510, 730, 170, 50),
            text = "Clear",
            font = font3,
            style = "background-color: #882400"
        )

        # REGISTER BUTTON
        self.register_button = createButton(
            parent = self.create_product_page,
            name = "register_button",
            geometry = QRect(690, 730, 250, 50),
            text = "Register Product",
            font = font3,
            style = "background-color: #006646"
        )

        self.register_button.clicked.connect(self.register_product)

    def edit_product(self):
        self.edit_product_page = QWidget()
        self.edit_product_page.setObjectName("main_page")
        self.stackedWidget.addWidget(self.edit_product_page)
       
        # ===========================================
        #            product PAGE LABELS
        # ===========================================

        self.product_text_label = createLabel(
            parent = self.edit_product_page,
            name = "product_text",
            geometry = QRect(280, 50, 430, 40),
            text = "Register Product",
            font = font4,
            style = "font: bold"
        )

        self.product_id_label = createLabel(
            parent = self.edit_product_page,
            name = "product_text",
            geometry = QRect(40, 150, 160, 40),
            text = "Product ID:",
            font = font1,
            style = ""
        )

        self.product_name_label = createLabel(
            parent = self.edit_product_page,
            name = "product_text",
            geometry = QRect(40, 210, 170, 40),
            text = "Product Name",
            font = font1,
            style = ""
        )

        self.product_brand_label = createLabel(
            parent = self.edit_product_page,
            name = "product_text",
            geometry = QRect(380, 210, 170, 40),
            text = "Brand",
            font = font1,
            style = ""
        )

        self.product_sku_label = createLabel(
            parent = self.edit_product_page,
            name = "product_text",
            geometry = QRect(40, 310, 130, 40),
            text = "SKU",
            font = font1,
            style = ""
        )

        self.product_quantity_label = createLabel(
            parent = self.edit_product_page,
            name = "product_text",
            geometry = QRect(380, 310, 170, 40),
            text = "Quantity",
            font = font1,
            style = ""
        )

        self.product_supplier_label = createLabel(
            parent = self.edit_product_page,
            name = "product_text",
            geometry = QRect(40, 420, 130, 40),
            text = "Supplier",
            font = font1,
            style = ""
        )

        self.product_price_label = createLabel(
            parent = self.edit_product_page,
            name = "product_text",
            geometry = QRect(380, 420, 160, 40),
            text = "Price",
            font = font1,
            style = ""
        )

        self.product_purchase_label = createLabel(
            parent = self.edit_product_page,
            name = "product_text",
            geometry = QRect(40, 530, 180, 40),
            text = "Purchase Date",
            font = font1,
            style = ""
        )

        self.product_price_label = createLabel(
            parent = self.edit_product_page,
            name = "product_text",
            geometry = QRect(380, 530, 160, 40),
            text = "Expiry Date",
            font = font1,
            style = ""
        )

        self.product_id_output_label = createLabel(
            parent = self.edit_product_page,
            name = "product_text",
            geometry = QRect(210, 150, 360, 40),
            text = "",
            font = font1,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # =================================================================

        self.name_input = createLineInput(
            parent = self.edit_product_page,
            name = "name_input",
            geometry = QRect(40, 260, 330, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.brand_input = createLineInput(
            parent = self.edit_product_page,
            name = "name_input",
            geometry = QRect(380, 260, 330, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.sku_input = createLineInput(
            parent = self.edit_product_page,
            name = "name_input",
            geometry = QRect(40, 360, 330, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.quantity_input = createLineInput(
            parent = self.edit_product_page,
            name = "name_input",
            geometry = QRect(380, 360, 200, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.supplier_input = createLineInput(
            parent = self.edit_product_page,
            name = "name_input",
            geometry = QRect(40, 470, 330, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.price_input = createLineInput(
            parent = self.edit_product_page,
            name = "name_input",
            geometry = QRect(380, 470, 200, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # ===================================================

        self.purchase_date = createDate(
            parent = self.edit_product_page,
            name = "purchase_date",
            geometry = QRect(40, 580, 230, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.expiry_date = createDate(
            parent = self.edit_product_page,
            name = "purchase_date",
            geometry = QRect(380, 580, 230, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # ====================================================
        self.back_button = createButton(
            parent = self.edit_product_page,
            name = "back_button",
            geometry = QRect(40, 50, 70, 50),
            text = "Back",
            font = font3,
            style = "background-color: #004F9A"
        )

        self.clear_button = createButton(
            parent = self.edit_product_page,
            name = "clear_button",
            geometry = QRect(510, 730, 170, 50),
            text = "Clear",
            font = font3,
            style = "background-color: #882400"
        )

        # REGISTER BUTTON
        self.register_button = createButton(
            parent = self.edit_product_page,
            name = "register_button",
            geometry = QRect(690, 730, 250, 50),
            text = "Register Product",
            font = font3,
            style = "background-color: #006646"
        )

        

    def register_product(self):
        print("hello")
        product_id = self.product_id_output_label.text()
        name = self.name_input.text()
        brand = self.brand_input.text()
        sku = self.sku_input.text()
        quantity = int(self.quantity_input.text())
        supplier = self.supplier_input.text()
        price = self.price_input.text()
        purchase_date = self.purchase_date.date()
        expiry_date = self.expiry_date.date()

        cursor.execute(
            """
            INSERT INTO Products
            (
            product_id, name, brand, sku, quantity, supplier, price, purchase_date, expiry_date
            ) VALUES
            (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                product_id,
                name,
                brand,
                sku,
                quantity,
                supplier,
                price,
                purchase_date.toString("yyyy-MM-dd"),
                expiry_date.toString("yyyy-MM-dd")
            )
        )

        connection.commit()
    
    def generate_product_id(self):
        
        query = "SELECT COUNT(*) FROM Products"
        cursor.execute(query)
        count = cursor.fetchone()[0] + 1
        identifier = "PD"
        current_time = datetime.now()
        formatted_time = current_time.strftime('%m%d%y')

        generated_id = f"{identifier}-{formatted_time}-{count:04}"
        self.product_id_output_label.setText(generated_id)
        
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Maintenance()
    window.show()
    sys.exit(app.exec_())

