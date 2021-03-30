from functools import partial
import lab8_resources
import os
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import (QPixmap, QFont, QIcon)
from PyQt5.QtWidgets import (QApplication, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit, QMainWindow,
        QProgressBar, QPushButton, QToolBar, QStatusBar, QStackedWidget, QStyleFactory, QVBoxLayout, QWidget)

class Player:
    """ player class to create player score keeping objects within the scorekeeper app"""
    def __init__(self):
        self.create_playerboard()
          
    def create_playerboard(self):
        """ creating playerboard"""
        self.button_group = QGroupBox()
        self.button_layout = QHBoxLayout()

        # score display box
        score = '0'
        self.score_display = QLineEdit(score)
        self.score_display.setReadOnly(True)
        self.score_display.setAlignment(Qt.AlignCenter)
        self.score_display.setFixedWidth(75)

        # increase and decrease buttons
        self.increase_button = QPushButton('+')
        self.decrease_button = QPushButton('-')

        # making button text bigger
        self.increase_button.setStyleSheet('font-size: 26px; border: 2px solid black;')
        self.decrease_button.setStyleSheet('font-size: 26px; border: 2px solid black;')

        # removing border from group
        self.button_group.setStyleSheet('border: 0px;')

        # adding to layout
        self.button_layout.addWidget(self.decrease_button)
        self.button_layout.addWidget(self.score_display)
        self.button_layout.addWidget(self.increase_button)

        # connections
        self.increase_button.clicked.connect(self.increase_score_onClick)
        self.decrease_button.clicked.connect(self.decrease_score_onClick)

        # setting layout
        self.button_group.setLayout(self.button_layout)

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

class ScoreTracker(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('ScoreKeeper 4.2')
        self.setFixedSize(400, 450)
        
        # creating stacked widgets
        self.stack = QStackedWidget(self)
        self.setCentralWidget(self.stack)

        # creating title
        self.create_titleScreen()
        self.create_scoreScreen()

        # shamelessly lifted from your code
        current_dir = os.path.dirname(os.path.abspath(__file__))
        styles = os.path.join(current_dir, 'score_tracker.css')
        with open(styles, 'r') as f:
            # external stylesheet
            self.setStyleSheet(f.read())
        
        #########################
        ### PLAYER BOARD HERE ###
        #########################

        # adding widgets to the stack
        self.stack.addWidget(self.title_screen)
        self.stack.addWidget(self.score_screen)

        # creating menu
        self._create_menu()

    def create_scoreScreen(self):
        # score screen picture
        self.score_header = QLabel()
        self.screen_image = QPixmap(':/images/score_board2.jpg')
        self.screen_image.scaledToWidth(0)
        self.score_header.setPixmap(self.screen_image)

        # score screen widgets, layout and labels
        self.score_screen = QWidget()
        self.score_screen.setObjectName("score_screen")
        self.score_screen_layout = QVBoxLayout()
        self.score_screen.setLayout(self.score_screen_layout)
        self.score_screen_layout.addWidget(self.score_header)
        self.score_label = QLabel()
        self.score_screen_layout.addWidget(self.score_label)

        # creating back button
        self.back_button = QPushButton('Back')
        self.back_button.setObjectName('back_button')

        # back button
        self.score_screen_layout.addWidget(self.back_button)
        
        # connection
        self.back_button.clicked.connect(self.title_screen_onClick)

    def create_titleScreen(self):
        # title screen picture
        self.header = QLabel()
        self.title_image = QPixmap(':/images/score_board.jpg')
        self.title_image.scaledToWidth(15)
        self.header.setPixmap(self.title_image)

        # title screen widgets, layout and labels
        self.title_screen = QWidget()
        self.title_screen.setObjectName("title_screen")
        self.title_screen_layout = QVBoxLayout()
        self.title_screen.setLayout(self.title_screen_layout)
        self.title_screen_layout.addWidget(self.header)
        self.title_button = QPushButton('Create Score Board')
        self.title_screen_layout.addWidget(self.title_button)

        # button connections
        self.title_button.clicked.connect(self.score_screen_onClick)
        
    # function to switch to the score page
    def score_screen_onClick(self):
        self.stack.setCurrentIndex(1)
    
    # switch to title screen
    def title_screen_onClick(self):
        self.stack.setCurrentIndex(0)
    
    def _create_menu(self): 
        """ creating menu """
        self.menu = self.menuBar().addMenu('&Menu')
        self.help = self.menuBar().addMenu('&Help')
        
        self.menu.addAction('&Exit', self.close)
        self.help.addAction('&About', self.display_about)

    def display_about(self):
        """ about section in the menu"""
        about = QDialog(self) 
        layout = QVBoxLayout()
        about_label = QLabel('Small ScoreKeeper app made in Python, \nshoutout to John Milley. \n\n\n\n\t\t CNA OOP Python 1890 ')
        layout.addWidget(about_label)
        about.setLayout(layout)
        about.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widgets = ScoreTracker()
    widgets.show()
    sys.exit(app.exec_()) 