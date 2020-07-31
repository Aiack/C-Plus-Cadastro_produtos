from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import time

from src.Table_teste import table_teste

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    window = table_teste()
    sys.exit(app.exec_())
    