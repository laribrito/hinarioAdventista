from PyQt5 import QtWidgets, uic
from lancarVideo import Reprodutor
class Principal(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("telas/principal.ui", self)
        self.show()

        self.campoBusca = self.findChild(QtWidgets.QLineEdit, "busca")

        self.btnTocar = self.findChild(QtWidgets.QPushButton, "tocar")
        self.btnTocar.clicked.connect(self.play)

        self.campoResultados = self.findChild(QtWidgets.QListView, "resultados")
        # setGeometry(left, top, width, height)
        self.campoResultados.setGeometry(120, 200, 451, 0)
    #inicia a música referente ao número digitado
    # obs.: o número tem que estar idêntico ao escrito no nome 
    #   do arquivo. Ex: HINO 1; Errado: 01, 001; Correto: 1
    def play(self):
        musica = self.campoBusca.text()
        Reprodutor.Tocar(musica)  
        self.campoBusca.setText("")      

	# def pesquisar(self):
	# 	self.cf.show()

	# def exibirFc(self):
	# 	self.fc.show()
