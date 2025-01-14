from PyQt6.QtWidgets import QApplication, QMainWindow, QSlider, QVBoxLayout, QWidget, QCheckBox, QLabel, QHBoxLayout
from PyQt6.QtCore import Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self, start_speed):
        super().__init__()
        
        # Set up the window title and size
        self.setWindowTitle("Two columns experiment")
        self.setGeometry(100, 100, 500, 500)

        self.augSpeed = start_speed
        self.actSpeed = start_speed

        # Create the Auger speed slider widget
        self.slider1 = QSlider(Qt.Orientation.Vertical)
        self.slider1.setMinimum(0)
        self.slider1.setMaximum(100)
        self.slider1.setValue(self.augSpeed)  # Set initial position to middle
        self.slider1.valueChanged.connect(lambda value: self.print_slider_value(value, "slider1"))

        # Creating Auger on or off switch
        self.augerPow = QCheckBox("Off")
        self.augerPow.setChecked(False)  # Default state is "Off"
        self.augerPow.stateChanged.connect(lambda state: self.toggle_switch1(state, "augerPow"))

        # Creating Auger Up or down switch
        self.augerDir = QCheckBox("Forward")
        self.augerDir.setChecked(False)  # Default state is "Off"
        self.augerDir.stateChanged.connect(lambda state: self.toggle_switch2(state, "augerDir"))

        # Creating Actuator Speed Slider
        slider_label2 = QLabel("Actuator Slider (0-100):")
        self.slider2 = QSlider(Qt.Orientation.Vertical)
        self.slider2.setMinimum(0)
        self.slider2.setMaximum(100)
        self.slider2.setValue(self.actSpeed)
        self.slider2.valueChanged.connect(lambda value: self.print_slider_value(value, "slider2"))

        # Creating Actuator On/Off switch
        switch_label1 = QLabel("Actuator On/Off")
        self.actPow = QCheckBox("Off")
        self.actPow.setChecked(False)
        self.actPow.stateChanged.connect(lambda state: self.toggle_switch1(state, "actPow"))

        # Creating Actuator Up/Down switch
        switch_label2 = QLabel("Actuator Up/Down")
        self.actDir = QCheckBox("Forward")
        self.actDir.setChecked(False)
        self.actDir.stateChanged.connect(lambda state: self.toggle_switch2(state, "actDir"))



        # Set up layouts for each column
        column1_layout = QVBoxLayout()
        column1_layout.addWidget(QLabel("Auger Speed"))
        column1_layout.addWidget(self.slider1)
        column1_layout.addWidget(QLabel("Auger Power"))
        column1_layout.addWidget(self.augerPow)
        column1_layout.addWidget(QLabel("Auger Direction"))
        column1_layout.addWidget(self.augerDir)

        column2_layout = QVBoxLayout()
        column2_layout.addWidget(slider_label2)
        column2_layout.addWidget(self.slider2)
        column2_layout.addWidget(switch_label1)
        column2_layout.addWidget(self.actPow)
        column2_layout.addWidget(switch_label2)
        column2_layout.addWidget(self.actDir)

        # Main layout to hold both columns
        main_layout = QHBoxLayout()
        main_layout.addLayout(column1_layout)
        main_layout.addLayout(column2_layout)

        # Set main widget and layout
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        

    def print_slider_value(self, value, slider_number):
        if slider_number == "slider1":
            self.augSpeed = value
        elif slider_number == "slider2":
            self.actSpeed = value
        print(f"Slider {slider_number} Value: {value}")
    
    # For on/off switch
    def toggle_switch1(self, state, switch_name):
        switch = getattr(self, f"{switch_name}")
        if state == Qt.CheckState.Checked.value:
            switch.setText("On")
            print(f"{switch_name} is On")
            if switch_name == "augerPow":
                print(f"Running auger at speed {self.augSpeed}")
                #speed(self.augSpeed)
        else:
            switch.setText("Off")
            print(f"{switch_name} is Off")

    # For up/down switch
    def toggle_switch2(self, state, switch_name):
        switch = getattr(self, f"{switch_name}")
        if state == Qt.CheckState.Checked.value:
            switch.setText("Backward")
            print(f"{switch_name} Going backward with speed ")
        else:
            switch.setText("Forward")
            print(f"{switch_name} Going forward")

# if __name__ == "__main__":
#     # Run the application
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec())