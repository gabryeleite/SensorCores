import win32api
import win32gui
import win32con 
import time
import math
from BancoCores import Color, cores

hdc = win32gui.GetDC(None)

while True:
    # verifica se houve um clique com o botão esquerdo do mouse
    if win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        # obtem a posicao atual do cursor
        cursorPos = win32api.GetCursorPos()

        # obtem a cor do pixel sob o cursor
        cor = win32gui.GetPixel(hdc, cursorPos[0], cursorPos[1])

        # extrai os componentes RGB da cor
        R = cor & 0xFF
        G = (cor >> 8) & 0xFF
        B = (cor >> 16) & 0xFF

        melhorCorrespondencia = 0 # inicializa com 0
        menorDistancia = 256 * 256 * 256 # inicializa com valor alto
        # percorre as cores do banco de cores
        for i in range(len(cores)):
            # calcula a distância euclidiana entre a cor atual e as cores na lista
            distancia = math.sqrt(pow((R - cores[i].r), 2) + pow((G - cores[i].g), 2) + pow((B - cores[i].b), 2))
            # verifica se a distância atual é menor que a menor distância encontrada até agora
            if distancia < menorDistancia:
                melhorCorrespondencia = i
                menorDistancia = distancia

        # imprime o nome da cor e seu valor RGB
        print("Cor: {} ({}, {}, {})".format(
            cores[melhorCorrespondencia].nome, R, G, B))

        time.sleep(0.5)

win32gui.ReleaseDC(None, hdc)
