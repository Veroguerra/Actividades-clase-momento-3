# -*- coding: utf-8 -*-
"""Analitica pantas VeroGuerraInicio_colab.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1J046jRMPGwYRBIz7wZRcuakD5-oi_6s-
"""

import pandas as pd

"""# Práctica Análica

#Importando Pandas

# Nueva sección
"""

df = pd.DataFrame({"Nombre del libro":["java a fondo","Deep Learning", "Arquitectura Limpia", "Big Data con python"]})

df

df = pd.DataFrame({"Nombre del libro":["java a fondo","Deep Learning", "Arquitectura Limpia", "Big Data con python"], "Autor":["Pablo Augusto Sz", "Jirdy Torres", "Uncle Bob","Jose Manuel Ortega"], "Numero de paginas":[450,350,420,408],"Precio":[120000,78000,230000,90000]})

df

df[['Nombre del libro','Precio']]

"""Usamos loc para encontrar el indice de la posicion que nos interesa mostrar."""

df.loc[3]

df.loc[[1,2,3]]

df.info()

df2 = pd.read_csv('Compras.csv')

df2

df3 = pd.concat([df,df2], axis = 1)

df3

df3.to_csv('Ventas.csv')

df3.to_excel('Ventas.xlsm')