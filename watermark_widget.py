from PySide6.QtGui import QFont, QPainter, QColor, QPen
from PySide6.QtCore import Qt, QDate
from PySide6.QtWidgets import QWidget

class WatermarkWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
    
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # Set semi-transparent color
        painter.setOpacity(0.05)
        
        # Set font for watermark text
        font = QFont("Arial", 72, QFont.Weight.Bold)
        painter.setFont(font)
        
        # Set text color
        painter.setPen(QColor(100, 100, 100))
        
        # Calculate center position
        rect = self.rect()
        width = rect.width()
        height = rect.height()

        print('rect: ', rect)
        print('width: ', width)
        print('height: ', height)
        # Draw watermark text rotated at 45 degrees
        painter.translate(rect.center())
        painter.rotate(-45)
        
        # Draw multiple watermarks in a pattern
        text = "Sri Vishwatitiksha"
        diagonal = int((width**2 + height**2)**0.5)
        for x in range(-diagonal, diagonal, 900):
            for y in range(-diagonal, diagonal, 250):
                painter.drawText(x, y, text)
        
        painter.end()
