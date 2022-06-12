# Importacion de paquetes y modulos
import streamlit as st
import pandas as pd
import numpy as np
from xlrd import read_excel

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

df_jul_2020 = pd.read_excel("https://www.datosabiertos.gob.pe/sites/default/files/Monitoreo_julio.xlsx")
df_ago_2020 = pd.read_excel("https://www.datosabiertos.gob.pe/sites/default/files/Monitoreo_agosto.xlsx")
df_set_2020 = pd.read_excel(link_set_2020)
df_oct_2020 = pd.read_excel(link_oct_2020)
df_nov_2020 = pd.read_excel(link_nov_2020)
df_dic_2020 = pd.read_excel(link_dic_2020)
df_ene_2021 = pd.read_excel(link_ene_2021)
df_feb_2021 = pd.read_excel(link_feb_2021)
df_mar_2021 = pd.read_excel(link_mar_2021)

# Obtencion de resumen () de cada dataframe



# Limpiar (eliminar row con null, y replace de data duplicada de columnas (Transporte, transporte, Tranportes))

# Generacion de columnas adicionales fecha (18-02-2019) -> anho (2019) y mes (02)

#

st.title('Proyecto final: ...')

st.dataframe(df_jul_2020)

