<<<<<<< HEAD
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sqlite3
from assets import *

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
        self.search_bar.setPlaceholderText("Enter Member ID here")
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

        self.loadData
        self.btn_search.clicked.connect(self.search)
        self.btn_record.clicked.connect(self.showRecord)
        self.retranslateUi()

    # Populate Table View
    def loadData(self):
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
                    # Handle BLOB data
                    if isinstance(data, bytes):
                        image = QImage.fromData(data)
                        if not image.isNull():
                            pixmap = QPixmap.fromImage(image)
                            label = QLabel()
                            label.setPixmap(pixmap.scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation))
                            label.setAlignment(Qt.AlignRight)
                            self.tableWidget.setCellWidget(row_number, column_number, label)
                        else:
                            item = QTableWidgetItem("Invalid Image")
                            item.setTextAlignment(Qt.AlignRight)
                            self.tableWidget.setItem(row_number, column_number, item)
                    else:
                        item = QTableWidgetItem(str(data))
                        item.setTextAlignment(Qt.AlignRight)
                        self.tableWidget.setItem(row_number, column_number, item)
            


    def search(self):
        search_term = self.search_bar.text()
        self.tableWidget.setRowCount(0)

        cursor.execute("SELECT * FROM Contracts WHERE member_id = ?", (search_term,))
        for row_number, row_data in enumerate(cursor):
            self.tableWidget.insertRow(row_number)  
            for column_number, data in enumerate(row_data):
                # Handle BLOB data
                if isinstance(data, bytes):
                    image = QImage.fromData(data)
                    if not image.isNull():
                        pixmap = QPixmap.fromImage(image)
                        label = QLabel()
                        label.setPixmap(pixmap.scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation))
                        label.setAlignment(Qt.AlignRight)
                        self.tableWidget.setCellWidget(row_number, column_number, label)
                    else:
                        item = QTableWidgetItem("Invalid Image")
                        item.setTextAlignment(Qt.AlignRight)
                        self.tableWidget.setItem(row_number, column_number, item)
                else:
                    item = QTableWidgetItem(str(data))
                    item.setTextAlignment(Qt.AlignRight)
                    self.tableWidget.setItem(row_number, column_number, item)
    

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
        self.setStyleSheet("background-color: #E0E0E0;")
         
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
        self.search_bar.setPlaceholderText("Enter Member ID here")
        self.search_bar.setStyleSheet("background: white")

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
        
        # Insert button
        insert = self.insert_button
        insert.setObjectName("record_insert_button")
        insert.setGeometry(QRect(50, 520, 361, 61))
        insert.setStyleSheet("background: red;\n""color: white")

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
        name_id.setStyleSheet("background: white;\n""border: 1px solid black")

        id_id = self.id_id
        id_id.setGeometry(QRect(40, 260, 361, 51))
        id_id.setFont(id_font)
        id_id.setStyleSheet("background: white;\n""border: 1px solid black")

        photo = self.photo
        photo.setGeometry(QRect(450, 100, 225, 255))
        photo.setStyleSheet("background: white;\n""border: 1px solid black")

        softcopy = self.softcopy
        softcopy.setGeometry(QRect(50, 373, 361, 151))
        softcopy.setStyleSheet("background: white;\n""border: 1px solid black")
        self.copy = None

        

        self.btn_search.clicked.connect(self.search)
        insert.clicked.connect(self.insert)
        add.clicked.connect(self.record)

        # translate
        add.setText(QCoreApplication.translate("Record", "Add"))
        search.setText(QCoreApplication.translate("Record", "Search"))
        insert.setText(QCoreApplication.translate("Record", "Insert File"))
    
    # Identify the member first
    def search(self):
        search_term = self.search_bar.text()

        cursor.execute("SELECT member_id, first_name || ' ' || middle_name || ' ' || last_name AS full_name, photo FROM Members WHERE member_id = ?", (search_term,))
        result = cursor.fetchone()

        if result:
            membership_id, full_name, photo = result
            self.name_id.setText(full_name)
            self.id_id.setText(str(membership_id))

            pixmap = QPixmap()
            pixmap.loadFromData(photo)
            if not pixmap.isNull():
                self.photo.setPixmap(pixmap.scaled(self.photo.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
            else:
                self.photo.setText("No image available")
                self.photo.setAlignment(Qt.AlignCenter)

            return membership_id, True
        
        else:
            self.name_id.setText('No match found.')
            self.id_id.setText('No match found.')
            self.photo.clear()
            self.photo.setText("No image available")
            self.photo.setAlignment(Qt.AlignCenter)
            
        return None, False
    
    # Insert Softcopy function
    def insert(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Image Files (*.png *.jpg *.bmp *.gif)")
        if file_name:
            self.copy = file_name
            pixmap = QPixmap(file_name)
            self.softcopy.setPixmap(pixmap.scaled(self.softcopy.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.softcopy.setAlignment(Qt.AlignCenter)

    def convert_to_bytes(self):
        if self.copy:
            try:
                pixmap = QPixmap(self.copy)
                image = pixmap.toImage()

                byte_array = QByteArray()
                buffer = QBuffer(byte_array)
                buffer.open(QIODevice.WriteOnly)
                image.save(buffer, 'PNG')  # Change 'PNG' to 'JPEG' or another format if needed
                buffer.close()
                bytes_data = bytes(byte_array)

                return bytes_data

            except Exception as e:
                print(f"Error converting image to bytes: {e}")
                QMessageBox.critical(self, "Error", f"Failed to convert image to bytes: {e}")

        return None


    # Then Record When The member is Identified and Softcopy is inserted
    def record(self):

        try:
            # Get count of existing rows in Contracts table
            cursor.execute("SELECT COUNT(reference_number) FROM Contracts")
            count_result = cursor.fetchone()  # Fetch the count result
            count = count_result[0] if count_result else 0  # Extract count value or default to 0

            # Call search to get membership_id and found
            membership_id, found = self.search()

            # Call insert to get softcopy data
            softcopy = self.convert_to_bytes()

            if softcopy is not None and found:
                # Insert new record into Contracts table
                cursor.execute("INSERT INTO Contracts (reference_number, member_id, softcopy_contract) VALUES (?, ?, ?)",
                            (count + 1, membership_id, softcopy))
                connection.commit()
                alert = QMessageBox()
                alert.setWindowTitle('Success')
                alert.setText('Recorded')
                alert.setIcon(QMessageBox.Information)
                alert.exec_()
    
            else:
                # Display error message if recording failed
                alert = QMessageBox()
                alert.setWindowTitle('Error')
                alert.setText('Recording failed. Please try again.')
                alert.setIcon(QMessageBox.Critical)
                alert.exec_()

        except sqlite3.Error as e:
            # Handle any SQLite errors
            alert = QMessageBox()
            alert.setWindowTitle('Error')
            alert.setText('Recording failed. Please try again.')
            alert.setIcon(QMessageBox.Critical)
            alert.exec_()
            connection.rollback()  # Rollback changes if error occurs



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Payment()
    window.show()
=======
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sqlite3
from assets import *
import time
import random

class Payment(QWidget):  # Inherit from QWidget
    def __init__(self, parent=None):
        super(Payment, self).__init__(parent)
        self.setWindowTitle("Payment")
        self.setObjectName("Payment")
        self.resize(950, 800)
        self.setStyleSheet("background-color: #E0E0E0;")

        # Search Bar Input Field
        self.search_bar = createLineInput(
            parent = self,
            name = "payment_search_bar",
            geometry = QRect(30, 20, 400, 61),
            font = font5,
            style = "background: white"
        )
        self.search_bar.setPlaceholderText("Enter Member ID / Reference Number here")

        # Search Button
        self.btn_search = createButton(
            parent = self,
            name = "payment_search_button",
            geometry = QRect(430, 20, 71, 61),
            text = "Search",
            font = font5,
            style = "background: #4681f4; color: white"
        )

        self.btn_load = createButton(
            parent = self,
            name = "payment_load_button",
            geometry = QRect(530, 20, 100, 60),
            text = "Load Data",
            font = font5,
            style = "background: #4681f4; color: white"
        )

        # Record option
        self.btn_record = createButton(
            parent = self,
            name = "payment_btn_record",
            geometry = QRect(770, 730, 140, 45),
            text = "Record",
            font = font5,
            style = "background: lime; color: white; border-radius: 5px"
        )

        self.btn_search.clicked.connect(self.search)
        self.btn_record.clicked.connect(self.showRecord)
        self.btn_load.clicked.connect(self.loadData)

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
        
        

       

    # Populate Table View
    def loadData(self):
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
                    # Handle BLOB data
                    if isinstance(data, bytes):
                        image = QImage.fromData(data)
                        if not image.isNull():
                            pixmap = QPixmap.fromImage(image)
                            label = QLabel()
                            label.setPixmap(pixmap.scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation))
                            label.setAlignment(Qt.AlignRight)
                            self.tableWidget.setCellWidget(row_number, column_number, label)
                        else:
                            item = QTableWidgetItem("Invalid Image")
                            item.setTextAlignment(Qt.AlignRight)
                            self.tableWidget.setItem(row_number, column_number, item)
                    else:
                        item = QTableWidgetItem(str(data))
                        item.setTextAlignment(Qt.AlignRight)
                        self.tableWidget.setItem(row_number, column_number, item)
            


    def search(self):
        search_term = self.search_bar.text()
        self.tableWidget.setRowCount(0)

        cursor.execute("""
                SELECT * 
                FROM Contracts 
                WHERE CAST(member_id AS TEXT) LIKE ? OR CAST(reference_number AS TEXT) LIKE ?
                """, (search_term + '%', search_term + '%'))
        
        for row_number, row_data in enumerate(cursor):
            self.tableWidget.insertRow(row_number)  
            for column_number, data in enumerate(row_data):
                # Handle BLOB data
                if isinstance(data, bytes):
                    image = QImage.fromData(data)
                    if not image.isNull():
                        pixmap = QPixmap.fromImage(image)
                        label = QLabel()
                        label.setPixmap(pixmap.scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation))
                        label.setAlignment(Qt.AlignRight)
                        self.tableWidget.setCellWidget(row_number, column_number, label)
                    else:
                        item = QTableWidgetItem("Invalid Image")
                        item.setTextAlignment(Qt.AlignRight)
                        self.tableWidget.setItem(row_number, column_number, item)
                else:
                    item = QTableWidgetItem(str(data))
                    item.setTextAlignment(Qt.AlignRight)
                    self.tableWidget.setItem(row_number, column_number, item)
    

    def showRecord(self):
        popup = Record(self)
        popup.exec_()




class Record(QDialog):
    def __init__(self, parent=None):
        super(Record, self).__init__(parent)
        self.setWindowTitle("Record")
        self.resize(700, 600)
        self.setStyleSheet("background-color: #E0E0E0;")
         
        # Search Bar
        self.search_bar = createLineInput(
            parent = self,
            name = "record_bar_record",
            geometry = QRect(30, 20, 574, 61),
            font = font5,
            style = "background: white"
        )
        self.search_bar.setPlaceholderText("Enter Member ID / Name here")

        # Search Button 
        self.btn_search = createButton(
            parent = self,
            name = "record_btn_search_record",
            geometry = QRect(604, 20, 71, 61),
            text = "Search",
            font = font5,
            style = "background: #4681f4; color: white"
        )
        

        # Add button 
        self.add_button = createButton(
            parent = self,
            name = "record_add_button",
            geometry = QRect(535, 530, 140, 45),
            text = "Add",
            font = font5,
            style = "background: lime; color: white"
        )
        add = self.add_button

        # Insert button
        self.insert_button = createButton(
            parent = self,
            name = "record_insert_button",
            geometry = QRect(50, 520, 361, 61),
            text = "Search",
            font = font5,
            style = "background: red; color: white"
        )
        insert = self.insert_button

        # Label Properties
        self.name = createLabel(
            parent = self,
            name = "record_name_label",
            geometry = QRect(40, 100, 121, 51),
            text = "Name",
            font = font1,
            style = "font: bold"
        )

        self.id = createLabel(
            parent = self,
            name = "record_id_label",
            geometry = QRect(40, 200, 301, 51),
            text = "Membership ID",
            font = font1,
            style = "font: bold"
        )

        self.name_id = createLabel(
            parent = self,
            name = "record_name_identity",
            geometry = QRect(40, 150, 361, 51),
            text = "Full Name",
            font = font6,
            style = "background: white; border: 1px solid black; font-style: italic; color: #A9A9AC"
        )

        self.id_id = createLabel(
            parent = self,
            name = "record_id_identity",
            geometry = QRect(40, 260, 361, 51),
            text = "Member ID",
            font = font6,
            style = "background: white; border: 1px solid black; font-style: italic; color: #A9A9AC"
        )

        self.photo = createLabel(
            parent = self,
            name = "record_photo_identity",
            geometry = QRect(450, 100, 225, 255),
            text = "Photo",
            font = font6,
            style = "background: white; border: 1px solid black; font-style: italic; color: #A9A9AC"
        )
        self.photo.setAlignment(Qt.AlignCenter)
        
        self.softcopy = createLabel(
            parent = self,
            name = "record_softcopy",
            geometry = QRect(50, 373, 361, 151),
            text = "",
            font = font6,
            style = "background: white; border: 1px solid black; font-style: italic; color: #A9A9AC"
        )
        self.copy = None

        
        # button clicks
        self.btn_search.clicked.connect(self.search)
        insert.clicked.connect(self.insert)
        add.clicked.connect(self.close)
        add.clicked.connect(self.record)
        
    # Identify the member first
    def search(self):
        search_term = self.search_bar.text()

        if search_term.isdigit():  # Check if the search term is a digit (assumed to be member_id)
            query = "SELECT member_id, first_name || ' ' || middle_name || ' ' || last_name AS full_name, photo FROM Members WHERE CAST(member_id AS TEXT) LIKE ?"
            params = ('%' + search_term + '%',)
        else:  # Full name search (partial match allowed)
            query = "SELECT member_id, first_name || ' ' || middle_name || ' ' || last_name AS full_name, photo FROM Members WHERE full_name LIKE ?"
            params = ('%' + search_term + '%',)

        cursor.execute(query, params)
        result = cursor.fetchone()

        if result:
            membership_id, full_name, photo = result
            self.name_id.setText(full_name)
            self.id_id.setText(str(membership_id))

            pixmap = QPixmap()
            pixmap.loadFromData(photo)
            if not pixmap.isNull():
                self.photo.setPixmap(pixmap.scaled(self.photo.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
            else:
                self.photo.setText("No image available")
                self.photo.setAlignment(Qt.AlignCenter)

            return membership_id, True
        
        else:
            self.name_id.setText('No match found.')
            self.id_id.setText('No match found.')
            self.photo.clear()
            self.photo.setText("No image available")
            self.photo.setAlignment(Qt.AlignCenter)
            
        return None, False
    
    # Insert Softcopy function
    def insert(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Image Files (*.png *.jpg *.bmp *.gif)")
        if file_name:
            self.copy = file_name
            pixmap = QPixmap(file_name)
            self.softcopy.setPixmap(pixmap.scaled(self.softcopy.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.softcopy.setAlignment(Qt.AlignCenter)

    def convert_to_bytes(self):
        if self.copy:
            try:
                pixmap = QPixmap(self.copy)
                image = pixmap.toImage()
                byte_array = QByteArray()
                buffer = QBuffer(byte_array)
                buffer.open(QIODevice.WriteOnly)
                image.save(buffer, 'PNG')  # Change 'PNG' to 'JPEG' or another format if needed
                buffer.close()
                bytes_data = bytes(byte_array)
                return bytes_data

            except Exception as e:
                print(f"Error converting image to bytes: {e}")
                QMessageBox.critical(self, "Error", f"Failed to convert image to bytes: {e}")

        return None

     # generate ref num    
    
    
    # Then Record When The member is Identified and Softcopy is inserted
    def record(self):

        def generate_reference_number():
            timestamp = int(time.time())  # Get current timestamp in seconds
            random_num = random.randint(1000, 9999)  # Generate a random 4-digit number
            reference_number = f"{timestamp}{random_num}"
            return reference_number

        try:
            # Get count of existing rows in Contracts table
            reference_number = int(generate_reference_number())
        

            # Call search to get membership_id and found
            membership_id, found = self.search()
            

            # Call insert to get softcopy data
            softcopy = self.convert_to_bytes()

            if softcopy is not None and found:
                # Insert new record into Contracts table
                cursor.execute("INSERT INTO Contracts (reference_number, member_id, softcopy_contract) VALUES (?, ?, ?)",
                            (reference_number, membership_id, softcopy))
                connection.commit()
                QMessageBox.information(None, 'Success', 'Recorded')
    
            else:
                # Display error message if recording failed
                QMessageBox.critical(None, 'Error', 'Recording failed. Please try again.')

        except sqlite3.Error as e:
            # Handle any SQLite errors
            QMessageBox.critical(None, 'Error', 'Recording failed. Please try again.')
            print("error in sqlite3", e)
            connection.rollback()  # Rollback changes if error occurs



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Payment()
    window.show()
>>>>>>> 3b07da491695c9983258646c3e525513bc5f42ed
    sys.exit(app.exec_())