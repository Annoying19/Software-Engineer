from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys
from inventory import *
from registration import *
from help import *
from about import *
from report import *
from scheduling import *
from payment import *
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 800)
        MainWindow.setMaximumSize(QSize(1200, 800))
        
        font = QFont()
        font.setPointSize(50)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.SIDE_FRAME = QFrame(self.centralwidget)
        self.SIDE_FRAME.setObjectName(u"SIDE_FRAME")
        self.SIDE_FRAME.setMaximumSize(QSize(250, 16777215))
        self.SIDE_FRAME.setLayoutDirection(Qt.LeftToRight)
        self.SIDE_FRAME.setFrameShape(QFrame.StyledPanel)
        self.SIDE_FRAME.setFrameShadow(QFrame.Raised)
        self.SIDE_FRAME.setStyleSheet(u"background-color: #002877")
        self.SIDE_FRAME_LAYOUT = QVBoxLayout(self.SIDE_FRAME)
        self.SIDE_FRAME_LAYOUT.setSpacing(0)
        self.SIDE_FRAME_LAYOUT.setObjectName(u"SIDE_FRAME_LAYOUT")
        self.SIDE_FRAME_LAYOUT.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.SIDE_FRAME_LAYOUT.setContentsMargins(0, 0, 0, 0)

        # LOGO FRAME
        self.LOGO_FRAME = QFrame(self.SIDE_FRAME)
        self.LOGO_FRAME.setObjectName(u"LOGO_FRAME")
        self.LOGO_FRAME.setMaximumSize(QSize(150, 150))
        self.LOGO_FRAME.setLayoutDirection(Qt.RightToLeft)
        self.LOGO_FRAME.setFrameShape(QFrame.NoFrame)
        self.LOGO_FRAME.setFrameShadow(QFrame.Raised)
        self.LOGO_FRAME_LAYOUT = QVBoxLayout(self.LOGO_FRAME)
        self.LOGO_FRAME_LAYOUT.setSpacing(0)
        self.LOGO_FRAME_LAYOUT.setObjectName(u"LOGO_FRAME_LAYOUT")
        self.LOGO_FRAME_LAYOUT.setContentsMargins(0, 0, 0, 0)
        # LOGO PICTURE
        self.LOGO = QLabel(self.LOGO_FRAME)
        self.LOGO.setObjectName(u"LOGO")
        self.LOGO.setLineWidth(1)
        self.LOGO.setPixmap(QPixmap(u"assets\logo.png"))
        self.LOGO.setScaledContents(True)
        self.LOGO.setAlignment(Qt.AlignCenter)
        self.LOGO.setWordWrap(False)
        self.LOGO.setIndent(1)

        self.LOGO_FRAME_LAYOUT.addWidget(self.LOGO)

        self.SIDE_FRAME_LAYOUT.addWidget(self.LOGO_FRAME)

        self.TASKBAR_FRAME = QFrame(self.SIDE_FRAME)
        self.TASKBAR_FRAME.setObjectName(u"TASKBAR_FRAME")
        self.TASKBAR_FRAME.setMaximumSize(QSize(16777215, 167777215))
        self.TASKBAR_FRAME.setStyleSheet(u"background-color: #002877")
        self.TASKBAR_FRAME.setFrameShape(QFrame.StyledPanel)
        self.TASKBAR_FRAME.setFrameShadow(QFrame.Raised)

        self.TASKBAR_FRAME_LAYOUT = QVBoxLayout(self.TASKBAR_FRAME)
        self.TASKBAR_FRAME_LAYOUT.setSpacing(0)
        self.TASKBAR_FRAME_LAYOUT.setObjectName(u"TASKBAR_FRAME_LAYOUT")
        self.TASKBAR_FRAME_LAYOUT.setContentsMargins(0, 0, 0, 0)

        # CREATING FONT SIZE OF THE BUTTONS
        FONT_BUTTON = QFont()
        FONT_BUTTON.setPointSize(16)
        FONT_BUTTON.setWeight(75)

        # INVENTORY BUTTON
        self.INVENTORY_BUTTON = QPushButton(self.TASKBAR_FRAME)
        self.INVENTORY_BUTTON.setObjectName(u"INVENTORY_BUTTON")
        self.INVENTORY_BUTTON.setMaximumSize(QSize(250, 60))
        self.INVENTORY_BUTTON.setFont(FONT_BUTTON)
        self.INVENTORY_BUTTON.setFocusPolicy(Qt.StrongFocus)
        self.TASKBAR_FRAME_LAYOUT.addWidget(self.INVENTORY_BUTTON)
    
        # REGISTRATION BUTTON
        self.REGISTRATION_BUTTON = QPushButton(self.TASKBAR_FRAME)
        self.REGISTRATION_BUTTON.setObjectName(u"REGISTRATION_BUTTON")
        self.REGISTRATION_BUTTON.setMaximumSize(QSize(250, 60))
        self.REGISTRATION_BUTTON.setFont(FONT_BUTTON)
        self.REGISTRATION_BUTTON.setFocusPolicy(Qt.StrongFocus)
        self.TASKBAR_FRAME_LAYOUT.addWidget(self.REGISTRATION_BUTTON)

        # SCHEDULING BUTTON
        self.SCHEDULING_BUTTON = QPushButton(self.TASKBAR_FRAME)
        self.SCHEDULING_BUTTON.setObjectName(u"SCHEDULING_BUTTON")
        self.SCHEDULING_BUTTON.setMaximumSize(QSize(250, 60))
        self.SCHEDULING_BUTTON.setFont(FONT_BUTTON)
        self.SCHEDULING_BUTTON.setFocusPolicy(Qt.StrongFocus)
        self.TASKBAR_FRAME_LAYOUT.addWidget(self.SCHEDULING_BUTTON)

        # REPORT BUTTON
        self.REPORT_BUTTON = QPushButton(self.TASKBAR_FRAME)
        self.REPORT_BUTTON.setObjectName(u"REPORT_BUTTON")
        self.REPORT_BUTTON.setMaximumSize(QSize(250, 60))
        self.REPORT_BUTTON.setFont(FONT_BUTTON)
        self.REPORT_BUTTON.setFocusPolicy(Qt.StrongFocus)
        self.TASKBAR_FRAME_LAYOUT.addWidget(self.REPORT_BUTTON)

        # PAYMENT BUTTON
        self.PAYMENT_BUTTON = QPushButton(self.TASKBAR_FRAME)
        self.PAYMENT_BUTTON.setObjectName(u"PAYMENT_BUTTON")
        self.PAYMENT_BUTTON.setMaximumSize(QSize(250, 60))
        self.PAYMENT_BUTTON.setFont(FONT_BUTTON)
        self.PAYMENT_BUTTON.setFocusPolicy(Qt.StrongFocus)
        self.TASKBAR_FRAME_LAYOUT.addWidget(self.PAYMENT_BUTTON)

        # HELP BUTTON
        self.HELP_BUTTON = QPushButton(self.TASKBAR_FRAME)
        self.HELP_BUTTON.setObjectName(u"HELP_BUTTON")
        self.HELP_BUTTON.setMaximumSize(QSize(250, 60))
        self.HELP_BUTTON.setFont(FONT_BUTTON)
        self.HELP_BUTTON.setFocusPolicy(Qt.StrongFocus)
        self.TASKBAR_FRAME_LAYOUT.addWidget(self.HELP_BUTTON)

        # ABOUT BUTTON
        self.ABOUT_BUTTON = QPushButton(self.TASKBAR_FRAME)
        self.ABOUT_BUTTON.setObjectName(u"ABOUT_BUTTON")
        self.ABOUT_BUTTON.setMaximumSize(QSize(250, 60))
        self.ABOUT_BUTTON.setFont(FONT_BUTTON)
        self.ABOUT_BUTTON.setFocusPolicy(Qt.StrongFocus)
        self.TASKBAR_FRAME_LAYOUT.addWidget(self.ABOUT_BUTTON)
        self.SIDE_FRAME_LAYOUT.addWidget(self.TASKBAR_FRAME)


    
        # LOGOUT BUTTON
        self.LOGOUT_FRAME = QFrame(self.SIDE_FRAME)
        self.LOGOUT_FRAME.setObjectName(u"LOGOUT_FRAME")
        self.LOGOUT_FRAME.setMaximumSize(QSize(250, 100))
        self.LOGOUT_FRAME.setFrameShape(QFrame.StyledPanel)
        self.LOGOUT_FRAME.setFrameShadow(QFrame.Raised)
        self.LOGOUT_BUTTON = QPushButton(self.LOGOUT_FRAME)
        self.LOGOUT_BUTTON.setObjectName(u"LOGOUT_BUTTON")
        self.LOGOUT_BUTTON.setMaximumSize(QSize(250, 60))
        self.LOGOUT_BUTTON.setFont(FONT_BUTTON)
        self.LOGOUT_BUTTON.setFocusPolicy(Qt.StrongFocus)
        self.LOGOUT_BUTTON.setStyleSheet(u"background-color: #000000; color: #FFFFFF; ")
        self.LOGOUT_FRAME_LAYOUT = QHBoxLayout(self.LOGOUT_FRAME)
        self.LOGOUT_FRAME_LAYOUT.setSpacing(0)
        self.LOGOUT_FRAME_LAYOUT.setObjectName(u"LOGOUT_FRAME_LAYOUT")
        self.LOGOUT_FRAME_LAYOUT.setContentsMargins(0, -1, 0, 0)
        self.LOGOUT_FRAME_LAYOUT.addWidget(self.LOGOUT_BUTTON)

        self.SIDE_FRAME_LAYOUT.addWidget(self.LOGOUT_FRAME)

        self.horizontalLayout.addWidget(self.SIDE_FRAME)

        self.MAIN_SCREEN = QFrame(self.centralwidget)
        self.MAIN_SCREEN.setObjectName(u"MAIN_SCREEN")
        self.MAIN_SCREEN.setMaximumSize(QSize(950, 800))
        self.MAIN_SCREEN.setStyleSheet(u"background-color: #FFFFFF")
        self.MAIN_SCREEN.setFrameShape(QFrame.StyledPanel)
        self.MAIN_SCREEN.setFrameShadow(QFrame.Raised)
        self.MAIN_SCREEN_LAYOUT = QVBoxLayout(self.MAIN_SCREEN)
        self.MAIN_SCREEN_LAYOUT.setObjectName(u"MAIN_SCREEN_LAYOUT")
        self.stackedWidget = QStackedWidget(self.MAIN_SCREEN)
        self.stackedWidget.setObjectName(u"stackedWidget")


        # Initializing QFRame of each
        self.Inventory = INVENTORY()
        self.Registration = REGISTRATION()
        self.Scheduling = SCHEDULING()
        self.Reports = REPORT()
        self.Payment = PAYMENT()
        self.Help = HELP()
        self.About = ABOUT()

        # Adding the Main Modules in a Stacked Widget
        self.stackedWidget.addWidget(self.Inventory)
        self.stackedWidget.addWidget(self.Registration)
        self.stackedWidget.addWidget(self.Scheduling)
        self.stackedWidget.addWidget(self.Reports)
        self.stackedWidget.addWidget(self.Payment)
        self.stackedWidget.addWidget(self.Help)
        self.stackedWidget.addWidget(self.About)

        self.MAIN_SCREEN_LAYOUT.addWidget(self.stackedWidget)
        self.horizontalLayout.addWidget(self.MAIN_SCREEN)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.INVENTORY_BUTTON.setText(QCoreApplication.translate("MainWindow", u"Inventory", None))
        self.REGISTRATION_BUTTON.setText(QCoreApplication.translate("MainWindow", u"Registration", None))
        self.SCHEDULING_BUTTON.setText(QCoreApplication.translate("MainWindow", u"Scheduling", None))
        self.REPORT_BUTTON.setText(QCoreApplication.translate("MainWindow", u"Reports", None))
        self.PAYMENT_BUTTON.setText(QCoreApplication.translate("MainWindow", u"Payment", None))
        self.HELP_BUTTON.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.ABOUT_BUTTON.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.LOGOUT_BUTTON.setText(QCoreApplication.translate("MainWindow", u"Logout", None))

    # retranslateUi


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        # Connect the buttons to switch to the appropriate page
        self.ui.INVENTORY_BUTTON.clicked.connect(lambda: self.switch_page(self.ui.INVENTORY_BUTTON, self.ui.Inventory))
        self.ui.REGISTRATION_BUTTON.clicked.connect(lambda: self.switch_page(self.ui.REGISTRATION_BUTTON, self.ui.Registration))
        self.ui.SCHEDULING_BUTTON.clicked.connect(lambda: self.switch_page(self.ui.SCHEDULING_BUTTON, self.ui.Scheduling))
        self.ui.REPORT_BUTTON.clicked.connect(lambda: self.switch_page(self.ui.REPORT_BUTTON, self.ui.Reports))
        self.ui.PAYMENT_BUTTON.clicked.connect(lambda: self.switch_page(self.ui.PAYMENT_BUTTON, self.ui.Payment))
        self.ui.HELP_BUTTON.clicked.connect(lambda: self.switch_page(self.ui.HELP_BUTTON, self.ui.Help))
        self.ui.ABOUT_BUTTON.clicked.connect(lambda: self.switch_page(self.ui.ABOUT_BUTTON, self.ui.About))
        self.ui.LOGOUT_BUTTON.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Inventory))  # Switch to INVENTORY page

        # Set initial styles
        self.update_button_styles(self.ui.INVENTORY_BUTTON)

    def switch_page(self, button, page):
        self.ui.stackedWidget.setCurrentWidget(page)
        self.update_button_styles(button)

    def update_button_styles(self, active_button):
        for button in [self.ui.INVENTORY_BUTTON, self.ui.REGISTRATION_BUTTON, self.ui.SCHEDULING_BUTTON,
                       self.ui.REPORT_BUTTON, self.ui.PAYMENT_BUTTON, self.ui.HELP_BUTTON, self.ui.ABOUT_BUTTON]:
            if button == active_button:
                button.setStyleSheet("background-color: #FFFFFF; color: #000000;")
            else:
                button.setStyleSheet("background-color: transparent; color: #FFFFFF;")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())