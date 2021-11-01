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

from PyQt5 import QtWidgets
import sys
from telaprincipal import Principal

app = QtWidgets.QApplication(sys.argv)
janela = Principal()
app.exec_()