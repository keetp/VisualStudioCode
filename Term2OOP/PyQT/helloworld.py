# handles exit status
import sys

# importing widgets from PyQt library
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

# initializing QApplication

app = QApplication(sys.argv)

# creating a display window
window = QWidget()
window.setWindowTitle('PyQt Hello World!')
window.setGeometry(100, 100, 250, 90)   # x, y, width, height
window.move(60,15)  # where the window appears  
helloMsg = QLabel('<h1>Hello World!</h1>', parent=window)   # display msg
helloMsg.move(60,15)    # where the msg appears in the window

# showing window
window.show()

sys.exit(app.exec_())