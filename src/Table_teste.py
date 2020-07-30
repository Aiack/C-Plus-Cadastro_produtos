from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import fdb

from src.api.FBprodutos import FBprodutos


from src.components.ui import Ui_tableWidget

from src.components.qTable.QTableWidgetHandler import QTableWidgetHandler

class table_teste(QtWidgets.QMainWindow, Ui_tableWidget.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        
        qTable = QTableWidgetHandler(self.table_with_paging, self.tableWidget)
        qTable.setupPaging()
        
        db = FBprodutos()
                
        # qTable.fillTable(data)
        
        self.show()
        
app = QtWidgets.QApplication(sys.argv)
app.setStyle("Fusion")
window = table_teste()
sys.exit(app.exec_())
