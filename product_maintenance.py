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

        self.open_product()
        self.create_product()
        self.edit_product()
        self.view_product()
        self.verticalLayout.addWidget(self.stackedWidget)
        self.stackedWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(self)


    def show_main_page(self):
        self.update_table_widget()
        self.stackedWidget.setCurrentIndex(0)

    def show_create_product(self):
        self.clear_inputs(self.create_product_page)
        self.generate_product_id()
        self.stackedWidget.setCurrentIndex(1)

    def show_edit_product(self):
        self.stackedWidget.setCurrentIndex(2)

    def show_view_product(self):
        self.stackedWidget.setCurrentIndex(3)

    def open_product(self):
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
            ["Product ID", "Name", " Quantity", "Expiry Date", "Status", "Actions"]
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
        self.update_table_widget()

    def create_product(self):
        self.create_product_page = QWidget()
        self.create_product_page.setObjectName("main_page")
        self.stackedWidget.addWidget(self.create_product_page)
       
        # ===========================================
        #            product PAGE LABELS
        # ===========================================

        self.create_product_text_label = createLabel(
            parent = self.create_product_page,
            name = "product_text",
            geometry = QRect(280, 50, 430, 40),
            text = "Register Product",
            font = font4,
            style = "font: bold"
        )

        self.create_product_id_label = createLabel(
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

        self.create_product_brand_label = createLabel(
            parent = self.create_product_page,
            name = "product_text",
            geometry = QRect(380, 210, 170, 40),
            text = "Brand",
            font = font1,
            style = ""
        )

        self.create_product_sku_label = createLabel(
            parent = self.create_product_page,
            name = "product_text",
            geometry = QRect(40, 310, 130, 40),
            text = "SKU",
            font = font1,
            style = ""
        )

        self.create_product_quantity_label = createLabel(
            parent = self.create_product_page,
            name = "product_text",
            geometry = QRect(380, 310, 170, 40),
            text = "Quantity",
            font = font1,
            style = ""
        )

        self.create_product_supplier_label = createLabel(
            parent = self.create_product_page,
            name = "product_text",
            geometry = QRect(40, 420, 130, 40),
            text = "Supplier",
            font = font1,
            style = ""
        )

        self.create_product_price_label = createLabel(
            parent = self.create_product_page,
            name = "product_text",
            geometry = QRect(380, 420, 160, 40),
            text = "Price",
            font = font1,
            style = ""
        )

        self.create_product_purchase_label = createLabel(
            parent = self.create_product_page,
            name = "product_text",
            geometry = QRect(40, 530, 180, 40),
            text = "Purchase Date",
            font = font1,
            style = ""
        )

        self.create_product_price_label = createLabel(
            parent = self.create_product_page,
            name = "product_text",
            geometry = QRect(380, 530, 160, 40),
            text = "Expiry Date",
            font = font1,
            style = ""
        )

        self.create_product_id_output_label = createLabel(
            parent = self.create_product_page,
            name = "product_text",
            geometry = QRect(210, 150, 360, 40),
            text = "",
            font = font1,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # =================================================================

        self.create_product_name_input = createLineInput(
            parent = self.create_product_page,
            name = "name_input",
            geometry = QRect(40, 260, 330, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.create_product_brand_input = createLineInput(
            parent = self.create_product_page,
            name = "name_input",
            geometry = QRect(380, 260, 330, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.create_product_sku_input = createLineInput(
            parent = self.create_product_page,
            name = "name_input",
            geometry = QRect(40, 360, 330, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.create_product_quantity_input = createLineInput(
            parent = self.create_product_page,
            name = "name_input",
            geometry = QRect(380, 360, 200, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.create_product_supplier_input = createLineInput(
            parent = self.create_product_page,
            name = "name_input",
            geometry = QRect(40, 470, 330, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.create_product_price_input = createLineInput(
            parent = self.create_product_page,
            name = "name_input",
            geometry = QRect(380, 470, 200, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # ===================================================

        self.create_product_purchase_date = createDate(
            parent = self.create_product_page,
            name = "purchase_date",
            geometry = QRect(40, 580, 230, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.create_product_expiry_date = createDate(
            parent = self.create_product_page,
            name = "purchase_date",
            geometry = QRect(380, 580, 230, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # ====================================================
        self.create_product_back_button = createButton(
            parent = self.create_product_page,
            name = "back_button",
            geometry = QRect(40, 50, 70, 50),
            text = "Back",
            font = font3,
            style = "background-color: #004F9A"
        )

        self.create_product_clear_button = createButton(
            parent = self.create_product_page,
            name = "clear_button",
            geometry = QRect(510, 730, 170, 50),
            text = "Clear",
            font = font3,
            style = "background-color: #882400"
        )

        # REGISTER BUTTON
        self.create_product_register_button = createButton(
            parent = self.create_product_page,
            name = "register_button",
            geometry = QRect(690, 730, 250, 50),
            text = "Register Product",
            font = font3,
            style = "background-color: #006646"
        )
        self.create_product_back_button.clicked.connect(self.show_main_page)
        self.create_product_clear_button.clicked.connect(lambda: self.clear_inputs(self.create_product_page))
        self.create_product_register_button.clicked.connect(self.register_product)

    def view_product(self):

        self.view_product_page = QWidget()
        self.view_product_page.setObjectName("main_page")
        self.stackedWidget.addWidget(self.view_product_page)
        
        # ===========================================
        #            product PAGE LABELS
        # ===========================================

        self.view_product_text_label = createLabel(
            parent=self.view_product_page,
            name="product_text",
            geometry=QRect(280, 50, 430, 40),
            text="View Product Details",
            font=font4,
            style="font: bold"
        )

        self.view_product_id_label = createLabel(
            parent=self.view_product_page,
            name="product_text",
            geometry=QRect(40, 150, 160, 40),
            text="Product ID:",
            font=font1,
            style=""
        )

        self.view_product_name_label = createLabel(
            parent=self.view_product_page,
            name="product_text",
            geometry=QRect(40, 210, 170, 40),
            text="Product Name",
            font=font1,
            style=""
        )

        self.view_product_brand_label = createLabel(
            parent=self.view_product_page,
            name="product_text",
            geometry=QRect(380, 210, 170, 40),
            text="Brand",
            font=font1,
            style=""
        )

        self.view_product_sku_label = createLabel(
            parent=self.view_product_page,
            name="product_text",
            geometry=QRect(40, 310, 130, 40),
            text="SKU",
            font=font1,
            style=""
        )

        self.view_product_quantity_label = createLabel(
            parent=self.view_product_page,
            name="product_text",
            geometry=QRect(380, 310, 170, 40),
            text="Quantity",
            font=font1,
            style=""
        )

        self.view_product_supplier_label = createLabel(
            parent=self.view_product_page,
            name="product_text",
            geometry=QRect(40, 420, 130, 40),
            text="Supplier",
            font=font1,
            style=""
        )

        self.view_product_price_label = createLabel(
            parent=self.view_product_page,
            name="product_text",
            geometry=QRect(380, 420, 160, 40),
            text="Price",
            font=font1,
            style=""
        )

        self.product_purchase_label = createLabel(
            parent=self.view_product_page,
            name="product_text",
            geometry=QRect(40, 530, 180, 40),
            text="Purchase Date",
            font=font1,
            style=""
        )

        self.view_product_expiry_label = createLabel(
            parent=self.view_product_page,
            name="product_text",
            geometry=QRect(380, 530, 160, 40),
            text="Expiry Date",
            font=font1,
            style=""
        )

        self.view_product_id_output_label = createLabel(
            parent=self.view_product_page,
            name="product_text",
            geometry=QRect(210, 150, 360, 40),
            text="",
            font=font1,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        # =================================================================

        self.view_product_name_input_label = createLabel(
            parent=self.view_product_page,
            name="name_input",
            geometry=QRect(40, 260, 330, 40),
            text="",
            font=font2,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        self.view_product_brand_input_label = createLabel(
            parent=self.view_product_page,
            name="brand_input",
            geometry=QRect(380, 260, 330, 40),
            text="",
            font=font2,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        self.view_product_sku_input_label = createLabel(
            parent=self.view_product_page,
            name="sku_input",
            geometry=QRect(40, 360, 330, 40),
            text="",
            font=font2,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        self.view_product_quantity_input_label = createLabel(
            parent=self.view_product_page,
            name="quantity_input",
            geometry=QRect(380, 360, 200, 40),
            text="",
            font=font2,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        self.view_product_supplier_input_label = createLabel(
            parent=self.view_product_page,
            name="supplier_input",
            geometry=QRect(40, 470, 330, 40),
            text="",
            font=font2,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        self.view_product_price_input_label = createLabel(
            parent=self.view_product_page,
            name="price_input",
            geometry=QRect(380, 470, 200, 40),
            text="",
            font=font2,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        # ===================================================

        self.view_product_purchase_date_label = createLabel(
            parent=self.view_product_page,
            name="purchase_date",
            geometry=QRect(40, 580, 230, 40),
            text="",
            font=font2,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        self.view_product_expiry_date_label = createLabel(
            parent=self.view_product_page,
            name="expiry_date",
            geometry=QRect(380, 580, 230, 40),
            text="",
            font=font2,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        # ====================================================
        self.view_product_back_button = createButton(
            parent=self.view_product_page,
            name="back_button",
            geometry=QRect(40, 50, 70, 50),
            text="Back",
            font=font3,
            style="background-color: #004F9A"
        )

        # REGISTER BUTTON
        self.view_product_edit_button = createButton(
            parent=self.view_product_page,
            name="register_button",
            geometry=QRect(690, 730, 250, 50),
            text="Edit",
            font=font3,
            style="background-color: #006646"
        )

        self.view_product_edit_button.clicked.connect(self.edit_product_button)
        self.view_product_back_button.clicked.connect(self.show_main_page)
   
    def edit_product(self):
        self.edit_product_page = QWidget()
        self.edit_product_page.setObjectName("main_page")
        self.stackedWidget.addWidget(self.edit_product_page)
       
        # ===========================================
        #            product PAGE LABELS
        # ===========================================

        self.edit_product_text_label = createLabel(
            parent = self.edit_product_page,
            name = "product_text",
            geometry = QRect(280, 50, 430, 40),
            text = "Edit Product Details",
            font = font4,
            style = "font: bold"
        )

        self.edit_product_id_label = createLabel(
            parent = self.edit_product_page,
            name = "product_text",
            geometry = QRect(40, 150, 160, 40),
            text = "Product ID:",
            font = font1,
            style = ""
        )

        self.edit_product_name_label = createLabel(
            parent = self.edit_product_page,
            name = "product_text",
            geometry = QRect(40, 210, 170, 40),
            text = "Product Name",
            font = font1,
            style = ""
        )

        self.edit_product_brand_label = createLabel(
            parent = self.edit_product_page,
            name = "product_text",
            geometry = QRect(380, 210, 170, 40),
            text = "Brand",
            font = font1,
            style = ""
        )

        self.edit_product_sku_label = createLabel(
            parent = self.edit_product_page,
            name = "product_text",
            geometry = QRect(40, 310, 130, 40),
            text = "SKU",
            font = font1,
            style = ""
        )

        self.edit_product_quantity_label = createLabel(
            parent = self.edit_product_page,
            name = "product_text",
            geometry = QRect(380, 310, 170, 40),
            text = "Quantity",
            font = font1,
            style = ""
        )

        self.edit_product_supplier_label = createLabel(
            parent = self.edit_product_page,
            name = "product_text",
            geometry = QRect(40, 420, 130, 40),
            text = "Supplier",
            font = font1,
            style = ""
        )

        self.edit_product_price_label = createLabel(
            parent = self.edit_product_page,
            name = "product_text",
            geometry = QRect(380, 420, 160, 40),
            text = "Price",
            font = font1,
            style = ""
        )

        self.edit_product_purchase_label = createLabel(
            parent = self.edit_product_page,
            name = "product_text",
            geometry = QRect(40, 530, 180, 40),
            text = "Purchase Date",
            font = font1,
            style = ""
        )

        self.edit_product_price_label = createLabel(
            parent = self.edit_product_page,
            name = "product_text",
            geometry = QRect(380, 530, 160, 40),
            text = "Expiry Date",
            font = font1,
            style = ""
        )

        self.edit_product_id_output_label = createLabel(
            parent = self.edit_product_page,
            name = "product_text",
            geometry = QRect(210, 150, 360, 40),
            text = "",
            font = font1,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # =================================================================

        self.edit_product_name_input = createLineInput(
            parent = self.edit_product_page,
            name = "name_input",
            geometry = QRect(40, 260, 330, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.edit_product_brand_input = createLineInput(
            parent = self.edit_product_page,
            name = "name_input",
            geometry = QRect(380, 260, 330, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.edit_product_sku_input = createLineInput(
            parent = self.edit_product_page,
            name = "name_input",
            geometry = QRect(40, 360, 330, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.edit_product_quantity_input = createLineInput(
            parent = self.edit_product_page,
            name = "name_input",
            geometry = QRect(380, 360, 200, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.edit_product_supplier_input = createLineInput(
            parent = self.edit_product_page,
            name = "name_input",
            geometry = QRect(40, 470, 330, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.edit_product_price_input = createLineInput(
            parent = self.edit_product_page,
            name = "name_input",
            geometry = QRect(380, 470, 200, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # ===================================================

        self.edit_product_purchase_date = createDate(
            parent = self.edit_product_page,
            name = "purchase_date",
            geometry = QRect(40, 580, 230, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.edit_product_expiry_date = createDate(
            parent = self.edit_product_page,
            name = "purchase_date",
            geometry = QRect(380, 580, 230, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # ====================================================
        self.edit_product_back_button = createButton(
            parent = self.edit_product_page,
            name = "back_button",
            geometry = QRect(40, 50, 70, 50),
            text = "Back",
            font = font3,
            style = "background-color: #004F9A"
        )

        self.edit_product_cancel_button = createButton(
            parent = self.edit_product_page,
            name = "clear_button",
            geometry = QRect(510, 730, 170, 50),
            text = "Cancel",
            font = font3,
            style = "background-color: #882400"
        )

        # REGISTER BUTTON
        self.edit_product_change_button = createButton(
            parent = self.edit_product_page,
            name = "register_button",
            geometry = QRect(690, 730, 250, 50),
            text = "Confirm Changes",
            font = font3,
            style = "background-color: #006646"
        )
        self.edit_product_back_button.clicked.connect(self.show_main_page)
        self.edit_product_cancel_button.clicked.connect(self.show_view_product)
        self.edit_product_change_button.clicked.connect(self.update_product)
    # =========================================================
    # ========================================================
    def register_product(self):
        print("hello")
        product_id = self.create_product_id_output_label.text()
        name = self.create_product_name_input.text()
        brand = self.create_product_brand_input.text()
        sku = self.create_product_sku_input.text()
        quantity = self.create_product_quantity_input.text()
        supplier = self.create_product_supplier_input.text()
        price = self.create_product_price_input.text()
        purchase_date = self.create_product_purchase_date.date()
        expiry_date = self.create_product_expiry_date.date()

        cursor.execute(
            """
            INSERT INTO Products
            (
            product_id, name, brand, sku, quantity, supplier, price, purchase_date, expiry_date, status
            ) VALUES
            (?, ?, ?, ?, ?, ?, ?, ?, ?, 'Active')
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
        self.create_product_id_output_label.setText(generated_id)

    def update_table_widget(self):
        data = self.fetch_product_by_column()
        self.table_widget.setRowCount(len(data))
        for row_index, row_data in enumerate(data):
            for col_index, col_data in enumerate(row_data):
                self.table_widget.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))
            
        for self.row in range(self.table_widget.rowCount()):
            view_button = QPushButton("View")
            view_button.clicked.connect(partial(self.show_view_product_temp, self.row))
            self.table_widget.setCellWidget(self.row, 5, view_button)

    def show_view_product_temp(self, row):
        product_id = self.table_widget.item(row, 0).text()

        cursor.execute(
            """
            SELECT * 
            FROM Products
            WHERE product_id = ?
            """,
            (product_id,)
        )

        results = cursor.fetchone()

        product_id, name, quantity, price, expiry_date, purchase_date, supplier, brand, status, sku = results


        self.view_product_id_output_label.setText(product_id)
        self.view_product_name_input_label.setText(name)
        self.view_product_quantity_input_label.setText(str(quantity))
        self.view_product_price_input_label.setText(str(price))
        self.view_product_purchase_date_label.setText(purchase_date)
        self.view_product_expiry_date_label.setText(expiry_date)
        self.view_product_supplier_input_label.setText(supplier)
        self.view_product_brand_input_label.setText(brand)
        self.view_product_sku_input_label.setText(sku)
        self.show_view_product()
  

    def fetch_product_by_column(self):
        query = f"""SELECT product_id, 
                  name,
                  quantity,
                  expiry_date,
                  status
                  FROM Products """
        cursor.execute(query)
        data = cursor.fetchall()
        return data
    
    def edit_product_button(self):
        product_id = self.view_product_id_output_label.text()
        name = self.view_product_name_input_label.text()
        quantity = self.view_product_quantity_input_label.text()
        price = self.view_product_price_input_label.text()
        purchase_date = self.view_product_purchase_date_label.text()
        expiry_date = self.view_product_expiry_date_label.text()
        supplier = self.view_product_supplier_input_label.text()
        brand = self.view_product_brand_input_label.text()
        sku = self.view_product_sku_input_label.text()

        expiry_date = datetime.strptime(expiry_date, '%Y-%m-%d')
        purchase_date = datetime.strptime(purchase_date, '%Y-%m-%d')

        self.edit_product_id_output_label.setText(product_id)
        self.edit_product_name_input.setText(name)
        self.edit_product_quantity_input.setText(quantity)
        self.edit_product_price_input.setText(price)
        self.edit_product_purchase_date.setDate(purchase_date)
        self.edit_product_expiry_date.setDate(expiry_date)
        self.edit_product_supplier_input.setText(supplier)
        self.edit_product_brand_input.setText(brand)
        self.edit_product_sku_input.setText(sku)

        self.update_table_widget()
        self.show_edit_product()

    def update_product(self):

        product_id = self.edit_product_id_output_label.text()
        name = self.edit_product_name_input.text()
        quantity = self.edit_product_quantity_input.text()
        price = self.edit_product_price_input.text()
        purchase_date = self.edit_product_purchase_date.date()
        expiry_date = self.edit_product_expiry_date.date()
        supplier = self.edit_product_supplier_input.text()
        brand = self.edit_product_brand_input.text()
        sku = self.edit_product_sku_input.text()

        cursor.execute(
            """
            UPDATE Products
            SET name = ?,
                quantity = ?,
                price = ?,
                purchase_date = ?,
                expiry_date = ?,
                supplier = ?,
                brand = ?,
                sku = ?
            WHERE product_id = ?
            """,
            (name, quantity, price, purchase_date.toString("yyyy-MM-dd"), expiry_date.toString("yyyy-MM-dd"),supplier, brand, sku, product_id)
        )

        connection.commit()

        self.show_main_page()

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

    
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Maintenance()
    window.show()
    sys.exit(app.exec_())

