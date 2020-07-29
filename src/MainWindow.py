from PyQt5 import QtCore, QtGui, QtWidgets
from src.components.ui import Ui_tableWidget
import sys

class Main(QtWidgets.QMainWindow, Ui_tableWidget.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        
        self.selectedPage = 1
        
        self.maxPage = 15
        
        self.addButton(self.maxPage, self.selectedPage)
        
        self.show()
        

    def addButton(self, pages_num, selected):
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        
        self.first_page_button = QtWidgets.QPushButton("<<")
        self.first_page_button.setSizePolicy(sizePolicy)
        self.paging_buttons.addWidget( self.first_page_button)
        
        # for x in range(selected, selected + 5):
        #     if x <= pages_num:
        #         pageButton = QtWidgets.QPushButton(str(x))
        #         pageButton.setObjectName(str(x))
        #         pageButton.setSizePolicy(sizePolicy)
        #         pageButton.clicked.connect(lambda _: print(x))
        #         self.paging_buttons.addWidget(pageButton)
                
        #         print(self.findChild(QtWidgets.QPushButton, str(x)))
                
        #         if self.selectedPage == x:
        #             pageButton.setEnabled(False)
        
        buttons = []
        for x in range(selected, selected + 5):
            if x <= pages_num:
                pageButton = QtWidgets.QPushButton(str(x))
                pageButton.setObjectName(str(x))
                pageButton.setSizePolicy(sizePolicy)
                pageButton.clicked.connect(lambda _: print(str(x)))
                buttons.append(pageButton)
        
        for button in buttons:
            self.paging_buttons.addWidget(button)
                    
        self.last_page_button = QtWidgets.QPushButton(">>")
        self.last_page_button.setSizePolicy(sizePolicy)
        self.paging_buttons.addWidget( self.last_page_button)
        
        if self.selectedPage == 1:
            self.first_page_button.setEnabled(False)
        if self.selectedPage == self.maxPage:
            self.last_page_button.setEnabled(False)
        
    
    def setPage(self, n):
        pass
    
app = QtWidgets.QApplication(sys.argv)
app.setStyle("Fusion")
window = Main()
sys.exit(app.exec_())