# -*- coding: utf-8 -*-
# Importacion de paquetes y modulos
import streamlit as st
import pandas as pd
import numpy as np
#from pandas._libs import index
import matplotlib
import matplotlib.pyplot as plt
import gdown
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

st.title('Analisis de datos de la calidad de aire QAIRA - Municipalidad de Miraflores')
st.markdown("""
###
1. Integrantes:
 * Flores Jamjachi, Alejandra Nicole
 * Marcelo Travezaño, Milagros Angela
 * Vega Perez, Zaraí Jhonmy
 * Vilca Benites, Karla Mishell
 * Zimic Sheen, Alen Mirko

2. ¿De qué trata el proyecto?
Este proyecto tiene como principal objetivo la comparación de los datos obtenidos en el
2020 y 2021, en el distrito de Miraflores, sobre los contaminantes encontrados.
Gracias a esto, se pudieron generar gráficos de barras en los cuales se puede apreciar la
concentración mensual en (ug/m3) de contaminantes como el monóxido de carbono (CO), ácido
sulfhídrico (H2S), dióxido de nitrógeno (NO2), ozono (O3), material particulado PM10 y PM2.5,
y dióxido de azufre SO2. 


Los datos dde obtuvieron de [https://www.datosabiertos.gob.pe/dataset/monitoreo-de-calidad-de-aire-qaira%C2%A0-municipalidad-de-miraflores](https://www.datosabiertos.gob.pe/dataset/monitoreo-de-calidad-de-aire-qaira%C2%A0-municipalidad-de-miraflores)

¡EMPIEZA YA!
""")

# Seleccion de dataframe
lista_anhos = [2020,2021]
opcion_anho = st.selectbox('Selecciona un año', lista_anhos)
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
            df = df.dropna()
            indexNames = df[ df['SO2 (ug/m3)'] == '-' ].index
            df.drop(indexNames , inplace=True)
            df['SO2 (ug/m3)'] = df['SO2 (ug/m3)'].astype(float)
      elif opcion_mes == lista_meses[5]:
            df = pd.read_excel(link_dic_2020)
            indexNames = df[ df['H2S (ug/m3)'] == '-' ].index
            df.drop(indexNames , inplace=True)
            df['H2S (ug/m3)'] = df['H2S (ug/m3)'].astype(float)
else:
      lista_meses = ['Enero','Febrero','Marzo']
      opcion_mes = st.selectbox('Selecciona un mes', lista_meses)
      if opcion_mes == lista_meses[0]:
            df = pd.read_excel(link_ene_2021)
      elif opcion_mes == lista_meses[1]:
            df = pd.read_excel(link_feb_2021)
      elif opcion_mes == lista_meses[2]:
            df = pd.read_excel(link_mar_2021)
            df = df.dropna()

num_filas = len(df.axes[0])
st.write('Se encontraron', num_filas,'registros')

st.dataframe(df)

#JULIO 2020
df_contaminantes = df.iloc[:,6:12]
st.bar_chart(pd.DataFrame(df_contaminantes.mean()))
