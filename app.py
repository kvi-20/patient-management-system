import sys
import sqlite3
from datetime import datetime
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                               QHBoxLayout, QTableWidget, QTableWidgetItem, 
                               QPushButton, QLineEdit, QLabel, QDialog, 
                               QFormLayout, QComboBox, QDateEdit, QTextEdit,
                               QMessageBox, QHeaderView, QSpinBox, QAbstractItemView,
                               QFrame, QButtonGroup, QStackedWidget)
from PySide6.QtCore import Qt, QDate
from PySide6.QtGui import QFont

from database_manager import DatabaseManager
from patient_dialog import PatientDialog
from config import config

from PySide6.QtGui import QFont, QPainter, QColor, QPen
from watermark_widget import WatermarkWidget

# from layouts.search_layout import SearchLayout
# from layouts.table_widget import TableWidget
from layouts.buttons_layout import ButtonsLayout

from pages.patient_page import PatientPage
from pages.appointment_page import AppointmentPage

from sidebar.sidebar import SideBar

class PatientManagementSystem(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db = DatabaseManager()
        self.search_result_count = 0
        self.setWindowTitle(config['title'])
        # self.search_layout = SearchLayout()
        # self.table_widget = TableWidget()
        self.btn_layout = ButtonsLayout()
        self.sidebar = SideBar()
        self.patient_page = PatientPage(self.btn_layout)
        self.setup_ui()
        self.load_patients()
        

    # def resizeEvent(self, event):
    #     super().resizeEvent(event)
    #     self.watermark.setGeometry(self.centralWidget().rect())


    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(5,5,5,5)

        # sidebar = QFrame()
        # sidebar.setFixedWidth(220)
        # sidebar.setStyleSheet("""
        #     QFrame {
        #         background-color: #1f2937;
        #     }
        #     QPushButton {
        #         color: white;
        #         border: none;
        #         padding: 12px;
        #         text-align: left;
        #         font-size: 14px;
        #     }
        #     QPushButton:hover {
        #         background-color: #374151;
        #     }
        #     QPushButton:checked {
        #         background-color: #2563eb;
        #         font-weight: bold;
        #     }
        # """)
        # sidebar_layout = QVBoxLayout(sidebar)
        # sidebar_layout.setSpacing(5)
        # sidebar_layout.setContentsMargins(10, 20, 10, 20)
        # title = QLabel("Clinic Panel")
        # title.setStyleSheet("color: white; font-size: 18px; font-weight: bold;")
        # sidebar_layout.addWidget(title)
        # sidebar_layout.addSpacing(20)
        # sidebar_layout.addStretch()
        # main_layout.addWidget(sidebar)

        sidebar = QWidget()
        sidebar.setFixedWidth(250)
        sidebar.setStyleSheet("""
            QWidget {
                background-color: #2c3e50;
                background-color: green;
                border-radius: 5px;
            }
            QPushButton {
                background-color: #34495e;
                color: white;
                border: none;
                border-radius: 0;
                padding: 15px;
                text-align: left;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #3498db;
            }
            QPushButton:checked {
                background-color: #2980b9;
            }
        """)

        sidebar_layout = QVBoxLayout(sidebar)
        # sidebar_layout.setSpacing(0)
        # sidebar_layout.setContentsMargins(10, 20, 10, 20)
        
        # Logo/Title
        # title = QLabel("CLINIC\nMANAGEMENT")
        # title.setStyleSheet("color: white; font-size: 16px; font-weight: bold; padding: 20px;")
        # title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # sidebar_layout.addWidget(title)

        # self.btn_patients = QPushButton("🧑 Patient Details")
        # self.btn_appointments = QPushButton("📅 Appointments")
        # self.btn_invoices = QPushButton("💳 Invoice Generation")
        # self.nav_group = QButtonGroup(self)
        # self.nav_group.setExclusive(True)

        # for btn in (self.btn_patients, self.btn_appointments, self.btn_invoices):
        #     btn.setCheckable(True)
        #     self.nav_group.addButton(btn)
        #     sidebar_layout.addWidget(btn)

        # sidebar_layout.addStretch()
        print('side bar: ', self.sidebar)
        
        main_layout.addWidget(self.sidebar)

        # content_layout = QVBoxLayout()
        # Header
        # header = QLabel("Patient Management System")
        # header.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        # header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # content_layout.addWidget(header)

        self.patient_page.btn_layout.add_btn.clicked.connect(self.add_patient)
        self.patient_page.btn_layout.edit_btn.clicked.connect(self.edit_patient)
        self.patient_page.btn_layout.delete_btn.clicked.connect(self.delete_patient)

        self.patient_page.search_layout.search_btn.clicked.connect(self.search_patients)
        self.patient_page.search_layout.clear_btn.clicked.connect(self.load_patients)

        self.stack = QStackedWidget()
        self.stack.addWidget(self.patient_page)
        self.stack.addWidget(AppointmentPage())
        
        

        # self.search_layout.layout.addStretch()
        # content_layout.addLayout(self.search_layout.layout)
        
        # content_layout.addWidget(self.table_widget.table)
        
        # # Buttons
        # btn_layout = QHBoxLayout()
        
        # add_btn = QPushButton("Add Patient")
        # add_btn.clicked.connect(self.add_patient)
        # btn_layout.addWidget(add_btn)
        
        # edit_btn = QPushButton("Edit Patient")
        # edit_btn.clicked.connect(self.edit_patient)
        # btn_layout.addWidget(edit_btn)
        
        # delete_btn = QPushButton("Delete Patient")
        # delete_btn.clicked.connect(self.delete_patient)
        # btn_layout.addWidget(delete_btn)
        
        # btn_layout.addStretch()
        # self.row_count_lable = QLabel("Total: 0")
        # font = self.row_count_lable.font()
        # font.setBold(True)
        # self.row_count_lable.setFont(font)
        
        # self.row_count_lable.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        # btn_layout.addWidget(self.row_count_lable)
        # content_layout.addLayout(self.btn_layout.layout)
        
        main_layout.addWidget(self.stack)

        self.sidebar.btn_patients.clicked.connect(lambda: self.stack.setCurrentIndex(0))
        self.sidebar.btn_appointments.clicked.connect(lambda: self.stack.setCurrentIndex(1))
        # main_layout.setStretch(0, 0)  # sidebar
        # main_layout.setStretch(1, 1)  
        print('central_widget: ',central_widget.rect() )
        self.watermark = WatermarkWidget(central_widget)
        self.watermark.setGeometry(central_widget.rect())
        self.watermark.raise_()

    def load_patients(self):
        patients = self.db.get_all_patients()
        # self.row_count_lable.setText()
        self.patient_page.btn_layout.row_count_lable.setText(f"Total: {len(patients)}")
        self.populate_table(patients)
    
    def populate_table(self, patients):
        self.patient_page.table_widget.table.setRowCount(len(patients))
        for row, patient in enumerate(patients):
            for col, value in enumerate(patient):
                self.patient_page.table_widget.table.setItem(row, col, QTableWidgetItem(str(value) if value else ""))
    
    def add_patient(self):
        print('add button clicked')
        dialog = PatientDialog(self)
        if dialog.exec():
            data = dialog.get_data()
            if data[0]:  # Check if name is provided
                self.db.add_patient(data)
                self.load_patients()
                QMessageBox.information(self, "Success", "Patient added successfully!")
            else:
                QMessageBox.warning(self, "Error", "Patient name is required!")
    
    def edit_patient(self):
        current_row = self.patient_page.table_widget.table.currentRow()
        print('current row: ', current_row)
        if current_row >= 0:
            item = self.patient_page.table_widget.table.item(current_row, 0)
            if item is None:
                QMessageBox.warning(self, "Error", "Invalid patient data!")
            print('item: ', item.text()) # type: ignore
            patient_id = int(item.text()) # type: ignore
            # patient_id = int(self.table.item(current_row, 0).text())
            patient_data = [self.patient_page.table_widget.table.item(current_row, col).text()  # type: ignore
                          for col in range(self.patient_page.table_widget.table.columnCount())]
            print('patient_data: ', patient_data)
            dialog = PatientDialog(self, patient_data)
            if dialog.exec():
                data = dialog.get_data()
                if data[0]:
                    self.db.update_patient(patient_id, data)
                    self.load_patients()
                    QMessageBox.information(self, "Success", "Patient updated successfully!")
                else:
                    QMessageBox.warning(self, "Error", "Patient name is required!")
        else:
            QMessageBox.warning(self, "Warning", "Please select a patient to edit!")
    
    def delete_patient(self):
        current_row = self.patient_page.table_widget.table.currentRow()
        if current_row >= 0:
            patient_id = int(self.patient_page.table_widget.table.item(current_row, 0).text()) # type: ignore
            patient_name = self.patient_page.table_widget.table.item(current_row, 1).text() # type: ignore
            
            reply = QMessageBox.question(
                self, "Confirm Delete",
                f"Are you sure you want to delete patient '{patient_name}'?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )
            
            if reply == QMessageBox.StandardButton.Yes:
                self.db.delete_patient(patient_id)
                self.load_patients()
                QMessageBox.information(self, "Success", "Patient deleted successfully!")
        else:
            QMessageBox.warning(self, "Warning", "Please select a patient to delete!")
    
    def search_patients(self):
        criteria = self.patient_page.search_layout.search_criteria.currentText()
        value = self.patient_page.search_layout.search_input.text()
        
        if value:
            patients = self.db.search_patients(criteria, value)
            row_count = len(patients)

            self.populate_table(patients)
            self.patient_page.btn_layout.row_count_lable.setText(f"Total: {row_count}")
        else:
            self.load_patients()

def main():
    app = QApplication(sys.argv)
    window = PatientManagementSystem()
    window.showMaximized()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()