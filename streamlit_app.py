# -*- coding: utf-8 -*-
# Importacion de paquetes y modulos
import streamlit as st
import pandas as pd
import numpy as np
#from pandas._libs import index
import matplotlib
import matplotlib.pyplot as plt

# Carga de datos (Todos los que vayas a utilizar)
link_jul_2020 = "https://www.datosabiertos.gob.pe/sites/default/files/Monitoreo_julio.xlsx"
link_ago_2020 = "https://www.datosabiertos.gob.pe/sites/default/files/Monitoreo_agosto.xlsx"
link_set_2020 = "https://www.datosabiertos.gob.pe/sites/default/files/Monitoreo_setiembre_Bonilla.xlsx"
link_oct_2020 = "https://www.datosabiertos.gob.pe/sites/default/files/Monitoreo_octubre.xlsx"
link_nov_2020 = "https://www.datosabiertos.gob.pe/sites/default/files/6_Monitoreo_Noviembre.xlsx"
link_dic_2020 = "https://www.datosabiertos.gob.pe/sites/default/files/7_Monitoreo_Diciembre.xlsx"

link_ene_2021 = "https://www.datosabiertos.gob.pe/sites/default/files/8_Monitoreo_Enero_2021.xlsx"
link_feb_2021 = "https://www.datosabiertos.gob.pe/sites/default/files/9_Monitoreo_Febrero_2021.xlsx"
link_mar_2021 = "https://www.datosabiertos.gob.pe/sites/default/files/10_Monitoreo_Marzo_2021.xlsx"

# Obtencion de resumen () de cada dataframe



# Limpiar (eliminar row con null, y replace de data duplicada de columnas (Transporte, transporte, Tranportes))

# Generacion de columnas adicionales fecha (18-02-2019) -> anho (2019) y mes (02)

#

st.title('Analisis de datos de ...')
st.markdown("""
### 1. De que trata el proyecto?
Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto.
Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500,
cuando un impresor (N. del T. persona que se dedica a la imprenta)
desconocido usó una galería de textos y los mezcló de tal manera que logró hacer un libro de textos especimen.
No sólo sobrevivió 500 años, sino que tambien ingresó como texto de relleno en documentos electrónicos.

Los datos dde obtuvieron de [https://google.com](https://google.com)

""")

# Seleccion de dataframe
lista_anhos = [2020,2021]
opcion_anho = st.selectbox('Selecciona un anho', lista_anhos)
df = pd.DataFrame()
if opcion_anho == 2020:
      lista_meses = ['Julio','Agosto','Setiembre','Octubre','Noviembre','Diciembre']
      opcion_mes = st.selectbox('Selecciona un mes', lista_meses)
      if opcion_mes == lista_meses[0]:
            df = pd.read_excel(link_jul_2020)
      elif opcion_mes == lista_meses[1]:
            df = pd.read_excel(link_ago_2020)
      elif opcion_mes == lista_meses[2]:
            df = pd.read_excel(link_set_2020)
      elif opcion_mes == lista_meses[3]:
            df = pd.read_excel(link_oct_2020)
      elif opcion_mes == lista_meses[4]:
            df = pd.read_excel(link_nov_2020)
      elif opcion_mes == lista_meses[5]:
            df = pd.read_excel(link_dic_2020)
else:
      lista_meses = ['Enero','Febrero','Marzo']
      opcion_mes = st.selectbox('Selecciona un mes', lista_meses)
      if opcion_mes == lista_meses[0]:
            df = pd.read_excel(link_ene_2021)
      elif opcion_mes == lista_meses[1]:
            df = pd.read_excel(link_feb_2021)
      elif opcion_mes == lista_meses[2]:
            df = pd.read_excel(link_mar_2021)

num_filas = len(df.axes[0])
st.write('Se encontraron', num_filas,'registros')

st.dataframe(df)

#JULIO 2020
df_contaminantes = df.iloc[:,6:12]
st.bar_chart(pd.DataFrame(df_contaminantes.mean()))

