"""
This file is part of Hinário Adventista - não oficial.

Hinário Adventista - não oficial is free software: you can redistribute
it and/or modify it under the terms of the GNU General Public License 
as published by the Free Software Foundation, either version 3 of
the License, or any later version.

Hinário Adventista - não oficial is distributed in the hope that 
it will be useful, but WITHOUT ANY WARRANTY; without even the 
implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Hinário Adventista - não oficial.  If not, see <https://www.gnu.org/licenses/>6.
"""

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

        self.setMsg = self.findChild(QtWidgets.QLabel, "setMensagem")

        # self.campoResultados = self.findChild(QtWidgets.QListView, "resultados")
        # setGeometry(left, top, width, height)
        # self.campoResultados.setGeometry(120, 200, 451, 0)

    #inicia a música referente ao número digitado
    # obs.: o número tem que estar idêntico ao escrito no nome 
    #   do arquivo. Ex: HINO 1; Errado: 01, 001; Correto: 1
    def play(self):
        musica = self.campoBusca.text()
        valido = Reprodutor.Tocar(musica)
        if not valido:
            self.setMsg.setText("Esse hino não está disponível ou não existe")
        else:
            self.setMsg.setText("")
        self.campoBusca.setText("")

	# def pesquisar(self):
	# 	self.cf.show()

	# def exibirFc(self):
	# 	self.fc.show()
