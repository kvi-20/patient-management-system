from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QPushButton, QScrollArea,
    QWidget, QHBoxLayout
)

from charges.appointment_widget import AppointmentWidget


class FeesDialog(QDialog):
    def __init__(self, total_appointments_till_now, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Fees & Appointments")
        self.setMinimumSize(800, 600)

        # self.appointment_count = 0
        self.total_appointments_till_now = total_appointments_till_now
        self.appointments = []

        main_layout = QVBoxLayout(self)

        self.add_appointment_btn = QPushButton("➕ Add Appointment")
        self.add_appointment_btn.clicked.connect(self.add_appointment)
        main_layout.addWidget(self.add_appointment_btn)

        self.container = QWidget()
        self.container_layout = QVBoxLayout(self.container)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setWidget(self.container)
        main_layout.addWidget(scroll)

        # ---- Save / Cancel buttons ----
        btn_layout = QHBoxLayout()
        btn_layout.addStretch()

        save_btn = QPushButton("Save")
        cancel_btn = QPushButton("Cancel")

        save_btn.clicked.connect(self.accept)
        cancel_btn.clicked.connect(self.reject)

        btn_layout.addWidget(save_btn)
        btn_layout.addWidget(cancel_btn)

        main_layout.addLayout(btn_layout)

    def add_appointment(self):
        # self.appointment_count += 1
        self.total_appointments_till_now = self.total_appointments_till_now + 1
        appt = AppointmentWidget(self.total_appointments_till_now)
        self.container_layout.addWidget(appt)
        self.appointments.append(appt)

    def get_fees_data(self):
        """Collect all appointment-wise data"""
        data = []

        for idx, appt in enumerate(self.appointments, start=self.total_appointments_till_now):
            data.append({
                "appointment": idx,
                "consultation": appt.consultation_fee.value(),
                "medicines": appt.get_medicines(),
                "therapies": appt.get_therapies()
            })

        return data


# from PySide6.QtWidgets import (
#     QDialog, QVBoxLayout, QPushButton, QScrollArea, QWidget
# )

# from charges.appointment_widget import AppointmentWidget


# class FeesDialog(QDialog):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setWindowTitle("Fees & Appointments")
#         self.setMinimumSize(800, 600)

#         self.appointment_count = 0

#         main_layout = QVBoxLayout(self)

#         self.add_appointment_btn = QPushButton("➕ Add Appointment")
#         self.add_appointment_btn.clicked.connect(self.add_appointment)

#         main_layout.addWidget(self.add_appointment_btn)

#         # Scroll area for multiple appointments
#         self.container = QWidget()
#         self.container_layout = QVBoxLayout(self.container)

#         scroll = QScrollArea()
#         scroll.setWidgetResizable(True)
#         scroll.setWidget(self.container)

#         main_layout.addWidget(scroll)

#     def add_appointment(self):
#         self.appointment_count += 1
#         appointment = AppointmentWidget(self.appointment_count)
#         self.container_layout.addWidget(appointment)
