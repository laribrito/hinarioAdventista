import os
import subprocess

class Reprodutor():
    def Tocar(musica):
        os.system(f'start videos/{musica}.mp4')