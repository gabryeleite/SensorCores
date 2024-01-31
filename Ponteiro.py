import win32api
import win32gui
import time
from BancoCores import Color, cores

hdc = win32gui.GetDC(None)

while True:
    # obtem a posicao atual do cursor
    cursorPos = win32api.GetCursorPos()

    # obtem a cor do pixel sob o cursor
    cor = win32gui.GetPixel(hdc, cursorPos[0], cursorPos[1])

    # extrai os componentes RGB da cor
    r = cor & 0xFF
    g = (cor >> 8) & 0xFF
    b = (cor >> 16) & 0xFF

    melhorCorrespondencia = 0 # inicializa com 0
    menorDistancia = 256 * 256 * 256 # inicializa com valor alto
    # percorre as cores do banco de cores
    for i in range(len(cores)):
        # calcula a distância euclidiana entre a cor atual e as cores na lista
        distancia = (r - cores[i].r) ** 2 + \
            (g - cores[i].g) ** 2 + (b - cores[i].b) ** 2
        # verifica se a distância atual é menor que a menor distância encontrada até agora
        if distancia < menorDistancia:
            melhorCorrespondencia = i
            menorDistancia = distancia

    # imprime o nome da cor e seu valor RGB
    print("Cor: {} ({}, {}, {})".format(
        cores[melhorCorrespondencia].nome, r, g, b))

    # espera pequeno intervalo
    time.sleep(0.5)

# Fecha o handle da tela
win32gui.ReleaseDC(None, hdc)
