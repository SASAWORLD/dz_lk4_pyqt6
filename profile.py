import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QFont, QPixmap, QPainter, QPainterPath
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(50, 50, 300, 400)
        self.setWindowTitle("2.1 - User Profile GUI")
        self.setUpMainWindow()
        self.show()

    def createImageLabels(self):
        self.bg_label = QLabel(self)
        self.bg_label.setGeometry(0, 0, 300, 155)
        self.bg_label.setStyleSheet("background-color: #854442;")

        image = "images/profile_image.png"
        try:
            pixmap = QPixmap(image)
            print("pixmap.isNull():", pixmap.isNull())

            crop = pixmap.copy(0, 0, pixmap.width(), pixmap.height())

            crop = crop.scaled(90, 90, Qt.AspectRatioMode.KeepAspectRatioByExpanding, Qt.TransformationMode.SmoothTransformation)

            size = 90
            rounded = QPixmap(size, size)
            rounded.fill(Qt.GlobalColor.transparent)
            painter = QPainter(rounded)
            painter.setRenderHint(QPainter.RenderHint.Antialiasing)
            path = QPainterPath()
            path.addEllipse(0, 0, size, size)
            painter.setClipPath(path)
            painter.drawPixmap(0, 0, crop)
            painter.end()

            self.photo_label = QLabel(self)
            self.photo_label.setPixmap(rounded)
            self.photo_label.setGeometry(110, 10, 90, 90)
        except Exception as e:
            print(f"Image not found.\nError: {e}")

    def setUpMainWindow(self):
        self.createImageLabels()
        user_label = QLabel(self)
        user_label.setText("Максим Зименс")
        user_label.setFont(QFont("Arial", 20))
        user_label.move(60, 120)

        bio_label = QLabel(self)
        bio_label.setText("Биография")
        bio_label.setFont(QFont("Arial", 17))
        bio_label.move(15, 155)

        about_label = QLabel(self)
        about_label.setText(
            "Я студент 2-го курса ВУЗ МАИ"
        )
        about_label.setWordWrap(True)
        about_label.move(15, 180)

        skills_label = QLabel(self)
        skills_label.setText("Умения")
        skills_label.setFont(QFont("Arial", 17))
        skills_label.move(15, 225)

        languages_label = QLabel(self)
        languages_label.setText("Python | Excel")
        languages_label.move(15, 250)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

