from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import os


class Help(QWidget):  # Inherit from QWidget
    def __init__(self, parent=None):
        super(Help, self).__init__(parent)
        self.setObjectName(u"Help")
        self.resize(950, 800)
        self.setStyleSheet(u"background-color: #FFFFFF;")
        self.setWindowTitle("Help")

        
        self.label = QLabel(self)
        self.label.setGeometry(QRect(40, 20, 401, 111))
        font = QFont()
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QLabel(self)
        self.label_2.setGeometry(QRect(50, 120, 881, 61))
        font = QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("background: transparent;")
        self.maintenance_button = QPushButton(self)
        self.maintenance_button.setGeometry(QRect(660, 530, 180, 50))
        self.maintenance_button.setMaximumSize(QSize(210, 70))
        self.maintenance_button.setStyleSheet("background: #4681f4; color: white; border-radius: 15px; font-weight: bold; ")
        self.maintenance_button.setObjectName("maintenance_button")
        self.label_3 = QLabel(self)
        self.label_3.setGeometry(QRect(50, 150, 861, 61))
        font = QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("background: transparent;")
        self.reports_button = QPushButton(self)
        self.reports_button.setGeometry(QRect(660, 460, 180, 50))
        self.reports_button.setMaximumSize(QSize(210, 70))
        self.reports_button.setStyleSheet("background: #4681f4; color: white; border-radius: 15px; font-weight: bold;")
        self.reports_button.setObjectName("reports_button")
        self.userlogs_button = QPushButton(self)
        self.userlogs_button.setGeometry(QRect(660, 670, 180, 50))
        self.userlogs_button.setMaximumSize(QSize(210, 70))
        self.userlogs_button.setStyleSheet("background: #4681f4; color: white; border-radius: 15px; font-weight: bold;")
        self.userlogs_button.setObjectName("userlogs_button")
        self.registration_button = QPushButton(self)
        self.registration_button.setGeometry(QRect(660, 320, 180, 50))
        self.registration_button.setMaximumSize(QSize(210, 70))
        self.registration_button.setStyleSheet("background: #4681f4; color: white; border-radius: 15px; font-weight: bold;")
        self.registration_button.setObjectName("registration_button")
        self.payment_button = QPushButton(self)
        self.payment_button.setGeometry(QRect(660, 600, 180, 50))
        self.payment_button.setMaximumSize(QSize(210, 70))
        self.payment_button.setStyleSheet("background: #4681f4; color: white; border-radius: 15px; font-weight: bold;")
        self.payment_button.setObjectName("payment_button")
        self.scheduling_button = QPushButton(self)
        self.scheduling_button.setGeometry(QRect(660, 390, 180, 50))
        self.scheduling_button.setMaximumSize(QSize(210, 70))
        self.scheduling_button.setStyleSheet("background: #4681f4; color: white; border-radius: 15px; font-weight: bold;")
        self.scheduling_button.setObjectName("scheduling_button")
        self.inventory_button = QPushButton(self)
        self.inventory_button.setGeometry(QRect(660, 250, 180, 50))
        self.inventory_button.setMaximumSize(QSize(210, 70))
        self.inventory_button.setStyleSheet("background: #4681f4; color: white; border-radius: 15px; font-weight: bold;")
        self.inventory_button.setObjectName("inventory_button")
        self.label_4 = QLabel(self)
        self.label_4.setGeometry(QRect(50, 180, 861, 61))
        font = QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_4.setStyleSheet("background: transparent;")
        self.faq_button = QPushButton(self)
        self.faq_button.setGeometry(QRect(660, 50, 180, 50))
        self.faq_button.setMaximumSize(QSize(210, 70))
        self.faq_button.setStyleSheet("background: #E34234; color: white; border-radius: 15px; font-weight: bold")
        self.faq_button.setObjectName("faq_button")
        self.label_5 = QLabel(self)
        self.label_5.setGeometry(QRect(50, 270, 71, 16))
        self.label_5.setStyleSheet("font-weight: bold;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QLabel(self)
        self.label_6.setGeometry(QRect(130, 270, 511, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QLabel(self)
        self.label_7.setGeometry(QRect(720, 210, 55, 16))
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QLabel(self)
        self.label_8.setGeometry(QRect(140, 340, 511, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QLabel(self)
        self.label_9.setGeometry(QRect(50, 340, 91, 16))
        self.label_9.setStyleSheet("font-weight: bold;")
        self.label_9.setObjectName("label_9")
        self.label_10 = QLabel(self)
        self.label_10.setGeometry(QRect(130, 410, 511, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QLabel(self)
        self.label_11.setGeometry(QRect(50, 410, 81, 16))
        self.label_11.setStyleSheet("font-weight: bold;")
        self.label_11.setObjectName("label_11")
        self.label_12 = QLabel(self)
        self.label_12.setGeometry(QRect(110, 480, 511, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QLabel(self)
        self.label_13.setGeometry(QRect(50, 480, 71, 16))
        self.label_13.setStyleSheet("font-weight: bold;")
        self.label_13.setObjectName("label_13")
        self.label_14 = QLabel(self)
        self.label_14.setGeometry(QRect(150, 550, 511, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QLabel(self)
        self.label_15.setGeometry(QRect(50, 550, 91, 16))
        self.label_15.setStyleSheet("font-weight: bold;")
        self.label_15.setObjectName("label_15")
        self.label_16 = QLabel(self)
        self.label_16.setGeometry(QRect(120, 620, 511, 16))
        self.label_16.setObjectName("label_16")
        self.label_17 = QLabel(self)
        self.label_17.setGeometry(QRect(50, 620, 71, 16))
        self.label_17.setStyleSheet("font-weight: bold;")
        self.label_17.setObjectName("label_17")
        self.label_18 = QLabel(self)
        self.label_18.setGeometry(QRect(50, 690, 71, 16))
        self.label_18.setStyleSheet("font-weight: bold;")
        self.label_18.setObjectName("label_18")
        self.label_19 = QLabel(self)
        self.label_19.setGeometry(QRect(120, 690, 511, 16))
        self.label_19.setObjectName("label_19")
        self.label_20 = QLabel(self)
        self.label_20.setGeometry(QRect(720, 220, 55, 16))
        self.label_20.setStyleSheet("font-weight: bold")
        self.label_20.setObjectName("label_20")
        self.label_21 = QLabel(self)
        self.label_21.setGeometry(QRect(150, 570, 511, 16))
        self.label_21.setObjectName("label_21")

        self.inventory_button.clicked.connect(lambda: self.display("inventory.pdf"))
        self.scheduling_button.clicked.connect(lambda: self.display("scheduling.pdf"))
        self.payment_button.clicked.connect(lambda: self.display("payment.pdf"))
        self.registration_button.clicked.connect(lambda: self.display("registration.pdf"))
        self.reports_button.clicked.connect(lambda: self.display("reports.pdf"))
        self.userlogs_button.clicked.connect(lambda: self.display("userlogs.pdf"))
        self.maintenance_button.clicked.connect(lambda: self.display("maintenance.pdf"))
        self.faq_button.clicked.connect(lambda: self.display("faq.pdf"))

        self.retranslateUi()
        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Help"))
        self.label.setText(_translate("self", "Users Manual"))
        self.label_2.setText(_translate("self", "The system is composed of modules that perselfs the various operations the gym operates in. It is modular in"))
        self.maintenance_button.setText(_translate("self", "Maintenance"))
        self.label_3.setText(_translate("self", "nature meaning each module is independent of each other, having the ability to function without it\'s other parts"))
        self.reports_button.setText(_translate("self", "Reports"))
        self.userlogs_button.setText(_translate("self", "User Logs"))
        self.registration_button.setText(_translate("self", "Registration"))
        self.payment_button.setText(_translate("self", "Payment"))
        self.scheduling_button.setText(_translate("self", "Scheduling"))
        self.inventory_button.setText(_translate("self", "Inventory"))
        self.label_4.setText(_translate("self", "The following are guidelines to the modular units within the system"))
        self.faq_button.setText(_translate("self", "FAQ"))
        self.label_5.setText(_translate("self", "Inventory: "))
        self.label_6.setText(_translate("self", "In the inventory module is where we view the items stored within the gym"))
        self.label_8.setText(_translate("self", "In the registration module is where we register new entries to our system"))
        self.label_9.setText(_translate("self", "Registration:"))
        self.label_10.setText(_translate("self", "In the scheduling module is where we book and monitor events within the gym"))
        self.label_11.setText(_translate("self", "Scheduling:"))
        self.label_12.setText(_translate("self", "In the reports module is where we generate reports to monitor the gym\'s perselfance"))
        self.label_13.setText(_translate("self", "Reports:"))
        self.label_14.setText(_translate("self", "In the maintenance module is where we update and backup the "))
        self.label_15.setText(_translate("self", "Maintenance:"))
        self.label_16.setText(_translate("self", "In the payment module is where we store and record contracts of the gym"))
        self.label_17.setText(_translate("self", "Payment: "))
        self.label_18.setText(_translate("self", "User Logs:"))
        self.label_19.setText(_translate("self", "In the user Logs module is where we view the activities of the user "))
        self.label_20.setText(_translate("self", "DETAILS"))
        self.label_21.setText(_translate("self", "contents of our system"))

    def display(self, option):
        file_path = (f"C:/Users/maver/OneDrive/Desktop/MyModule/Software-Engineer-master/ui/{option}")
        print(file_path)
        if os.path.isfile(file_path):
            os.startfile(file_path)

        
        


        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Help()
    window.show()
    sys.exit(app.exec_())
