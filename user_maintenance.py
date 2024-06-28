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


class UserMaintenance(QWidget):
    def __init__(self, parent=None):
        super(UserMaintenance, self).__init__(parent)
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
        self.open_view_user_page()

        self.verticalLayout.addWidget(self.stackedWidget)
        self.stackedWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(self)


    def show_user_page(self):
        self.update_usert_table_widget()
        self.stackedWidget.setCurrentIndex(0)
    def show_create_user(self):
        clear_inputs(self.create_user_page)
        self.stackedWidget.setCurrentIndex(1)

    def show_edit_user(self):
        self.stackedWidget.setCurrentIndex(2)

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
        self.user_manage_search_input = createLineInput(
            parent=self.user_page,
            name="search_input",
            geometry=QRect(130, 140, 580, 40),
            font=font2,
            style="background-color: #F9F7FF; border: 1px solid black"
        )

        self.user_manage_search_input.setPlaceholderText("Equipment ID / Name")

        # ===========================================
        #         MANAGE MEMBER TABLE WIDGET
        # ===========================================
        self.user_table_widget = QTableWidget(self.user_page)
        self.user_table_widget.setGeometry(QRect(10, 200, 930, 590))
        self.user_table_widget.setRowCount(0)
        self.user_table_widget.setColumnCount(4)  # Limited columns

        # Set the horizontal header labels
        self.user_table_widget.setHorizontalHeaderLabels(
            ["Employee ID", "Username", "Role", "Actions"]
        )

        self.stackedWidget.addWidget(self.user_page)
        self.user_table_widget.resizeColumnsToContents()
        self.user_table_widget.resizeRowsToContents()
        self.user_table_widget.horizontalHeader().setStretchLastSection(True)
        self.user_table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.user_manage_search_input.textChanged.connect(lambda: self.search_user(self.user_table_widget, self.user_manage_search_input))
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
            text="Add Users",
            font=font2,
            style="background-color: #28a745; color: #FFFFFF"
        )

        self.user_add_button.clicked.connect(self.show_create_user)
    def fetch_user_by_column(self):
        query = f"""SELECT employee_id, 
                  username,
                  role
                  FROM Users """
        cursor.execute(query)
        data = cursor.fetchall()
        return data
    
    def update_usert_table_widget(self):
        data = self.fetch_user_by_column()
        self.user_table_widget.setRowCount(len(data))
        for row_index, row_data in enumerate(data):
            for col_index, col_data in enumerate(row_data):
                self.user_table_widget.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))
            view_button = QPushButton("View")
            view_button.clicked.connect(partial(self.show_view_user_temp, row_index))
            self.user_table_widget.setCellWidget(row_index, 3, view_button)

    

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

        self.user_employee_id_label = createLabel(
            parent = self.create_user_page,
            name = "membership_id",
            geometry = QRect(40, 210, 190, 40),
            text = "Employee ID",
            font = font1,
            style = ""
        )

        self.user_employee_id_output_label = createLabel(
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

        self.update_usert_table_widget()
    


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

        self.password_input.setEchoMode(QLineEdit.Password)

        self.re_password_input = createLineInput(
            parent = self.create_user_page,
            name = "re_password_input",
            geometry = QRect(470 ,630, 410, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.re_password_input.setEchoMode(QLineEdit.Password)

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

        self.user_register_button.clicked.connect(lambda: register_entity("Users", self.assigned_inputs("Users")))
        self.user_back_button.clicked.connect(self.show_user_page)
        self.user_clear_button.clicked.connect(lambda: clear_inputs(self.create_user_page))

    def open_view_user_page(self):
        self.view_user_page = QWidget()
        self.view_user_page.setObjectName("view_user_page")
        self.stackedWidget.addWidget(self.view_user_page)
        # ===========================================
        #             USER ACCOUNTS LABELS
        # ===========================================


        self.view_user_registration_label = createLabel(
            parent = self.view_user_page,
            name = "view_user_registration",
            geometry = QRect(270, 50, 430, 40),
            text = "User Registration",
            font = font4,
            style = "font: bold"
        )

        self.view_user_member_name_label = createLabel(
            parent = self.view_user_page,
            name = "member_name",
            geometry = QRect(40, 150, 190, 40),
            text = "Employee Name:",
            font = font1,
            style = ""
        )

        self.view_user_employee_id_label = createLabel(
            parent = self.view_user_page,
            name = "membership_id",
            geometry = QRect(40, 210, 190, 40),
            text = "Employee ID",
            font = font1,
            style = ""
        )

        self.view_user_employee_id_output_label = createLabel(
            parent = self.view_user_page,
            name = "output",
            geometry = QRect(40, 260, 330, 40),
            text = "",
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.view_user_gender_label = createLabel(
            parent = self.view_user_page,
            name = "gender",
            geometry = QRect(380, 210, 130, 40),
            text = "Gender",
            font = font1,
            style = ""
        )

        self.view_user_gender_output_label = createLabel(
            parent = self.view_user_page,
            name = "output",
            geometry = QRect(380, 260, 260, 40),
            text = "",
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.view_user_phone_number_label = createLabel(
            parent = self.view_user_page,
            name = "phone_number",
            geometry = QRect(40, 320, 180, 40),
            text = "Phone Number",
            font = font1,
            style = ""
        )

        self.view_user_phone_number_output_label = createLabel(
            parent = self.view_user_page,
            name = "output",
            geometry = QRect(40, 360, 330, 40),
            text = "",
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.view_user_hire_date_label = createLabel(
            parent = self.view_user_page,
            name = "hire_date",
            geometry = QRect(380, 320, 210, 40),
            text = "Hire Date",
            font = font1,
            style = ""
        )

        self.view_user_hire_date_output_label = createLabel(
            parent = self.view_user_page,
            name = "output",
            geometry = QRect(380, 360, 260, 40),
            text = "",
            font = font1,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.view_user_image_output_label = createLabel(
            parent = self.view_user_page,
            name = "output",
            geometry = QRect(680, 140, 250, 250),
            text = "",
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.username_label = createLabel(
            parent = self.view_user_page,
            name = "username",
            geometry = QRect(40, 480, 130, 40),
            text = "Username",
            font = font2,
            style = ""
        )

        self.view_user_password_label = createLabel(
            parent = self.view_user_page,
            name = "password",
            geometry = QRect(470, 480, 130, 40),
            text = "Password",
            font = font2,
            style = ""
        )

        self.view_user_re_password_label = createLabel(
            parent = self.view_user_page,
            name = "re_password",
            geometry = QRect(470, 580, 210, 40),
            text = "Re-type Password",
            font = font2,
            style = ""
        )

        self.view_user_role_label = createLabel(
            parent = self.view_user_page,
            name = "role",
            geometry = QRect(40, 580, 60, 40),
            text = "Role",
            font = font2,
            style = ""
        )

        self.update_usert_table_widget()
    


        # ===========================================
        #            USER ACCOUNT INPUTS
        # ===========================================

        self.view_user_member_name_input = createLabel(
            parent = self.view_user_page,
            name = "member_name_input",
            geometry = QRect(240, 150, 410, 40),
            font = font2,
            text = "",
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.edit_username_input = createLineInput(
            parent = self.view_user_page,
            name = "view_user_name_input",
            geometry = QRect(40 ,530, 410, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.edit_password_input = createLineInput(
            parent = self.view_user_page,
            name = "password_input",
            geometry = QRect(470 ,530, 410, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"

        )   

        self.re_edit_password_input  = createLineInput(
            parent = self.view_user_page,
            name = "password_input",
            geometry = QRect(470 ,630, 410, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"

        )   

        self.edit_password_input.setEchoMode(QLineEdit.Password)
        self.re_edit_password_input.setEchoMode(QLineEdit.Password)
        # ===========================================
        #         USER ACCOUNT COMBO BOX
        # =========================================== 

        self.edit_role_combo_box_output = createComboBox(
            parent = self.view_user_page,
            name = "role",
            geometry = QRect(40, 630, 190, 40),
            font = font2,
            item = ["Staff", "Admin"],
            style = "background-color: #F9F7FF; border: 1px solid black"

        )

        # ===========================================
        #           view_user_a PAGE BUTTONS
        # ===========================================

        # REGISTER BUTTON
        self.view_user_edit_button = createButton(
            parent = self.view_user_page,
            name = "register_button",
            geometry = QRect(690, 730, 250, 50),
            text = "Change",
            font = font3,
            style = "background-color: #006646"
        )

        # BACK BUTTON
        self.view_user_back_button = createButton(
            parent = self.view_user_page,
            name = "back_button",
            geometry = QRect(40, 50, 70, 50),
            text = "Back",
            font = font3,
            style = "background-color: #004F9A"
        )


        self.view_user_edit_button.clicked.connect(lambda: update_entity("Users", self.assigned_inputs("Update Users")))
        self.view_user_back_button.clicked.connect(self.show_user_page)


    def assigned_inputs(self, entity_type):
        if entity_type == "Users":
            INPUTS = {
                "employee_id": self.user_employee_id_output_label.text(),
                "username": self.username_input.text(),
                "password": self.password_input.text(),
                "retry_password": self.re_password_input.text(),
                "role": self.role_combo_box.currentText()
            }

        elif entity_type == "Update Users":
            INPUTS = {
                "employee_id": self.view_user_employee_id_output_label.text(),
                "username": self.edit_username_input.text(),
                "password": self.edit_password_input.text(),
                "retry_password": self.re_edit_password_input.text(),
                "role": self.edit_role_combo_box_output.currentText()
            }

        return INPUTS

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

        self.user_employee_id_output_label.setText(self.employee_id)
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
    
    def show_view_user_temp(self, row):
        # Get the employee_id from the selected row
        member_id = self.user_table_widget.item(row, 0).text()

        try:
            # Fetch the user details from the Users table
            cursor.execute(
                """
                SELECT employee_id, username, password_hash, role 
                FROM Users
                WHERE employee_id = ?
                """,
                (member_id,)
            )
            results = cursor.fetchone()

            if results:
                employee_id, username, password, role = results

                # Fetch the employee details from the Employees table
                cursor.execute(
                    '''
                    SELECT first_name || " " || last_name as full_name,
                    gender, phone, hire_date, photo
                    FROM Employees
                    WHERE employee_id = ?
                    ''',
                    (member_id,)
                )
                employee_results = cursor.fetchone()

                if employee_results:
                    name, gender, phone, hire_date, photo= employee_results
                    pixmap = QPixmap()
                    picture = pixmap.loadFromData(photo)
                    # Update the UI elements with the fetched data
                    self.view_user_member_name_input.setText(name)
                    self.view_user_employee_id_output_label.setText(employee_id)
                    self.view_user_gender_output_label.setText(gender)
                    self.view_user_phone_number_output_label.setText(phone)
                    self.view_user_hire_date_output_label.setText(hire_date)
                    self.username_input.setText(username)
                    self.password_input.setText(password)
                    self.view_user_image_output_label.setPixmap(pixmap)
                    self.edit_role_combo_box_output.setCurrentText(role)
                    self.re_password_input.setText(password)
                    self.edit_username_input.setText(self.username_input.text())
                    self.edit_password_input.setText(self.password_input.text())
                    self.re_edit_password_input.setText(self.re_password_input.text())

                    # Call the function to display the edit user page
                    self.show_edit_user()
                else:
                    print("No employee details found for the given employee_id")
            else:
                print("No user details found for the given employee_id")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")

    def search_user(self, table_widget, input_text):
        search_term = input_text.text()
        query = """
            SELECT employee_id,
               username,
               role
            FROM Users
            WHERE employee_id LIKE ? OR username LIKE ?;
        """
        try:
            cursor.execute(query, (f'%{search_term}%', f'%{search_term}%'))
            results = cursor.fetchall()

            table_widget.setRowCount(len(results))
            for row_idx, row_data in enumerate(results):
                for col_idx, col_data in enumerate(row_data):
                    table_widget.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))
                view_button = QPushButton("View")
                view_button.clicked.connect(partial(self.show_view_user_temp, row_idx))
                table_widget.setCellWidget(row_idx, len(row_data), view_button)

            self.add_user_view_button(table_widget)  # Call the function to add view buttons

        except Exception as e:
            print(f"Error executing query for Employees: {e}")


    def add_user_view_button(self, table_widget):
        for row_idx in range(table_widget.rowCount()):
            view_button = QPushButton("View")
            view_button.clicked.connect(partial(self.show_view_user_temp, row_idx))
            table_widget.setCellWidget(row_idx, 5, view_button)
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = UserMaintenance()
    window.show()
    sys.exit(app.exec_())