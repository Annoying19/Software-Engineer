from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sqlite3


class Payment(QWidget):  # Inherit from QWidget
    def __init__(self, parent=None):
        super(Payment, self).__init__(parent)
        self.setObjectName("Payment")
        self.resize(950, 800)
        self.setStyleSheet("background-color: #E0E0E0;")

        # Search Bar Input Field
        self.search_bar = QLineEdit(self)
        self.search_bar.setGeometry(QRect(30, 20, 400, 61))
        self.search_bar.setObjectName("search_bar_payment")
        self.search_bar.setStyleSheet("background: white")

        # Search Button
        self.btn_search = QPushButton(self)
        self.btn_search.setGeometry(QRect(430, 20, 71, 61))
        self.btn_search.setObjectName("btn_search_payment")
        self.btn_search.setStyleSheet("background: #4681f4;\n""color: white")

        # Table Widget Properties
        self.tableWidget = QTableWidget(self)
        table = self.tableWidget
        table.setGeometry(QRect(30, 100, 880, 620))
        table.setRowCount(0)
        table.setColumnCount(3)
        table.setObjectName("tableWidget")
        table.verticalHeader().setVisible(False)
        header = table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        header.setDefaultAlignment(Qt.AlignCenter)
        table.setStyleSheet("background: white")
        self.loadData()
        
        

        # Record option
        self.btn_record = QPushButton(self)
        self.btn_record.setGeometry(QRect(770, 730, 140, 45))
        self.btn_record.setObjectName("btn_record")
        self.btn_record.setStyleSheet(u"background: lime;\n""color: white")


        self.btn_search.clicked.connect(self.loadData)
        self.btn_record.clicked.connect(self.showRecord)
        self.retranslateUi()

    # Populate Table View
    def loadData(self):
            conn = sqlite3.connect("Software-Engineer-master/database.db")
            cursor = conn.cursor()
            
            # Load Table
            self.tableWidget.setRowCount(0)
            cursor.execute('PRAGMA table_info(Contracts)')
            columns_info = cursor.fetchall()
            column_names = [info[1] for info in columns_info]

            # Set column count and column names in table widget
            self.tableWidget.setHorizontalHeaderLabels(column_names)
            cursor.execute("SELECT * FROM Contracts")
            for row_number, row_data in enumerate(cursor):
                self.tableWidget.insertRow(row_number)  
                for column_number, data in enumerate(row_data):
                    item = QTableWidgetItem(str(data))
                    item.setTextAlignment(Qt.AlignRight)  # Align text to the right
                    self.tableWidget.setItem(row_number, column_number, item)
            
            conn.close()

    def insert_image(self, image):
        # Open a file dialog to select an image file
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Image Files (*.png *.jpg *.bmp *.gif)")
        image_label = image
        if file_name:
            # Load the image and set it to the label
            pixmap = QPixmap(file_name)
            image_label.setPixmap(pixmap.scaled(image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))


    def showRecord(self):
        popup = Record(self)
        popup.exec_()

    def retranslateUi(self):
        self.setWindowTitle("Payment")
        self.btn_search.setText(QCoreApplication.translate("Payment", "Search"))
        self.btn_record.setText(QCoreApplication.translate("Payment", "Record"))



class Record(QDialog):
    def __init__(self, parent=None):
        super(Record, self).__init__(parent)
        self.setWindowTitle("Record")
        self.resize(700, 600)
        self.setStyleSheet("background-color: #FFFFFF;")
         
        # initializaitons
        self.btn_search = QPushButton(self)
        self.add_button = QPushButton(self)
        self.insert_button = QPushButton(self)
        self.name = QLabel(self)
        self.id = QLabel(self)
        self.name_id = QLabel(self)
        self.id_id = QLabel(self)
        self.photo = QLabel(self)
        self.softcopy = QLabel(self)



        # Search Bar
        self.search_bar = QLineEdit(self)
        self.search_bar.setGeometry(QRect(30, 20, 574, 61))
        self.search_bar.setObjectName("search_bar_record")

        # Search Button 
        search = self.btn_search
        search.setGeometry(QRect(604, 20, 71, 61))
        search.setObjectName("btn_search_record")
        search.setStyleSheet("background: #4681f4;\n""color: white")

        # Add button
        add = self.add_button
        add.setObjectName("btn_record")
        add.setGeometry(QRect(535, 530, 140, 45))
        add.setStyleSheet(u"background: lime;\n""color: white")
        add.clicked.connect(self.close)

        # label font Style 
        label_font = QFont()
        label_font.setPointSize(20)
        label_font.setBold(True)

        # identifier font style
        id_font = QFont()
        id_font.setPixelSize(16)


        # Label Properties
        name = self.name
        name.setGeometry(QRect(40, 100, 121, 51))
        name.setText("Name")
        name.setFont(label_font)

        id = self.id
        id.setGeometry(QRect(40, 200, 301, 51))
        id.setText("Membership ID")
        id.setFont(label_font)

        name_id = self.name_id
        name_id.setGeometry(QRect(40, 150, 361, 51))
        name_id.setFont(id_font)

        id_id = self.id_id
        id_id.setGeometry(QRect(40, 260, 361, 51))
        id_id.setFont(id_font)

        photo = self.photo
        photo.setGeometry(QRect(450, 100, 225, 255))
        photo.setStyleSheet(u"border: 1px solid black")

        softcopy = self.softcopy
        softcopy.setGeometry(QRect(50, 373, 361, 151))
        softcopy.setStyleSheet(u"border: 1px solid black")

        insert = self.insert_button
        insert.setObjectName("record_insert_button")
        insert.setGeometry(QRect(50, 520, 361, 61))



        # translate
        add.setText(QCoreApplication.translate("Record", "Add"))
        search.setText(QCoreApplication.translate("Record", "Search"))
        insert.setText(QCoreApplication.translate("Record", "Insert File"))
    
    def searchData(self):
        search_term = self.search_bar.text()
        conn = sqlite3.connect("Software-Engineer-master/database.db")
        cursor = conn.cursor()




        



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Payment()
    window.show()
    sys.exit(app.exec_())