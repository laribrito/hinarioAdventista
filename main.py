from PyQt5 import QtWidgets
import sys
from telaprincipal import Principal

app = QtWidgets.QApplication(sys.argv)
janela = Principal()
app.exec_()