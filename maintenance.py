from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from assets import *
import sqlite3
import re
from functools import partial
from datetime import datetime
import uuid

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

        self.verticalLayout.addWidget(self.stackedWidget)
        self.stackedWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(self)



    def show_manage_main_page(self):
        self.stackedWidget.setCurrentIndex(0)

    def show_manage_member_page(self):
        self.stackedWidget.setCurrentIndex(1)


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

        self.switch_user_account_page_button = createButton(
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

        self.switch_member_page_button.clicked.connect(self.show_manage_member_page)

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
        self.manage_search_input.textChanged.connect(self.update_search_results)

        # ===========================================
        #         MANAGE MEMBER TABLE WIDGET
        # ===========================================
        self.member_table_widget = QTableWidget(self.manage_member_page)
        self.member_table_widget.setGeometry(QRect(10, 200, 930, 590))
        self.member_table_widget.setRowCount(0)
        self.member_table_widget.setColumnCount(7)  # Limited columns

        # Set the horizontal header labels
        self.member_table_widget.setHorizontalHeaderLabels(
            ["Member ID", "First Name", "Last Name", "Membership Type", "Membership Start Date", "Membership End Date", "Actions"]
        )

        self.stackedWidget.addWidget(self.manage_member_page)

        # Load and display data in the table
        self.connect_member_table()

        self.member_table_widget.resizeColumnsToContents()
        self.member_table_widget.resizeRowsToContents()
        
        self.member_table_widget.setColumnWidth(0, 100)  # Member ID
        self.member_table_widget.setColumnWidth(1, 150)  # First Name
        self.member_table_widget.setColumnWidth(2, 150)  # Last Name
        self.member_table_widget.setColumnWidth(3, 150)  # Membership Type
        self.member_table_widget.setColumnWidth(4, 150)  # Membership Start Date
        self.member_table_widget.setColumnWidth(5, 150)  # Membership End Date
        # ===========================================
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

    # =============================================================
    #                      BACK-END FUNCTIONS
    # =============================================================

    
    def connect_member_table(self):
        cursor.execute('PRAGMA table_info(Members)')
        column_names = ["Member ID", "First Name", "Last Name", "Type", "Start Date", "End Date"]

        self.member_table_widget.setHorizontalHeaderLabels(column_names + ["Actions"])
        cursor.execute("SELECT member_id, first_name, last_name, membership_type, membership_start_date, membership_end_date FROM Members")

        self.member_data = cursor.fetchall()  # Store data for filtering

        # Load the full data initially
        self.update_search_results()

    def update_search_results(self):
        search_text = self.manage_search_input.text().strip().lower()
        self.member_table_widget.setRowCount(0)

        for row_number, row_data in enumerate(self.member_data):
            if any(search_text in str(data).lower() for data in row_data):
                self.member_table_widget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    item = QTableWidgetItem(str(data))
                    item.setTextAlignment(Qt.AlignLeft)  # Align text to the left for better readability
                    self.member_table_widget.setItem(row_number, column_number, item)

                view_button = QPushButton("View")
                view_button.clicked.connect(partial(self.open_member_details, row_data[0]))
                self.member_table_widget.setCellWidget(row_number, len(row_data), view_button)

        # Adjust the size of rows and columns after inserting new data
        self.member_table_widget.resizeColumnsToContents()
        self.member_table_widget.resizeRowsToContents()

    def open_member_details(self, member_id):
        # Open a new screen and show member details
        # Implement the logic to fetch and display member details
        print(f"Open details for member ID: {member_id}")
        # You can replace the above print statement with your logic to open a new screen
        pass

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Maintenance()
    window.show()
    sys.exit(app.exec_())