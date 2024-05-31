from PySide2.QtCore import QSize, Qt, QCoreApplication
from PySide2.QtGui import QPixmap, QFont
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Window")
        self.resize(1200, 800)
        self.setMaximumSize(QSize(1200, 800))
        self.setStyleSheet("background-color: #002877")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.init_ui()

    def init_ui(self):
        self.init_fonts()
        self.init_logo()
        self.init_input_fields()
        self.init_login_button()

    def init_fonts(self):
        self.username_password_font = QFont()
        self.username_password_font.setPointSize(12)

        self.login_font = QFont()
        self.login_font.setPointSize(12)
        self.login_font.setBold(True)

    def init_logo(self):
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

    def init_input_fields(self):
        label_style = "background-color: #FFFFFF"
        self.username_label = QLabel("Username", self.central_widget, objectName="username_label")
        self.username_label.setGeometry(440, 460, 71, 16)
        self.username_label.setFont(self.username_password_font)
        self.username_label.setStyleSheet(label_style)

        self.username_input = QLineEdit(self.central_widget, objectName="username_input")
        self.username_input.setGeometry(440, 480, 341, 31)
        self.username_input.setStyleSheet("background-color: #D9D9D9")

        self.password_label = QLabel("Password", self.central_widget, objectName="password_label")
        self.password_label.setGeometry(440, 530, 71, 16)
        self.password_label.setFont(self.username_password_font)
        self.password_label.setStyleSheet(label_style)

        self.password_input = QLineEdit(self.central_widget, objectName="password_input")
        self.password_input.setGeometry(440, 550, 341, 31)
        self.password_input.setStyleSheet("background-color: #D9D9D9")

    def init_login_button(self):
        button_style = "background-color: #002877; border-radius: 10px;"
        self.login_button = QPushButton("Login", self.central_widget, objectName="login_button")
        self.login_button.setGeometry(560, 600, 111, 41)
        self.login_button.setFont(self.login_font)
        self.login_button.setStyleSheet(button_style)

if __name__ == "__main__":
    app = QApplication([])
    window = LoginWindow()
    window.show()
    app.exec_()
