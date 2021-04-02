'''
    CP1890: Test 2
'''

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator 
from PyQt5.QtWidgets import (
                                QApplication, QCheckBox, QComboBox, QDialog,
                                QFormLayout, QGridLayout, QGroupBox, 
                                QHBoxLayout, QLabel, QLineEdit, QPushButton,
                                QStyleFactory,  QTextEdit, QVBoxLayout, QWidget
                            )


class HotDogSurvey(QDialog):
    """A very serious survey of user's hot dog eating habits"""
    def __init__(self, parent=None):
        """This init builds the survey window"""
        super().__init__(parent)

        # main layout + header
        self.setWindowTitle('Hot Dog Survey')
        self.main_layout = QVBoxLayout()
        self.header_label = QLabel('<h1 style=color:red; text-align:center;> Hot Dog Survey</h1>')
        self.header_label.setAlignment(Qt.AlignCenter)
        
        # combo box
        self.hotdog_box = QComboBox()
        self.combo_choices = ['1', '2', '3', '4', '5+ (you animal)']
        self.hotdog_box.addItems(self.combo_choices)
        self.box_label = QLabel('How many hot dogs would you consume for a single meal?')
        self.box_label.setBuddy(self.hotdog_box)
        
        # calling creation methods
        self._create_user_input()
        self._create_checkbox_group()
        self._create_buttons()

        # adding widgets to main layout
        self.main_layout.addWidget(self.header_label)
        self.main_layout.addLayout(self.survey_layout)
        self.main_layout.addWidget(self.box_label)
        self.main_layout.addWidget(self.hotdog_box)
        self.main_layout.addWidget(self.checkbox_group)
        self.main_layout.addLayout(self.button_layout)
        
        self.setLayout(self.main_layout)

    def _create_user_input(self):
        ''' creating user input boxes '''
        self.survey_layout = QFormLayout()
        self.name_input = QLineEdit()
        self.age_input = QLineEdit()
        self.name_label = QLabel('Name:')
        self.age_label = QLabel('Age:')
        self.survey_layout.addRow(self.name_label, self.name_input)
        self.survey_layout.addRow(self.age_label, self.age_input)
        
    def _create_checkbox_group(self):
        ''' creating checkbox group '''
        self.checkbox_group = QGroupBox("Select preferred condiments:")
        self.checkbox_layout = QGridLayout()

        # creating checkboxes and adding to layout
        self.checkbox1 = QCheckBox('Ketchup')
        self.checkbox2 = QCheckBox('Mustard')
        self.checkbox3 = QCheckBox('Relish')
        self.checkbox4 = QCheckBox('Cheese')
        self.checkbox5 = QCheckBox('Onions')
        self.checkbox6 = QCheckBox('Bacon')
        self.checkbox_layout.addWidget(self.checkbox1, 0, 0)
        self.checkbox_layout.addWidget(self.checkbox2, 0, 1)
        self.checkbox_layout.addWidget(self.checkbox3, 0, 2)
        self.checkbox_layout.addWidget(self.checkbox4, 1, 0)
        self.checkbox_layout.addWidget(self.checkbox5, 1, 1)
        self.checkbox_layout.addWidget(self.checkbox6, 1, 2)
        # setting the layout
        self.checkbox_group.setLayout(self.checkbox_layout)
    
    def _create_buttons(self):
        ''' creating buttons for form '''
        self.button_layout = QHBoxLayout()
        self.submit_button = QPushButton('Submit')
        self.cancel_button = QPushButton('Cancel')
        self.button_layout.addWidget(self.submit_button)
        self.button_layout.addWidget(self.cancel_button)

        # connections
        self.submit_button.clicked.connect(self.confirm_window)
        self.cancel_button.clicked.connect(self.close)

    def confirm_window(self):
        ''' Dialog window which displays the inputted information '''
        self.confirm_layout = QVBoxLayout()
        self.confirm_window = QDialog()
        self.information_confirm = QLabel('Is this information correct?')
        self.inputted_age = QLabel(self.name_input.text())
        self.inputted_name = QLabel(self.age_input.text())
        self.hotdog_number = QLabel(self.hotdog_box.currentText())
        
        # went down a rabbit hole and made this way more complicated than it needed to be
        # verbose commenting so its less confusing when i go back over it

        # creating a list of checkbox selections
        self.condiment_list = self.checkbox_group.findChildren(QCheckBox)
        # initializing a list of objects to be displayed
        self.display_list = []
        # checking if the checkbox is ticked
        for val in range(len(self.condiment_list)):
            if self.condiment_list[val].isChecked() == True:
                # appending the text to the display list
                self.display_list.append(self.condiment_list[val].text())
        
        # making a string to add list items to
        self.holding_string = 'Condiment preference: '
        # iterating through the list and appending to the string
        for i in range(len(self.display_list)):
            self.holding_string += self.display_list[i] + ' '
        # sticking the string into a label
        self.condiment_display = QLabel(self.holding_string)

        # adding to layout
        self.confirm_layout.addWidget(self.information_confirm)
        self.confirm_layout.addWidget(self.inputted_age)
        self.confirm_layout.addWidget(self.inputted_name)
        self.confirm_layout.addWidget(self.hotdog_number)
        self.confirm_layout.addWidget(self.condiment_display)
        
        self.confirm_window.setLayout(self.confirm_layout)
        self.confirm_window.setWindowTitle('Confirmation Window')
        self.confirm_window.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = HotDogSurvey()
    dlg.show()
    sys.exit(app.exec_())
