import sys
import os

args = sys.argv
qtd_args = len(args)

if qtd_args <= 1:
    print('Faltando argumentos')
    print('-a', 'Para listar todos os arquivos nesta pasta', sep='\t')
    print('-d', 'Para listar todos os diretorios nesta pasta', sep='\t')
    sys.exit()

so_arquivos = False
if '-a' in args:
    so_arquivos = True

so_diretorio = False
if '-d' in args:
    so_diretorio = True

for arquivo in os.listdir('.'):
    if so_arquivos:
        if os.path.isfile(arquivo):
            print(arquivo)
    if so_diretorio:
        if os.path.isdir(arquivo):
            print(arquivo)

print(args)
