import sys
import PySide6
from PySide6.QtWidgets import QApplication, QMainWindow


def main():
    app = QApplication(sys.argv)
    print(f"Running pyside6 version : {PySide6.__version__}")
    window = QMainWindow()
    window.setWindowTitle("Annot8")
    window.setStyleSheet("QMainWindow {background-color: #000000}")
    window.resize(1000, 700)
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
