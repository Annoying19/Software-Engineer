from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from functools import partial
from login import *
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        MainWindow.setMaximumSize(QSize(1200, 800))

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.centralwidget_Layout = QHBoxLayout(self.centralwidget)
        self.centralwidget_Layout.setSpacing(0)
        self.centralwidget_Layout.setContentsMargins(0, 0, 0, 0)

        self.side_frame = QFrame(self.centralwidget)
        self.side_frame.setObjectName("side_frame")
        self.side_frame.setMinimumSize(QSize(250, 800))
        self.side_frame.setStyleSheet("background-color: #002877")
        self.side_frame.setFrameShape(QFrame.StyledPanel)

        self.side_frame_layout = QVBoxLayout(self.side_frame)
        self.side_frame_layout.setSpacing(0)
        self.side_frame_layout.setContentsMargins(0, 0, 0, 0)
        
        self.logo_frame = QFrame(self.side_frame)
        self.logo_frame.setObjectName("logo_frame")
        self.logo_frame.setMinimumSize(QSize(150, 190))
        self.logo_frame.setMaximumSize(QSize(250, 190))

        self.logo_frame_layout = QVBoxLayout(self.logo_frame)
        self.logo_frame_layout.setSpacing(0)
        self.logo_frame_layout.setContentsMargins(25, 0, 0, 0)

        self.logo = QLabel(self.logo_frame)
        self.logo.setObjectName("logo")
        self.logo.setMinimumSize(QSize(150, 190))
        self.logo.setMaximumSize(QSize(200, 190))
        self.logo.setPixmap(QPixmap("assets\slimmerslogo.jpg"))
        self.logo.setStyleSheet("border-radius: 20px; background-color: #FFFFFF")
        self.logo.setScaledContents(True)

        self.taskbar_frame = QFrame(self.side_frame)
        self.taskbar_frame.setObjectName("taskbar_frame")
        self.taskbar_frame.setMinimumSize(QSize(250, 550))

        self.taskbar_frame_layout = QVBoxLayout(self.taskbar_frame)
        self.taskbar_frame_layout.setSpacing(0)
        self.taskbar_frame_layout.setContentsMargins(0, 6, 0, 0)

        self.buttons = {}
        button_names = [
            "Inventory", "Registration", "Scheduling", "Reports", "Payment",
            "User Logs", "Maintenance", "Help", "About"
        ]

        font = QFont()
        font.setPointSize(16)

        # Creating the Buttons
        for name in button_names:
            button = QPushButton(self.taskbar_frame)
            button.setObjectName(f"{name.lower()}_button")
            button.setMinimumSize(QSize(250, 60))
            button.setFont(font)
            button.setText(name)
            self.taskbar_frame_layout.addWidget(button)
            self.buttons[name.lower()] = button

        # logout frame
        self.logout_frame = QFrame(self.side_frame)
        self.logout_frame.setObjectName("logout_frame")
        self.logout_frame.setMinimumSize(QSize(250, 60))

        self.logout_frame_layout = QVBoxLayout(self.logout_frame)
        self.logout_frame_layout.setSpacing(0)
        self.logout_frame_layout.setContentsMargins(0, 0, 0, 0)

        # logout button
        self.logout_button = QPushButton(self.logout_frame)
        self.logout_button.setObjectName("logout_button")
        self.logout_button.setMinimumSize(QSize(250, 60))
        self.logout_button.setFont(font)
        self.logout_button.setStyleSheet("background-color: #000000; color: #FFFFFF")
        self.logout_button.setText("Logout")

        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName("main_frame")
        self.main_frame.setMinimumSize(QSize(950, 800))
        self.main_frame.setStyleSheet("background-color: #FFFFFF")

        self.main_frame_layout = QVBoxLayout(self.main_frame)
        self.main_frame_layout.setSpacing(0)
        self.main_frame_layout.setContentsMargins(0, 0, 0, 0)

        self.stacked_widget = QStackedWidget(self.main_frame)
        self.stacked_widget.setObjectName("stacked_widget")

        self.pages = {}
        for name in button_names:
            page = QWidget()
            page.setObjectName(name.lower())
            self.stacked_widget.addWidget(page)
            self.pages[name.lower()] = page

        self.logo_frame_layout.addWidget(self.logo)
        self.side_frame_layout.addWidget(self.logo_frame)
        self.side_frame_layout.addWidget(self.taskbar_frame)
        self.side_frame_layout.addWidget(self.logout_frame)
        self.logout_frame_layout.addWidget(self.logout_button)
        self.centralwidget_Layout.addWidget(self.side_frame)
        self.main_frame_layout.addWidget(self.stacked_widget)
        self.centralwidget_Layout.addWidget(self.main_frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "MainWindow", None))
        self.logout_button.setText(QCoreApplication.translate("MainWindow", "Logout", None))


class Admin(QMainWindow):
    def __init__(self):
        super(Admin, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect the buttons to switch to the appropriate page
        for name, button in self.ui.buttons.items():
            button.clicked.connect(partial(self.switch_page, name))

        self.ui.logout_button.clicked.connect(self.switch_login_window)

        self.update_button_styles("inventory")

    def switch_login_window(self):
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()

    def switch_page(self, page_name):
        self.ui.stacked_widget.setCurrentWidget(self.ui.pages[page_name])
        self.update_button_styles(page_name)

    def update_button_styles(self, active_page):
        for name, button in self.ui.buttons.items():
            if name == active_page:
                button.setStyleSheet("background-color: #FFFFFF; color: #000000;")
            else:
                button.setStyleSheet("background-color: transparent; color: #FFFFFF;")


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Admin()
    window.show()
    sys.exit(app.exec_())
