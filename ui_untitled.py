from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(950, 800)
        Form.setStyleSheet(u"background-color: #FFFFFF")

        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")

        # Setup pages
        self.setupMainPage()
        self.setupMemberPage()
        self.setupAttendancePage()

        self.verticalLayout.addWidget(self.stackedWidget)
        self.stackedWidget.setCurrentIndex(0)

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def setupMainPage(self):
        self.main_page = QWidget()
        self.main_page.setObjectName(u"main_page")

        button_style = "background-color: #002877; color: #FFFFFF"
        self.member_button = self.createButton(
            self.main_page, "member_button", QRect(240, 190, 450, 100), "Members", 25, button_style
        )
        self.attendance_button = self.createButton(
            self.main_page, "attendance_button", QRect(240, 430, 450, 100), "Attendance", 25, button_style
        )

        self.stackedWidget.addWidget(self.main_page)

    def setupMemberPage(self):
        self.member_page = QWidget()
        self.member_page.setObjectName(u"member_page")

        self.register_member_button = self.createButton(
            self.member_page, "register_member_button", QRect(680, 730, 251, 50),
            "Register Member", 16, "background-color: #28a745"
        )

        self.insert_signature_button = self.createButton(
            self.member_page, "insert_signature_button", QRect(670, 470, 251, 50),
            "Insert Signature", 16, "background-color: #007bff"
        )

        self.insert_image_button = self.createButton(
            self.member_page, "insert_image_button", QRect(670, 270, 251, 50),
            "Insert Image", 16, "background-color: #007bff"
        )

        self.clear_button = self.createButton(
            self.member_page, "clear_button", QRect(500, 730, 171, 50), "Clear", 16,
            "background-color: #ff9800"
        )

        self.back_button = self.createButton(
            self.member_page, "back_button", QRect(20, 10, 121, 41), "Back", 16,
            "background-color: #002877; color: #FFFFFF"
        )

        self.createMemberInputs()
        self.stackedWidget.addWidget(self.member_page)

    def createMemberInputs(self):
        font1 = QFont()
        font1.setPointSize(22)

        labels = [
            ("end_date_label", QRect(410, 660, 131, 50), "End Date", font1),
            ("phone_number_label", QRect(20, 520, 221, 50), "Phone Number", font1),
            ("last_name_label", QRect(20, 240, 160, 40), "Last Name", font1),
            ("first_name_label", QRect(20, 120, 160, 40), "First Name", font1),
            ("address_label", QRect(20, 370, 121, 40), "Address", font1),
            ("start_date_label", QRect(20, 660, 161, 50), "Start Date", font1),
            ("birthday_label", QRect(310, 300, 121, 50), "Birthday", font1),
            ("membership_label", QRect(20, 590, 231, 50), "Membership Type", font1),
            ("membership_id_label", QRect(20, 60, 225, 40), "Membership ID", font1),
            ("duration_label", QRect(460, 590, 131, 50), "Duration", font1),
            ("gender_label", QRect(20, 300, 121, 50), "Gender", font1),
            ("middle_name_label", QRect(20, 180, 190, 40), "Middle Name", font1),
        ]

        for name, rect, text, font in labels:
            label = QLabel(self.member_page)
            label.setObjectName(name)
            label.setGeometry(rect)
            label.setText(text)
            label.setFont(font)

        inputs = [
            ("last_name_input", QRect(190, 240, 461, 50)),
            ("first_name_input", QRect(190, 120, 461, 50)),
            ("membership_id_input", QRect(260, 60, 391, 50)),
            ("phone_number_input", QRect(240, 520, 401, 50)),
            ("address_input", QRect(150, 370, 501, 141)),
            ("duration_input", QRect(600, 590, 261, 50)),
            ("middle_name_input", QRect(220, 180, 431, 50))
        ]

        for name, rect in inputs:
            input_field = QLineEdit(self.member_page)
            input_field.setObjectName(name)
            input_field.setGeometry(rect)

        self.start_date_edit = QDateEdit(self.member_page)
        self.start_date_edit.setObjectName(u"start_date_edit")
        self.start_date_edit.setGeometry(QRect(180, 660, 211, 50))
        self.start_date_edit.setFont(QFont("", 20))

        self.end_date_edit = QDateEdit(self.member_page)
        self.end_date_edit.setObjectName(u"end_date_edit")
        self.end_date_edit.setGeometry(QRect(560, 660, 211, 50))
        self.end_date_edit.setFont(QFont("", 20))

        self.birthday_date = QDateEdit(self.member_page)
        self.birthday_date.setObjectName(u"birthday_date")
        self.birthday_date.setGeometry(QRect(440, 300, 211, 50))
        self.birthday_date.setFont(QFont("", 20))

        self.gender_combo_box = QComboBox(self.member_page)
        self.gender_combo_box.setObjectName(u"gender_combo_box")
        self.gender_combo_box.setGeometry(QRect(140, 300, 151, 50))
        self.gender_combo_box.addItem("")
        self.gender_combo_box.addItem("")
        self.gender_combo_box.setFont(QFont("", 20))

        self.membership_combo_box = QComboBox(self.member_page)
        self.membership_combo_box.setObjectName(u"membership_combo_box")
        self.membership_combo_box.setGeometry(QRect(280, 590, 161, 50))
        self.membership_combo_box.addItem("")
        self.membership_combo_box.addItem("")
        self.membership_combo_box.setFont(QFont("", 20))

        self.signature_label = QLabel(self.member_page)
        self.signature_label.setObjectName(u"signature_label")
        self.signature_label.setGeometry(QRect(670, 370, 250, 91))
        self.signature_label.setStyleSheet(u"border: 1px solid black; background-color: #BDBDBD")

        self.image_label = QLabel(self.member_page)
        self.image_label.setObjectName(u"image_label")
        self.image_label.setGeometry(QRect(670, 10, 250, 250))
        self.image_label.setStyleSheet(u"border: 1px solid black; background-color: #BDBDBD")

    def setupAttendancePage(self):
        self.attendance_page = QWidget()
        self.attendance_page.setObjectName(u"attendance_page")

        self.attendance_back_button = self.createButton(
            self.attendance_page, "attendance_back_button", QRect(30, 20, 121, 41), "Back", 16,
            "background-color: #002877; color: #FFFFFF"
        )

        self.submit_button = self.createButton(
            self.attendance_page, "submit_button", QRect(680, 730, 251, 50),
            "Submit", 16, "background-color: #28a745"
        )

        self.attendance_clear_button = self.createButton(
            self.attendance_page, "attendance_clear_button", QRect(500, 730, 171, 50),
            "Clear", 16, "background-color: #ff9800"
        )

        self.search_button = self.createButton(
            self.attendance_page, "search_button", QRect(520, 190, 141, 50),
            "Search", 16, "background-color: #007bff"
        )

        self.member_id_input = QLineEdit(self.attendance_page)
        self.member_id_input.setObjectName(u"member_id_input")
        self.member_id_input.setGeometry(QRect(190, 190, 311, 50))

        self.member_id_label = self.createLabel(
            self.attendance_page, "member_id_label", QRect(10, 190, 171, 50), "Member ID:", 16
        )

        self.attendance_table = QTableWidget(self.attendance_page)
        self.attendance_table.setObjectName(u"attendance_table")
        self.attendance_table.setGeometry(QRect(30, 260, 900, 450))

        self.createAttendanceTable()

        self.stackedWidget.addWidget(self.attendance_page)

    def createAttendanceTable(self):
        self.attendance_table.setColumnCount(7)
        self.attendance_table.setHorizontalHeaderLabels([
            "Member ID", "Last Name", "First Name", "Middle Name", "Membership Type", "Date", "Time"
        ])

    def createButton(self, parent, name, geometry, text, font_size, style_sheet):
        button = QPushButton(parent)
        button.setObjectName(name)
        button.setGeometry(geometry)
        button.setText(text)
        button.setFont(QFont("", font_size))
        button.setStyleSheet(style_sheet)
        return button

    def createLabel(self, parent, name, geometry, text, font_size):
        label = QLabel(parent)
        label.setObjectName(name)
        label.setGeometry(geometry)
        label.setText(text)
        label.setFont(QFont("", font_size))
        return label

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.gender_combo_box.setItemText(0, QCoreApplication.translate("Form", u"Male", None))
        self.gender_combo_box.setItemText(1, QCoreApplication.translate("Form", u"Female", None))
        self.membership_combo_box.setItemText(0, QCoreApplication.translate("Form", u"Type 1", None))
        self.membership_combo_box.setItemText(1, QCoreApplication.translate("Form", u"Type 2", None))
