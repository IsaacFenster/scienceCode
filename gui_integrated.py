from gui_experiment import MainWindow
from PyQt6.QtWidgets import QApplication, QMainWindow, QSlider, QVBoxLayout, QWidget, QCheckBox, QLabel, QHBoxLayout
from PyQt6.QtCore import Qt
import sys

def main():
    app = QApplication(sys.argv)
    window = MainWindow(20)
    window.show()
    sys.exit(app.exec())

main()