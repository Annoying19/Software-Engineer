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
        self.edit_employee_clear_button = createButton(
            parent = self.edit_employee_page,
            name = "clear_button",
            geometry = QRect(510, 730, 170, 50),
            text = "Clear",
            font = font3,
            style = "background-color: #882400"
        )

        # REGISTER BUTTON
        self.edit_employee_register_button = createButton(
            parent = self.edit_employee_page,
            name = "register_button",
            geometry = QRect(690, 730, 250, 50),
            text = "Register",
            font = font3,
            style = "background-color: #006646"

        )