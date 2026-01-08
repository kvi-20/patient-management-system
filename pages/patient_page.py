from PySide6.QtWidgets import (QWidget, QVBoxLayout, QLabel)
from PySide6.QtGui import QFont, QPainter, QColor, QPen
from PySide6.QtCore import Qt

from layouts.search_layout import SearchLayout
from layouts.table_widget import TableWidget
from layouts.buttons_layout import ButtonsLayout

class PatientPage(QWidget):
    def __init__(self, btn_layout):
        super().__init__()
        layout = QVBoxLayout(self)
        self.btn_layout = btn_layout
        self.search_layout = SearchLayout()
        self.table_widget = TableWidget()
        

        header = QLabel("Patient Management System")
        header.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(header)

        self.search_layout.layout.addStretch()
        layout.addLayout(self.search_layout.layout)

        layout.addWidget(self.table_widget.table)

        layout.addWidget(btn_layout)
