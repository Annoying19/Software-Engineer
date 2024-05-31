from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class REPORT(QWidget):  # Inherit from QWidget
    def __init__(self, parent=None):
        super(REPORT, self).__init__(parent)
        self.setObjectName(u"Inventory")
        self.resize(950, 800)
        self.setStyleSheet(u"background-color: #FFFFFF;")
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(50)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.retranslateUi()

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("Inventory", u"Inventory", None))
        self.label.setText(QCoreApplication.translate("Inventory", u"REPORTS", None))