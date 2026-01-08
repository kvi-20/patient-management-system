from PySide6.QtWidgets import (QHBoxLayout, QLabel, QComboBox, QLineEdit, QPushButton)


class SearchLayout:
    def __init__(self) -> None:
        self.layout = QHBoxLayout()
        self.layout.addWidget(QLabel('Search by:'))

        self.search_criteria = QComboBox()
        self.search_criteria.addItems(["name", "phone", "major_complain", "gender"])
        self.layout.addWidget(self.search_criteria)

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Enter search term...")
        self.layout.addWidget(self.search_input)

        self.search_btn = QPushButton("Search")
        # search_btn.clicked.connect()
        self.layout.addWidget(self.search_btn)

        self.clear_btn = QPushButton("Show All")
        # clear_btn.clicked.connect(self.load_patients)
        self.layout.addWidget(self.clear_btn)



