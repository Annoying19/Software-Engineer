from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QMessageBox, QDateEdit, \
    QDialog, QDialogButtonBox
from PyQt5.QtCore import QDate
import sqlite3
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.colors import blue
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from reportlab.platypus.flowables import Spacer
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.enums import TA_CENTER
import sys
import os
from datetime import datetime

# Define the output directory for PDF reports
OUTPUT_DIR = 'reports'
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

ADDRESS = "49A, Main Building SM City, North Avenue corner, Bagong Pag-asa, Quezon City"
CONTACT = "(02) 8929 5424"

# Function to generate Membership Report
def generate_membership_report():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    query = """
    SELECT member_id, first_name, middle_name, last_name, address, gender, birthdate, phone_number, 
           membership_type, membership_start_date, membership_end_date
    FROM Members
    ORDER BY
        CASE
            WHEN membership_type = 'Lifetime' THEN 1
            WHEN membership_type = 'Standard' THEN 2
            ELSE 3
        END,
        first_name
    """

    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()

    pdf_file = os.path.join(OUTPUT_DIR, f'Membership_Report_{datetime.now().strftime("%Y%m%d_%H%M%S")}.pdf')

    doc = SimpleDocTemplate(pdf_file, pagesize=landscape(A4))
    elements = []

    styles = getSampleStyleSheet()
    pdfmetrics.registerFont(TTFont('TimesNewRoman', 'times.ttf'))

    # Center the title
    title_style = styles['Title']
    title_style.alignment = TA_CENTER
    title = Paragraph("<font name='TimesNewRoman' color='blue' size=18>Slimmer World</font>", styles['Title'])

    # Center the address
    address_style = styles['Normal']
    address_style.alignment = TA_CENTER
    address = Paragraph(f"<font name='TimesNewRoman' size=12>{ADDRESS}</font>", styles['Normal'])

    # Center the contact
    contact_style = styles['Normal']
    contact_style.alignment = TA_CENTER
    contact = Paragraph(f"<font name='TimesNewRoman' size=12>{CONTACT}</font>", styles['Normal'])
    elements.append(title)
    elements.append(address)
    elements.append(contact)

    # Add spacer to title
    elements.append(Spacer(1, 12))
    report_title = Paragraph("<font name='TimesNewRoman' size=14>Membership Report</font>", styles['Title'])
    elements.append(report_title)

    # Add space
    elements.append(Spacer(1, 12))

    # Table Header
    table_data = [
        ["Member ID", "First Name", "Middle Name", "Last Name", "Address", "Gender", "Birthdate", "Phone Number",
         "Membership Type", "Start Date", "End Date"]
    ]

    # Adding data to table
    for row in rows:
        table_data.append(list(row))

    # Specifying smaller column widths to fit the table
    col_widths = [70, 60, 60, 60, 190, 40, 60, 70, 80, 70, 70]

    # Creating table with smaller font size and styles
    table = Table(table_data, colWidths=col_widths)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), blue),
        ('TEXTCOLOR', (0, 0), (-1, 0), 'white'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'TimesNewRoman'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('BACKGROUND', (0, 1), (-1, -1), '#f0f0f0'),
        ('GRID', (0, 0), (-1, -1), 1, 'black'),
        ('WORDWRAP', (0, 0), (-1, -1), 'ON'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP')
    ]))

    elements.append(table)
    elements.append(Spacer(1, 12))

    timestamp = datetime.now().strftime('%B %d, %Y %I:%M %p')
    generated_time = Paragraph(f"Generated on: {timestamp}", styles['Normal'])
    elements.append(generated_time)

    doc.build(elements)

    QMessageBox.information(None, 'Success', f'Membership Report generated successfully!\nSaved at: {pdf_file}')


# Function to generate Equipment Report
def generate_equipment_report():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    query = """
    SELECT equipment_id, equipment_name, equipment_serial_number, equipment_category, 
           equipment_purchase_date, equipment_warranty_expiry, equipment_price, equipment_manufacturer, 
           equipment_location, equipment_status
    FROM Equipments
    ORDER BY equipment_name
    """

    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()

    pdf_file = os.path.join(OUTPUT_DIR, f'Equipment_Report_{datetime.now().strftime("%Y%m%d_%H%M%S")}.pdf')

    doc = SimpleDocTemplate(pdf_file, pagesize=landscape(A4))
    elements = []

    styles = getSampleStyleSheet()
    pdfmetrics.registerFont(TTFont('TimesNewRoman', 'times.ttf'))

    # Center the title
    title_style = styles['Title']
    title_style.alignment = TA_CENTER
    title = Paragraph("<font name='TimesNewRoman' color='blue' size=18>Slimmer World</font>", styles['Title'])

    # Center the address
    address_style = styles['Normal']
    address_style.alignment = TA_CENTER
    address = Paragraph(f"<font name='TimesNewRoman' size=12>{ADDRESS}</font>", styles['Normal'])

    # Center the contact
    contact_style = styles['Normal']
    contact_style.alignment = TA_CENTER
    contact = Paragraph(f"<font name='TimesNewRoman' size=12>{CONTACT}</font>", styles['Normal'])

    elements.append(title)
    elements.append(address)
    elements.append(contact)

    # Add spacer to title
    elements.append(Spacer(1, 12))
    report_title = Paragraph("<font name='TimesNewRoman' size=14>Equipment Report</font>", styles['Title'])
    elements.append(report_title)

    # Add space
    elements.append(Spacer(1, 12))

    # Table Header
    table_data = [
        ["Equipment ID", "Name", "Serial Number", "Category", "Purchase Date", "Warranty Expiry",
         "Price", "Manufacturer", "Location", "Status"]
    ]

    # Adding data to table
    for row in rows:
        table_data.append(list(row))

    # Specifying smaller column widths to fit the table
    col_widths = [60, 100, 100, 80, 80, 80, 60, 100, 80, 60]

    # Creating table with smaller font size and styles
    table = Table(table_data, colWidths=col_widths)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), blue),
        ('TEXTCOLOR', (0, 0), (-1, 0), 'white'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'TimesNewRoman'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('BACKGROUND', (0, 1), (-1, -1), '#f0f0f0'),
        ('GRID', (0, 0), (-1, -1), 1, 'black'),
        ('WORDWRAP', (0, 0), (-1, -1), 'ON'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP')
    ]))

    elements.append(table)
    elements.append(Spacer(1, 12))

    timestamp = datetime.now().strftime('%B %d, %Y %I:%M %p')
    generated_time = Paragraph(f"Generated on: {timestamp}", styles['Normal'])
    elements.append(generated_time)

    doc.build(elements)

    QMessageBox.information(None, 'Success', f'Equipment Report generated successfully!\nSaved at: {pdf_file}')


# Function to generate Scheduling Report
def generate_scheduling_report():
    dialog = DateSelectionDialog()
    if dialog.exec_() == QDialog.Accepted:
        selected_date = dialog.getDate()

        try:
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()

            query = """
            SELECT schedule_id, member_id, employee_id, appointment_type, appointment_name, appointment_date,
            appointment_start_time, appointment_end_time, status 
            FROM Schedule WHERE appointment_date = ?
            """

            cursor.execute(query, (selected_date,))
            rows = cursor.fetchall()
            conn.close()

            pdf_file = os.path.join(OUTPUT_DIR, f'Scheduling_Report_{selected_date}.pdf')

            doc = SimpleDocTemplate(pdf_file, pagesize=landscape(A4))
            elements = []

            styles = getSampleStyleSheet()
            pdfmetrics.registerFont(TTFont('TimesNewRoman', 'times.ttf'))

            # Center the title
            title_style = styles['Title']
            title_style.alignment = TA_CENTER
            title = Paragraph("<font name='TimesNewRoman' color='blue' size=18>Slimmer World</font>", styles['Title'])

            # Center the address
            address_style = styles['Normal']
            address_style.alignment = TA_CENTER
            address = Paragraph(f"<font name='TimesNewRoman' size=12>{ADDRESS}</font>", styles['Normal'])

            # Center the contact
            contact_style = styles['Normal']
            contact_style.alignment = TA_CENTER
            contact = Paragraph(f"<font name='TimesNewRoman' size=12>{CONTACT}</font>", styles['Normal'])
            elements.append(title)
            elements.append(address)
            elements.append(contact)

            # Add spacer to title
            elements.append(Spacer(1, 12))
            report_title = Paragraph("<font name='TimesNewRoman' size=14>Scheduling Report</font>", styles['Title'])
            elements.append(report_title)

            # Add space
            elements.append(Spacer(1, 12))

            # Table Header
            table_data = [
                ["Schedule ID", "Member ID", "Employee ID", "Appointment Type", "Appointment Name",
                 "Appointment Date", "Start Time", "End Time", "Status"]
            ]

            # Adding data to table
            for row in rows:
                table_data.append(list(row))

            # Specifying smaller column widths to fit the table
            col_widths = [60, 60, 60, 100, 100, 80, 60, 60, 60]

            # Creating table with smaller font size and styles
            table = Table(table_data, colWidths=col_widths)
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), blue),
                ('TEXTCOLOR', (0, 0), (-1, 0), 'white'),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'TimesNewRoman'),
                ('FONTSIZE', (0, 0), (-1, 0), 10),
                ('FONTSIZE', (0, 1), (-1, -1), 8),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
                ('BACKGROUND', (0, 1), (-1, -1), '#f0f0f0'),
                ('GRID', (0, 0), (-1, -1), 1, 'black'),
                ('WORDWRAP', (0, 0), (-1, -1), 'ON'),
                ('VALIGN', (0, 0), (-1, -1), 'TOP')
            ]))

            elements.append(table)
            elements.append(Spacer(1, 12))

            timestamp = datetime.now().strftime('%B %d, %Y %I:%M %p')
            generated_time = Paragraph(f"Generated on: {timestamp}", styles['Normal'])
            elements.append(generated_time)

            doc.build(elements)

            QMessageBox.information(None, 'Success', f'Scheduling Report generated successfully!\nSaved at: {pdf_file}')

        except Exception as e:
            QMessageBox.critical(None, 'Error', f'An error occurred: {str(e)}')


# Function to generate Stock Report
def generate_stock_report():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    query = """
    SELECT stock_id, product_name, product_description, quantity, stock_date, expiry_date, supplier, 
           purchase_price, selling_price
    FROM Stock
    ORDER BY product_name
    """

    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()

    pdf_file = os.path.join(OUTPUT_DIR, f'Stock_Report_{datetime.now().strftime("%Y%m%d_%H%M%S")}.pdf')

    doc = SimpleDocTemplate(pdf_file, pagesize=landscape(A4))
    elements = []

    styles = getSampleStyleSheet()
    pdfmetrics.registerFont(TTFont('TimesNewRoman', 'times.ttf'))

    # Center the title
    title_style = styles['Title']
    title_style.alignment = TA_CENTER
    title = Paragraph("<font name='TimesNewRoman' color='blue' size=18>Slimmer World</font>", styles['Title'])

    # Center the address
    address_style = styles['Normal']
    address_style.alignment = TA_CENTER
    address = Paragraph(f"<font name='TimesNewRoman' size=12>{ADDRESS}</font>", styles['Normal'])

    # Center the contact
    contact_style = styles['Normal']
    contact_style.alignment = TA_CENTER
    contact = Paragraph(f"<font name='TimesNewRoman' size=12>{CONTACT}</font>", styles['Normal'])
    elements.append(title)
    elements.append(address)
    elements.append(contact)

    # Add spacer to title
    elements.append(Spacer(1, 12))
    report_title = Paragraph("<font name='TimesNewRoman' size=14>Stock Report</font>", styles['Title'])
    elements.append(report_title)

    # Add space
    elements.append(Spacer(1, 12))

    # Table Header
    table_data = [
        ["Stock ID", "Product Name", "Description", "Quantity", "Stock Date", "Expiry Date",
         "Supplier", "Purchase Price", "Selling Price"]
    ]

    # Adding data to table
    for row in rows:
        table_data.append(list(row))

    # Specifying smaller column widths to fit the table
    col_widths = [60, 100, 120, 60, 80, 80, 100, 80, 80]

    # Creating table with smaller font size and styles
    table = Table(table_data, colWidths=col_widths)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), blue),
        ('TEXTCOLOR', (0, 0), (-1, 0), 'white'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'TimesNewRoman'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('BACKGROUND', (0, 1), (-1, -1), '#f0f0f0'),
        ('GRID', (0, 0), (-1, -1), 1, 'black'),
        ('WORDWRAP', (0, 0), (-1, -1), 'ON'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP')
    ]))

    elements.append(table)
    elements.append(Spacer(1, 12))

    timestamp = datetime.now().strftime('%B %d, %Y %I:%M %p')
    generated_time = Paragraph(f"Generated on: {timestamp}", styles['Normal'])
    elements.append(generated_time)

    doc.build(elements)

    QMessageBox.information(None, 'Success', f'Stock Report generated successfully!\nSaved at: {pdf_file}')


class DateSelectionDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Select Date')
        self.setGeometry(100, 100, 300, 100)

        layout = QVBoxLayout()

        self.dateEdit = QDateEdit()
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QDate.currentDate())

        layout.addWidget(self.dateEdit)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)

        layout.addWidget(buttons)

        self.setLayout(layout)

    def getDate(self):
        return self.dateEdit.date().toString('yyyy-MM-dd')


class Reports(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Slimmers World Report Generator')
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        self.btn_generate_membership = QPushButton('Generate Membership Report')
        self.btn_generate_membership.clicked.connect(generate_membership_report)

        self.btn_generate_equipment = QPushButton('Generate Equipment Report')
        self.btn_generate_equipment.clicked.connect(generate_equipment_report)

        self.btn_generate_schedule = QPushButton('Generate Scheduling Report')
        self.btn_generate_schedule.clicked.connect(generate_scheduling_report)

        self.btn_generate_stock = QPushButton('Generate Stock Report')
        self.btn_generate_stock.clicked.connect(generate_stock_report)

        layout.addWidget(self.btn_generate_membership)
        layout.addWidget(self.btn_generate_equipment)
        layout.addWidget(self.btn_generate_schedule)
        layout.addWidget(self.btn_generate_stock)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = Reports()
    mainWin.show()
    sys.exit(app.exec_())