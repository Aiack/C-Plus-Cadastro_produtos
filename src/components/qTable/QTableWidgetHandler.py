from PyQt5 import QtCore, QtGui, QtWidgets
from src.components.ui import Ui_tableWidget
import math
import sys

class QTableWidgetHandler(QtWidgets.QMainWindow):
    def __init__(self, Qlayout, qTableWidget):
        self.Qlayout = Qlayout
        self.qTableWidget = qTableWidget
        
        
    def fillTable(self, data):
        self.qTableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.qTableWidget.setColumnCount(len(data[0]))
        
        self.qTableWidget.setRowCount(len(data))
        self.qTableWidget.setAlternatingRowColors(True)
        
        self.qTableWidget.setSortingEnabled(False)
        
        if data:
            for column in range(len(data[0])):
                for row in range(len(data)):
                    newitem = QtWidgets.QTableWidgetItem((data[row][column]))
                    self.qTableWidget.setItem(row, column, newitem)
                    
        self.qTableWidget.resizeColumnsToContents()
        self.qTableWidget.setSortingEnabled(True)
        
    def setupPaging(self, maxPage = 1):
        self.selectedPage = 1
        self.maxPage = maxPage
        
        self.buttonLayout = QtWidgets.QHBoxLayout()
        self.buttonLayout.setObjectName("buttonLayout")
        self.Qlayout.addLayout(self.buttonLayout)
        
        self.pagingLogic()

    def pagingLogic(self):
        #Clean the view
        self.cleanLayout(self.buttonLayout)
            
        #Size Policy for the buttons
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        
        leftHorizontalSpacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.buttonLayout.addItem(leftHorizontalSpacer)
                
        first_page_button = QtWidgets.QPushButton("<<")
        first_page_button.setSizePolicy(sizePolicy)
        first_page_button.setMaximumSize(QtCore.QSize(40, 16777215))
        self.buttonLayout.addWidget( first_page_button)
        first_page_button.clicked.connect(lambda _: self.setPage(1))
        
        before_page_button = QtWidgets.QPushButton("...")
        before_page_button.setSizePolicy(sizePolicy)
        before_page_button.setMaximumSize(QtCore.QSize(40, 16777215))
        self.buttonLayout.addWidget( before_page_button)
        before_page_button.clicked.connect(lambda _: self.setPage(self.selectedPage - 1))
        
        pageRangeIndex = (math.ceil(self.selectedPage / 5) - 1) * 5 + 1
                
        for x in range(pageRangeIndex, pageRangeIndex + 5):
            if x <= self.maxPage:
                pageButton = QtWidgets.QPushButton(str(x))
                pageButton.setMaximumSize(QtCore.QSize(40, 16777215))
                pageButton.setObjectName(str(x))
                pageButton.setSizePolicy(sizePolicy)
                pageButton.clicked.connect(self.setPage)
                self.buttonLayout.addWidget(pageButton)
                                
                if self.selectedPage == x:
                    pageButton.setEnabled(False)
        
        after_page_button = QtWidgets.QPushButton("...")
        after_page_button.setMaximumSize(QtCore.QSize(40, 16777215))
        after_page_button.setSizePolicy(sizePolicy)
        self.buttonLayout.addWidget( after_page_button)
        after_page_button.clicked.connect(lambda _: self.setPage(self.selectedPage + 1))
            
        last_page_button = QtWidgets.QPushButton(">>")
        last_page_button.setMaximumSize(QtCore.QSize(40, 16777215))
        last_page_button.setSizePolicy(sizePolicy)
        self.buttonLayout.addWidget( last_page_button)
        last_page_button.clicked.connect(lambda _: self.setPage(self.maxPage))
        
        rightHorizontalSpacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.buttonLayout.addItem(rightHorizontalSpacer)
        
        if self.selectedPage == 1:
            first_page_button.setEnabled(False)
            before_page_button.setEnabled(False)
        if self.maxPage == self.selectedPage:
            last_page_button.setEnabled(False)
            after_page_button.setEnabled(False)
        
    
    def setPage(self, selected = 0):
        if selected == 0:
            self.selectedPage = int(self.sender().objectName())
        else:
            self.selectedPage = selected
        self.pagingLogic()
        
    def cleanLayout(self, layout):
        for i in reversed(range(layout.count())):
            widget = layout.itemAt(i).widget()
            
            if widget is not None:
                widget.deleteLater()
            else:
                layout.takeAt(i)
        
        