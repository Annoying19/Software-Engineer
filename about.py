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
        Form.resize(950, 866)
        font = QFont()
        font.setFamily(u"Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        Form.setFont(font)
        Form.setStyleSheet(u"background-color: #FFFFFF; border-radius: px")
        
        self.label_12 = QLabel(Form)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(300, 60, 391, 40))
        font1 = QFont()
        font1.setPointSize(26)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setWeight(75)
        self.label_12.setFont(font1)
        self.label_12.setStyleSheet(u"font: bold")
        
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 140, 250, 250))
        self.label.setPixmap(QPixmap(u"assets/14f1ef7a-3baf-4e60-868a-ab6c82e10abd.jpg"))
        self.label.setScaledContents(True)
        
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(360, 140, 250, 250))
        self.label_2.setPixmap(QPixmap(u"assets/414460821_3703127910009500_350932625528996546_n.jpg"))
        self.label_2.setScaledContents(True)
        
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(660, 140, 250, 250))
        self.label_3.setPixmap(QPixmap(u"assets/448420613_1507002639889547_2312077778305819575_n (2).png"))
        self.label_3.setScaledContents(True)
        
        self.label_13 = QLabel(Form)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(370, 400, 241, 31))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setWeight(75)
        self.label_13.setFont(font2)
        self.label_13.setStyleSheet(u"font: bold")
        
        self.label_14 = QLabel(Form)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(700, 400, 171, 31))
        self.label_14.setFont(font2)
        self.label_14.setStyleSheet(u"font: bold")
        
        self.label_15 = QLabel(Form)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(70, 400, 241, 31))
        self.label_15.setFont(font2)
        self.label_15.setStyleSheet(u"font: bold")
        
        self.label_16 = QLabel(Form)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(430, 440, 111, 31))
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(50)
        self.label_16.setFont(font3)
        self.label_16.setStyleSheet(u"")
        
        self.label_17 = QLabel(Form)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(740, 440, 81, 31))
        self.label_17.setFont(font3)
        self.label_17.setStyleSheet(u"")
        
        self.label_18 = QLabel(Form)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(140, 440, 81, 31))
        self.label_18.setFont(font3)
        self.label_18.setStyleSheet(u"")
        
        self.label_19 = QLabel(Form)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(420, 500, 141, 40))
        self.label_19.setFont(font1)
        self.label_19.setStyleSheet(u"font: bold")
        
        self.label_20 = QLabel(Form)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(440, 560, 81, 31))
        self.label_20.setFont(font3)
        self.label_20.setStyleSheet(u"")
        
        self.label_21 = QLabel(Form)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(430, 610, 111, 31))
        self.label_21.setFont(font3)
        self.label_21.setStyleSheet(u"")
        
        self.label_22 = QLabel(Form)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(440, 660, 91, 31))
        self.label_22.setFont(font3)
        self.label_22.setStyleSheet(u"")
        
        self.label_23 = QLabel(Form)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(440, 710, 91, 31))
        self.label_23.setFont(font3)
        self.label_23.setStyleSheet(u"")

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"About the Developers", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_13.setText(QCoreApplication.translate("Form", u"Salenga, Joseph Edgar L.", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"Estanislao, Kier P.", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Robias, John Maverick B.", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Main Developer", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"Developer", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"Developer", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"System", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"python ^9.8", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"SQLite ^3.46.0", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"PySide ^2.0", None))
        self.label_23.setText(QCoreApplication.translate("Form", u"PyQt ^5.0", None))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    widget = About()
    widget.show()
    sys.exit(app.exec_())
