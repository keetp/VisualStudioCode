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
app = QApplication(sys.argv)

# window properties
window = QWidget()  # initializing
window.setWindowTitle('Modulo Calculator')  # window title
window.resize(250, 200)  # window size
window.setStyleSheet('border: 1px solid black;')

# layout 
layout = QGridLayout(window)    # grid layout being applied to the window

# label for title
label_title = QLabel('Modulo Calculator')
layout.addWidget(label_title, 0, 1)

# input labels
label_int = QLabel('Integer: ') # integer label 
layout.addWidget(label_int, 1, 0) # position
label_mod = QLabel('Modulus: ') # mod label
layout.addWidget(label_mod, 2, 0) # position

# user inputs
user_int = QLineEdit() # integer input box
layout.addWidget(user_int, 1, 1) # position
user_mod = QLineEdit() # mod input box
layout.addWidget(user_mod, 2, 1) # position

# calculation button
calc_button = QPushButton('Calculate')
layout.addWidget(calc_button, 3, 1) # position

# display box/label for the calculation (Read Only)
label_calc = QLabel('Result: ') # result label
layout.addWidget(label_calc, 4, 0) # position
calc_display = QLineEdit() # display box
calc_display.setReadOnly(True)  # setting to read only
layout.addWidget(calc_display, 4, 1) # position

# setting label borders
label_title.setStyleSheet('border: 0px; font-size: 16px; color: red;')
label_calc.setStyleSheet('border: 1px solid black;')
label_int.setStyleSheet('border: 1px solid black;')
label_mod.setStyleSheet('border: 1px solid black;')

# connecting button to the modulo calculation function
calc_button.clicked.connect(mod_calc)

# also connecting the enter key to the function while the user has the input boxes selected
user_int.returnPressed.connect(mod_calc) 
user_mod.returnPressed.connect(mod_calc)


# showing window
window.show()
# exit handling
sys.exit(app.exec_())