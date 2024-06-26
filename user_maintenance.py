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
        self.open_create_user_page()

        self.verticalLayout.addWidget(self.stackedWidget)
        self.stackedWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(self)


    def show_user_page(self):
        self.stackedWidget.setCurrentIndex(0)
    def show_create_user(self):
        self.stackedWidget.setCurrentIndex(1)

    def open_user_page(self):
        self.user_page = QWidget()
        self.user_page.setObjectName("user_page")
        self.stackedWidget.addWidget(self.user_page)
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
        self.table_widget.setColumnCount(5)  # Limited columns

        # Set the horizontal header labels
        self.table_widget.setHorizontalHeaderLabels(
            ["Employee ID", "Username", "Password", "Role", "Actions"]
        )

        self.stackedWidget.addWidget(self.user_page)
        self.table_widget.resizeColumnsToContents()
        self.table_widget.resizeRowsToContents()
        self.table_widget.horizontalHeader().setStretchLastSection(True)
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


        #         MANAGE MEMBER BUTTONS
        # ===========================================
        self.user_equipment_back_button = createButton(
            parent=self.user_page,
            name="back_button",
            geometry=QRect(20, 40, 70, 50),
            text="Back",
            font=font2,
            style=""
        )

        self.user_add_button = createButton(
            parent=self.user_page,
            name="add_button",
            geometry=QRect(680, 40, 250, 50),
            text="Add Equipments",
            font=font2,
            style="background-color: #28a745; color: #FFFFFF"
        )

        self.user_add_button.clicked.connect(self.show_create_user)
    def fetch_user_by_column(self):
        query = f"""SELECT employee_id, 
                  username,
                  password_hash,
                  role,
                  FROM Users """
        cursor.execute(query)
        data = cursor.fetchall()
        return data
    
    def update_table_widget(self):
        data = self.fetch_user_by_column()
        self.table_widget.setRowCount(len(data))
        for row_index, row_data in enumerate(data):
            for col_index, col_data in enumerate(row_data):
                self.table_widget.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))
            
        for self.row in range(self.table_widget.rowCount()):
            view_button = QPushButton("View")
            view_button.clicked.connect(partial(self.show_view_member_temp, self.row))
            self.table_widget.setCellWidget(self.row, 5, view_button)

    def open_create_user_page(self):
        self.create_user_page = QWidget()
        self.create_user_page.setObjectName("create_user_page")
        self.stackedWidget.addWidget(self.create_user_page)
        # ===========================================
        #             USER ACCOUNTS LABELS
        # ===========================================


        self.user_registration_label = createLabel(
            parent = self.create_user_page,
            name = "user_registration",
            geometry = QRect(270, 50, 430, 40),
            text = "User Registration",
            font = font4,
            style = "font: bold"
        )

        self.user_member_name_label = createLabel(
            parent = self.create_user_page,
            name = "member_name",
            geometry = QRect(40, 150, 190, 40),
            text = "Employee Name:",
            font = font1,
            style = ""
        )

        self.user_membership_id_label = createLabel(
            parent = self.create_user_page,
            name = "membership_id",
            geometry = QRect(40, 210, 190, 40),
            text = "Employee ID",
            font = font1,
            style = ""
        )

        self.user_membership_id_output_label = createLabel(
            parent = self.create_user_page,
            name = "output",
            geometry = QRect(40, 260, 330, 40),
            text = "",
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.user_gender_label = createLabel(
            parent = self.create_user_page,
            name = "gender",
            geometry = QRect(380, 210, 130, 40),
            text = "Gender",
            font = font1,
            style = ""
        )

        self.user_gender_output_label = createLabel(
            parent = self.create_user_page,
            name = "output",
            geometry = QRect(380, 260, 260, 40),
            text = "",
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.user_phone_number_label = createLabel(
            parent = self.create_user_page,
            name = "phone_number",
            geometry = QRect(40, 320, 180, 40),
            text = "Phone Number",
            font = font1,
            style = ""
        )

        self.user_phone_number_output_label = createLabel(
            parent = self.create_user_page,
            name = "output",
            geometry = QRect(40, 360, 330, 40),
            text = "",
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.user_hire_date_label = createLabel(
            parent = self.create_user_page,
            name = "hire_date",
            geometry = QRect(380, 320, 210, 40),
            text = "Hire Date",
            font = font1,
            style = ""
        )

        self.user_hire_date_output_label = createLabel(
            parent = self.create_user_page,
            name = "output",
            geometry = QRect(380, 360, 260, 40),
            text = "",
            font = font1,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.user_image_output_label = createLabel(
            parent = self.create_user_page,
            name = "output",
            geometry = QRect(680, 140, 250, 250),
            text = "",
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.username_label = createLabel(
            parent = self.create_user_page,
            name = "username",
            geometry = QRect(40, 480, 130, 40),
            text = "Username",
            font = font2,
            style = ""
        )

        self.user_password_label = createLabel(
            parent = self.create_user_page,
            name = "password",
            geometry = QRect(470, 480, 130, 40),
            text = "Password",
            font = font2,
            style = ""
        )

        self.user_re_password_label = createLabel(
            parent = self.create_user_page,
            name = "re_password",
            geometry = QRect(470, 580, 210, 40),
            text = "Re-type Password",
            font = font2,
            style = ""
        )

        self.user_role_label = createLabel(
            parent = self.create_user_page,
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
            parent = self.create_user_page,
            name = "member_name_input",
            geometry = QRect(240, 150, 410, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )
        self.user_member_name_input.setPlaceholderText("Search Employee Name")
        self.user_member_name_input.textChanged.connect(self.update_search_results)
        self.username_input = createLineInput(
            parent = self.create_user_page,
            name = "user_name_input",
            geometry = QRect(40 ,530, 410, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.password_input = createLineInput(
            parent = self.create_user_page,
            name = "password_input",
            geometry = QRect(470 ,530, 410, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"

        )

        self.re_password_input = createLineInput(
            parent = self.create_user_page,
            name = "re_password_input",
            geometry = QRect(470 ,630, 410, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"

        )

        # ===========================================
        #         USER ACCOUNT COMBO BOX
        # =========================================== 

        self.role_combo_box = createComboBox(
            parent = self.create_user_page,
            name = "role",
            geometry = QRect(40, 630, 190, 40),
            font = font2,
            item = ["Staff", "Admin"],
            style = "background-color: #F9F7FF; border: 1px solid black"

        )

        # ===========================================
        #         USER ACCOUNT LIST WIDGETS
        # =========================================== 

        self.search_results = QListWidget(self.create_user_page)
        self.search_results.hide()  # Hide initially
        self.search_results.setGeometry(240, 190, 410, 400)
        self.search_results.setFont(font2)
        self.search_results.itemClicked.connect(self.handle_item_selection)

        # ===========================================
        #           user_a PAGE BUTTONS
        # ===========================================

        # CLEAR BUTTON
        self.user_clear_button = createButton(
            parent = self.create_user_page,
            name = "clear_button",
            geometry = QRect(510, 730, 170, 50),
            text = "Clear",
            font = font3,
            style = "background-color: #882400"
        )

        # REGISTER BUTTON
        self.user_register_button = createButton(
            parent = self.create_user_page,
            name = "register_button",
            geometry = QRect(690, 730, 250, 50),
            text = "Register",
            font = font3,
            style = "background-color: #006646"
        )

        # BACK BUTTON
        self.user_back_button = createButton(
            parent = self.create_user_page,
            name = "back_button",
            geometry = QRect(40, 50, 70, 50),
            text = "Back",
            font = font3,
            style = "background-color: #004F9A"
        )

        self.user_register_button.clicked.connect(self.register_user)
        self.user_back_button.clicked.connect(lambda: self.back_main_button(self.create_user_page))
        self.user_clear_button.clicked.connect(lambda: self.clear_inputs(self.create_user_page))

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
    
    def show_view_member_temp(self, row):
        member_id = self.table_widget.item(row, 0).text()

        cursor.execute(
            """
            SELECT * 
            FROM Users
            WHERE employee_id = ?
            """,
            (member_id,)
        )

        results = cursor.fetchone()

        employee_id, username, password, role = results

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
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Maintenance()
    window.show()
    sys.exit(app.exec_())