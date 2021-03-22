# different pyqt5 widgets implemented into a GUI form.

from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QFormLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget)

class FormWidget(QDialog):
    def __init__(self):
        super().__init__()

        # main layout
        layout = QFormLayout()
        title = QLabel("<h1 style=color:#c0c0c0;>User Information Form</h1>")
        layout.addWidget(title)

        # Combo box for primary computing device
        device = QComboBox()
        choices = {'Desktop': 1, 'Laptop': 2, 'Tablet': 3, 'Mobile Phone': 4}
        device.addItems(choices.keys())
        device_label = QLabel('<h3>&Please Select Primary Device:</h3>')
        device_label.setBuddy(device)

        # submit button
        button = QPushButton('Submit')

        # Creation of widgets
        self.create_checkboxes()
        self.create_user_inputs()
        self.create_text_edit()

        # adding widgets to the main window
        layout.addWidget(device_label)
        layout.addWidget(device)
        layout.addWidget(self.input_group)
        layout.addWidget(self.checkbox_group)
        layout.addWidget(self.text_group)
        layout.addWidget(button)

        # setting the layout
        self.setLayout(layout)

    def create_checkboxes(self):
        """Creating checkbox widgets"""
        self.checkbox_group = QGroupBox("Check off the software you currently use:")
        checkbox_layout = QGridLayout()

        # creating checkboxes and adding to layout
        checkbox1 = QCheckBox('Email')
        checkbox2 = QCheckBox('Instant Mesaging')
        checkbox3 = QCheckBox('Games')
        checkbox4 = QCheckBox('Office Suite')
        checkbox5 = QCheckBox('Coding Editors')
        checkbox_layout.addWidget(checkbox1)
        checkbox_layout.addWidget(checkbox2)
        checkbox_layout.addWidget(checkbox3)
        checkbox_layout.addWidget(checkbox4)
        checkbox_layout.addWidget(checkbox5)

        # setting the layout
        self.checkbox_group.setLayout(checkbox_layout)

    def create_user_inputs(self):
        """Creating user input boxes"""
        self.input_group = QGroupBox()
        input_layout = QGridLayout()
        
        # user inputs and labels
        input1 = QLineEdit()
        input1_label = QLabel('First Name: ')
        input2 = QLineEdit()
        input2_label = QLabel('Last Name: ')
        input3 = QLineEdit()
        input3_label = QLabel('Email: ')
        input_layout.addWidget(input1_label, 0, 0)
        input_layout.addWidget(input2_label, 1, 0)
        input_layout.addWidget(input3_label, 2, 0)
        input_layout.addWidget(input1, 0, 1)
        input_layout.addWidget(input2, 1, 1)
        input_layout.addWidget(input3, 2, 1)

        # setting layout
        self.input_group.setLayout(input_layout)
        
    def create_text_edit(self):
        """Creating box for more detailed user information"""
        self.text_group = QGroupBox()
        text_layout = QVBoxLayout()

        # label
        text_label = QLabel('How do you use your device on a typical day?')

        # one big text box
        textbox = QTextEdit()
        text_layout.addWidget(text_label)
        text_layout.addWidget(textbox)
        self.text_group.setLayout(text_layout)

if __name__ == '__main__':  
    import sys

    app = QApplication(sys.argv)    
    form = FormWidget()
    form.show()
    sys.exit(app.exec_())
