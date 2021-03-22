from functools import partial
import os
import sys


from PyQt5.QtCore import Qt
from PyQt5.QtGui import (QPixmap, QFont, QIcon)
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit, QMainWindow,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStackedWidget, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget, QToolBar)

class ScoreTracker(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('ScoreKeeper 4.2')
        self.setFixedSize(300, 100)
        
        # creating stacked widgets
        self.stack = QStackedWidget(self)
        self.setCentralWidget(self.stack)

        # shamelessly lifted from your code
        current_dir = os.path.dirname(os.path.abspath(__file__))
        styles = os.path.join(current_dir, 'score_tracker.css')
        with open(styles, 'r') as f:
            # external stylesheet
            self.setStyleSheet(f.read())

        # title screen widgets, layout and labels
        self.title_screen = QWidget()
        self.title_screen.setObjectName("title_screen")
        self.title_screen_layout = QVBoxLayout()
        self.title_screen.setLayout(self.title_screen_layout)
        self.title_label = QLabel()
        self.title_screen_layout.addWidget(self.title_label)
        self.title_button = QPushButton('Create Score Board')
        self.title_screen_layout.addWidget(self.title_button)

        # score screen widgets, layout and labels
        self.score_screen = QWidget()
        self.score_screen.setObjectName("score_screen")
        self.score_screen_layout = QGridLayout()
        self.score_screen.setLayout(self.score_screen_layout)
        self.score_label = QLabel()
        self.score_screen_layout.addWidget(self.score_label, 0, 1)

        # score display box
        score = 0
        self.score_display = QLineEdit(str(score))
        self.score_display.setReadOnly(True)
        self.score_display.setAlignment(Qt.AlignCenter)
        self.score_display.setFixedWidth(75)
        self.score_screen_layout.addWidget(self.score_display, 1, 1)
        
        # increase and decrease buttons
        self.increase_button = QPushButton('+')
        self.decrease_button = QPushButton('-')
        self.score_screen_layout.addWidget(self.increase_button, 1, 2)
        self.score_screen_layout.addWidget(self.decrease_button, 1, 0)

        # button connections
        self.title_button.clicked.connect(self.score_screen_onClick)
        self.increase_button.clicked.connect(self.increase_score_onClick)
        self.decrease_button.clicked.connect(self.decrease_score_onClick)

        # adding widgets to the stack
        self.stack.addWidget(self.title_screen)
        self.stack.addWidget(self.score_screen)

    # function to switch to the score page
    def score_screen_onClick(self):
        self.stack.setCurrentIndex(1)

    # increasing displayed number
    def increase_score_onClick(self):
        score = self.score_display.text()
        score = str(int(score) + 1)
        self.score_display.setText(score)

    # decreasing displayed number, won't go below 0
    def decrease_score_onClick(self):
        score = self.score_display.text()
        if int(score) > 0:
            score = str(int(score) - 1)
        else:
            score = '0'
        self.score_display.setText(score)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widgets = ScoreTracker()
    widgets.show()
    sys.exit(app.exec_()) 