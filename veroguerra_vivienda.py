# -*- coding: utf-8 -*-
"""VeroGuerra_vivienda.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GXDxTljv0bQVhFWiaALYLHSHtBtSaRM1
"""

import pandas as pd

datos_viviendas = pd.read_csv("/content/drive/MyDrive/CSV/alquileres_viviendas.csv", sep = ";")

datos_viviendas.head(30)

sel_departamentos = datos_viviendas["Tipo"]== "Departamento"
cant_dpto = datos_viviendas[sel_departamentos].shape[0]
cant_dpto

sel_otros_departamentos = datos_viviendas["Tipo"]== "Departamento"
cant_otras_viv = datos_viviendas[~sel_otros_departamentos].shape[0]
cant_otras_viv

sel_casa_hab_cochera = (datos_viviendas["Tipo"]== "Casa" )|(datos_viviendas["Tipo"]== "Habitación")|(datos_viviendas["Tipo"]== "Cochera")
cant_casa_hab_cochera = datos_viviendas[sel_casa_hab_cochera].shape[0]
cant_casa_hab_cochera

sel_area = (datos_viviendas['Area']>=60)&(datos_viviendas['Area']<=100)
cant_viv_area = datos_viviendas[sel_area].shape[0]
cant_viv_area

sel_hab_precio = (datos_viviendas['Cuartos']>=4)&(datos_viviendas['Valor']<=2000)
cant_hab_precio = datos_viviendas[sel_hab_precio].shape[0]
cant_hab_precio

print("Se encontraron los siguientes resultados")
print(f"El numero de dptos es de {cant_dpto}")
print(f"El numero de viviendas restantes es de {cant_otras_viv}")
print(f"El numero de viviendas tipo, Habitacion y cochera es de {cant_casa_hab_cochera}")
print(f"La cantidad de viviendas con un area entre 60 y 100 metros cuadrados es de {cant_viv_area}")
print(f"La cantidad de viviendas con al menos 4 hab y con el valor menor o igual a 2000 reales es de {cant_hab_precio}")

"""Manejo de datos faltantes"""

datos_viviendas.isnull()

datos_viviendas.info()

datos_viviendas[datos_viviendas['Valor'].isnull()]

viviendas_nan= datos_viviendas.shape[0]
datos_viviendas.dropna(subset=['Valor'],inplace = True)
viviendas_nan_b = datos_viviendas.shape[0]
viviendas_nan - viviendas_nan_b

datos_viviendas[datos_viviendas['Valor'].isnull()]

"""#Cuando la decision es conservar los datos debemos sobre escribir con un valor, en este caso 0. para conservar la fila."""

datos_viviendas[datos_viviendas['Mantenimiento'].isnull()].shape[0]

sel = (datos_viviendas['Tipo']== 'Departamento')% (datos_viviendas['Mantenimiento'].isnull())

sel_A = datos_viviendas.shape[0]
datos_viviendas = datos_viviendas[~sel]
sel_B = datos_viviendas.shape[0]
sel_A - sel_B