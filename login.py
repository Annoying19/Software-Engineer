import sqlite3
import hashlib
from PySide2.QtCore import QSize, Qt, QCoreApplication
from PySide2.QtGui import QPixmap, QFont
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
from staff import *
from admin import * 

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Window")
        self.resize(1200, 800)
        self.setMaximumSize(QSize(1200, 800))
        self.setStyleSheet("background-color: #002877")
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.user_interfaec()

    def user_interfaec(self):
        self.fonts()
        self.logo()
        self.input_fields()
        self.login_button()

    def fonts(self):
        self.username_password_font = QFont()
        self.username_password_font.setPointSize(12)
        self.login_font = QFont()
        self.login_font.setPointSize(12)
        self.login_font.setBold(True)

    def logo(self):
        border_logo_style = "background-color: #FFFFFF; border: 5px solid; border-radius: 75px"
        self.border_logo = QLabel(self.central_widget, objectName="border_logo")
        self.border_logo.setGeometry(360, 30, 500, 720)
        self.border_logo.setStyleSheet(border_logo_style)

        logo_style = "border-radius: 75px"
        self.logo = QLabel(self.central_widget, objectName="logo")
        self.logo.setGeometry(490, 80, 261, 571)
        self.logo.setStyleSheet(logo_style)
        self.logo.setPixmap(QPixmap("assets/slimmers_login.png"))
        self.logo.setScaledContents(True)

    def input_fields(self):
        label_style = "background-color: #FFFFFF"
        input_style = "background-color: #D9D9D9"
        self.username_label = QLabel("Username", self.central_widget, objectName="username_label")
        self.username_label.setGeometry(440, 460, 71, 16)
        self.username_label.setFont(self.username_password_font)
        self.username_label.setStyleSheet(label_style)

        self.username_input = QLineEdit(self.central_widget, objectName="username_input")
        self.username_input.setGeometry(440, 480, 341, 31)
        self.username_input.setStyleSheet(input_style)

        self.password_label = QLabel("Password", self.central_widget, objectName="password_label")
        self.password_label.setGeometry(440, 530, 71, 16)
        self.password_label.setFont(self.username_password_font)
        self.password_label.setStyleSheet(label_style)

        self.password_input = QLineEdit(self.central_widget, objectName="password_input")
        self.password_input.setGeometry(440, 550, 341, 31)
        self.password_input.setStyleSheet(input_style)
        self.password_input.setEchoMode(QLineEdit.Password)

    def login_button(self):
        button_style = "background-color: #002877; border-radius: 10px;"
        self.login_button = QPushButton("Login", self.central_widget, objectName="login_button")
        self.login_button.setGeometry(560, 600, 111, 41)
        self.login_button.setFont(self.login_font)
        self.login_button.setStyleSheet(button_style)
        self.login_button.clicked.connect(self.handle_login)

    def open_main_window(self, role):
        if role == "Admin":
            self.main_window = Admin()
            self.main_window.show()
            self.close()
        else:
            self.main_window = Staff()
            self.main_window.show()
            self.close()

    def handle_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        valid, role = self.check_credentials(username, password)
        if valid:
            QMessageBox.information(self, "Login Successful", "You have successfully logged in.")                         
            self.open_main_window(role)
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password.")
            

    def check_credentials(self, username, password):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        cursor.execute('''
        SELECT password_hash, role FROM Users WHERE username = ?
        ''', (username,))
        result = cursor.fetchone()
        print(result)
        connection.close()
        
        if result:
            password_hash, role = result
            if self.verify_password(password, password_hash):
                print(f"Logged in as {role}")
                return True, role
        return False

    def verify_password(self, password, password_hash):
        # Assuming password_hash is stored as SHA256 hash
        password_bytes = password.encode()
        hashed_password = hashlib.sha256(password_bytes).hexdigest()
        return hashed_password == password_hash

    
if __name__ == "__main__":
    app = QApplication([])
    window = Login()
    window.show()
    app.exec_()
