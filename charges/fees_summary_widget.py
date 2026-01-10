from PySide6.QtWidgets import QGroupBox, QLabel, QVBoxLayout, QScrollArea, QWidget


class FeesSummaryWidget(QGroupBox):
    def __init__(self, fees_data):
        super().__init__("Fees Summary")
        layout = QVBoxLayout(self)

        # Scroll Area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setFixedHeight(200)  # adjust as needed
        scroll_area.setStyleSheet("QScrollArea { border: none; }")

        # Inner widget
        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)
        content_layout.setSpacing(6)

        for appt in fees_data:
            total = appt["consultation"]

            content_layout.addWidget(QLabel(f"<b>Appointment {appt['appointment']}</b>"))
            content_layout.addWidget(QLabel(f"Consultation: ₹{appt['consultation']}"))

            if appt["medicines"]:
                content_layout.addWidget(QLabel("Medicines:"))
                for med in appt["medicines"]:
                    content_layout.addWidget(QLabel(f" • {med['name']} – ₹{med['fee']}"))
                    total += med["fee"]

            if appt["therapies"]:
                content_layout.addWidget(QLabel("Panchakarma Therapies:"))
                for th in appt["therapies"]:
                    content_layout.addWidget(QLabel(f" • {th['name']} – ₹{th['fee']}"))
                    total += th["fee"]

            content_layout.addWidget(QLabel(f"<b>Total: ₹{total}</b>"))
            content_layout.addSpacing(10)
            scroll_area.setWidget(content_widget)
            layout.addWidget(scroll_area)
