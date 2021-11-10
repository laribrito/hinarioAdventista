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

import os

#CONSTANTES###############################################################
LIMITE = 120

class Reprodutor():
    def Tocar(musica):
        try:
            # Converte a string para inteiro
            # Assim o teste não dá erro
            musica = int(musica)
            if musica < 1 or musica > LIMITE:
                return False
            os.system(f'xdg-open videos/{musica}.mp4' or f'start videos/{musica}.mp4')
            return True
        except ValueError:
            # Se a conversão der errado...
            return False
        