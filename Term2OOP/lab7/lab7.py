from functools import partial
import os
import sys
import lab7_resources

from PyQt5.QtCore import Qt
from PyQt5.QtGui import (QPixmap, QFont, QIcon)
from PyQt5.QtWidgets import (QApplication, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit, QMainWindow,
        QProgressBar, QPushButton, QStackedWidget, QStyleFactory, QVBoxLayout, QWidget)

class ScoreTracker(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('ScoreKeeper 4.2')
        self.setFixedSize(400, 450)
        
        # creating stacked widgets
        self.stack = QStackedWidget(self)
        self.setCentralWidget(self.stack)

        # shamelessly lifted from your code
        current_dir = os.path.dirname(os.path.abspath(__file__))
        styles = os.path.join(current_dir, 'score_tracker.css')
        with open(styles, 'r') as f:
            # external stylesheet
            self.setStyleSheet(f.read())
        
        # title screen picture
        self.header = QLabel()
        self.title_image = QPixmap(':/images/score_board.jpg')
        self.title_image.scaledToWidth(15)
        self.header.setPixmap(self.title_image)

        # score screen picture
        self.score_header = QLabel()
        self.screen_image = QPixmap(':/images/score_board2.jpg')
        self.screen_image.scaledToWidth(0)
        self.score_header.setPixmap(self.screen_image)

        # score display box
        score = '0'
        self.score_display = QLineEdit(score)
        self.score_display.setReadOnly(True)
        self.score_display.setAlignment(Qt.AlignCenter)
        self.score_display.setFixedWidth(75)
        
        # title screen widgets, layout and labels
        self.title_screen = QWidget()
        self.title_screen.setObjectName("title_screen")
        self.title_screen_layout = QVBoxLayout()
        self.title_screen.setLayout(self.title_screen_layout)
        self.title_screen_layout.addWidget(self.header)
        self.title_button = QPushButton('Create Score Board')
        self.title_screen_layout.addWidget(self.title_button)
        
        # creating buttons
        self.create_button_layout()
        back_button = QPushButton('Back')
        back_button.setObjectName('back_button')

        # score screen widgets, layout and labels
        self.score_screen = QWidget()
        self.score_screen.setObjectName("score_screen")
        self.score_screen_layout = QVBoxLayout()
        self.score_screen.setLayout(self.score_screen_layout)
        self.score_screen_layout.addWidget(self.score_header)
        self.score_label = QLabel()
        self.score_screen_layout.addWidget(self.score_label)
        self.score_screen_layout.addWidget(self.button_group)
        self.score_screen_layout.addWidget(back_button)
        

        # button connections
        self.title_button.clicked.connect(self.score_screen_onClick)
        back_button.clicked.connect(self.title_screen_onClick)
        
        # adding widgets to the stack
        self.stack.addWidget(self.title_screen)
        self.stack.addWidget(self.score_screen)

    def create_button_layout(self):
        self.button_group = QGroupBox()
        button_layout = QHBoxLayout()
        
        # increase and decrease buttons
        increase_button = QPushButton('+')
        decrease_button = QPushButton('-')

        # making button text bigger
        increase_button.setStyleSheet('font-size: 26px; border: 2px solid black;')
        decrease_button.setStyleSheet('font-size: 26px; border: 2px solid black;')

        # removing border from group
        self.button_group.setStyleSheet('border: 0px;')

        # adding to layout
        button_layout.addWidget(decrease_button)
        button_layout.addWidget(self.score_display)
        button_layout.addWidget(increase_button)

        # connections
        increase_button.clicked.connect(self.increase_score_onClick)
        decrease_button.clicked.connect(self.decrease_score_onClick)

        # setting layout
        self.button_group.setLayout(button_layout)

    # function to switch to the score page
    def score_screen_onClick(self):
        self.stack.setCurrentIndex(1)
    
    def title_screen_onClick(self):
        self.stack.setCurrentIndex(0)

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