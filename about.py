from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class About(QWidget):  # Inherit from QWidget
    def __init__(self):
        super(About, self).__init__()
        self.setupUi(self)

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(950, 800)
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        Form.setFont(font)
        Form.setStyleSheet(u"background-color: #FFFFFF; border-radius: px")
        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(30, 150, 891, 171))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(False)
        font1.setWeight(50)
        self.label_8.setFont(font1)
        self.label_12 = QLabel(Form)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(340, 90, 321, 40))
        font2 = QFont()
        font2.setPointSize(26)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setWeight(75)
        self.label_12.setFont(font2)
        self.label_12.setStyleSheet(u"font: bold")
        self.label_16 = QLabel(Form)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(380, 370, 201, 40))
        self.label_16.setFont(font2)
        self.label_16.setStyleSheet(u"font: bold")
        self.label_15 = QLabel(Form)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(410, 640, 151, 31))
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_15.setFont(font3)
        self.label_18 = QLabel(Form)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(740, 640, 101, 31))
        self.label_18.setFont(font3)
        self.label_19 = QLabel(Form)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(130, 640, 101, 31))
        self.label_19.setFont(font3)
        self.label_20 = QLabel(Form)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(80, 430, 200, 200))
        self.label_20.setFont(font3)
        self.label_20.setPixmap(QPixmap(u"assets\mav.jpg"))
        self.label_20.setScaledContents(True)
        self.label_21 = QLabel(Form)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(390, 430, 200, 200))
        self.label_21.setFont(font3)
        self.label_21.setPixmap(QPixmap(u"assets\joseph.jpg"))
        self.label_21.setScaledContents(True)
        self.label_22 = QLabel(Form)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(680, 430, 200, 200))
        self.label_22.setFont(font3)
        self.label_22.setStyleSheet(u"opacity: 50%")
        self.label_22.setPixmap(QPixmap(u"assets\kier.png"))
        self.label_22.setScaledContents(True)
        self.label_23 = QLabel(Form)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(400, 670, 191, 31))
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(False)
        font4.setWeight(50)
        self.label_23.setFont(font4)
        self.label_24 = QLabel(Form)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(720, 670, 131, 31))
        self.label_24.setFont(font4)
        self.label_25 = QLabel(Form)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(90, 670, 181, 31))
        self.label_25.setFont(font4)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Welcome to the Gym Management System of SM North Edsa Main Building. The system is <br> specifically designed for employees at SM North EDSA Main Building to ensure an efficient and <br> hassle-free management of gym operations. The system simplifies gym operations and has an <br> efficient way to manage memberships, schedules, facilities, and many more. The system utilizes<br> Python v9.8 as its main programming language, PyQt v5.0 and PySide v2.0 as its front-end <Br> framework, and SQLite v3.46.0 as its backend.\n"
        "", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"About the System", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Developers", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Lead Developer", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"Developer", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"Developer", None))
        self.label_20.setText("")
        self.label_21.setText("")
        self.label_22.setText("")
        self.label_23.setText(QCoreApplication.translate("Form", u"Salenga, Joseph Edgar L.", None))
        self.label_24.setText(QCoreApplication.translate("Form", u"Estanislao, Kier P.", None))
        self.label_25.setText(QCoreApplication.translate("Form", u"Robias, John Maverick B.", None))
    # retranslateUi


    # retranslateUi

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    widget = About()
    widget.show()
    sys.exit(app.exec_())
