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

    central = QWidget()
    window.setCentralWidget(central)

    main_layout = QVBoxLayout(central)
    main_layout.setContentsMargins(0, 0, 0, 0)

    top_bar = QWidget()
    top_bar.setFixedHeight(100)
    top_layout = QHBoxLayout(top_bar)
    top_layout.setContentsMargins(20, 10, 20, 10)

    title = QLabel("annot8")

    open_button = QPushButton("OPEN")
    save_button = QPushButton("SAVE")
    settings_button = QPushButton("SETTINGS")
    open_button.setFixedSize(100, 50)
    save_button.setFixedSize(100, 50)
    settings_button.setFixedSize(100, 50)

    top_layout.addWidget(title)
    top_layout.addStretch()
    top_layout.addWidget(open_button)
    top_layout.addWidget(save_button)
    top_layout.addWidget(settings_button)

    main_layout.addWidget(top_bar)

    operating_panel = QWidget()
    operating_panel_layout = QHBoxLayout(operating_panel)
    operating_panel_layout.setContentsMargins(20, 10, 20, 10)

    operator_sidebar = QWidget()
    operator_sidebar_layout = QVBoxLayout(operator_sidebar)
    operator_sidebar.setStyleSheet("background-color: #333333;")
    operating_panel_layout.addStretch(3)
    operating_panel_layout.addWidget(operator_sidebar, 1)
    main_layout.addWidget(operating_panel)

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
