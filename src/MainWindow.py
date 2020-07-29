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
        for i in reversed(range(self.paging_buttons.count())): 
            self.paging_buttons.itemAt(i).widget().deleteLater()
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
                
        first_page_button = QtWidgets.QPushButton("<<")
        first_page_button.setSizePolicy(sizePolicy)
        self.paging_buttons.addWidget( first_page_button)
        first_page_button.clicked.connect(lambda _: self.setPage(1))
        
        before_page_button = QtWidgets.QPushButton("...")
        before_page_button.setSizePolicy(sizePolicy)
        self.paging_buttons.addWidget( before_page_button)
        before_page_button.clicked.connect(lambda _: self.setPage(selected - 1))
        
        pageRange = int((selected / 6) + 1)
        print(pageRange)
        
        for x in range(pageRange, pageRange + 5):
            if x <= pages_num:
                pageButton = QtWidgets.QPushButton(str(x))
                pageButton.setObjectName(str(x))
                pageButton.setSizePolicy(sizePolicy)
                pageButton.clicked.connect(self.setPage)
                self.paging_buttons.addWidget(pageButton)
                                
                if selected == x:
                    pageButton.setEnabled(False)
        
        after_page_button = QtWidgets.QPushButton("...")
        after_page_button.setSizePolicy(sizePolicy)
        self.paging_buttons.addWidget( after_page_button)  
            
        last_page_button = QtWidgets.QPushButton(">>")
        last_page_button.setSizePolicy(sizePolicy)
        self.paging_buttons.addWidget( last_page_button)
        
        if selected == 1:
            first_page_button.setEnabled(False)
            before_page_button.setEnabled(False)
        if pages_num == selected:
            last_page_button.setEnabled(False)
            after_page_button.setEnabled(False)
        
    
    def setPage(self, selected = 0):
        if selected == 0:
            selected = int(self.sender().objectName())
        self.addButton(self.maxPage, selected)
        
        
    
app = QtWidgets.QApplication(sys.argv)
app.setStyle("Fusion")
window = Main()
sys.exit(app.exec_())