from zipfile import ZipFile
import os

caminho = r'C:\Users\Zed\Desktop\learning-python\modules\zip'

## criando um arquivo compactado
with ZipFile('arquivo.zip', 'w') as zip:
    for arq in os.listdir(caminho):
        ## jogando um arquivo dentro do zip
        caminho_completo = os.path.join(caminho, arq)
        zip.write(caminho_completo, arq)

with ZipFile('arquivo.zip', 'r') as zip:
    for arq in zip.namelist():
        print(arq)


with ZipFile('arquivo.zip', 'r') as zip:
    zip.extractall('descompactado')