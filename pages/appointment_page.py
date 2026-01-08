from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

class AppointmentPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Appointment Details Page"))
