from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import fdb
import time

from src.components.ui import Ui_tableWidget
from src.components.qTable.QTableWidgetHandler import QTableWidgetHandler
from src.config.Firebird import Firebird
from src.api.FBprodutos import FBprodutos


class table_teste(QtWidgets.QMainWindow, Ui_tableWidget.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        
        #Database setup
        cur = Firebird().cur
        fBprodutos = FBprodutos(cur)
        
        
        QTableWidgetHandler(self.table_with_paging, self.tableWidget, dataBaseAPI = fBprodutos, addPaging=True, addFilter=True)
                        
        
                
        self.show()
        
        

