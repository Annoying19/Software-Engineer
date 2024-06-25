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

        self.open_user_page()

        self.verticalLayout.addWidget(self.stackedWidget)
        self.stackedWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(self)

    def open_user_page(self):
        self.user_page = QWidget()
        self.user_page.setObjectName("user_page")

        # ===========================================
        #         MANAGE MEMBER PAGE LABELS
        # ===========================================
        self.manage_employee_text_label = createLabel(
            parent=self.user_page,
            name="manage_members_text",
            geometry=QRect(120, 40, 350, 40),
            text="Manage Users",
            font=font4,
            style="font: bold"
        )

        self.manage_search_text_label = createLabel(
            parent=self.user_page,
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
            parent=self.user_page,
            name="search_input",
            geometry=QRect(130, 140, 580, 40),
            font=font2,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        self.manage_search_input.setPlaceholderText("Equipment ID / Name")

        # ===========================================
        #         MANAGE MEMBER TABLE WIDGET
        # ===========================================
        self.table_widget = QTableWidget(self.user_page)
        self.table_widget.setGeometry(QRect(10, 200, 930, 590))
        self.table_widget.setRowCount(0)
        self.table_widget.setColumnCount(6)  # Limited columns

        # Set the horizontal header labels
        self.table_widget.setHorizontalHeaderLabels(
            ["Equipment ID", "Name", "Serial Number", "Category", "Status", "Actions"]
        )

        self.stackedWidget.addWidget(self.user_page)
        self.table_widget.resizeColumnsToContents()
        self.table_widget.resizeRowsToContents()
        self.table_widget.horizontalHeader().setStretchLastSection(True)
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


        #         MANAGE MEMBER BUTTONS
        # ===========================================
        self.equipment_back_button = createButton(
            parent=self.user_page,
            name="back_button",
            geometry=QRect(20, 40, 70, 50),
            text="Back",
            font=font2,
            style=""
        )

        self.equipment_add_button = createButton(
            parent=self.user_page,
            name="add_button",
            geometry=QRect(680, 40, 250, 50),
            text="Add Equipments",
            font=font2,
            style="background-color: #28a745; color: #FFFFFF"
        )

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Maintenance()
    window.show()
    sys.exit(app.exec_())