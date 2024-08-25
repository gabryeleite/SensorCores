# Sensor de Cores

Projeto desenvolvido para o Ramo Estudantil IEEE.

## Modelos:
- [Cursor](#cursor)
- [Upload](#upload)
- [Webcam](#webcam)

## Integrantes: 
- [gabryeleite](https://github.com/gabryeleite)
- [Leloana](https://github.com/Leloana)
- [rafatokairin](https://github.com/rafatokairin)

## Requisitos:
- Python3
- pip install opencv-python
- pip install pywin32 
- [Banco de cores](https://github.com/gabryeleite/Sensor_Cor/blob/main/BancoCores.py)

---

## Cursor <a name='cursor'></a>

Neste modelo o programa utiliza o cursor para analisar determinado pixel da imagem, retornando o nome da cor e seu valor RGB, assemelhando-se com um conta gotas.

[Código-fonte](https://github.com/gabryeleite/Sensor_Cor/blob/main/PonteiroClick.py)

## Upload <a name='upload'></a>

A partir de determinado endereço de imagem passado, o programa analisará seus pixels e retornará sua cor predominante e seu valor RGB.

[Código-fonte](https://github.com/gabryeleite/Sensor_Cor/blob/main/Upload.py)

## Webcam <a name='webcam'></a>

O programa inicia a webcam, deste modo o usuário poderá selecionar determinado ponto e então será retornado a cor e o valor RGB obtidos. O programa pode ser realizado indefinidamente, sendo finalizado àpos selecionat a tecla 's'.

[Código-fonte](https://github.com/gabryeleite/Sensor_Cor/blob/main/Webcam.py)
