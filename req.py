# App para quitar versiones de requeriments
import sys

with open('requirements.txt', 'r') as txt:
    lineas = txt.readlines()

lineas_nuevas = []
for linea in lineas:
    lineas_nuevas.append(linea[0:(linea.find('='))])
print(lineas_nuevas)

with open('requirements_sinVersion.txt', 'w') as txt:
    for linea in lineas_nuevas:
        txt.write(linea + '\n')

