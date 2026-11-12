import sys
import PySide6
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QLabel,
)

VERSION = "0.0.1"


def main():
    app = QApplication(sys.argv)
    screen = QApplication.primaryScreen()
    wid, hei = screen.size().toTuple()
    print(f"Running PySide6 Version : {PySide6.__version__}")
    print(f"annot8 Version : {VERSION} started")

    window = QMainWindow()
    window.setWindowTitle("annot8")
    window.setStyleSheet("QMainWindow {background-color: #000000}")
    window.resize(wid, hei)

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
