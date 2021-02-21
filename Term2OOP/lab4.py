import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QLineEdit, QPushButton 



# takes an integer and a modulus input and shows the remainder of the integer divided by the modulus
def mod_calc():
    try: 
        # taking the input text and converting to int
        calc_int = int(user_int.text())
        calc_mod = int(user_mod.text())
        # making the remainder calculation
        calc_result = calc_int % calc_mod
        # displaying it in the read only box
        calc_display.setText(str(calc_result))
# handling a ValueError being raised
    except ValueError:
        calc_display.setText('ERROR: Enter 2 integers!')

    
# initializing the application
app = QApplication([])
# window properties
window = QWidget()  # initializing
window.setWindowTitle('Modulo Calculator')  # window title
window.resize(250,250)  # window size
# layout 
layout = QGridLayout(window)    # grid layout being applied to the window
# input labels
label_int = QLabel('Integer: ') # integer label 
layout.addWidget(label_int, 0, 0) # position
label_mod = QLabel('Modulus: ') # mod label
layout.addWidget(label_mod, 1, 0) # position
# user inputs
user_int = QLineEdit() # integer input box
layout.addWidget(user_int, 0, 1) # position
user_mod = QLineEdit() # mod input box
layout.addWidget(user_mod, 1, 1) # position
# calculation button
calc_button = QPushButton('Calculate')
layout.addWidget(calc_button, 2, 1) # position
# display box/label for the calculation (Read Only)
label_calc = QLabel('Result: ') # result label
layout.addWidget(label_calc, 3, 0) # position
calc_display = QLineEdit() # display box
calc_display.setReadOnly(True)  # setting to read only
layout.addWidget(calc_display, 3, 1) # position
# connecting button to the modulo calculation function
calc_button.clicked.connect(mod_calc)  
# showing window
window.show()
# exit handling
sys.exit(app.exec_())