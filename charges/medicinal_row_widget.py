from PySide6.QtWidgets import (
    QWidget, QHBoxLayout, QLineEdit, QSpinBox, QPushButton
)


class MedicineRowWidget(QWidget):
    def __init__(self, parent_layout):
        super().__init__()
        self.parent_layout = parent_layout

        layout = QHBoxLayout(self)

        self.name = QLineEdit()
        self.name.setPlaceholderText("Medicine name")

        self.fee = QSpinBox()
        self.fee.setMaximum(100000)

        delete_btn = QPushButton("❌")
        delete_btn.setFixedWidth(30)
        delete_btn.clicked.connect(self.remove_self)

        layout.addWidget(self.name)
        layout.addWidget(self.fee)
        layout.addWidget(delete_btn)

    def remove_self(self):
        self.setParent(None)
        self.deleteLater()
