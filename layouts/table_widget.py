from PySide6.QtWidgets import (QTableWidget, QHeaderView, QAbstractItemView)


class TableWidget:
    def __init__(self) -> None:
        self.table = QTableWidget()
        self.table.setColumnCount(11)
        self.table.setHorizontalHeaderLabels([
            "ID", "Name", "Age", "Gender", "DOB", "Phone", "Address",
            "1st Appointment", "Major Complain", "Follow-up Date", "Total Follow-ups"
        ])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)